import json, shutil
from pathlib import Path


mmc_path = Path.home() / "curseforge/minecraft/Instances/Fabulously Optimized/"
config_root = mmc_path / "config/"
title_screen_name = "isxander-main-menu-credits.json"
title_screen_path = config_root / title_screen_name
overrides_name = "fabric_loader_dependencies.json"
overrides_path = config_root / overrides_name
modpack_defaults_name = "modpack_defaults/config/"
modpack_defaults_path = config_root / modpack_defaults_name
modpack_defaults = True


def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def save_file(path: Path, obj) -> None:
    with open(path, "w") as f:
        json.dump(obj, f, separators=(",", ":"))

def copy_file(from_path: Path, to_path: Path, from_desc: str, to_desc: str) -> None:
    if from_path.is_file():
        shutil.copy2(from_path, to_path)
        print(f"Copied {from_desc} to {to_desc}")
    else:
        print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


title_screen_obj = load_json(title_screen_path)
existing_version = title_screen_obj["main_menu"]["bottom_right"][0]["text"]

print(f"Current version: {existing_version}")
new_version = input("Enter new version: Fabulously Optimized ")

title_screen_obj["main_menu"]["bottom_right"][0]["text"] = f"Fabulously Optimized {new_version}"
save_file(title_screen_path, title_screen_obj)

overrides_file_obj = load_json(overrides_path)
overrides_file_obj["overrides"]["minecraft"]["+recommends"]["Fabulously Optimized"] = f">{new_version}"
save_file(overrides_path, overrides_file_obj)

if modpack_defaults:
    copy_file(title_screen_path, modpack_defaults_path / title_screen_name, title_screen_name, modpack_defaults_name)
    copy_file(overrides_path, modpack_defaults_path / overrides_name, overrides_name, modpack_defaults_name)