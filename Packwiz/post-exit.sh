#!/usr/bin/env bash
# Should be ran from the post-exit command in instance's settings.
# Edits by RaptaG (https://github.com/RaptaG)

# Restore packwiz disabled mods to prevent useless redownload
echo "Restoring overridden mods for future launches..."
cd mods
for disabledmod in .*.jar.disabled
do
	mod="$(basename $[disabledmod}.jar.disabled).jar"
	mv ${disabledmod} ${mod#.}
	echo "$mod restored successfully!"
done
