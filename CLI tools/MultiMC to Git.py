import os, shutil
from distutils import dir_util

user_path = os.path.expanduser("~")
mmc_path = user_path + "/Documents/MultiMC/instances/Fabulously Optimized 2.0.0b1/"
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"

# Functions

def copy_file(from_path, to_path, from_desc, to_desc):
    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

# MultiMC to Git

copy_file(mmc_path + "instance.cfg", git_path + "MultiMC\Fabulously Optimized x.y.z/instance.cfg", "MultiMC instance.cfg", "Git")
copy_file(mmc_path + "mmc-pack.json", git_path + "MultiMC\Fabulously Optimized x.y.z/mmc-pack.json", "MultiMC mmc-pack.json", "Git")
copy_file(mmc_path + "pack.png", git_path + "MultiMC\Fabulously Optimized x.y.z/pack.png", "MultiMC pack.png", "Git")