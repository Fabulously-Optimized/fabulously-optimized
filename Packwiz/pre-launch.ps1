# By Ultrasonic#7662

$mods = @(
    'farsight.fabric-1.18-1.8.jar'
)

# Upgrading Fabulously Optimized
Write-Output "Checking for FO updates..."
Set-Location ..

#Set-Location "C:\Users\sonic\AppData\Roaming\PolyMC\instances\afd8656e-675c-464a-8e56-0d2676af0ad7\" #TEMP

$json = Get-Content "mmc-pack.json" | ConvertFrom-Json

$table = $json.components | Where-Object { $_.cachedName -eq "Minecraft" }
$mcVersion = $table.version

if (Test-Path -Path ".\.minecraft") {
    Set-Location ".\.minecraft"
} else {
    Set-Location ".\minecraft"
}

#$INST_JAVA = "C:/Program Files/Eclipse Adoptium/jdk-17.0.1.12-hotspot/bin/javaw.exe" #TEMP

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