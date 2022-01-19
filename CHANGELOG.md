# Fabulously Optimized changelog
This is the changelog for the Fabric modpack [Fabulously Optimized](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized). See the [version support FAQ](https://github.com/Madis0/fabulously-optimized/wiki/Version-support-FAQ).

## 1.18.1

Notes:
* See an error about "cloth-client-events-v0.mixins.json"? This is known, simply launch again until I find a fix. See [#192](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/192)

### 3.1.0-beta.1 (2022-01-15)

First beta for 1.18.1!

New mods
* Puzzle - adds some Optifine features like emissive mobs and resource pack-provided splash screen
* TieFix - disables telemetry and fixes some bugs
* Starlight - improves chunk performance, 75% preferred it so here it is! (1.0.0 stable version)

Removed mods
* Phosphor - replaced with Starlight as a result of the public vote
* No Telemetry - replaced with TieFix which has the same feature but can be toggled as well

Other
* Sodium got a bugfix update - fixing lag spikes, fog, memory leak and more
* Updated CIT Resewn, Cloth API, Dynamic FPS, Fabric API, Indium, Iris Shaders, Not Enough Crashes, Sodium, Sodium Extra
* Colormatic temporarily removed as it breaks with the new Sodium
* Don't Clear Chat History is still forced, Hydrogen is still removed - will not highlight in changelog anymore until something changes

### 3.1.0-alpha.7 (2022-01-07)

* Iris got a performance update, the game should run better regardless of whether you have shaders enabled.
* Updated Animatica, Colormatic, Fabric API, Iris Shaders, Reese's Sodium Options
* Currently forced (do NOT report any issues to those mods!): Don't Clear Chat History
* Currently removed Hydrogen

### 3.1.0-alpha.6 (2022-01-02)

Happy new year, time to test Phosphor! [Vote here!](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/21#issuecomment-1003749296)

* Swapped Starlight with Phosphor for testing
* Updated Architectury API, CIT Resewn, FastOpenLinksAndFolders, LambdaBetterGrass, Lithium, Not Enough Crashes, Reese's Sodium Options
* Currently forced (do NOT report any issues to those mods!): Don't Clear Chat History
* Currently removed Hydrogen

### 3.1.0-alpha.5 (2021-12-23)

Thank you for 200K downloads! Starlight testing is ongoing, [don't forget to vote](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/21#issuecomment-998162829).

* Updated Animatica, Architectury API, Fabric API
* Enabled Cull Leaves resource pack
* Slightly simplified MultiMC/MultiMC auto-update instance config
* Currently forced (do NOT report any issues to those mods!): Don't Clear Chat History
* Currently removed Hydrogen, Phosphor

### 3.1.0-alpha.4 (2021-12-20)

It's time to test Starlight! [Your vote matters, read more here!](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/21#issuecomment-998162829)

* Added Starlight for testing
* Added back Cull Leaves (oops!)
* Updated Fabric Language Kotlin, Item Model Fix, Mod Menu
* Currently forced (do NOT report any issues to those mods!): Animatica, Don't Clear Chat History
* Currently removed Hydrogen, Phosphor

### 3.1.0-alpha.3 (2021-12-15)

* Another patch for the multiplayer bug (updated Fabric Loader to 0.12.12)
* Currently forced (do NOT report any issues to those mods!): Animatica, Don't Clear Chat History
* Currently removed Hydrogen, Phosphor

### 3.1.0-alpha.2 (2021-12-14)

* Re-added Lithium
* Updated Architectury API, Cloth Config API, Custom Entity Models
* Currently forced (do NOT report any issues to those mods!): Animatica, Don't Clear Chat History
* Currently removed Hydrogen, Phosphor

### 3.1.0-alpha.1 (2021-12-11)

* 1.18.1 has fixed [the critical multiplayer bug](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition)
* Updated Wi Zoom
* Currently forced (do NOT report any issues to those mods!): Animatica, Don't Clear Chat History
* Currently removed Lithium, Hydrogen, Phosphor

## 1.18

Notes:
* MultiMC: Minecraft 1.18 requires [Java 17 or higher](https://www.oracle.com/java/technologies/downloads/). 
* GDLauncher: make sure you are using the latest version, click the green arrow in titlebar when available

### 3.0.0-alpha.4 (2021-12-15)

* Another patch for the multiplayer bug (updated Fabric Loader to 0.12.12)
* Updated Architectury API, Cloth Config API, Custom Entity Models

### 3.0.0-alpha.3 (2021-12-11)

Some fixes for 1.18 before moving to 1.18.1.

General

* Fixed [the critical multiplayer bug](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition) (updated Fabric Loader to 0.12.11)
* Fixed Continuity resource packs not being applied
* Added German and Portuguese (Brazil) translations to Mod Menu Helper by nsde and PaperKing13isPro!

Mod changes

* Added Borderless Mining - allows you to have Minecraft in full screen and interact with a different window (disabled by default)
* Added FastOpenLinksAndFolders - fixes the game freezing when you open resource pack folders, a screenshot etc.
* Updated Architectury API, Better Mount HUD, CompleteConfig, No Fade
* Re-added Enhanced Block Entities, removed the replacement FastChest
* Currently forced (do NOT report any issues to those mods!): Animatica, Don't Clear Chat History
* Currently removed Hydrogen, Phosphor

### 3.0.0-alpha.2 (2021-12-05)

Still an alpha, make backups and expect crashes.

* Added first-launch crash workaround back
* Re-added Colormatic, FerriteCore, Lithium, Smooth Boot
* Updated Cloth Config API, Continuity, Fabric API, MoreChatHistory, No Telemetry, Not Enough Crashes
* Currently forced (do NOT report any issues to those mods!): Animatica, Don't Clear Chat History, No Fade
* Currently removed Enhanced Block Entities (temp. replacement FastChest), Hydrogen, Phosphor

### 3.0.0-alpha.1 (2021-12-02)

The first 1.18 alpha is here!

Added:
* No Telemetry - prevents sending diagnostics data to Mojang; protects your privacy and modded instance data helps Mojang less anyway

Removed:
* No Potion Offset - no longer needed in 1.18
* LittleTweaks - no longer needed in 1.18

Changes:
* Iris' Max Shadow Distance reduced to 6 chunks
* Simulation Distance reduced to 6 chunks
* Alternative mods are now marked with a red asterisk on Mod Menu

Current mod changes:
* Updated: AdvancementInfo, AntiGhost, Architectury API, CIT Resewn, Cloth Config API, CompleteConfig, Entity Culling, Fabric API, Fabric Capes, Fabrishot, Indium, Iris Shaders, Mod Menu, Not Enough Crashes, Reese's Sodium Options, Sodium, Sodium Extra, ToolTipFix, WI Zoom
* Forcefully enabled (do NOT report any issues to those mods!): Animatica, Continuity, Don't Clear Chat History, MoreChatHistory, No Fade
* Temporarily removed: Colormatic, Enhanced Block Entities (temp. replacement FastChest), FerriteCore, Lithium, Hydrogen, Phosphor, Smooth Boot
* Unlisted mods either didn't require 1.18 in the first place or were cross-compatible.

## 1.17.1

### 2.6.3 (2022-01-14)

* Sodium got an update with some bugfixes, including a memory leak fix.
* Updated Fabric API, Iris Shaders, Sodium

### 2.6.2 (2022-01-07)

* Iris got a performance update, the game should run better regardless of whether you have shaders enabled.
* Updated Animatica, Architectury API, CIT Resewn, Fabric API, Fabric Language Kotlin, FastOpenlinksAndFolders, Iris Shaders, Item Model Fix, LambdaBetterGrass, Reese's Sodium Options

### 2.6.1 (2021-12-15)

* Another patch for the multiplayer bug (updated Fabric Loader to 0.12.12)
* Updated Architectury API, Cloth Config API

### 2.6.0 (2021-12-11)

General
* Fixed [the critical multiplayer bug](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition) (updated Fabric Loader to 0.12.11)
* Backported config changes from 3.0.0-alpha.3

Mods
* Added Borderless Mining - allows you to have Minecraft in full screen and interact with a different window (disabled by default)
* Added FastOpenLinksAndFolders - fixes the game freezing when you open resource pack folders, a screenshot etc.
* Updated Architectury API, Continuity, Fabric API

### 2.5.0 (2021-11-30)

Major update with Phosphor and bugfixes for Sodium and Iris!

* Sodium is updated with better performance and several bugfixes!
* Added Phosphor back
* Iris is now separate from Sodium (faster updates and better compatibility)
* Changelog now lists dates for even more transparency
* Updated AdvancementInfo, Fabric API, Fabric Language Kotlin, Indium, Iris, LambDynamicLights, Not Enough Crashes, Reese's Sodium Options, Sodium Extra

### 2.4.1 (2021-11-22)

* AdvancementInfo now has settings, you can set the colors or info box width
* Disabled 'Slight' GUI Modifications' "satisfying screenshots" to make the screenshot instantly accessible (clickable link on chat like vanilla)
* Updated Mod Menu Helper phrases a bit
* Removed irrelevant suggestions from launcher logs
* Updated AdvancementInfo, Cloth Config API, Colormatic, Not Enough Crashes
* Skipped Sodium Extra update for now due to a crash

### 2.4.0 (2021-11-10)

* Updated Fabric Loader to 0.12.5
* ~~You may start preparing your worlds for 1.18 by clicking `Edit` -> `Optimize World` -> `Create Backup and Load` in the world list.~~ Not needed anymore. [Read more](https://github.com/CaffeineMC/lithium-fabric/releases/tag/mc1.17.1-0.7.5#repo-content-pjax-container)
* Updated 'Slight' GUI Modifications, Fabric API, Lithium, LittleTweaks

### 2.3.3 (2021-11-01)

* Updated Fabric API, Fabric Capes, Language Reload

### 2.3.2 (2021-10-30)

* Updated Architectury API, CIT Resewn, Continuity, Cull Leaves, Not Enough Crashes

### 2.3.1 (2021-10-21)

* Added a small disclaimer to Mod Menu (via Mod Menu Helper)
* Disabled Mod Menu's deprecation warnings
* Configured MidnightLib (part of Cull Leaves) to be more vanilla-like
* Updated Cull Leaves, Dynamic FPS

### 2.3.0 (2021-10-19)

New mods

* **Animatica** - Optifine's animated textures!
* **ToolTipFix** - makes sure all tooltips fit to screen
* **No Potion Offset** - removes the potion offset on Creative inventory (similar to 1.18)

Other stuff

* Game will attempt to reduce RAM usage when unfocused (enabled Dynamic FPS's GC on unfocus)
* Optimized the Mod Menu Helper resource pack and MultiMC/MultiMC (auto-update) icon
* Updated Fabric Loader
* Updated Architectury API, CIT Resewn, CompleteConfig, Continuity, Fabric API, Not Enough Crashes

### 2.2.1 (2021-10-08)

2.2.0 had a bit of a rocky launch but we're back with mod updates!

* Fixed Curseforge Launcher installation (see [#140](https://github.com/Madis0/fabulously-optimized/issues/140) for more info)
* Fixed CIT Resewn config not being applied
* Added Russian translation for Mod Menu Helper by RozeFound
* Updated Architectury API, Fabric API, Fabric Language Kotlin, Language Reload, LittleTweaks, Mod Menu, Not Enough Crashes, Sodium Extra

### 2.2.0 (2021-09-29)

New mods, new Mod Menu style and a new Discord server! https://discord.gg/yxaXtaQqdB
Also known as "the update that couldn't be installed with Curseforge Launcher".

New mods

* **Continuity** - Optifine's connected textures!
* **CIT Resewn** - Optifine's custom items!
* **Enhanced Block Entities** - makes chests, signs, beds etc. render faster
* **More Chat History** - increases chat history limit
* **Don't Clear Chat History** - keeps your written message log across worlds
* **Language Reload** - makes language switching instant
* **LittleTweaks** - adds audio output menu (1.18 parity!)

Removed mods

* **FastChest** - replaced by Enhanced Block Entities
* **Better Beds** - replaced by Enhanced Block Entities

Other stuff

* Mod Menu now has a consistent list of mods' features and options (provided by a bundled resource pack)
  * Hidden Fabric Language Kotlin and Indium from Mod Menu as they are just APIs
  * Enabled children mod counting in Mod Menu (Sodium Extra and Reese's Sodium Options are now reflected)
* Reverted vanilla's particle settings defaults as they are better managed in Sodium Extra's settings anyway
* MultiMC and MultiMC auto-update now use Fabric's default Java arguments (smoother experience)
* Updated Architectury API, Colormatic, Cull Leaves, Mod Menu, Not Enough Crashes

### 2.1.1 (2021-09-11)

* Temporary fix for first launch crash
* Fixed tree leaves glitching (thanks, Altirix!) 
* Updated Fabric API

### 2.1.0 (2021-09-06)

It is time to finally release Fabulously Optimized for Minecraft 1.17.1! Here are the major updates from 1.9.1 to 2.1.0:

New mods

* **Iris** - Optifine shaders! [See here](https://github.com/IrisShaders/Iris#what-shader-packs-can-i-use-right-now) for the recommended ones.
* **LambdaBetterGrass** - Optifine's "better grass"!
* **CustomEntityModels** - Optifine's custom entity models (partial support, see mod description)
* **AdvancementInfo** - bigger and more detailed advancement screen
* **Better Mount HUD** - improves the HUD while riding a horse, like in Bedrock Edition
* **Reese's Sodium Options** - makes the graphics settings vertical to make sure all options fit and look good
* **WI Zoom** - a simple, scrollable zoom mod 
* **Indium** - adds Rendering API to Sodium, which makes some important parity mods work 
* **YOSBR** - keeps your settings across modpack updates

Removed mods

* **Ok Zoomer** - servers can now disable or limit your zoom, I think *you* should be in charge of that
* **Custom Fog** - Sodium Extra now provides a simpler fog management experience
* **Smooth Scrolling Everywhere** - seems to be abandoned
* **Phosphor** - not yet updated

Other changes

* New default options [(read more)](https://github.com/Madis0/fabulously-optimized/wiki/Changed-options)
* Curseforge pack is now 100% Fabric (faster launch and better mod management)
* An auto-updating MultiMC pack is available on GitHub
* Now using semantic versioning
* All mods updated
* For more changes between alpha and beta versions, see the changelog

### Changes from beta 4 to release

* Added AdvancementInfo, Better Mount HUD, Reese's Sodium Options
* MultiMC (auto-update) is now split by version for future-proofing, please re-download if you use it
* Updated Iris+Sodium, Lithium, Sodium Extra, Custom Entity Models, Not Enough Crashes, Mod Menu, Fabric API, Fabric Language Kotlin, Architectury API

### 2.1.0-beta.4 (2021-08-25)

Added
* LambdaBetterGrass (Optifine's "better grass"!)
* CustomEntityModels and CompleteConfig (Optifine's custom entity models, in alpha though)
* Colormatic (water/biome colors, FO 1.9.1 parity)
* FastChest and Better Beds (were removed in the previous beta)

Removed
* Enhanced Block Entities (postponing the addition due to mod compatibility bugs)

Updated mods: FerriteCore, Mod Menu, Fabric API, Architectury API

### 2.1.0-beta.3 (2021-08-12)

It's time to test Indium! Please let me know how it goes: [the poll has ended]

Changes from beta 2
* Added Indium (rendering API, allows for more parity mods in the future)
* Added Enhanced Block Entities (makes chests, signs, bells and beds render faster)
* Removed FastChest and Better Beds (replaced by Enhanced Block Entities)
* Removed Custom Fog (Sodium Extra provides a simpler experience for most people)
* Mods updated: Architectury API, Cloth Config API, Dynamic FPS, Fabric API, Fabric Capes, LambDynamicLights

Thanks for 100 000 downloads!

### 2.1.0-beta.2 (2021-07-29)

Changes from beta 1

* Replaced Sodium with Iris+Sodium for shaders and bugfixes
* Reset global graphics to Fancy to make Cull Leaves work
* Mods updated

### 2.1.0-beta.1 (2021-07-18)

Changes from alpha 3

* Added Sodium and Sodium Extra
* Removed Canvas
* Removed AntiGhost keybind to prevent accidental presses (you can use /ghost)
* Updated mods

### 2.1.0-alpha.3 (2021-07-15)

Changes from a2

* (No Sodium yet)
* Added Custom Fog back
* Enabled Cull Leaves by default
* Mods updated
* Now using semantic versioning

### 2.1.0a2 (2021-07-10)

Changes from a1

* (No Sodium yet)
* Readded 'Slight' Gui Modifications and Fabrishot
* Fixed version in the main menu
* Updated mods

### 2.1.0a1 (2021-07-08)

First alpha for 1.17.1!

* Temporarily added Canvas again because Iris+Sodium broke with 1.17.1
* Added FerriteCore back
* Removed mods that broke with 1.17.1: Iris+Sodium, 'Slight' Gui Modifications, Fabrishot
* You cannot see the version in the main menu at the moment
* Updated mods

## 1.17

Notes for all 1.17 releases:

* Curseforge Launcher: if you're upgrading from MC 1.16.x, please ☑️ Update to new Profile
* MultiMC: Minecraft 1.17 requires [Java 16 or higher](https://www.oracle.com/java/technologies/downloads/). 

### 2.0.0b4 (2021-07-01)

Differences from b3

* Added **Iris with Sodium**! (Yes, FPS boost and Optifine shaders!)
* Set the default graphics to fast for general performance improvement
* Re-enabled dynamic light for entities in LambDynamicLights
* Updated mods
* Removed Canvas
* FO is currently still in beta because 1.17.1 is coming soon and Sodium Extra is not there yet

### 2.0.0b3 (2021-06-21)

Differences from b2

* (No Sodium yet)
* Added Hydrogen, No Fade, Not Enough Crashes back
* Mods updated
* Experimental auto-updating MultiMC pack is available on Github, try it out! (packwiz by comp500)

### 2.0.0b2 (2021-06-17)

Differences from b1
* Sodium is not there yet, please have patience
* Mods updated, should fix some graphics issues
* Added Fabrishot back
* Inclusion of Not Enough Crashes is delayed because it is still an alpha
* Reverted FOV change for better FPS in some devices
* Fixed an issue that could show the wrong version number in the main menu

### 2.0.0b1 (2021-06-10)

Mods
* Several mods still missing, including Sodium
* Sodium temporarily replaced with Canvas
* Ok Zoomer temporarily/permanently replaced with WI Zoom
* Added YOSBR to keep your settings between modpack upgrades
* More new mods will come in a stable release!

Other
* Added [new default options](https://github.com/Madis0/fabulously-optimized/wiki/Changed-options) to improve the experience
* CF version is now 100% Fabric, meaning faster startup and better mod management!

## 1.16.5

### 1.12.0 (2022-01-19)

Individual shader settings can now be configured!

* Updated Architectury API, Cloth API, Iris Shaders, Not Enough Crashes

### 1.11.2 (2022-01-07)

* Iris got a performance update, the game should run better regardless of whether you have shaders enabled.
* Updated FastOpenLinksAndFolders, Iris Shaders, Item Model Fix, Reese's Sodium Options
* Skipped Architectury API update as something broke in its last few versions for 1.16.5

### 1.11.1 (2021-12-15)

* Another patch for the multiplayer bug (updated Fabric Loader to 0.12.12)
* Updated Architectury API, Cloth Config API

### 1.11.0 (2021-12-11)

General
* Fixed [the critical multiplayer bug](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition) (updated Fabric Loader to 0.12.11)
* Backported config changes from 3.0.0-alpha.3
* Hydrogen warns you when you're using incompatible Java

Mods
* Added Borderless Mining - allows you to have Minecraft in full screen and interact with a different window (disabled by default)
* Added FastOpenLinksAndFolders - fixes the game freezing when you open resource pack folders, a screenshot etc.
* Added Reese's Sodium Options
* Iris is now separate from Sodium
* Updated Architectury API, Cloth Config API, Fabric API, Fabric Language Kotlin, Iris Shaders, Not Enough Crashes, Phosphor, Sodium Extra

### 1.10.0 (2021-11-01)

An unexpected backport update that matches the mods with 2.3.2 ones, released because 1.9.1 got broken due to a Java 16 and Jumploader issue. For the best experience I recommend upgrading to the latest version though.

* Updated all mods
* Added AdvancementInfo, Better Mount HUD, Cloth API, Custom Entity Models, Indium, Iris Shaders, LambdaBetterGrass, No Potion Offset, ToolTipFix, WI Zoom, YOSBR
* Removed Jumploader, Ok Zoomer, Smooth Scrolling Everywhere
* Added Mod Menu Helper
* Applied configs from 2.3.2
* Now uses native Fabric Loader 0.11.7 (0.12.3 is still in beta)
* Hydrogen is disabled by default in MultiMC version to be compatible with Java 16 (vanilla launcher uses bundled Java 8 anyway)
* Made a MultiMC auto-update version in Github ¯\\\_(ツ)_/¯

### 1.9.1 (2021-05-27)

* Several mods updated
* Sodium Extra update skipped because it temporarily changes the UI

### 1.9.0 (2021-05-04)

New mods
* **FerriteCore** - reduces RAM usage 
* **LazyDFU** - improves startup speed even more
* **Better Beds** - improves FPS when around beds (villager farms, anyone?)
* **Item Model Fix** - fixes transparent gaps in held items

Removed mods
* **Raised Clouds** - Sodium Extra now includes a more intuitive cloud height setting

Other stuff
* Lots of mod updates
* The new mods were suggested by the community, thank you!

### 1.8.0 (2021-04-02)

New mods
* **EntityCulling Fabric/Forge** - stops rendering entities that are behind a wall, useful in large servers and mobfarms

Other stuff
* SmoothBoot's config system slightly changed and it is now smaller
* Mods updated

### 1.7.1 (2021-03-07)

New mods:
* **No Fade** - makes game startup and resourcepack loading faster by removing some animations

Other stuff
* Sodium Extra got an update with many new toggles, check them out!
* Jumploader got support for Microsoft Accounts, so you can upgrade now when Mojang asks you to (only if you use CF or vanilla launcher)
* Fixed zoom key by unbinding the save toolbar activator by default (that option was always there... oops)
* 25k download milestone! Thank you all for the support!
* Mods updated
* Yes, I added another new mod but I felt like that one didn't warrant a new major update lol, it also might get included with 'Slight' Gui Modifications later on

### 1.7.0 (2021-03-02)

New mods:
* **Hydrogen** - somewhat reduces RAM usage (in my case 2,8 GB -> 2,6 GB)

Other stuff:
* Several mods updated
* The modpack size is much bigger for Curseforge now, because Hydrogen is an external mod
* Sodium Extra update currently skipped as the next version will fix an issue
* Cull Leaves changed the way its config works - if you are upgrading, you may delete the json5 file

### 1.6.0 (2021-02-18)
New mods
* **Sodium Extra** - adds toggles to Sodium settings: animations, particles, weather, fog, FPS indicator
* **Cloth Config API** - makes the config work in many mods, now it is separate to reduce space (every mod doesn't have to include it)

Other stuff
* Updated mods

### 1.5.2 (2021-02-07)
* Hid Minecraft, Jumploader and Cloth API from Mod Menu (because they are not really mods, but dependencies)
* Updated mods

### 1.5.1 (2021-02-01)
* Mod Menu received a major configurability update, so I've made it more cleaner-looking
* Removed Better Mod Button mod as it is now redundant 
* Not Enough Crashes received a lot of updates for better detection and compatibility
* Updated mods

### 1.5.0 (2021-01-24)
New mods
* **FastChest** - greatly improves FPS when surrounded by chests (e.g. in a storage room)
* **Cull Leaves** - optionally makes fancy tree leaves more see-through, which could improve FPS (enable in mod settings)

Other stuff
* Dynamic FPS and Custom Fog have new config screens, tweak ahead!
* Fancy introduction video - see main page!
* Slightly improved manifests for both launchers
* Updated mods
* MultiMC: Not Enough Crashes is 2.1.4+1.16.2 due to CF error

### 1.5.0b2 (2021-01-21)
* Mods updated
* Improved manifests for both launchers
* Dynamic FPS now has a config screen so it can be disabled or configured
* Lithium and Custom Fog are missing, waiting for an update
* MultiMC: Not Enough Crashes is 2.1.4+1.16.2 due to CF error

### 1.5.0b1 (2021-01-15, 2021-01-16)
* Lithium and Custom Fog are currently incompatible and therefore missing
* Mods updated
* MultiMC doesn't list 1.16.5 yet, so I cannot update it (Edit: added later, same Not Enough Crashes comment applies)

## 1.16.4

### 1.4.5 (2021-01-04)
* Mods updated
* You may notice that there are less mods now - this is normal as some APIs are now properly marked as such, the main mods are still the same
* Curseforge: fixed Fabric Loader update
* MultiMC: Not Enough Crashes is 2.1.4+1.16.2 due to CF error

### 1.4.4 (2020-12-20)
* Mods updated
* MultiMC: Not Enough Crashes is 2.1.4+1.16.2 due to CF error

### 1.4.3 (2020-12-15)
* Mods updated
* MultiMC: Not Enough Crashes is 2.1.4+1.16.2 due to CF error

### 1.4.2 (2020-11-27)
* Mods updated
* Added Architectury because 'Slight' Gui Modifications now depends on it
* In MultiMC, Not Enough Crashes is at version 2.1.4+1.16.2 (due to CF error) but according to the developer it is identical to newer anyway.

### 1.4.1 (2020-11-15)
* Mods updated

### 1.4.0 (2020-11-11)
**Now stable with more ways to optimize!**

Added
* Smooth Boot - makes the game use less power when it starts
* Custom Fog - lets you customize the fog distance and density
* AntiGhost - fixes getting stuck in blocks with the press of G

Other
* Lithium is back
* Mods updated

### 1.4.0b2 (2020-11-06)
* Lithium is currently incompatible and therefore missing
* Mods updated

### 1.4.0b1 (2020-11-02)
**Fastest beta release yet, thanks to Jumploader magic!**
* Lithium is currently incompatible and therefore missing
* Mods updated

## 1.16.3

### 1.3.4 (2020-10-23)
* Added a clickable modpack version to title screen (courtesy of 'Slight' Gui Modifications)
* Adjusted Fabric Capes config to show all types and default to Minecraft Capes
* Removed Minecraft Capes mod because Fabric Capes already provided it
* Mods updated

### 1.3.3 (2020-10-13)
* Mods updated

### 1.3.2 (2020-09-30)
* Colormatic readded.

### 1.3.1 (2020-09-29)
Thanks to users' feedback, the mod list has been updated.

**Added**
* Ok Zoomer - fancy zooming mod, back by a popular demand (configurable)
* Fabric Capes - gives options for viewing Optifine, LabyMod and MinecraftCapes' capes in-game
* Fabric Language Kotlin - needed for Fabric Capes

**Removed**
* OF Capes - replaced by Fabric Capes

### 1.3.0 (2020-09-28)
Sodium has been updated, so it's time for a release!

**Added**
* OF Capes - lets you see Optifine capes and zoom
* MinecraftCapes - lets you get a free cape, textured elytra or mouse ears (configurable)
* Raised Clouds - lets you adjust the cloud height like Optifine (configurable)
* Fabrishot - lets you take a high-res screenshot like Optifine (press F9, configurable)

**Removed**
* motioNO - now built-in, find it under Accessibility Settings... > FOV Effects
* Ok Zoomer - OF Capes mod also provides zoom, so it is not needed
* Colormatic - currently crashes with Sodium, will readd after an update

Other
* Mods updated

### 1.3.0b1 (2020-09-26)
**First beta with Twitch launcher.**
* Sodium still missing
* Canvas added as replacement
* TheYTG123 helped me get a Twitch Launcher-compatible version even though it wasn't listed. Hint: Jumploader manifest.
* Mods updated

### 1.3.0a1 (MultiMC, 2020-09-12)
First alpha version only for MultiMC, stuck next to 1.16.2 versions because Twitch launcher did not list that version yet.
**Notes**
* Sodium and Lithium are missing
* Canvas temporarily added as a replacement
* motioNO is removed

## 1.16.2

### 1.2.0b2 (2020-09-08)
**Notes**
* Sodium still missing
* Canvas temporarily added
* Mods updated

### 1.2.0b1 (2020-08-26)
**First beta for 1.16.2.**
* Sodium is missing
* Canvas added as a temporary replacement. Thanks fishywishyef for the suggestion!
* motioNO is removed as it is built-in to 1.16.2.

### 1.2.0a1 (MultiMC, 2020-08-15)
A never-released version because Curseforge doesn't like MultiMC-only versions. Ah well.

## 1.16.1

### 1.1.2 (2020-08-10)
* Mods updated

### 1.1.1 (2020-08-01)
* Mods updated

### 1.1.0 (2020-07-24)
Major update with new mods.
**Added**
* Dynamic FPS - renders Minecraft slower if it is in the background to save memory
* Smooth Scrolling Everywhere - makes the scrolling smooth on various menus
* 'Slight' Gui Modifications - adds fancy animations to the menus and containers
* Colormatic - adds support for Optifine resource packs' custom colors

### 1.0.1 (2020-07-21)
Updated mods. 
**MultiMC-specific:**
* Replaced Jumploader and Forge with real Fabric
* Added icon

### 1.0.1a1 (2020-07-21)
A testing version to see if making mods optional is handled well in Twitch launcher. Hint: it isn't.

### 1.0.0 (2020-07-17)
First release for Twitch and MultiMC launchers. Containing:
* Better Mod Button
* Fabric API
* Jumploader
* LambDynamicLights
* Lithium (Fabric)
* Mod Menu
* motioNO
* Not Enough Crashes
* Ok Zoomer
* Phosphor (Fabric)
* Sodium
