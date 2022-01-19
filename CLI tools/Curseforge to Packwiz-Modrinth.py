import os
from zipfile import ZipFile
from pathlib import Path
import toml # pip install toml

user_path = os.path.expanduser("~")
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
minecraft_version = "1.18.1"
packwiz_path = git_path + "Packwiz/" + minecraft_version + "/"
packwiz_exe_path = "..\packwiz.exe"
mods_path = packwiz_path + "mods"
packwiz_manifest = "pack.toml"

refresh_only = False
is_legacy = False

def extract_file(from_zip, from_file, to_path, from_desc, to_desc):
    with ZipFile(from_zip, 'r') as zip:
        if from_file in zip.namelist():
                zip.extract(from_file, to_path)
                print("Copied " + from_desc + " to " + to_desc)
        else:
            print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

mod_files = os.listdir(mods_path)
if refresh_only == False:
    for item in mod_files:
        os.remove( os.path.join(mods_path, item))

os.chdir(packwiz_path)
if refresh_only == False:
    cf_zip_path = input("Please drag the Curseforge zip file here: ")[3:][:-1] # Because dragging the file adds "& " and double quotes
    
    # Update pack.toml first
    pack_version = str(Path(cf_zip_path).with_suffix("")).split("-")[1:][0]
    with open(packwiz_manifest, "r") as f:
        pack_toml = toml.load(f)
    pack_toml["version"] = pack_version
    with open(packwiz_manifest, "w") as f:
        toml.dump(pack_toml, f)

    # Packwiz import
    os.system(packwiz_exe_path + " curseforge import \"" + cf_zip_path + "\"")
    if is_legacy:
        os.system(packwiz_exe_path + " remove hydrogen")
        os.system(packwiz_exe_path + " mr install hydrogen")
os.system(packwiz_exe_path + " refresh")

# Copy fresh manifest/modlist to git
if is_legacy == False and refresh_only == False:
    extract_file(cf_zip_path, "manifest.json", git_path + "Curseforge", "Curseforge manifest.json", "Git")
    extract_file(cf_zip_path, "modlist.html", git_path + "Curseforge", "Curseforge modlist.html", "Git")

# Export Modrinth pack and manifest
if refresh_only == False:
    os.system(packwiz_exe_path + " modrinth export")
    for pack in os.listdir(packwiz_path):
        if pack.endswith('.mrpack'):
            if is_legacy == False:
                extract_file(packwiz_path + "/" + pack, "modrinth.index.json", git_path + "/" + "Modrinth", "Modrinth manifest", "Git")
            os.replace(packwiz_path + "/" + pack, os.path.expanduser("~/Desktop") + "/" + pack)
            print("Moved " + pack + " to desktop")