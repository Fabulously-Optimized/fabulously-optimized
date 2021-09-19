import os

user_path = os.path.expanduser("~")
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
version_no = "1.17.1"
packwiz_path = git_path + "Packwiz/" + version_no + "/"
exe_path = "packwiz.exe"
mods_path = packwiz_path + "mods"

mod_files = os.listdir(mods_path)
for item in mod_files:
    os.remove( os.path.join(mods_path, item))

os.chdir(packwiz_path)
from_file = input("Please drag the Curseforge zip file here: ")[3:][:-1] # Because dragging the file adds "& " and double quotes
os.system(exe_path + " curseforge import \"" + from_file + "\"")
os.system(exe_path + " remove hydrogen")
os.system(exe_path + " mr install hydrogen")
os.system(exe_path + " remove indium")
os.system(exe_path + " mr install indium")
os.system(exe_path + " refresh")

# TODO: Update Modrinth json