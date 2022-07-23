# Fabulously Optimized changelog
This is the changelog for the Fabric modpack [Fabulously Optimized](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized). See the [version support FAQ](https://fabulously-optimized.gitbook.io/modpack/readme/version-support).

## 1.19

### 4.0.0-beta.11 (2022-07-21)

Another beta, now with FPS stuff! 
Also, 1.19.1-rc2 is out, with 1.19.1 release date being estimated as "next week". Let's see...

- Added More Culling - stops rendering hidden sides of blocks
  - Item frame optimizations currently disabled because it doesn't work with custom items yet
  - It may eventually obsolete Cull Less Leaves, to be tested
  - Mod Menu Helper does not currently work with it, so you'll see its own description in Mod Menu
- Removed Don't Clear Chat History - various issues, including unintended behaviour in 1.19

- Updated Debugify, Fabric Language Kotlin, MemoryLeakFix, Reese's Sodium Options
- Removed duplicate config files from YOSBR folder
  - This was there to make resetting settings a bit easier when needed, but now a better method is described in the wiki
- Updated Greek in MMH by RaptaG

### 4.0.0-beta.10 (2022-07-19)

- Added Mixin Conflict Helper - tells you when you've installed two mods that don't like each other!
- Updated MemoryLeakFix

### 4.0.0-beta.9 (2022-07-14)

- Updated Cull Less Leaves, Mod Menu, OptiGUI
- Added small wording fix for MMH
- Slightly reordered resource packs

### 4.0.0.beta.8 (2022-07-09)

- Updated Borderless Mining, Lithium, MidnightControls, Puzzle
  - Lithium fixed a critical portal linking issue, others have bugfixes as well
- Updated Portuguese in MMH by PaperKing13isPro
- Modrinth version no longer includes JARs, only download links
  - It means the Modrinth version is becoming more sustainable as mods are cross-posting to it :)

### 4.0.0-beta.7 (2022-07-05)

- Updated Greek and Portuguese in MMH by RaptaG and PaperKing13isPro
- Enabled Bedrock resource pack for MidnightControls

### 4.0.0-beta.6 (2022-07-02)

As you might know, 1.19.1 was postponed with the release date of "soon". This affects FO as well because there are bugs that need fixing, I can't really consider 1.19 "stable" yet. 
In the meanwhile, I've added a treat for the controller/touchscreen fans: MidnightControls. Enjoy testing!

- Added MidnightControls - controller and touchscreen support!
- Updated CIT Resewn, Fabric API, Fabric Language Kotlin, Item Model Fix, No Chat Reports
- Removed LambdaBetterGrass from incompatible resource packs in options.txt as it is no longer incompatible

### 4.0.0-beta.5 (2022-06-26)

- Readded Animatica
- Updated Fabric API, Fabric Capes, Main Menu Credits, No Chat Reports, Zoomify
  - Zoomify config got removed as FO defaults are that mod's defaults now
  - AntiGhost is now described in the pause menu
- Updated Russian in MMH by RozeFound

### 4.0.0-beta.4 (2022-06-22)

- Added No Chat Reports - protects you and others from some account bans
  - Mostly a preparation for 1.19.1, but helps a bit on 1.19 too
- Updated Debugify, Enhanced Block Entities, Fabric Capes, Farsight
  - Enabled fix for MC-22882 - Ctrl+Q won't work on Mac
- Slightly updated Estonian in MMH

---

- Temporarily removed Animatica

### 4.0.0-beta.3 (2022-06-20)

* Updated Entity Texture Features, Fabric API, Indium
  * Entity Texture Features got an important performance fix

---

