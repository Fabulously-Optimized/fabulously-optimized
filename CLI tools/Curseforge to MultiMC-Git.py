import os, shutil
from distutils import dir_util

user_path = os.path.expanduser("~")
cf_path = user_path + "/curseforge/minecraft/Instances/Fabulously Optimized/"
mmc_path = user_path + "/Documents/MultiMC/instances/Fabulously Optimized/"
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
minecraft_version = "1.18.1"
packwiz_path = git_path + "Packwiz/" + minecraft_version

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
remove_dir(mmc_path + "minecraft/resourcepacks/", "MultiMC resourcepacks")
copy_dir(cf_path + "config/", mmc_path + "minecraft/config/", "Curseforge configs", "MultiMC")
copy_dir(cf_path + "mods/", mmc_path + "minecraft/mods/", "Curseforge mods", "MultiMC")
copy_dir(cf_path + "resourcepacks/", mmc_path + "minecraft/resourcepacks/", "Curseforge resource packs", "MultiMC")

# Curseforge to Git 

# Manifest and json copying moved to "Curseforge to Packwiz.py" to make sure they are always newest
remove_dir(packwiz_path + "/config/", "Packwiz configs in Git")
copy_dir(cf_path + "config/", packwiz_path + "/config/", "Curseforge configs", "Git (Packwiz)")
copy_dir(cf_path + "resourcepacks/", packwiz_path + "/resourcepacks/", "Curseforge resource packs", "Git (Packwiz)")
