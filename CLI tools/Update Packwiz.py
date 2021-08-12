import os

user_path = os.path.expanduser("~")
git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
exe_path = "packwiz.exe"

os.chdir(git_path + "Packwiz")
from_file = input("Please drag the Curseforge zip file here: ")[2:] # Because dragging the file adds "& " for some reason
os.system(exe_path + " curseforge import " + from_file) # TODO: something's wrong here, packwiz claims there are two arguments
os.system(exe_path + " remove hydrogen")
os.system(exe_path + " mr install hydrogen")
os.system(exe_path + " remove indium")
os.system(exe_path + " mr install indium")
os.system(exe_path +" refresh")

# TODO: Update Modrinth json