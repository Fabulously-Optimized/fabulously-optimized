import re
import shutil
import zipfile
from pathlib import Path

mmc_path = Path(Path.home(), "Documents/MultiMC/instances/Fabulously Optimized/")
git_path = Path(Path.home(), "Documents/GitHub/fabulously-optimized/")
output_path = Path(Path.home(), "Desktop/")


def copy_file(from_path: Path, to_path: Path, from_desc: str, to_desc: str) -> None:
    if from_path.is_file():
        shutil.copy2(from_path, to_path)
        print(f"Copied {from_desc} to {to_desc}")
    else:
        print(f"Skipped {from_desc} copying to {to_desc}, didn't exist")


def copy_to_archive(from_path: Path, to_path: Path, archive_path: Path) -> None:
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

with open(Path(mmc_path, "instance.cfg"), "r") as file:
    if match := pattern.search(file.read()):
        version = match.group()

with open(Path(git_path, "MultiMC/Fabulously Optimized x.y.z/instance.cfg"), "r+") as file:
    data = pattern.sub(version, file.read())
    file.seek(0)
    file.truncate()
    file.write(data)

copy_to_archive(
    Path(git_path, "MultiMC/Fabulously Optimized x.y.z/instance.cfg"),
    Path(f"Fabulously Optimized {version}/instance.cfg"),
    Path(output_path, f"Fabulously Optimized {version}.zip"),
)
copy_file(
    Path(mmc_path, "mmc-pack.json"),
    Path(git_path, "MultiMC/Fabulously Optimized x.y.z/mmc-pack.json"),
    "MultiMC mmc-pack.json",
    "Git",
)
copy_file(
    Path(mmc_path, "pack.png"),
    Path(git_path, "MultiMC/Fabulously Optimized x.y.z/pack.png"),
    "MultiMC pack.png",
    "Git",
)
