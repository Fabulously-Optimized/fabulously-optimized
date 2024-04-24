import shutil
from pathlib import Path


minecraft_version = "1.20.5"
git_path = Path.home() / "Documents/GitHub/fabulously-optimized/"
packwiz_path = git_path / "Packwiz" / minecraft_version
cf_path = Path.home() / "curseforge/minecraft/Instances/Fabulously Optimized/"
mmc_path = Path.home() / "Documents/MultiMC/instances/Fabulously Optimized/minecraft/"


def remove_dir(path: Path, description: str) -> None:
    if path.is_dir():
        print(f"Deleting {description}")
        shutil.rmtree(path)
        print(f"Deleted {description}")
    else:
        print(f"Skipped {description} deletion, didn't exist")


def remove_file(path: Path, description: str) -> None:
    if path.is_file():
        print(f"Deleting {description}")
        path.unlink()
        print(f"Deleted {description}")
    else:
        print(f"Skipped {description} deletion, didn't exist")


def copy_dir(from_path: Path, to_path: Path, from_desc: str, to_desc: str) -> None:
    if from_path.is_dir():
        print(f"Copying {from_desc} to {to_desc}")
        shutil.copytree(from_path, to_path, dirs_exist_ok=True)
        print(f"Copied {from_desc} to {to_desc}")
    else:
        print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


def copy_file(from_path: Path, to_path: Path, from_desc: str, to_desc: str) -> None:
    if from_path.is_file():
        print(f"Copying {from_desc} to {to_desc}")
        shutil.copy2(from_path, to_path)
        print(f"Copied {from_desc} to {to_desc}")
    else:
        print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


# CurseForge to MultiMC
remove_dir(mmc_path / "mods", "MultiMC mods")
remove_dir(mmc_path / "config", "MultiMC configs")
remove_dir(mmc_path / "resourcepacks", "MultiMC resourcepacks")
remove_file(mmc_path / "options.txt", "MultiMC options.txt")
copy_dir(cf_path / "mods", mmc_path / "mods", "CurseForge mods", "MultiMC")
copy_dir(cf_path / "config", mmc_path / "config", "CurseForge configs", "MultiMC")
copy_dir(cf_path / "resourcepacks", mmc_path / "resourcepacks", "CurseForge resource packs", "MultiMC")

# CurseForge to Git
remove_dir(packwiz_path / "config", "Packwiz configs in Git")
copy_dir(cf_path / "config", packwiz_path / "config", "CurseForge configs", "Git (Packwiz)")
copy_dir(cf_path / "resourcepacks", packwiz_path / "resourcepacks", "CurseForge resource packs", "Git (Packwiz)")
