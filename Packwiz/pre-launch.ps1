# By Ultrasonic1209

$mods = @(
    'ModYouDislike.jar'
    'AnotherMod.jar'
)

# Upgrading Fabulously Optimized
Write-Output "Checking for FO updates..."
Set-Location ..

$json = Get-Content "mmc-pack.json" | ConvertFrom-Json

$table = $json.components | Where-Object { $_.cachedName -eq "Minecraft" }
$mcVersion = $table.version

if (Test-Path -Path ".\.minecraft") {
    Set-Location ".\.minecraft"
} else {
    Set-Location ".\minecraft"
}

$processOptions = @{
    FilePath = $Env:INST_JAVA
    ArgumentList = "-jar packwiz-installer-bootstrap.jar",
        "https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/$mcVersion/pack.toml"
}
Start-Process @processOptions -Wait

# Disabling the mods
Write-Output "Disabling mods..."

Set-Location ".\mods"
foreach ($mod in $mods) {
    Move-Item -Path $mod -Destination "$mod.disabled" -Force
}
