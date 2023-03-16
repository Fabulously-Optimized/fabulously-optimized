import os, shutil

user_path = os.path.expanduser("~")
cf_path = user_path + "/curseforge/minecraft/Instances/Fabulously Optimized/"
mmc_path = user_path + "/Documents/MultiMC/instances/Fabulously Optimized/minecraft/"
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
minecraft_version = "1.19.4"
packwiz_path = git_path + "Packwiz/" + minecraft_version

# Functions

def remove_dir(path, description):
    if os.path.isdir(path):
        shutil.rmtree(path)
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
        shutil.copytree(from_path, to_path, dirs_exist_ok=True)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

def copy_file(from_path, to_path, from_desc, to_desc):
    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

# CurseForge to MultiMC

remove_dir(mmc_path + "config/", "MultiMC configs")
remove_file(mmc_path + "options.txt", "MultiMC options.txt")
remove_dir(mmc_path + "mods/", "MultiMC mods")
remove_dir(mmc_path + "resourcepacks/", "MultiMC resourcepacks")
copy_dir(cf_path + "config/", mmc_path + "config/", "CurseForge configs", "MultiMC")
copy_dir(cf_path + "mods/", mmc_path + "mods/", "CurseForge mods", "MultiMC")
copy_dir(cf_path + "resourcepacks/", mmc_path + "resourcepacks/", "CurseForge resource packs", "MultiMC")

# CurseForge to Git 

# Manifest and json copying moved to "CurseForge to Packwiz.py" to make sure they are always newest
remove_dir(packwiz_path + "/config/", "Packwiz configs in Git")
copy_dir(cf_path + "config/", packwiz_path + "/config/", "CurseForge configs", "Git (Packwiz)")
copy_dir(cf_path + "resourcepacks/", packwiz_path + "/resourcepacks/", "CurseForge resource packs", "Git (Packwiz)")
