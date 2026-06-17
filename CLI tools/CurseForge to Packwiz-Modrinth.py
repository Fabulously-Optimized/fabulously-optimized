import os
import shlex
import sys
import json
import subprocess
import toml  # pip install toml
from typing import IO
from pathlib import Path
from zipfile import ZipFile
from shutil import unpack_archive

macos = sys.platform == "darwin"
minecraft_version = "26.2"

git_path = Path.home() / "Documents/GitHub/fabulously-optimized"
packwiz_path = git_path / "Packwiz" / minecraft_version

if macos:
    packwiz_exe_path = git_path / "Packwiz/packwiz"
    mmc_export_path = git_path / ".venv/bin/mmc-export"
else:
    packwiz_exe_path = Path("..") / "packwiz.exe"
    mmc_export_path = Path("mmc-export")

mods_path = packwiz_path / "mods"
packwiz_manifest = "pack.toml"

refresh_only = False
is_legacy = False
modrinth_overrides = True

mmc_export_packwiz_export = True
mmc_export_modrinth_export = False
purge_cache = macos

packwiz_modrinth_export = True
manual_jar_removal = False

def extract_file(from_zip: str, from_file: str, to_path: str, from_desc: str, to_desc: str) -> None:
    with ZipFile(from_zip, "r") as archive:
        if from_file in archive.namelist():
            print(f"Copying {from_desc} to {to_desc}")
            archive.extract(from_file, to_path)
            print(f"Copied {from_desc} to {to_desc}")
        else:
            print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


def remove_from_archive(file_path: str, archive_path: str) -> None:
    files = []

    with ZipFile(archive_path) as archive:
        for zipinfo in archive.infolist():
            if zipinfo.filename != file_path:
                files.append((zipinfo.filename, archive.read(zipinfo.filename)))

    with ZipFile(archive_path, "w") as archive:
        for filename, content in files:
            archive.writestr(filename, content)


def read_mod_meta(file_handle: IO[bytes]) -> dict:
    with ZipFile(file_handle) as archive:
        data = archive.read("fabric.mod.json")
        return json.loads(data, strict=False)


def remove_mod_from_archive(mod_name: str, archive_path: str) -> None:
    with ZipFile(archive_path) as archive:
        for zipinfo in archive.infolist():
            name = zipinfo.filename

            if not name.endswith(".jar"):
                continue

            with archive.open(name) as mod_file:
                mod_meta = read_mod_meta(mod_file)

                if mod_meta["name"] == mod_name:
                    remove_from_archive(name, archive_path)
                    return


def run_shell_command(args):
    #print("debug:", args)
    return subprocess.run(list(args), shell=False).returncode

def main():
    mod_files = [p.name for p in Path(mods_path).iterdir()]

    if refresh_only:
        run_shell_command([str(packwiz_exe_path), "refresh"])
        return

    for item in mod_files:
        (Path(mods_path) / item).unlink() # Delete files

    os.chdir(packwiz_path)
    # Slicing: Windows removes leading '& "' and trailing '"' ; macOS removes only ' from start and end
    raw_cf = input("Please drag the CurseForge zip file here: ")
    cf_zip_path = raw_cf[1:-1] if macos else raw_cf[3:-1]
    pack_version = "-".join(str(Path(cf_zip_path).with_suffix("")).split("-")[1:])

    mmc_zip_root = Path(cf_zip_path).parent
    mmc_zip_path = mmc_zip_root / f"Fabulously Optimized {pack_version}.zip"

    if not mmc_export_packwiz_export:
        # Update pack.toml first
        with open(packwiz_manifest, "r") as f:
            pack_toml = toml.load(f)
        pack_toml["version"] = pack_version
        with open(packwiz_manifest, "w") as f:
            toml.dump(pack_toml, f)

        # Packwiz import
        run_shell_command([str(packwiz_exe_path), "curseforge", "import", str(cf_zip_path)])
        if modrinth_overrides:
            run_shell_command([str(packwiz_exe_path), "remove", "entityculling"])
            run_shell_command([str(packwiz_exe_path), "mr", "install", "entityculling"])

    # Copy fresh manifest/modlist to git
    if not is_legacy:
        extract_file(cf_zip_path, "manifest.json", str(git_path / "CurseForge"), "CurseForge manifest.json", "Git")
        extract_file(cf_zip_path, "modlist.html", str(git_path / "CurseForge"), "CurseForge modlist.html", "Git")

    if (mmc_export_packwiz_export or mmc_export_modrinth_export) and macos and purge_cache: # For some reason the macos environment needs purging cache more often
        run_shell_command([str(mmc_export_path), "purge-cache"])

    # Export Packwiz pack via mmc-export method
    if mmc_export_packwiz_export:
        packwiz_config_path = git_path / "Packwiz/mmc-export.toml"

        args = (
            str(mmc_export_path),
            "-i", str(mmc_zip_path),
            "-f", "packwiz",
            "--modrinth-search", "loose",
            "-o", str(mmc_zip_root),
            "-c", str(packwiz_config_path),
            "-v", pack_version,
            "--exclude-providers", "GitHub", # Currently not needed to use GitHub
            "--provider-priority", "Modrinth", "CurseForge", "Other",
            "--scheme", "mmc_export_packwiz_output"
        )
        run_shell_command(args)

        packwiz_zip_path = Path(mmc_zip_root) / "mmc_export_packwiz_output.zip"
        packwiz_out_path = Path(git_path) / "Packwiz" / minecraft_version
        packwiz_out_path.mkdir(parents=True, exist_ok=True)
        unpack_archive(packwiz_zip_path, packwiz_out_path)

        os.remove(packwiz_zip_path)

    # Export Modrinth pack and manifest via mmc-export method
    if mmc_export_modrinth_export:
        modrinth_config_path = git_path / "Modrinth/mmc-export.toml"

        args = (
            str(mmc_export_path),
            "-i", str(mmc_zip_path),
            "-f", "Modrinth",
            "--modrinth-search", "loose",
            "-o", str(mmc_zip_root),
            "-c", str(modrinth_config_path),
            "-v", pack_version,
            "--scheme", "{name}-{version}",
        )
        run_shell_command(args)

        if not is_legacy:
            extract_file(
                str(mmc_zip_root / f"Fabulously Optimized-{pack_version}.mrpack"),
                "modrinth.index.json",
                str(Path(git_path) / "Modrinth"),
                "Modrinth manifest",
                "Git",
            )

    # Export Modrinth pack and manifest via Packwiz method
    if packwiz_modrinth_export:
        run_shell_command([str(packwiz_exe_path), "modrinth", "export"])
        for pack in os.listdir(packwiz_path):
            if pack.endswith(".mrpack"):
                if not is_legacy:
                    extract_file(
                        str(Path(packwiz_path) / pack),
                        "modrinth.index.json",
                        str(Path(git_path) / "Modrinth"),
                        "Modrinth manifest",
                        "Git",
                    )
                (Path(packwiz_path) / pack).replace(Path.home() / "Desktop" / pack)
                print(f"Moved {pack} to desktop")
        run_shell_command([str(packwiz_exe_path), "refresh"])

    if manual_jar_removal:
        mmc_zip_root = Path(cf_zip_path).parent
        mmc_zip_path = mmc_zip_root / f"Fabulously Optimized {pack_version}.zip"
        #remove_mod_from_archive("Sodium", mmc_zip_path)
        #remove_mod_from_archive("Iris", mmc_zip_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Operation aborted by user.")
        exit(-1)
