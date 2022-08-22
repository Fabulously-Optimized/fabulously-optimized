import os, json
from turtle import title

user_path = os.path.expanduser("~")
cf_path = user_path + "/curseforge/minecraft/Instances/Fabulously Optimized/"
title_screen_path = cf_path + "config/isxander-main-menu-credits.json"
warning_path = cf_path + "config/fabric_loader_dependencies.json"

title_screen_obj = json.load(open(title_screen_path))
existing_version = title_screen_obj["main_menu"]["bottom_right"][0]["text"]

print("Current version: " + existing_version)
new_version = "Fabulously Optimized " + input("Enter new version: Fabulously Optimized ")

title_screen_obj = json.load(open(title_screen_path))
title_screen_obj["main_menu"]["bottom_right"][0]["text"] = new_version

warning_file_obj = json.load(open(warning_path))
warning_file_obj["overrides"]["fabric-api"]["+recommends"]["Fabulously Optimized"] = "newer than " + new_version

with open(title_screen_path, "w") as f:
    json.dump(title_screen_obj, f, separators=(',', ':'))

with open(warning_path, "w") as f:
    json.dump(warning_file_obj, f, separators=(',', ':'))