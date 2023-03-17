# Fabulously Optimized changelog
This is the changelog for the Fabric modpack [Fabulously Optimized](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized). See the [version support FAQ](https://fabulously-optimized.gitbook.io/modpack/readme/version-support).

## 1.19.4

### 4.7.0-alpha.3 (2023-03-17)

- Readded FerriteCore, No Chat Reports, MoreCulling
- Updated Capes, Fabric API, Mod Menu
  - You can now click on the list icons in Mod Menu to open mod config, if one exists; on pause menu Bugs button is replaced with Mods
- Temporarily removed AdvancementInfo, CIT Resewn, Custom Entity Models, Enhanced Block Entities, LambDynamicLights, MemoryLeakFix

### 4.7.0-alpha.2-2 (2023-03-17)

Modrinth-exclusive reupload to fix the Prism Launcher crash. Visible version is still "4.7.0-alpha.2".

### 4.7.0-alpha.2 (2023-03-16)

- Updated Cloth Config API, FabricSkyboxes, Mod Menu
  - Mods button now appears on pause menu, FSB fixed some resource pack compat
- Readded Lithium 
- Temporarily removed AdvancementInfo, CIT Resewn, Custom Entity Models, Enhanced Block Entities, FerriteCore, LambDynamicLights, MemoryLeakFix, MoreCulling, No Chat Reports

### 4.7.0-alpha.1 (2023-03-15)

Who let the mods out?!

- Updated Debugify, Entity Culling, Entity Texture Features, Fabric API, FabricSkyboxes, FabricSkyBoxes Interop, Fast Better Grass, Indium, Iris Shaders, Language Reload, MidnightControls, Mod Menu, Puzzle, Reese's Sodium Options, Sodium, Sodium Extra, YetAnotherConfigLib
  - Known bug: pause menu lacks the Mods button
- Forced Borderless Mining, Capes
- Temporarily removed AdvancementInfo, CIT Resewn, Custom Entity Models, Enhanced Block Entities, FerriteCore, LambDynamicLights, Lithium, MemoryLeakFix, MoreCulling, No Chat Reports
- MMH, CRH, FBG descriptions are now translatable
- All 4.6.0-beta.12 changes
  - The "accessibility onboarding" was already previously disabled

## 1.19.3

### 4.6.0-beta.13-2 (2023-03-17)

Modrinth-exclusive reupload to fix the Prism Launcher crash. Visible version is still "4.6.0-beta.13".

### 4.6.0-beta.13 (2023-03-16)

- Updated Lithium, FabricSkyboxes
  - Lithium had bugfixes, FSB fixed some resource pack compat

### 4.6.0-beta.12 (2023-03-15)

- Updated Fabric Language Kotlin, FabricSkyboxes, Language Reload, MemoryLeakFix, Sodium Extra
- Enforced Fabric Loader 0.14.17
- Updated MMH and CRH translations in Greek, Korean, Russian

### 4.6.0-beta.11 (2023-03-05)

Casual reminder: if you get any questions or issues while using FO, our Discord (https://discord.gg/yxaXtaQqdB) is the first place to ask in. Asking in other generic or mod-specific servers may not give you the same support, as they don't know how FO is configured.

- Readded Enhanced Block Entities
- Removed Better Beds
- Updated Custom Entity Models, Entity Texture Features, Fabric API, Lithium
- Updated CRH translations in English, Estonian, Korean
- Updated Fabric Loader to 0.14.17 and enforced 0.14.14
  - Mainly because 0.14.15+ is still considered a beta, so some vanilla users got confused on how to install it. But I consider 0.14.17 to be stable enough anyway, so ¯\\\_(ツ)_/¯
- Updated the way FO warns about old Loader and logs about FO version
  - You may now get an error if you install FO with a partial config

### 4.6.0-beta.10 (2023-02-23)

- Updated Fabric Capes, Entity Culling, Entity Texture Features, Fabric API, Mod Menu
- Disabled Mod Menu's mod update checker and enforced config
- Updated and enforced Fabric Loader 0.14.15

### 4.6.0-beta.9 (2023-02-12)

- Re-added Custom Entity Models
- Updated Indium, MoreCulling
- Translated MMH to Italian by glaav

### 4.6.0-beta.8 (2023-02-08)

- (Temporarily) removed Custom Entity Models (CEM)
  - Apparently it is not compatible with the new Sodium yet, so mobs turned invisible when a model-changing resource pack was active

### 4.6.0-beta.7 (2023-02-07)

- Updated Fabric API, Fabric Language Kotlin, Indium, Iris Shaders, Sodium, Sodium Extra
  - Sodium and Iris improved performance, others received bugfixes
- Updated Polish, Korean and Ukrainian MMH by Radplay, myself, Den4enko
- Translated CRH to Korean by AlphaKR93
- Unified spacing in MMH and CRH language files on the repo (in the resource pack they are minified)
- Updated and enforced Fabric Loader 0.14.14

### 4.6.0-beta.6 (2023-01-29)

100k downloads on Modrinth!

- Added Better Beds as a (temporary) alternative to Enhanced Block Entities
- Updated MoreCulling, No Chat Reports
- Fast Better Grass resource pack is now separately distributed
  - Which means you can recommend it to friends who don't use FO yet :)
  - Will remain bundled in FO for as long as needed though, so **you don't need to download it separately**
  - Fixed bugs with randomized textures and dirt paths
  - New icon
  - Download links for those interested:

  <details>
  
    - CF https://www.curseforge.com/minecraft/texture-packs/fast-better-grass
    - MR https://modrinth.com/resourcepack/fast-better-grass
    - PMC https://www.planetminecraft.com/texture-pack/fast-better-grass
  
  </details>
  
- Updated Russian in MMH by RozeFound
- FastChest is no longer considered an Enhanced Block Entities alternative
- Removed Farsight config

### 4.6.0-beta.5-rp.1 (2023-01-26)

A test release containing my resource pack Update Edition for determining how well do linked resource packs work.

https://www.curseforge.com/minecraft/texture-packs/update-edition
https://modrinth.com/resourcepack/update-edition

Because this is available on both CF and MR, MMC-Export successfully detected the link and uses the Modrinth version in Packwiz.

### 4.6.0-beta.5 (2023-01-25)

- Added MoreCulling - does everything Cull Less Leaves does while having more optimizations
- Removed Cull Less Leaves - replaced by MoreCulling
- Added Fast Better Grass resource pack
  - Imitates OptiFine's Better Grass (fast mode); fancy mode cannot be replicated
  - Serves as a substitute to LambdaBetterGrass in case that doesn't become usable in time
  - Must be the first activated resource pack to work
  - Uses only models, so it works with any other resource pack (breaks varied textures though, if any)
- Updated Fabric API, FabricSkyBoxes, FabricSkyBoxes Interop, Model Gap Fix
- Updated and enforced Fabric Loader 0.14.13
- Enforced Farsight length back to 64 due to unexpected side effects (limiting max render distance)
  - Will consider other measures if this causes problems
- Updated Russian, Korean and Polish MMH translations by RozeFound, AlphaKR93, RadPlay respectively
- More MMH wording changes
  - Item Model Fix is now considered an alternative to Model Gap Fix instead of the opposite
  - Cull Less Leaves is now considered an alternative to MoreCulling
- Temporarily removed Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass
  - As an effort to speed up 1.19.3 release, between these only Continuity will now be considered a required mod before FO 4.6.0 is released, others will (may) be re-added later 

### 4.6.0-beta.4 (2023-01-18)

- Added FastQuit - makes quitting singleplayer worlds instant
- Updated Farsight, Language Reload
- Reduced and currently enforced Farsight distance to 16 (from 64)
- Preemptively disabled the "accessibility onboarding" of 1.19.4
- Temporarily removed Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass

### 4.6.0-beta.3 (2023-01-10)

- Updated Fabric API, Language Reload, MidnightControls
- Updated Portuguese MMH translation by PaperKing13
- Latest versions on Modrinth now include Minecraft version numbers
- Temporarily removed Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass

### 4.6.0-beta.2 (2023-01-03)

- Updated Entity Texture Features, Indium, Iris Shaders, Sodium
  - Sodium and related mods improved NVIDIA crash fix
  - Entity Texture Features received bugfixes
- Unbound Zoomify's secondary zoom (again) and FabricSkyBoxes' toggle keybinds
- Temporarily removed Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass

### 4.6.0-beta.1 (2023-01-02)

- Updated CIT Resewn, Language Reload, Indium
- Updated Simplified Chinese by GodGun968
- Removed Smooth Boot - did not seem to improve performance/needs device-specific setup
- Temporarily removed Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass

### 4.6.0-alpha.13 (2023-01-01)

- Updated Entity Texture Features, Fabric Language Kotlin, Iris Shaders, Language Reload, Sodium, Sodium Extra, YetAnotherConfigLib
- Set and enforced ETF's invalid path support to entities only for better mod compat/to fix resource pack applying issues
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Indium, LambdaBetterGrass
  - Removed Indium because it's not up to date with newest Sodium

### 4.6.0-alpha.12 (2022-12-25)

- Updated Fabric API, Puzzle
- Mod Menu, No Chat Reports, Puzzle now persist your option changes across upgrades
  - Occasionally configs will be enforced again for long-term better UX
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass

### 4.6.0-alpha.11 (2022-12-24)

- Updated LambDynamicLights
- Compressed CRH icons more, again
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass, Puzzle 

### 4.6.0-alpha.10 (2022-12-22)

Also known as the update that didn't get approved on CurseForge in time (though MMC version did).

- Added Ukrainian MMH translation by Den4enko
- Removed Chinese Traditional MMH translation by eric122805 (likely machine-translated)
- Increased CRH icons' contrast
- Updated and enforced Fabric Loader 0.14.12 everywhere
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass, LambDynamicLights, Puzzle 

### 4.6.0-alpha.9 (2022-12-20)

- Added Model Gap Fix - replacement for Item Model Fix, maybe permanently if it is better
- Updated Sodium Extra, Zoomify
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, LambdaBetterGrass, LambDynamicLights, Puzzle 
- Updated Fabric Loader to 0.14.12 where available

### 4.6.0-alpha.8 (2022-12-16)

- Updated Cull Less Leaves, Debugify, OptiGUI, Zoomify
  - Cull Less Leaves, Debugify, Zoomify now have visual configurations again :D
  - Game should also no longer crash on first start
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Item Model Fix, LambdaBetterGrass, LambDynamicLights, Puzzle 

### 4.6.0-alpha.7 (2022-12-15)

We've reached 800 000 downloads on CurseForge!

- Updated Fabric Capes, YetAnotherConfigLib
  - Another game freeze fix
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Item Model Fix, LambdaBetterGrass, LambDynamicLights, OptiGUI, Puzzle 

.

- Enabled Cosmetica capes in Fabric Capes
- Added Russian CRH translation by RozeFound

### 4.6.0-alpha.6 (2022-12-14)

Resource pack features are slowly coming back :eyes:

- Updated CEM, Fabric API, Fabric Capes
- Temporarily removed CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Item Model Fix, LambdaBetterGrass, LambDynamicLights, OptiGUI, Puzzle 

.

- Enabled Labymod and Wynntils cape types in Fabric Capes as the dev said freezes are fixed

### 4.6.0-alpha.5 (2022-12-12)

- Updated Borderless Mining, Fabric API, No Chat Reports, YetAnotherConfigLib
- Temporarily removed CEM, CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Item Model Fix, LambdaBetterGrass, LambDynamicLights, OptiGUI, Puzzle 

.

- Updated Polish and Russian in MMH by Radplay and RozeFound
- Added singleplayer tooltip to CRH

### 4.6.0-alpha.4 (2022-12-10)

- Updated Indium, MidnightControls, Mod Menu
- Added Chinese Traditional in MMH by eric122805
- Updated Language Reload description in MMH

.

- Temporarily removed Borderless Mining, CEM, CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Item Model Fix, LambdaBetterGrass, LambDynamicLights, OptiGUI, Puzzle 

### 4.6.0-alpha.3 (2022-12-09)

- Updated AdvancementInfo, AntiGhost, Entity Texture Features, Lithium 

.

- Temporarily removed Borderless Mining, CEM, CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Indium, Item Model Fix, LambdaBetterGrass, LambDynamicLights, MidnightControls, OptiGUI, Puzzle 

### 4.6.0-alpha.2 (2022-12-09)

- Updated MemoryLeakFix, BetterMountHUD
- Temporarily removed OptiGUI because it caused a crash on right click lmao

.

- Temporarily removed AdvancementInfo, AntiGhost, Borderless Mining, CEM, CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Entity Texture Features, Indium, Item Model Fix, LambdaBetterGrass, LambDynamicLights, MidnightControls, OptiGUI, Puzzle 

### 4.6.0-alpha.1 (2022-12-08)

This is it, the first 1.19.3 alpha! Cool new stuff, but also many broken mods due to major internal changes to the game. 
But more broken mods now mean less broken mods in 1.20 💪

**Please use a separate instance for alphas and betas like this, just in case.**

Mods
- Updated Cloth Config API, Debugify, Entity Culling, Fabric API, FabricSkyboxes, FabricSkyBoxes Interop, FerriteCore, Iris Shaders, Language Reload, Lithium, Mod Menu, No Chat Reports, Sodium, Sodium Extra, Zoomify, YetAnotherConfigLib
- Temporarily removed AdvancementInfo, AntiGhost, BetterMountHUD, Borderless Mining, CEM, CIT Resewn, Colormatic, Continuity, Enhanced Block Entities, Entity Texture Features, Indium, Item Model Fix, LambdaBetterGrass, LambDynamicLights, MidnightControls, Puzzle 

Other
- Added Chat Reporting Helper resource pack 
  - Designed to concisely inform players of chat reporting's existence and where/how it applies, without perceiving it as "good" or "bad".
  - Makes No Chat Reports icons more neutral
  - Makes relevant vanilla and No Chat Reports tooltips shorter, clearer, more accurate and unbiased
  - Feedback and translations welcome on GitHub 
- Enabled operator blocks in creative menu (if you have operator access)
- Enabled advanced tooltips (F3+H) by default
  - This helps people use commands, get precise durability, learn English faster etc, so I believe it is useful for more than just "debugging"
- Updated and enforced Fabric Loader 0.14.11 everywhere

## 1.19.2

### 4.5.6 (2023-01-01)

- Updated Entity Texture Features, Fabric API, Fabric Language Kotlin, Iris Shaders, LambDynamicLights, Sodium Extra
- Updated Fabric Loader to 0.14.12 everywhere
- Set ETF's invalid path support to entities only for better mod compat
- Added Ukrainian MMH translation by Den4enko

### 4.5.5 (2022-12-09)

- Updated FabricSkyBoxes, FabricSkyBoxes Interop, Farsight, Iris Shaders, Language Reload, Lithium, Mod Menu, MemoryLeakFix, Zoomify
- Enabled advanced tooltips (F3+H) by default
  - This helps people use commands, get precise durability, learn English faster etc, so I believe it is useful for more than just "debugging"
- Updated Fabric Loader to 0.14.11 everywhere

### 4.5.4 (2022-12-01)

- Updated Fabric API, Fabric Language Kotlin, FerriteCore, Iris Shaders, Language Reload, Reese's Sodium Options, Sodium Extra
  - Mostly bug and crash fixes for all
  - You can now search creative menu and recipe book in all selected languages (or disable it in Language Reload settings)
- Added Polish MMH translation by Radplay
- Fixed Estonian MMH translation
- Updated Fabric Loader to 0.14.11 where available
- MultiMC: reverted _.minecraft_ change because it made vanilla users' install harder on Unix-like systems

### 4.5.3 (2022-11-24)

- Updated Fabric API, Mod Menu, Sodium Extra
  - Sodium Extra fixed a crash related to fog and particle toggles
- MultiMC version now uses _.minecraft_ (instead of _minecraft_) as the folder

### 4.5.2 (2022-11-18)

Iris had a bruh moment and fixed its issue again, properly.

- Updated Iris Shaders

### 4.5.1 (2022-11-18)

- Updated Entity Texture Features, Iris Shaders, No Chat Reports, Sodium Extra, YetAnotherConfigLib
  - Iris got important fixes for some resource packs
  - Sodium Extra got additional toast toggles
  - Entity Texture Features got new texture features and bugfixes
  - Others got bugfixes
- Added Chinese in MMH by GodGun968
- Updated Russian in MMH by RozeFound
- Unbound Zoomify's secondary zoom keybind by default

### 4.5.0 (2022-11-11)

Finally you can have custom clouds and stars in the sky :) 
Use any OptiFine- or FabricSkyBoxes-compatible custom skybox resource pack to get it.

- Added FabricSkyboxes - custom skies!
- Added FabricSkyboxes Interop - OptiFine resourcepack support for FabricSkyboxes!
- Updated Fabric API, Fabric Language Kotlin, Lithium, Mod Menu
- Enforced Fabric Loader 0.14.10
- Updated Hold That Chunk to 2.0.1 in Modrinth version

### 4.4.6 (2022-11-04)

- Updated Debugify
- Enabled MC-135973 "Can't hold Q to drop items rapidly from container inventories" in Debugify (1.19.3 parity)
- Fixed some strings not being shown in Mod Menu Helper
  - Thanks Mod Menu folks Prospector and haykam!
- Updated Hold That Chunk to 2.0.0 in Modrinth version

### 4.4.5 (2022-10-30)

More bugfixes!

- Updated Lithium, No Chat Reports

### 4.4.4 (2022-10-28)

- Updated Enhanced Block Entities, Fabric API, MidnightControls, No Chat Reports, YetAnotherConfigLib
  - Enhanced Block Entities has some crash fixes
  - No Chat Reports has bugfixes, improved status icon contrast, clarified Realms icon/warning
  - MidnightControls has improved compatibility with mods and interface screens
- Updated Fabric Loader to 0.14.10 everywhere now

### 4.4.3 (2022-10-20)

- Updated Fabric API, Fabric Language Kotlin, Lithium, MidnightControls, Zoomify
  - Zoomify now has a secondary zoom option with separate settings
  - Lithium and MidnightControls got several fixes
- Updated Fabric Loader to 0.14.10 where available

### 4.4.2 (2022-10-13)

- Updated Better Mount HUD, Hold That Chunk, Iris Shaders, Lithium, No Chat Reports
  - Better Mount HUD got an icon in Mod Menu
  - Iris supports more shader features now
  - Lithium got new performance improvements
  - No Chat Reports got several bugfixes and UX improvements
  - Hold That Chunk is updated to an experimental version (ad4dfd0) so the FO Modrinth users can now test whether it functions better and closer to Farsight. 
- Enabled a new warning screen for Minecraft Realms, courtesy of No Chat Reports
  - If you use Realms regularly, I recommend enabling encryption in NCR config.
- Removed Lithium performance workaround as it is now the default

### 4.4.1 (2022-10-04)

- Updated Fabric Language Kotlin, Fabrishot, Farsight, No Chat Reports
  - Farsight now officially supports 1.19.2 ¯\\\_(ツ)_/¯

### 4.4.0 (2022-09-28)

- Removed ToolTipFix - replaced by an improved fix on Debugify
- Updated Cull Less Leaves, Debugify, Fabric API, No Chat Reports, OptiGUI, Sodium Extra, YetAnotherConfigLib
  - Cull Less Leaves uses a new config so any changed settings have been reset
  - No Chat Reports now supports chat encryption, enable in config file if interested
  - Sodium Extra now allows for per-dimension fog distance and has other fog fixes
- Enabled MC-26757 in Debugify - tooltip overflow fix

### 4.3.5 (2022-09-23)

- Updated Debugify, MidnightControls, YetAnotherConfigLib, Zoomify
  - MidnightControls got a lot of fixes, others got fewer
- Enabled MC-59810 in Debugify to fix Ctrl+Click on Macs
- Added an empty file "Copy all 3 folders!" to MultiMC version to remind vanilla users that they should do that

### 4.3.4 (2022-09-19)

- Updated Debugify, Entity Texture Features, OptiGUI, YetAnotherConfigLib
  - Debugify fixed a bug that made game startup slower
  - OptiGUI received several fixes to performance and crashes
- Disabled MC-228976 on Debugify as it's already fixed by Lithium
- Removed MoreCulling config as it is not currently included in FO 
- Removed Bobby config as people prefer its defaults when they install it (it is still a supported alternative mod)

### 4.3.3 (2022-09-16)

Performance improvements!

- Updated Entity Texture Features, Fabric API, No Chat Reports, YetAnotherConfigLib
  - Entity Texture Features is now smaller, has a new config menu and a lot of fixes
  - No Chat Reports fixed one server-joining error and got an option to disable its functionality (use it only if you can't join a server)
  - Skipped MemoryLeakFix update as the version compatibility is improperly marked
- Backported an upcoming Lithium fix for improved stability, thanks @Kichura!
- Limited enabled cape providers to Mojang, MinecraftCapes and OptiFine as a way to workaround some freezing issues
  - Eventually there will be a better fix though; feel free to re-enable any providers you need in skin settings
- MultiMC (auto-update) now prefers Modrinth mods where available
  - That way the downloads actually increase download count for the dev and you get more stable, potentially faster downloads!

### 4.3.2-pw.2 (2022-09-13)

Now without Modrinth-specific changes, so it's closer to the CurseForge version.

### 4.3.2-pw.1 (2022-09-13)

It works:tm: and it successfully uses Hold That Chunk, similar to Modrinth version (even though it doesn't need to).

### 4.3.2 (2022-09-12)

- Enabled MC-112730 and MC-228976 in Debugify because I already intended to enable them at some point but forgot
  - Should improve performance with beacons and mob farms
- Disabled MC-162253 in Debugify because Starlight already fixes that
  - This may fix some some of the chunk/freeze issues, you tell me
- Updated Turkish in MMH by localfossa

### 4.3.1-pw.1 (2022-09-12)

Second test, Farsight should be fine now. Also using the new priority parameter instead of exclusion.

Edit: no, it's not fine, it has an invalid hash.

(the name is arbitrary and not reflected in-game)

### 4.3.1 (2022-09-11)

A small reminder, somewhat related to the Iris bugfix:

If you see that your resourcepack says "contains broken paths" as you try to activate it, please tell the resource pack maker to only use the following characters in file/folder names: `a-z0-9/._-`. 
That way everyone will have resource packs that work better and have less bugs!

More info: https://fabulously-optimized.gitbook.io/modpack/readme/resource-pack-issues

- Updated CIT Resewn, Iris Shaders, YetAnotherConfigLib, Zoomify
  - CIT Resewn and Iris have bugfixes
  - Zoomify has a new config screen
  - Zoomify and Debugify settings now have a searchbar and tweaked category look

### 4.3.0-pw.1 (2022-09-10)

An attempt to source packwiz mods from Modrinth...
Somehow Farsight didn't get substituted though.

(the name is arbitrary and not reflected in-game)

### 4.3.0 (2022-09-09)

- Updated Iris
  - Now supports PBR aka resource packs that support 3D overlay effects on blocks

### 4.2.2 (2022-09-09)

Aka the update that was never announced (because the next superseded it in minutes) (:

- Added YetAnotherConfigLib - for Debugify and probably more in the future
- Re-included separate Cloth Config API
  - Mainly because it adds a searchbar to many mod configs now
- Updated Debugify, Fabric Capes, No Chat Reports, Zoomify
  - Debugify has a new config screen; you have to hover and click ◀ on the category to show options inside it
- Another file size fix for Modrinth

### 4.2.1 (2022-08-30)

- Updated Indium, Iris Shaders, No Chat Reports, Sodium, Sodium Extra
  - Sodium and Iris received several fixes
  - No Chat Reports has a new config so your settings have been reset to FO ones
- Disabled Adaptive VSync by default as it caused issues with some drivers/GPUs
  - Existing users can disable it from video settings, or just keep using it if it works for you
- Disabled safe server icon and related options in No Chat Reports to reduce confusion
- Enabled MC-90683 "Received unknown passenger" bugfix in Debugify
- Modrinth-only: included time in Hold That Chunk config for easier management

### 4.2.0 (2022-08-27)

Fabulously Optimized 4.2.0 has been released for 1.19.2! 
Thank you for 600k+ downloads on CurseForge, 30k+ downloads and 200+ followers on Modrinth!

**Major changes in 3.12.2 -> 4.2.0**

- Added No Chat Reports - replaces misleading chat indicators with accurate ones, opts out from chat signing where possible. More info: https://fabulously-optimized.gitbook.io/modpack/readme/chat-reporting-faq
- Added Mixin Config Helper - shows an user-readable alert when two mods conflict
- Added MixinTrace - helps developers find the cause of crashes
- Removed Don't Clear Chat History - had several issues, including unintended features on 1.19
- Removed Not Enough Crashes - did not help the mod developers, caused other issues
- Some mods did not make it to the release yet and some were already backported :P

.

- Enabled Adaptive VSync on supported devices for smoother FPS
- Zoomify is now smoother by default and has presets 
- You can now select multiple languages in the language menu, highly recommend selecting all languages you can speak for better mod language support
- Added Cloaks+ and Cosmetica cape support
- Disabled chat previews to protect your privacy
- Known issue: currently AdvancementInfo description is missing in Mod Menu for some languages, including English (US)

See full changelog for more details.

**Changes in 4.2.0-beta.6 -> 4.2.0**

- Added back Farsight
- Removed Hold That Chunk as it was not deemed ready yet
- Updated Debugify, Fabric Language Kotlin, No Chat Reports, Zoomify
- Updated Russian in MMH by RozeFound

Modrinth-only:

- Modrinth version will use Hold That Chunk as part of extended testing, and because Farsight is not available there anyway
- Fixed CIT Resewn's file size in manifest

### 4.2.0-beta.6 (2022-08-23)

- Updated Hold That Chunk
  - Hold That Chunk fixed the config so now, again, it has Farsight parity. It was partly my fault too :D
- Zoomify update temporarily skipped due to a bug
- Updated Greek in MMH by RaptaG

### 4.2.0-beta.5 (2022-08-22)

- Updated Hold That Chunk, Reese's Sodium Options
- Removed Cloth Config API - I think it is no longer separately needed, let me know if you still get errors related to it though
- Enabled "ignoreServerRenderDistance" in Hold That Chunk
  - With that it should now _actually_ have full Farsight parity, so please test that again.
- Logs now mention your version of FO

### 4.2.0-beta.4 (2022-08-20)

- Updated Cull Less Leaves, Fabric API, Mixin Conflict Helper, No Chat Reports, Sodium Extra, Zoomify
  - No Chat Reports now has graphical options
  - Zoomify now has selectable presets in options (default, OptiFine, Ok Zoomer). FO continues to use the default preset because that looks the smoothest.
- Enabled Adaptive VSync for big performance gains on supported devices
  - Only applies for new profiles, for existing ones just set VSync to Adaptive in video settings (if you can)
- Removed Cull Less Leaves crash workaround

### 4.2.0-beta.3 (2022-08-15)

FO 4.2.0 is still estimated to be released in August, we have just a few more things to test...

- Added MixinTrace - helps developers find the cause of crashes
- Added Cloth Config API - technically it has always been there inside some mod, but currently a specific version of it is required
- Removed Not Enough Crashes - turned out to be not that helpful for developers
- Removed MoreCulling - performance testing results were inconclusive, some mods had incompatibilities. Decided not to add it for 4.2.0 yet, but keeping an eye on it for the future.

.

- Updated Entity Texture Features, Language Reload, Reese's Sodium Options
- Updated Korean in MMH by AlphaKR93
- Added a workaround to fix Cull Less Leaves crash for some players

### 4.2.0-beta.2 (2022-08-12)

- Added Hold That Chunk - keeps rendered chunks in memory for extended render distance on servers, but also clears cached chunks if they haven't been visited for an hour
  - Depending on your playstyle, this may reduce the game's memory usage for long playtime sessions
  - Modrinth users: if this mod runs well, FO will have 100% mod parity on Modrinth :)
- Removed Farsight - now redundant
- Updated Continuity, MoreCulling, No Chat Reports, Not Enough Crashes, Reese's Sodium Options

### 4.2.0-beta.1 (2022-08-08)

- Updated Debugify, Fabric API, Lithium, MidnightControls, Mod Menu, MoreCulling, No Chat Reports, Not Enough Crashes, Zoomify
- MidnightControls now shows a toast once, suggesting you to enable a controller if you have one connected
  - The game will no longer switch to it automatically unless you enable that in settings
- No Chat Reports: disabled full-screen warnings to avoid warning fatigue, the status is still shown in chat's bottom right corner
  - Feel free to re-enable the warning from config (disable "whitelistAllServers")
  - When updating to this version, this change will apply for everyone
- Updated Turkish and Portuguese (Brazil) in MMH by Localfossa and PaperKing13isPro
- Updated Fabric Loader to 0.14.9

## 1.19.1

### 4.1.0-beta.2 (2022-08-02)

- Updated Farsight, Indium, MemoryLeakFix, MoreCulling, No Chat Reports, Puzzle, Zoomify
  - Zoomify and MoreCulling received major updates
  - Puzzle no longer shows buttons that lead to empty screens in its settings
- Adjusted No Chat Reports
  - Adjusted description in MMH to reflect its features better
  - Re-enabled convertToGameMessage again as it still turned out to be useful in LAN
  - You can now report others on servers that allow reports, use it only in case of real danger

### 4.1.0-beta.1 (2022-07-30)

- Readded Lithium
- Updated AdvancementInfo, AntiGhost, NoChatReports
  - AdvancementInfo and AntiGhost are now smaller in size
  - Currently AdvancementInfo is not shown in Mod Menu Helper
  - NoChatReports fixed Realms access
- Adjusted NoChatReports to disable convertToGameMessage (unnecessary in LAN) and enable vanilla's yellow messages (informative)

### 4.1.0-alpha.2 (2022-07-27)

- Temporarily removed Lithium
  - Because keeping it as disabled caused many problems

### 4.1.0-alpha.1 (2022-07-26)

It's time to start testing 1.19.1. Read the FAQ: https://fabulously-optimized.gitbook.io/modpack/readme/1-19-1-faq
Also, we've reached 500k downloads on CurseForge and almost 20k downloads on Modrinth! Thank you again for your support!

- Updated Debugify, Fabric API, MemoryLeakFix, Mod Menu, More Chat History, MoreCulling, No Chat Reports
- Temporarily disabled Lithium

.

- Disabled bugfixes MC-145929 and MC-148149 on Debugify as they are now fixed in vanilla
- Configured No Chat Reports for 1.19.1
- Updated Korean and Turkish in MMH by AlphaKR93 and localfossa

## 1.19

### 4.0.0-beta.12 (2022-07-26)

- Updated Entity Texture Features, Fabric API, Iris Shaders, MoreCulling, Sodium Extra
  - ETF and Iris received major performance upgrades
- Fixed MoreCulling in MMH for English and Estonian
- Updated Turkish in MMH by localfossa and egeesin

### 4.0.0-beta.11 (2022-07-21)

Another beta, now with FPS stuff! 
Also, 1.19.1-rc2 is out, with 1.19.1 release date being estimated as "next week". Let's see...

- Added More Culling - stops rendering hidden sides of blocks
  - Item frame optimizations currently disabled because it doesn't work with custom items yet
  - It may eventually obsolete Cull Less Leaves, to be tested
  - Mod Menu Helper does not currently work with it, so you'll see its own description in Mod Menu
- Removed Don't Clear Chat History - various issues, including unintended behaviour in 1.19

.

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

### 3.14.1 (2022-09-11)

- Updated Iris
  - Bugfixes

### 3.14.0 (2022-09-09)

- Updated Iris
  - Now supports PBR aka resource packs that support 3D overlay effects on blocks
- Re-included separate Cloth Config API
  - Mainly because it adds a searchbar to many mod configs now
- Another file size fix for Modrinth

### 3.13.1 (2022-08-30)

- Updated Iris Shaders, Sodium Extra
  - Iris received some bugfixes
- Disabled Adaptive VSync by default as it caused issues with some drivers/GPUs
  - Existing users can disable it from video settings, or just keep using it if it works for you

### 3.13.0 (2022-08-27)

- Added MixinTrace - helps developers find the cause of crashes
- Removed Not Enough Crashes - turned out to be not that helpful for developers
- Updated Continuity, Entity Texture Features, Fabric Language Kotlin, Reese's Sodium Options, Sodium Extra
- Updated MMH translations from 4.2.0
- Enabled Adaptive VSync for big performance gains on supported devices
  - Only applies for new profiles, for existing ones just set VSync to Adaptive in video settings (if you can)
- Enforced Fabric Loader 0.14.9
- Logs now mention your version of FO

### 3.12.2 (2022-08-08)

- Updated Indium, MemoryLeakFix, MidnightControls, Puzzle
- MidnightControls now shows a toast once, suggesting you to enable a controller if you have one connected
  - The game will no longer switch to it automatically unless you enable that in settings
- Adjusted Puzzle configs to match 4.2.0-beta.1
- Updated MMH languages
- Updated Fabric Loader to 0.14.9

### 3.12.1 (2022-07-30)

- Updated Fabric API, Fabric Language Kotlin, Iris Shaders, MemoryLeakFix, Reese's Sodium Options, Sodium Extra
  - Iris received a major performance upgrade
- Removed duplicate config files from YOSBR folder
  - This was there to make resetting settings a bit easier when needed, but now a better method is described in the wiki
- Backported MMH language updates

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
