import json
from pathlib import Path


mmc_path = Path.home() / "curseforge/minecraft/Instances/Fabulously Optimized/"
title_screen_path = mmc_path / "config/isxander-main-menu-credits.json"
warning_path = mmc_path / "config/fabric_loader_dependencies.json"


def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def save_file(path: Path, obj) -> None:
    with open(path, "w") as f:
        json.dump(obj, f, separators=(",", ":"))


title_screen_obj = load_json(title_screen_path)
existing_version = title_screen_obj["main_menu"]["bottom_right"][0]["text"]

print(f"Current version: {existing_version}")
new_version = input("Enter new version: Fabulously Optimized ")

title_screen_obj["main_menu"]["bottom_right"][0]["text"] = f"Fabulously Optimized {new_version}"
save_file(title_screen_path, title_screen_obj)

warning_file_obj = load_json(warning_path)
warning_file_obj["overrides"]["minecraft"]["+recommends"]["Fabulously Optimized"] = f">{new_version}"
save_file(warning_path, warning_file_obj)
