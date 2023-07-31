import shutil
from pathlib import Path


cf_path = Path(Path.home(), "/curseforge/minecraft/Instances/Fabulously Optimized/")
mmc_path = Path(Path.home(), "/Documents/MultiMC/instances/Fabulously Optimized/minecraft/")
git_path = Path(Path.home(), "/Documents/GitHub/fabulously-optimized/")
minecraft_version = "1.20.1"
packwiz_path = Path(git_path, "Packwiz", minecraft_version)


def remove_dir(path: Path, description: str) -> None:
    if path.is_dir():
        shutil.rmtree(path)
        print(f"Deleted {description}")
    else:
        print(f"Skipped {description} deletion, didn't exist")


def remove_file(path: Path, description: str) -> None:
    if path.is_file():
        path.unlink()
        print(f"Deleted {description}")
    else:
        print(f"Skipped {description} deletion, didn't exist")


def copy_dir(from_path: Path, to_path: Path, from_desc: str, to_desc: str) -> None:
    if from_path.is_dir():
        shutil.copytree(from_path, to_path, dirs_exist_ok=True)
        print(f"Copied {from_desc} to {to_desc}")
    else:
        print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


def copy_file(from_path: Path, to_path: Path, from_desc: str, to_desc: str) -> None:
    if from_path.is_file():
        shutil.copy2(from_path, to_path)
        print(f"Copied {from_desc} to {to_desc}")
    else:
        print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


# CurseForge to MultiMC
remove_dir(Path(mmc_path, "mods"), "MultiMC mods")
remove_dir(Path(mmc_path, "config"), "MultiMC configs")
remove_dir(Path(mmc_path, "resourcepacks"), "MultiMC resourcepacks")
remove_file(Path(mmc_path, "options.txt"), "MultiMC options.txt")
copy_dir(Path(cf_path, "mods"), Path(mmc_path, "mods"), "CurseForge mods", "MultiMC")
copy_dir(Path(cf_path, "config"), Path(mmc_path, "config"), "CurseForge configs", "MultiMC")
copy_dir(Path(cf_path, "resourcepacks"), Path(mmc_path, "resourcepacks"), "CurseForge resource packs", "MultiMC")

# CurseForge to Git
# Manifest and json copying moved to "CurseForge to Packwiz.py" to make sure they are always newest
remove_dir(Path(packwiz_path, "config"), "Packwiz configs in Git")
copy_dir(Path(cf_path, "config"), Path(packwiz_path, "config"), "CurseForge configs", "Git (Packwiz)")
copy_dir(Path(cf_path, "resourcepacks"), Path(packwiz_path, "resourcepacks"), "CurseForge resource packs", "Git (Packwiz)")
