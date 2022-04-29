# By Ultrasonic#7662

# Restore packwiz disabled mods to prevent useless redownload
Write-Output "Restoring overridden mods for future launches..."
Set-Location ".\mods"

$mods = Get-ChildItem *.jar.disabled

foreach ( $mod in $mods ) {
    Move-Item -Path $mod.name -Destination ($mod.FullName).Replace(".disabled","") -Force
    Write-Output "Restored mod $($mod.name.Replace(".disabled", ''))"
}