* Forcefully enabled (don't report bugs to their devs!): Farsight
* Temporarily removed Animatica

### 4.0.0-beta.2 (2022-06-19)

* Readded Enhanced Block Entities
* Removed Better Beds
* Updated Entity Texture Features, Language Reload, Starlight
  * Fixed multiple languages resetting on restart
* Updated Greek in MMH by RaptaG
* Removed some irrelevant log warnings
  * Mentioned FO in logs for better debugging, don't be alarmed if you're already using the latest version
* Updated Fabric Loader to 0.14.8

---

* Forcefully enabled (don't report bugs to their devs!): Farsight
* Temporarily removed Animatica

### 4.0.0-beta.1 (2022-06-16)

Yay, a beta! Note that Minecraft 1.19.1 is coming soon, so the process may start all over again, depending on how many changes are needed to mods.

* Updated Borderless Mining, Indium, LambdaBetterGrass
* Removed disabled mods for better UX on GDLauncher and MultiMC (auto-update)
  * I will probably still include disabled mods in future alphas because it's easier for me to iterate this way, but will avoid it in beta and stable
* Fixed Don't Clear Chat History in Modrinth version

---

* Forcefully enabled (don't report bugs to their devs!): Farsight
* Temporarily removed Animatica, Enhanced Block Entities
* Temporarily added Better Beds

### 4.0.0-alpha.5 (2022-06-15)

* Updated Borderless Mining, Debugify, Entity Texture Features, Fabric API, Fabric Capes, Language Reload, Puzzle
* You can now select multiple languages in the language menu, helps with partial (mod) translations.
   * Cool or confusing? Please let me know!
* Fixed some punctuation in Mod Menu Helper for all languages

---

* Forcefully enabled (don't report bugs to their devs!): Farsight
* Temporarily disabled Animatica, Enhanced Block Entities, LambdaBetterGrass
* Temporarily added Better Beds
* Note: some not-yet-updated mods may lack the config button in Mod Menu.

### 4.0.0-alpha.4 (2022-06-12)

* Updated AdvancementInfo, AntiGhost, Don't Clear Chat History, Dynamic FPS, Fabrishot, MemoryLeakFix, Puzzle, Zoomify
* Removed separate Architectury API, Cloth API, Cloth Config, CompleteConfig, MidnightLib as they don't seem to be necessary right now
  * Either dependant mods are removed or these are already bundled inside some, some may be readded later when necessary
  * Removal of Cloth API should also mean that there is no more first-time crash, yay!
* Borderless Mining is now disabled as it was indeed found incompatible
* Disabled Entity Culling donor features

---

* Forcefully enabled (don't report bugs to their devs!): Farsight
* Temporarily disabled Animatica, Borderless Mining, Enhanced Block Entities, LambdaBetterGrass
* Temporarily added Better Beds
* Note: some not-yet-updated mods may lack the config button in Mod Menu.

### 4.0.0-alpha.3 (2022-06-10)

Updates!

* Seems that the Sodium-related mods now stay enabled
* Updated Architectury API, CIT Resewn, Entity Culling, Fabric API, Fabric Language Kotlin, FerriteCore, Indium, LambDynamicLights, Lithium, More Chat History, Not Enough Crashes
* Updated Fabric Loader to 0.14.7
* Re-enabled Continuity, which now supports emissive block textures!

---

* Forcefully enabled (don't report bugs to their devs!): Borderless Mining, Don't Clear Chat History, Farsight
* Temporarily disabled Animatica, AntiGhost, Cloth API, Enhanced Block Entities, LambdaBetterGrass, Puzzle
* Temporarily added Better Beds


### 4.0.0-alpha.2 (2022-06-08)

This needed a quick fix, so download again please.

* Updated Architectury API, Entity Culling
* ~~Actually enabled Sodium and related mods~~ Failed, see Discord for help
* Disabled Continuity as it causes a crash without Indium

---

* Forcefully enabled (don't report bugs to their devs!): Borderless Mining, Don't Clear Chat History, Farsight, FerriteCore, More Chat History
* Temporarily disabled Animatica, AntiGhost, CIT Resewn, Cloth API, Continuity, Enhanced Block Entities, Indium, Lithium, LambDynLights, LambdaBetterGrass, Not Enough Crashes, Puzzle
* Temporarily added Better Beds

### 4.0.0-alpha.1 (2022-06-08)

First alpha for 1.19! It is an alpha mainly because connected textures and other resource pack features don't work yet.

Mods
* Updated Architectury API, Cloth Config API, Colormatic, CompleteConfig, Continuity, Cull Less Leaves, Custom Entity Models, Debugify, Entity Texture Features, Fabric Capes, Iris Shaders, Language Reload, LazyDFU, MemoryLeakFix, MidnightLib, Mod Menu, OptiGUI, Reese's Sodium Options, Smooth Boot, Sodium, Sodium Extra, Starlight, TooltipFix, Zoomify
* Forcefully enabled (don't report bugs to their devs!): Borderless Mining, Don't Clear Chat History, Entity Culling, Farsight, FerriteCore, More Chat History
* Temporarily disabled Animatica, AntiGhost, CIT Resewn, Cloth API, Enhanced Block Entities, Indium, Lithium, LambDynLights, LambdaBetterGrass, Not Enough Crashes, Puzzle
* Temporarily added Better Beds
* Other mods worked as-is

Other
* Disabled chatPreview vanilla setting for privacy and to remove annoying warnings
* Enabled Cloaks+ in Fabric Capes
* Disabled Iris' update checker

## 1.18.2

### 3.12.0 (2022-07-14)

- Added MidnightControls - controller and touchscreen support!
  - Enabled Bedrock resource pack
- Updated Puzzle
  - Removed the workaround resource pack
- Backported Portuguese MMH update; added small wording fix for Eng/Est
- Modrinth version no longer includes JARs, only download links

### 3.11.0 (2022-07-05)

- Updated Animatica, CIT Resewn, Enhanced Block Entities, Fabric API, Fabric Language Kotlin, Main Menu Credits, Mod Menu
- Added a workaround resource pack for monochrome splash screen (fixes PuzzleMC/Puzzle#34)
- Backported some 4.0.0-betas changes:
  - MMH updates
  - AntiGhost is now described in the pause menu
  - Removed LambdaBetterGrass from incompatible resource packs
- Enforced Fabric Loader 0.14.8

### 3.10.1 (2022-06-20)

* Updated Enhanced Block Entities, Entity Texture Features, Fabric API, Indium
  * Entity Texture Features got an important performance fix
* Updated Fabric Loader to 0.14.8
* Backported 4.0.0-beta.2 changes: Greek update, FO mention in logs

### 3.10.0-mr.1 (2022-06-15)

* Should now be identical to the CF version (Don't Clear Chat History was missing)

### 3.10.0 (2022-06-15)

* Updated CIT Resewn, Entity Texture Features, Fabric API, Fabric Language Kotlin, LambdaBetterGrass
* Removed separate Architectury API, Cloth API, Cloth Config, CompleteConfig, MidnightLib as they don't seem to be necessary right now
  * Either dependant mods are removed or these are already bundled inside some, some may be readded later when necessary
  * Removal of Cloth API should also mean that there is no more first-time crash, yay!
* Fixed some punctuation in Mod Menu Helper for all languages
  * Brought back the Puzzle MMH workaround as it was actually not fixed in 1.18.2 yet
* Enforced Fabric Loader 0.14.7

### 3.9.3 (2022-06-09)

* Updated Architectury API, Continuity, Iris Shaders, MidnightLib, Reese's Sodium Options, Sodium Extra
* Continuity now supports emissive block/item textures!
* Iris should now have better performance
* Disabled Iris' update checker
* Updated Fabric Loader to 0.14.7

### 3.9.2 (2022-06-06)

* Updated Fabric API, Puzzle, MidnightLib
* Resource pack splash screens should work better now
* Updated Korean and Greek in MMH by AlphaKR93 and RaptaG
* Removed Puzzle workaround from MMH

### 3.9.1 (2022-06-04)

* Updated MemoryLeakFix to fix a crash
* Updated Russian in MMH by RozeFound

### 3.9.0 (2022-06-03)

* Added MemoryLeakFix - does what the name says, haha
* Updated Architectury API, Debugify, Entity Texture Features, Fabric API
* Enabled MC-112730 and MC-228976 fixes on Debugify
* Enabled smoother animation for Zoomify
* Updated Russian in MMH by RozeFound
* Enforced Fabric Loader 0.14.6
* Removed memory and JVM flags from MultiMC and MultiMC (auto-update) to let the launcher handle them

### 3.8.3-mr.1 (2022-05-31)

The next integrity test is up. Known differences:

* Farsight is missing, install link below
* DCCH uses a near-identical fork
* Cloth Config API is slightly outdated (shouldn't affect the experience)
* Config folder is 5 bytes larger (because version name lol)

Instructions

1. Install MultiMC, update to development branch
2. Install 3.8.3-mr.1 through the launcher or https://modrinth.com/modpack/fabulously-optimized/version/3.8.3-mr.1
3. Install Farsight to the pack: https://www.curseforge.com/minecraft/mc-mods/farsight-fabric/files/3778514
4. Install 3.8.3: https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files/3807874
4. Report any _additional differences between the two FO versions_ in Discord. If you're having generic issues, make sure they are reproducible in normal 3.8.3 and report to #support/GitHub instead. 

### 3.8.3 (2022-05-28)

* Updated Architectury API, Entity Texture Features, Fabric API, OptiGUI
* Lots of improvements for Entity Texture Features, including a memory leak fix
* Fixed an issue where some resource packs didn't work
* Removed an irrelevant console warning for Debugify

### 3.8.2-mr.1 (2022-05-25)

**3.8.2: the Modrinth integrity test 1**

This is essentially the same 3.8.2 as released in CurseForge, but unlike the previous versions which used 100% CurseForge links, this uses zero. 
All mods are either sourced from Modrinth, GitHub or bundled, if their license allows.

**Goal? Test the differences between this and the normal 3.8.2 to determine the feasibility of minimal CF dependency.**

1. Install MultiMC, update to development branch
2. Install 3.8.2-mr.1 through the launcher or https://modrinth.com/modpack/fabulously-optimized/version/3.8.2-mr.1
3. Install Farsight to the pack: https://www.curseforge.com/minecraft/mc-mods/farsight-fabric/files/3778514
4. Install 3.8.2: https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files/3801677
4. Report any _differences between the two FO versions_ in Discord. If you're having generic issues, make sure they are reproducible in normal 3.8.2 and report to #support/GitHub instead. 

### 3.8.2 (2022-05-22)

* Updated Architectury API, Cull Less Leaves, Fabric API, Lithium, Main Menu Credits, Sodium Extra, Zoomify
* Updated Fabric Loader to 0.14.6
* Removed the Sodium Extra's sculk sensor animation toggle workaround

GDLauncher, MultiMC (auto-update) and Modrinth are temporarily unsupported until further notice.
Edit: MultiMC (auto-update) is now up.

### 3.8.1 (2022-05-14)

* Updated Architectury API, Mod Menu, OptiGUI
* Fixed the Sculk Sensor toggle being disabled in Sodium Extra's Animations tab (video settings)
* Updated Greek, Korean MMH translations by AlphaKR93, RaptaG

### 3.8.0 (2022-05-09)

* Added OptiGUI - OptiFine custom GUI support in resourcepacks!
* Swapped the Architectury API with the new listing
* Updated Architectury API, Cloth Config API, Debugify, Fabric Capes, Farsight
* Updated Fabric Loader to 0.14.5
* Enabled Cosmetica cape in Fabric Capes
* Updated Greek, Korean, Russian MMH translations by AlphaKR93, RaptaG, RozeFound
* Relicensed the modpack under BSD-3-Clause (tl;dr: use a different name when you fork)

### 3.7.0 (2022-05-02)

Mods

* Added Main Menu Credits - a small mod for the version number in title screen
* Added Cull Less Leaves - looks better and has better Sodium integration, including a toggle in the video settings
* Removed 'Slight' Gui Modifications - now redundant
* Removed Cull Leaves - now redundant
* Updated Architectury API, CompleteConfig

Other 

* Overall the modpack is now 26% smaller
* Optimized all mod configs
* Disabled Better Snow of LambdaBetterGrass as it looked out of place with resource packs
* Updated Fabric Loader to 0.14.4

### 3.6.1 (2022-04-27)

* Updated Iris to fix several bugs
* Updated Mod Menu Helper's Russian by RozeFound
* Updated Fabric Loader to 0.14.3 in supported launchers

### 3.6.0 (2022-04-25)

Lots of fixes and mod updates!

* Removed No Telemetry, enabled the respective setting in Debugify instead
* Updated Architectury API, Borderless Mining, Debugify, Fabric API, Fabric Language Kotlin, FerriteCore, Indium, Iris Shaders, Mod Menu, Not Enough Crashes
* Updated Fabric Loader to 0.14.2
* Replaced Cloth Config with the new CurseForge listing one
* Updated Mod Menu Helper's Russian and Portuguese (Brazil) translations by RozeFound and PaperKing13isPro, respectively
* Disabled "Always Defer Chunk Updates" in Sodium as it caused more issues than it fixed

### 3.5.0 (2022-04-14)

* Added No Telemetry - smaller mod that does one job
* Removed TieFix - now redundant by Debugify (except for the telemetry)
* Updated Architectury API, Debugify, Entity Culling, Fabric API, Fabric Capes, Mod Menu
* Fabric Capes received several bugfixes, should work smoother now
* Enabled fix for MC-89146 - Pistons forget update when being reloaded
* Disabled Debugify's update checker

### 3.4.1 (2022-04-06)

* Updated Debugify, Fabric Language Kotlin, Sodium Extra
* Enabled fixes for MC-140646, MC-199467, MC-235035 (details in wiki)
* Default-disabled FPS limit for improved UX when VSync is disabled by the user (on fast computers/monitors)
* Credit where due: 3.4.0 also got Turkish for Mod Menu Helper by egeesin!

### 3.4.0 (2022-04-03)

Thank you for over 300 000 downloads on CurseForge! 🎉🎉🎉

We have a new fancy wiki where everyone can contribute: https://fabulously-optimized.gitbook.io/

Added mods

* Debugify - a selection of bugfixes, see the FO wiki for which ones are applied

Removed mods

* FastOpenLinksAndFolders - made redundant by Debugify
* Forget Me Chunk - made redundant by Debugify

Other news
* Updated Architectury API, Entity Texture Features, Zoomify
* Enabled relative sensitivity for Zoomify
* Disabled entities on LambDynamicLights for improved performance

### 3.3.0 (2022-03-27)

Fabulously Optimized is now ready for 1.18.2! 

New mods
* Farsight - keeps rendered long-distance chunks visible on servers
* Forget me Chunk - fixes some chunk border lag spikes

Other major changes
* Enabled Always Defer Chunk Updates on Sodium for additional performance gains
* Added Greek translation to Mod Menu Helper by RaptaG!
* Added Korean translation to Mod Menu Helper by AlphaKR93!

Changes from beta 3
* Updated Architectury API, CompleteConfig, Custom Entity Models, Don't Clear Chat History, Entity Texture Features
* Re-added Enhanced Block Entities, Colormatic
* Removed Better Beds and FastChest
* Removed DCCH workaround as it now works with 1.18.2 directly

### 3.3.0-beta.3 (2022-03-20)

* Added Farsight for testing and voting
* Removed Bobby
* Added Greek translation to Mod Menu Helper by RaptaG!
* Unblanked empty option buttons in Puzzle
* Updated Architectury API, CIT Resewn, Entity Texture Features, Puzzle
* Temporarily added: Better Beds, FastChest (replacement for Enhanced Block Entities)
* Temporarily removed: Colormatic, Enhanced Block Entities

### 3.3.0-beta.2 (2022-03-14)

Time for another public mod vote! Read more here.

* Added Bobby for testing and voting
* Added ForgetMeChunk which fixes some chunk border lag spikes
* Re-added AdvancementInfo, AntiGhost, Smooth Boot
* Updated Architectury API, Entity Texture Features, Fabric API, Iris Shaders, Not Enough Crashes, Puzzle
* Removed Advancements Enlarger as AdvancementInfo is back
* Enabled Always Defer Chunk Updates on Sodium for additional performance gains
* Puzzle update fixed the crash on macOS
* Fixed incompatible mods crash on GDLauncher
* Temporarily added: Better Beds, FastChest (replacement for Enhanced Block Entities)
* Temporarily removed: Colormatic, Enhanced Block Entities

### 3.3.0-beta.1 (2022-03-11)

Time for a beta as the most visible mods are all updated.

* Re-added LambdaBetterGrass
* Updated Entity Texture Features, Reese's Sodium Options, Sodium Extra, Zoomify
* Temporarily added: Better Beds, FastChest (replacement for Enhanced Block Entities), Advancements Enlarger (replacement for AdvancementInfo)
* Temporarily disabled/removed: AdvancementInfo, AntiGhost, Colormatic, Enhanced Block Entities, Smooth Boot

### 3.3.0-alpha.5 (2022-03-08)

* Updated Entity Texture Features to fix the player rendering crash
* Updated Zoomify

### 3.3.0-alpha.4 (2022-03-07)

**Player rendering crash has been discovered, this version has been reverted from CurseForge.**

* Re-added 'Slight' GUI Modifications, Continuity
* Main menu version text is back
* Updated Entity Texture Features, Fabric API, Zoomify
* Updated Entity Texture Features config and Mod Menu Helper string
* Temporarily disabled/removed: AdvancementInfo, AntiGhost, Colormatic, Enhanced Block Entities, LambdaBetterGrass, Smooth Boot

### 3.3.0-alpha.3 (2022-03-04)

* Re-added Entity Texture Features, Lithium, FerriteCore
* Updated Architectury API, Fabric API, Fabrishot
* Sodium and Sodium Extra were disabled for some reason, this is now fixed
* Temporarily disabled/removed: 'Slight' Gui Modifications, AdvancementInfo, AntiGhost, ARRP, Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass, Smooth Boot

### 3.3.0-alpha.2 (2022-03-02)

Sodium and friends are back!

* Updated Architectury API
* Re-added Indium, Iris Shaders, Reese's Sodium Options, Sodium, Sodium Extra
* Temporarily disabled/removed: 'Slight' Gui Modifications, AdvancementInfo, AntiGhost, ARRP, Colormatic, Continuity, Enhanced Block Entities, Entity Texture Features, FerriteCore, LambdaBetterGrass, Lithium, Smooth Boot

### 3.3.0-alpha.1 (2022-03-01)

It... runs? Half of the mods are missing though, it's so alpha that it doesn't even have a version text in the main menu.

* Updated Architectury API, Cloth API, Fabric API, Mod Menu, Starlight
* Temporarily disabled/removed: 'Slight' Gui Modifications, AdvancementInfo, AntiGhost, ARRP, Colormatic, Continuity, Enhanced Block Entities, Entity Texture Features, FerriteCore, Indium, Iris Shaders, LambdaBetterGrass, Lithium, Reese's Sodium Options, Smooth Boot, Sodium, Sodium Extra
* Other mods seem to work as-is

## 1.18.1

Notes:
* See an error about "cloth-client-events-v0.mixins.json"? This is known, simply launch again until I find a fix. See [#192](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/192)

### 3.2.6 (2022-03-14)

* Updated Entity Texture Features, Puzzle
* Puzzle update fixed the crash on macOS

### 3.2.5 (2022-03-08)

* Updated Entity Texture Features to fix the player rendering crash

### 3.2.4 (2022-03-07)

**Player rendering crash has been discovered, this version has been reverted from CurseForge.**

* Updated Architectury API, Entity Texture Features, Fabric API, Indium
* Forcefully updated Reese's Sodium Options to fix video settings bug on macOS (already fixed on FO 3.3.0-alpha.2 or later)
* Updated Entity Texture Features config and Mod Menu Helper string

### 3.2.3 (2022-02-27)

* Updated Fabric Loader to 0.13.3
* Updated Animatica, Continuity, Lithium, MidnightLib

### 3.2.2 (2022-02-20)

* Updated Fabric Loader to 0.13.2
* Readded Colormatic
* Updated Architectury API, Entity Texture Features, FerriteCore, Sodium Extra

### 3.2.1 (2022-02-12)

* Updated Architectury API, Better Mount HUD, Cloth Config API, Entity Culling, Entity Texture Features, Fabric API, Fabrishot, FerriteCore, Language Reload
* Updated Fabric Loader to 0.13.1
* Updated FO version label's/MultiMC notes' link
* Disabled some potentially conflicting tweaks on TieFix

### 3.2.0 (2022-01-31)

New mods

* Entity Texture Features - random and emissive mob textures!
* Zoomify - customizable zoom!

Removed mods

* WI Zoom - superseded by Zoomify

Other

* Updated 'Slight' Gui Modifications, Architectury API, Fabric API, FastOpenLinksAndFolders, Sodium Extra, TieFix

### 3.1.0 (2022-01-25)

Even though MC 1.18.2 is coming soon, I now consider FO to be stable for MC 1.18.1 and I recommend you to update to it.
Major changes compared to 2.7.0:

New mods

* Starlight - improves chunk performance, 75% preferred it in the public vote (1.0.0 stable version)
* Puzzle - adds some OptiFine features like emissive mobs and resource pack-provided splash screen
* TieFix - disables telemetry (sending diagnostics data to Mojang) and fixes some bugs

Removed mods

* Phosphor - replaced with Starlight as a result of the public vote
* Hydrogen - deprecated, but FerriteCore already exists and has similar features

Other

* Colormatic temporarily removed as it breaks with the new Sodium
* Between beta 2 and stable: updated Fabric API, Reese's Sodium Options

### 3.1.0-beta.2 (2022-01-19)

Individual shader settings can now be configured!

* Updated CIT Resewn, Cloth API, Fabric API, Iris Shaders

### 3.1.0-beta.1 (2022-01-15)

First beta for 1.18.1!

New mods
* Puzzle - adds some OptiFine features like emissive mobs and resource pack-provided splash screen
* TieFix - disables telemetry and fixes some bugs
* Starlight - improves chunk performance, 75% preferred it so here it is! (1.0.0 stable version)

Removed mods
* Phosphor - replaced with Starlight as a result of the public vote
* No Telemetry - replaced with TieFix which has the same feature but can be toggled as well

Other
* Sodium got a bugfix update - fixing lag spikes, fog, memory leak and more
* Updated CIT Resewn, Cloth API, Dynamic FPS, Fabric API, Indium, Iris Shaders, Not Enough Crashes, Sodium, Sodium Extra
* Colormatic temporarily removed as it breaks with the new Sodium
* Don't Clear Chat History is still forced, Hydrogen is deprecated - will not highlight in changelog anymore until something changes

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

### 2.7.3 (2022-02-28)

* Updated Animatica, Continuity, Sodium Extra
* Updated Fabric Loader to 0.13.3

### 2.7.2 (2022-02-12)

* Updated Architectury API, Cloth Config API, Entity Culling
* Updated Fabric Loader to 0.13.1
* Updated FO version label's/MultiMC notes' link

### 2.7.1 (2022-01-31)

* Updated FastOpenLinksAndFolders, Reese's Sodium Options, Sodium Extra

### 2.7.0 (2022-01-19)

Individual shader settings can now be configured!

* Updated CIT Resewn, Fabric API, Iris Shaders, Not Enough Crashes
* Skipped Cloth API update as things broke

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

* **Animatica** - OptiFine's animated textures!
* **ToolTipFix** - makes sure all tooltips fit to screen
* **No Potion Offset** - removes the potion offset on Creative inventory (similar to 1.18)

Other stuff

* Game will attempt to reduce RAM usage when unfocused (enabled Dynamic FPS's GC on unfocus)
* Optimized the Mod Menu Helper resource pack and MultiMC/MultiMC (auto-update) icon
* Updated Fabric Loader
* Updated Architectury API, CIT Resewn, CompleteConfig, Continuity, Fabric API, Not Enough Crashes

### 2.2.1 (2021-10-08)

2.2.0 had a bit of a rocky launch but we're back with mod updates!

* Fixed CurseForge Launcher installation (see [#140](https://github.com/Madis0/fabulously-optimized/issues/140) for more info)
* Fixed CIT Resewn config not being applied
* Added Russian translation for Mod Menu Helper by RozeFound
* Updated Architectury API, Fabric API, Fabric Language Kotlin, Language Reload, LittleTweaks, Mod Menu, Not Enough Crashes, Sodium Extra

### 2.2.0 (2021-09-29)

New mods, new Mod Menu style and a new Discord server! https://discord.gg/yxaXtaQqdB
Also known as "the update that couldn't be installed with CurseForge Launcher".

New mods

* **Continuity** - OptiFine's connected textures!
* **CIT Resewn** - OptiFine's custom items!
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

* **Iris** - OptiFine shaders! [See here](https://github.com/IrisShaders/Iris#what-shader-packs-can-i-use-right-now) for the recommended ones.
* **LambdaBetterGrass** - OptiFine's "better grass"!
* **CustomEntityModels** - OptiFine's custom entity models (partial support, see mod description)
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
* CurseForge pack is now 100% Fabric (faster launch and better mod management)
* An auto-updating MultiMC pack is available on GitHub
* Now using semantic versioning
* All mods updated
* For more changes between alpha and beta versions, see the changelog

Changes from beta 4 to release

* Added AdvancementInfo, Better Mount HUD, Reese's Sodium Options
* MultiMC (auto-update) is now split by version for future-proofing, please re-download if you use it
* Updated Iris+Sodium, Lithium, Sodium Extra, Custom Entity Models, Not Enough Crashes, Mod Menu, Fabric API, Fabric Language Kotlin, Architectury API

### 2.1.0-beta.4 (2021-08-25)

Added
* LambdaBetterGrass (OptiFine's "better grass"!)
* CustomEntityModels and CompleteConfig (OptiFine's custom entity models, in alpha though)
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

* CurseForge Launcher: if you're upgrading from MC 1.16.x, please ☑️ Update to new Profile
* MultiMC: Minecraft 1.17 requires [Java 16 or higher](https://www.oracle.com/java/technologies/downloads/). 

### 2.0.0b4 (2021-07-01)

Differences from b3

* Added **Iris with Sodium**! (Yes, FPS boost and OptiFine shaders!)
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
* Experimental auto-updating MultiMC pack is available on GitHub, try it out! (packwiz by comp500)

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

### 1.12.3 (2022-02-28)

* Updated Architectury API, Sodium Extra
* Downgraded Entity Culling to 1.3.0 due to crashes
* Updated Fabric Loader to 1.13.3

### 1.12.2 (2022-02-12)

* Updated Architectury API, Cloth Config API, Entity Culling
* Updated Fabric Loader to 1.13.1
* Updated FO version label's/MultiMC notes' link

### 1.12.1 (2022-01-31)

* Updated FastOpenLinksAndFolders, Reese's Sodium Options, Sodium Extra

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
* Made a MultiMC auto-update version in GitHub ¯\\\_(ツ)_/¯

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
* The modpack size is much bigger for CurseForge now, because Hydrogen is an external mod
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
* CurseForge: fixed Fabric Loader update
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
* Fabric Capes - gives options for viewing OptiFine, LabyMod and MinecraftCapes' capes in-game
* Fabric Language Kotlin - needed for Fabric Capes

**Removed**
* OF Capes - replaced by Fabric Capes

### 1.3.0 (2020-09-28)
Sodium has been updated, so it's time for a release!

**Added**
* OF Capes - lets you see OptiFine capes and zoom
* MinecraftCapes - lets you get a free cape, textured elytra or mouse ears (configurable)
* Raised Clouds - lets you adjust the cloud height like OptiFine (configurable)
* Fabrishot - lets you take a high-res screenshot like OptiFine (press F9, configurable)

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
A never-released version because CurseForge doesn't like MultiMC-only versions. Ah well.

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
* Colormatic - adds support for OptiFine resource packs' custom colors

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
