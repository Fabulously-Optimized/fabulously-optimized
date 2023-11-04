import os
import json
from typing import IO
from pathlib import Path
from zipfile import ZipFile
from shutil import unpack_archive

import toml  # pip install toml


user_path = os.path.expanduser("~")
git_path = user_path + "\\Documents\\GitHub\\fabulously-optimized\\"
minecraft_version = "1.20.2"
packwiz_path = git_path + "Packwiz\\" + minecraft_version + "\\"
packwiz_exe_path = os.path.join("..", "packwiz.exe")
mods_path = packwiz_path + "mods"
packwiz_manifest = "pack.toml"

cf_zip_path = ""
pack_version = ""

refresh_only = False
is_legacy = False
hydrogen = False
modrinth_overrides = True
mmc_export_packwiz_export = True
mmc_export_modrinth_export = True
packwiz_modrinth_export = False


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


def main():
    mod_files = os.listdir(mods_path)
    if not refresh_only:
        for item in mod_files:
            os.remove(os.path.join(mods_path, item))

    os.chdir(packwiz_path)
    if not refresh_only:
        # Slicing, because dragging the file adds "& " and double quotes
        cf_zip_path = input("Please drag the CurseForge zip file here: ")[3:][:-1]
        pack_version = "-".join(str(Path(cf_zip_path).with_suffix("")).split("-")[1:])

    if not mmc_export_packwiz_export and not refresh_only:
        # Update pack.toml first
        with open(packwiz_manifest, "r") as f:
            pack_toml = toml.load(f)
        pack_toml["version"] = pack_version
        with open(packwiz_manifest, "w") as f:
            toml.dump(pack_toml, f)

        # Packwiz import
        os.system(f'{packwiz_exe_path} curseforge import "{cf_zip_path}"')
        if hydrogen:
            os.system(f"{packwiz_exe_path} remove hydrogen")
            os.system(f"{packwiz_exe_path} mr install hydrogen")
        if modrinth_overrides:
            os.system(f"{packwiz_exe_path} remove entityculling")
            os.system(f"{packwiz_exe_path} mr install entityculling")

    elif refresh_only:
        os.system(f"{packwiz_exe_path} refresh")

    # Copy fresh manifest/modlist to git
    if not is_legacy and not refresh_only:
        extract_file(cf_zip_path, "manifest.json", git_path + "CurseForge", "CurseForge manifest.json", "Git")
        extract_file(cf_zip_path, "modlist.html", git_path + "CurseForge", "CurseForge modlist.html", "Git")

    # Export Packwiz pack via mmc-export method
    if mmc_export_packwiz_export and not refresh_only:
        mmc_zip_root = str(Path(cf_zip_path).parents[0])
        mmc_zip_path = mmc_zip_root + "\\Fabulously Optimized " + pack_version + ".zip"
        packwiz_config = git_path + "Packwiz\\mmc-export.toml"

        os.system(
            " ".join(
                (
                    "mmc-export",
                    f'-i "{mmc_zip_path}"',
                    "-f packwiz",
                    "--modrinth-search loose",
                    f'-o "{mmc_zip_root}"',
                    f'-c "{packwiz_config}"',
                    f"-v {pack_version}",
                    "--provider-priority Modrinth CurseForge Other",
                    "--scheme mmc_export_packwiz_output",
                )
            )
        )

        packwiz_zip_path = Path(mmc_zip_root) / "mmc_export_packwiz_output.zip"
        packwiz_out_path = Path(git_path) / "Packwiz" / minecraft_version
        packwiz_out_path.mkdir(parents=True, exist_ok=True)
        unpack_archive(packwiz_zip_path, packwiz_out_path)

        os.remove(packwiz_zip_path)

    # Export Modrinth pack and manifest via mmc-export method
    if mmc_export_modrinth_export and not refresh_only:
        mmc_zip_root = str(Path(cf_zip_path).parents[0])
        mmc_zip_path = mmc_zip_root + "\\Fabulously Optimized " + pack_version + ".zip"
        modrinth_config = git_path + "Modrinth\\mmc-export.toml"

        os.system(
            " ".join(
                (
                    "mmc-export",
                    f'-i "{mmc_zip_path}"',
                    "-f Modrinth",
                    "--modrinth-search loose",
                    f'-o "{mmc_zip_root}"',
                    f'-c "{modrinth_config}"',
                    f"-v {pack_version}",
                    f'--scheme {"{name}-{version}"}',
                )
            )
        )

        if not is_legacy:
            extract_file(
                mmc_zip_root + "\\Fabulously Optimized-" + pack_version + ".mrpack",
                "modrinth.index.json",
                git_path + "\\" + "Modrinth",
                "Modrinth manifest",
                "Git",
            )

    # Export Modrinth pack and manifest via Packwiz method
    if packwiz_modrinth_export:
        os.system(f"{packwiz_exe_path} modrinth export")
        for pack in os.listdir(packwiz_path):
            if pack.endswith(".mrpack"):
                if not is_legacy:
                    extract_file(
                        packwiz_path + "\\" + pack,
                        "modrinth.index.json",
                        git_path + "\\" + "Modrinth",
                        "Modrinth manifest",
                        "Git",
                    )
                os.replace(packwiz_path + "\\" + pack, os.path.expanduser("~/Desktop") + "\\" + pack)
                print(f"Moved {pack} to desktop")
        os.system(f"{packwiz_exe_path} refresh")

    if not refresh_only:
        mmc_zip_root = str(Path(cf_zip_path).parents[0])
        mmc_zip_path = mmc_zip_root + "\\Fabulously Optimized " + pack_version + ".zip"
        # remove_mod_from_archive("Sodium", mmc_zip_path)
        # remove_mod_from_archive("Iris", mmc_zip_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Operation aborted by user.")
        exit(-1)
