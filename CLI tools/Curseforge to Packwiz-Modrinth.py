import os
from zipfile import ZipFile

user_path = os.path.expanduser("~")
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
version_no = "1.18.1"
packwiz_path = git_path + "Packwiz/" + version_no + "/"
pw_exe_path = "..\packwiz.exe"
mods_path = packwiz_path + "mods"

mod_files = os.listdir(mods_path)
for item in mod_files:
    os.remove( os.path.join(mods_path, item))

def extract_file(from_zip, from_file, to_path, from_desc, to_desc):
    with ZipFile(from_zip, 'r') as zip:
        if from_file in zip.namelist():
                zip.extract(from_file, to_path)
                print("Copied " + from_desc + " to " + to_desc)
        else:
            print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")


os.chdir(packwiz_path)
cf_zip_path = input("Please drag the Curseforge zip file here: ")[3:][:-1] # Because dragging the file adds "& " and double quotes
os.system(pw_exe_path + " curseforge import \"" + cf_zip_path + "\"")
#os.system(pw_exe_path + " remove hydrogen")
#os.system(pw_exe_path + " mr install hydrogen")
os.system(pw_exe_path + " refresh")

# Copy fresh manifest/modlist to git
extract_file(cf_zip_path, "manifest.json", git_path + "Curseforge", "Curseforge manifest.json", "Git")
extract_file(cf_zip_path, "modlist.html", git_path + "Curseforge", "Curseforge modlist.html", "Git")

# Export Modrinth pack and manifest
os.system(pw_exe_path + " modrinth export")
for pack in os.listdir(packwiz_path):
    if pack.endswith('.mrpack'):
        extract_file(packwiz_path + "/" + pack, "modrinth.index.json", git_path + "/" + "Modrinth", "Modrinth manifest", "Git")
        os.replace(packwiz_path + "/" + pack, os.path.expanduser("~/Desktop") + "/" + pack)
        print("Moved " + pack + " to desktop")