# Fabulously Optimized repository

Welcome to my repository.
Here you'll find the resources for:

* Curseforge modpack [(read more)](https://support.curseforge.com/en/support/solutions/articles/9000196904-creating-a-custom-profile)
* MultiMC modpack [(read more)](https://github.com/MultiMC/MultiMC5/wiki/Instance-settings)
* MultiMC modpack with packwiz [(read more)](https://github.com/comp500/packwiz#packwiz-installer-for-pack-installation)
* Packwiz files [(read more)](https://github.com/comp500/packwiz#packwiz)
* Modrinth files [(read more)](https://github.com/Madis0/fabulously-optimized/issues/63)
* Changelog, license, readme, [cape](https://github.com/Madis0/fabulously-optimized/wiki/Free-cape)
* GitHub meta files in `.github` [(read more)](https://stackoverflow.com/a/61301254)
* GitHub page in `docs` [(read more)](https://pages.github.com/) - currently just a redirection to CF page

Other things to note:

* As seen in the `.gitignore` file, this repo will not include JAR files of any kind to respect the modders. If you want to build a pack based on this, get the JARs manually via any method you like (Curseforge launcher, Curseforge website, Modrinth, packwiz, ...).
   * Because there are no JARs, some folders would usually not be uploaded by Git at all, this is worked around using a `.gitkeep` file [(read more)](https://stackoverflow.com/a/7229996) to keep the folder structure.
* Since some folders are duplicated - such as config folders, I am using Windows-like soft symlinks [(read more)](https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/). Those don't work very well in GitHub, so I recommend using a [local Git client](https://desktop.github.com).

### Build process

Contact us in Discord if you have ideas on how to streamline this process while still testing the pack in the launchers.

1. Download the latest modpack version to Curseforge Launcher
2. Do changes, test
3. Export to ZIP manually via Curseforge Launcher's option
4. Copy to MultiMC using `Curseforge to MultiMC-Git.py`
   * If needed, change the Minecraft version in the script
5. Run it in MultiMC, test
6. Export to ZIP manually via MultiMC's option
   * (Optionally) Run `MultiMC to Git.py` to reflect any manifest updates in Git
5. Run `Curseforge to Packwiz-Modrinth.py`
   * If needed, change the Minecraft version or variables in the script
7. Drag the exported Curseforge ZIP to the console window and hit enter - Packwiz changes will be made and Modrinth ZIP will be exported
8. Publish manually to Github, Curseforge, Modrinth
9. Announce on modpack's Discord, Fabric's Discord
