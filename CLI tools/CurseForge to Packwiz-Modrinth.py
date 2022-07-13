import os
from zipfile import ZipFile
from pathlib import Path
import toml # pip install toml

user_path = os.path.expanduser("~")
git_path = user_path + "\\Documents\\GitHub\\fabulously-optimized\\"
minecraft_version = "1.19"
packwiz_path = git_path + "Packwiz\\" + minecraft_version + "\\"
packwiz_exe_path = "..\packwiz.exe"
mods_path = packwiz_path + "mods"
packwiz_manifest = "pack.toml"

cf_zip_path = ""
pack_version = ""

refresh_only = False
is_legacy = False
hydrogen = False
modrinth_overrides = True
mmc_export_modrinth_export = True
packwiz_modrinth_export = False

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
    cf_zip_path = input("Please drag the CurseForge zip file here: ")[3:][:-1] # Because dragging the file adds "& " and double quotes
    
    # Update pack.toml first
    pack_version = "-".join(str(Path(cf_zip_path).with_suffix("")).split("-")[1:])
    with open(packwiz_manifest, "r") as f:
        pack_toml = toml.load(f)
    pack_toml["version"] = pack_version
    with open(packwiz_manifest, "w") as f:
        toml.dump(pack_toml, f)

    # Packwiz import
    os.system(packwiz_exe_path + " curseforge import \"" + cf_zip_path + "\"")
    if hydrogen:
        os.system(packwiz_exe_path + " remove hydrogen")
        os.system(packwiz_exe_path + " mr install hydrogen")
    if modrinth_overrides:
        os.system(packwiz_exe_path + " remove entityculling")
        os.system(packwiz_exe_path + " mr install entityculling")
os.system(packwiz_exe_path + " refresh")

# Copy fresh manifest/modlist to git
if is_legacy == False and refresh_only == False:
    extract_file(cf_zip_path, "manifest.json", git_path + "CurseForge", "CurseForge manifest.json", "Git")
    extract_file(cf_zip_path, "modlist.html", git_path + "CurseForge", "CurseForge modlist.html", "Git")


# Export Modrinth pack and manifest via mmc-export method
if mmc_export_modrinth_export:
    mmc_zip_root = str(Path(cf_zip_path).parents[0])
    mmc_zip_path = mmc_zip_root + "\\Fabulously Optimized " + pack_version + ".zip"
    modrinth_config = git_path + "Modrinth\\mmc-export.toml"
    os.system("mmc-export -i \"" + mmc_zip_path + "\" -f Modrinth --modrinth-search loose -o \"" + mmc_zip_root + "\" -c \"" + modrinth_config + "\" -v " + pack_version + " --scheme \"{abbr}_{name}_{version}\"")
    if is_legacy == False:
        extract_file(mmc_zip_root + "\\MR_Fabulously Optimized_" + pack_version + ".mrpack", "modrinth.index.json", git_path + "\\" + "Modrinth", "Modrinth manifest", "Git")

# Export Modrinth pack and manifest via packwiz method
if packwiz_modrinth_export:
    os.system(packwiz_exe_path + " modrinth export")
    for pack in os.listdir(packwiz_path):
        if pack.endswith('.mrpack'):
            if is_legacy == False:
                extract_file(packwiz_path + "\\" + pack, "modrinth.index.json", git_path + "\\" + "Modrinth", "Modrinth manifest", "Git")
            os.replace(packwiz_path + "\\" + pack, os.path.expanduser("~/Desktop") + "\\" + pack)
            print("Moved " + pack + " to desktop")
    os.system(packwiz_exe_path + " refresh")
