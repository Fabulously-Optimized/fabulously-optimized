# Original by https://github.com/RozeFound, modified by Madis0

from pathlib import Path, PurePosixPath

import pkg_resources as dist

try: dist.require(['tomli']) # python -m pip install tomli
except dist.DistributionNotFound as Error:
    exit(Error.report() + '\nThe following dependency is missing: {}"'.format(Error.req))

from tomli import load as parse_toml

class ModrinthManager(object):

    def __init__(self, packwiz_folder:Path, output_folder:Path) -> None:

        pack_summary = "A Fabric-based modpack for Minecraft that focuses on performance and graphics optimizations"

        self.root_dir = packwiz_folder
        self.output_dir = output_folder if output_folder else Path()

        with open(self.root_dir / "pack.toml") as file:
            pack_info = parse_toml(file)

        self.index = {
            "formatVersion": int(1),
            "game": "minecraft",
            "versionId": pack_info['version'] if 'version' in pack_info else input("Specify pack version: "),
            "name": pack_info['name'], # Can be optional
            "summary": pack_summary, # input("Describe your pack: "),
            "files": [],
            "dependencies": {
                "minecraft": pack_info['versions']['minecraft']
            }
        }

        if 'fabric' in pack_info['versions']: self.index['dependencies']['fabric-loader'] = pack_info['versions']['fabric']
        elif 'forge' in pack_info['versions']: self.index['dependencies']['forge'] = pack_info['versions']['forge']

        from zipfile import ZipFile
        self.zip = ZipFile(self.output_dir / (self.index['name'] + " " + self.index['versionId'] + " Modrinth.zip"), "w")

        super().__init__()

    def __del__(self):

        from json import dumps

        self.zip.writestr("index.json", dumps(self.index, indent=4))
        self.zip.close()

    def add_override(self, path:Path):
        
        override_dir = PurePosixPath("overrides")
        relative_path = path.relative_to(self.root_dir)
        self.zip.write(path, override_dir / relative_path)   

    def add_mod(self, path:Path):

        mods_dir = PurePosixPath("mods")
        
        with open(path) as file:
            mod_info = parse_toml(file)

        mod_index = {
            "path": str(mods_dir / mod_info['filename']),
            "hashes": {mod_info['download']['hash-format']: mod_info['download']['hash']},
            "downloads": [mod_info['download']['url']]
        }

        self.index['files'].append(mod_index)

def main():

    # from argparse import ArgumentParser
    # parser = ArgumentParser(description="Python script for converting packwiz to modrinth modpack format")
    # parser.add_argument('-i', '--input', dest='input_dir', type=Path, help='Specify packwiz pack directory', required=True)
    # parser.add_argument('-o', '--output', dest='output_dir', type=Path, help='Specify output directory (optional)')
    # args = parser.parse_args()
    
    # manager = ModrinthManager(args.input_dir, args.output_dir)

    import os

    user_path = os.path.expanduser("~")
    git_path = user_path + "/Documents/GitHub/fabulously-optimized/"
    version_no = "1.18"
    packwiz_path = git_path + "Packwiz/" + version_no
    modrinth_path = git_path + "Modrinth/"

    input_dir = PurePosixPath(packwiz_path)
    output_dir = PurePosixPath(user_path + "/Desktop")
    manager = ModrinthManager(input_dir, output_dir)

    with open(input_dir / "index.toml") as file:
        index = parse_toml(file)

    for file in index['files']:
        if 'metafile' in file and file['metafile'] is True:
            manager.add_mod(input_dir / file['file'])
        else: manager.add_override(input_dir / file['file'])

    # Export index.json to git

    from json import dump
    with open(modrinth_path + "index.json", "w") as file:
        dump(manager.index, file, indent = 4)

if __name__ == "__main__":
    main()