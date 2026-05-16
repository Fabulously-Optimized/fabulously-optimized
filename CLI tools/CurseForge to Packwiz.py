import os
import json
import subprocess
import sys
import toml  # pip install toml
from typing import IO
from pathlib import Path
from zipfile import ZipFile

minecraft_version = "26.1.2"
macos = sys.platform == "darwin"

user_path = os.path.expanduser("~")
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
packwiz_path = git_path + "Packwiz/" + minecraft_version + "/"

if macos:
    packwiz_exe_path = git_path + "Packwiz/packwiz"
else:
    packwiz_exe_path = os.path.join("..", "packwiz.exe")

mods_path = packwiz_path + "mods"
packwiz_manifest = "pack.toml"

cf_zip_path = ""
pack_version = ""

refresh_only = False
modrinth_overrides = True
packwiz_modrinth_export = True

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

    if refresh_only:
        subprocess.call(f"{packwiz_exe_path} refresh", shell=True)
        return

    for item in mod_files:
        os.remove(os.path.join(mods_path, item))

    os.chdir(packwiz_path)
    # Slicing, because dragging the file adds "& " and double quotes
    cf_zip_path = input("Please drag the CurseForge zip file here: ")[3:][:-1]
    pack_version = "-".join(str(Path(cf_zip_path).with_suffix("")).split("-")[1:])

    # Update pack.toml first
    with open(packwiz_manifest, "r") as f:
        pack_toml = toml.load(f)
    pack_toml["version"] = pack_version
    with open(packwiz_manifest, "w") as f:
        toml.dump(pack_toml, f)

    # Packwiz import
    subprocess.call(f'{packwiz_exe_path} curseforge import "{cf_zip_path}"', shell=True)
    if modrinth_overrides:
        os.system(f"{packwiz_exe_path} remove entityculling")
        os.system(f"{packwiz_exe_path} mr install entityculling")

    # Copy fresh manifest/modlist to git
    extract_file(cf_zip_path, "manifest.json", git_path + "CurseForge", "CurseForge manifest.json", "Git")
    extract_file(cf_zip_path, "modlist.html", git_path + "CurseForge", "CurseForge modlist.html", "Git")

    # Export Modrinth pack and manifest via Packwiz method
    if packwiz_modrinth_export:
        os.system(f"{packwiz_exe_path} modrinth export")
        for pack in os.listdir(packwiz_path):
            if pack.endswith(".mrpack"):
                extract_file(
                    packwiz_path + "/" + pack,
                    "modrinth.index.json",
                    git_path + "/" + "Modrinth",
                    "Modrinth manifest",
                    "Git",
                )
                os.replace(packwiz_path + "/" + pack, os.path.expanduser("~/Desktop") + "/" + pack)
                print(f"Moved {pack} to desktop")
        subprocess.call(f"{packwiz_exe_path} refresh", shell=True)

    mmc_zip_root = str(Path(cf_zip_path).parents[0])
    mmc_zip_path = mmc_zip_root + "/Fabulously Optimized " + pack_version + ".zip"
    #remove_mod_from_archive("Sodium", mmc_zip_path)
    #remove_mod_from_archive("Iris", mmc_zip_path)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Operation aborted by user.")
        exit(-1)