import re
import shutil
import zipfile
from pathlib import Path


mmc_path = Path.home() / "Documents/MultiMC/instances/Fabulously Optimized/"
git_path = Path.home() / "Documents/GitHub/fabulously-optimized/"
output_path = Path.home() / "Desktop/"


def copy_file(from_path: Path, to_path: Path, from_desc: str, to_desc: str):
    if from_path.is_file():
        print(f"Copying {from_desc} to {to_desc}")
        shutil.copy2(from_path, to_path)
        print(f"Copied {from_desc} to {to_desc}")
    else:
        print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


def copy_to_archive(from_path: Path, to_path: str, archive_path: Path):
    files = []

    with zipfile.ZipFile(archive_path, "r") as archive:
        for info in archive.infolist():
            if info.filename != to_path:
                files.append((info.filename, archive.read(info.filename)))

    with zipfile.ZipFile(archive_path, "w") as archive:
        for filename, content in files:
            archive.writestr(filename, content)
        archive.write(from_path, to_path)


# MultiMC to Git
version = "0.0.0"
pattern = re.compile(r"\d+\.\d+\.\d+-?\w*\.?\d*")

with open(mmc_path / "instance.cfg", "r") as file:
    if match := pattern.search(file.read()):
        version = match.group()

with open(git_path / "MultiMC/Fabulously Optimized x.y.z/instance.cfg", "r+") as file:
    data = pattern.sub(version, file.read())
    file.seek(0)
    file.truncate()
    file.write(data)

copy_to_archive(
    git_path / "MultiMC/Fabulously Optimized x.y.z/instance.cfg",
    f"Fabulously Optimized {version}/instance.cfg",
    output_path / f"Fabulously Optimized {version}.zip",
)

copy_file(
    mmc_path / "mmc-pack.json",
    git_path / "MultiMC/Fabulously Optimized x.y.z/mmc-pack.json",
    "MultiMC mmc-pack.json",
    "Git",
)

copy_file(
    mmc_path / "pack.png",
    git_path / "MultiMC/Fabulously Optimized x.y.z/pack.png",
    "MultiMC pack.png",
    "Git",
)
