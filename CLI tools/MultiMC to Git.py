import os, shutil, re, zipfile
from distutils import dir_util

user_path = os.path.expanduser("~")
mmc_path = user_path + "/Documents/MultiMC/instances/Fabulously Optimized/"
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
output_path = user_path + "/Desktop/"

# Functions

def copy_file(from_path, to_path, from_desc, to_desc):
    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

def copy_to_archive(from_path, to_path, archive_path):

    files = []

    with zipfile.ZipFile(archive_path) as archive:
        for zipinfo in archive.infolist():
            if zipinfo.filename != to_path:
                files.append((zipinfo.filename, archive.read(zipinfo.filename)))

    with zipfile.ZipFile(archive_path, "w") as archive:
        for filename, content in files:
            archive.writestr(filename, content)
        archive.write(from_path, to_path)

# MultiMC to Git

version = "0.0.0"
pattern = re.compile(r"\d+\.\d+\.\d+-?\w*\.?\d*")

with open(mmc_path + "instance.cfg") as file:
    if match := pattern.search(file.read()):
        version = match.group()

with open(git_path + "/MultiMC/Fabulously Optimized x.y.z/instance.cfg", "r+") as file:
    data = pattern.sub(version, file.read())
    file.seek(0); file.truncate(); file.write(data)

copy_to_archive(git_path + "/MultiMC/Fabulously Optimized x.y.z/instance.cfg", f"Fabulously Optimized {version}/instance.cfg", output_path + f"Fabulously Optimized {version}.zip")
copy_file(mmc_path + "mmc-pack.json", git_path + "MultiMC/Fabulously Optimized x.y.z/mmc-pack.json", "MultiMC mmc-pack.json", "Git")
copy_file(mmc_path + "pack.png", git_path + "MultiMC/Fabulously Optimized x.y.z/pack.png", "MultiMC pack.png", "Git")