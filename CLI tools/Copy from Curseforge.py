import os, shutil
from distutils import dir_util

user_path = os.path.expanduser("~")
cf_path = user_path + "/curseforge/minecraft/Instances/Fabulously Optimized/"
mmc_path = user_path + "/Documents/MultiMC/instances/Fabulously Optimized 2.0.0b1/"
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"

# Functions

def remove_dir(path, description):
    if os.path.isdir(path):
        dir_util.remove_tree(path)
        print("Deleted " + description)
    else:
        print("Skipped " + description + " deletion, didn't exist")

def remove_file(path, description):
    if os.path.isfile(path):
        os.remove(path)
        print("Deleted " + description)
    else:
        print("Skipped " + description + " deletion, didn't exist")

def copy_dir(from_path, to_path, from_desc, to_desc):
    if os.path.isdir(from_path):
        dir_util.copy_tree(from_path, to_path)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

def copy_file(from_path, to_path, from_desc, to_desc):
    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

# Curseforge to MultiMC

remove_dir(mmc_path + "minecraft/config/", "MultiMC configs")
remove_file(mmc_path + "minecraft/options.txt", "MultiMC options.txt")
remove_dir(mmc_path + "minecraft/mods/", "MultiMC mods")
copy_dir(cf_path + "config/", mmc_path + "minecraft/config/", "Curseforge configs", "MultiMC")
copy_dir(cf_path + "mods/", mmc_path + "minecraft/mods/", "Curseforge mods", "MultiMC")

# Curseforge to Git 

copy_file(cf_path + "manifest.json", git_path + "Curseforge/manifest.json", "Curseforge manifest.json", "Git")
copy_file(cf_path + "modlist.html", git_path + "Curseforge/modlist.html", "Curseforge modlist.html", "Git")
remove_dir(git_path + "Packwiz/config/", "Packwiz configs in Git")
copy_dir(cf_path + "config/", git_path + "Packwiz/config/", "Curseforge configs", "Git (Packwiz)")
