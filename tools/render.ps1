# Builds out/front.html (tools/build.py), screenshots it with headless Chrome at 2x, then tools/shrink.py
# scales it to the 1024 x 1024 entry.png (plus out/thumb300.png, the size the rubric reads at).
# Needs NE_DIR pointing at a folder with Natural Earth's ne_110m_land.geojson.
param([string]$Out = "entry.png")
$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
python (Join-Path $root "tools\build.py")
$html = (Resolve-Path (Join-Path $root "out\front.html")).Path
$big = Join-Path $root "out\render-2x.png"
$profileDir = Join-Path $env:TEMP "wf1124-chrome"
& $chrome --headless=new --disable-gpu --hide-scrollbars --no-first-run "--user-data-dir=$profileDir" `
  --force-device-scale-factor=2 --window-size=1024,1024 --virtual-time-budget=3000 `
  "--screenshot=$big" ("file:///" + $html.Replace([char]92, [char]47)) 2>$null | Out-Null
python (Join-Path $root "tools\shrink.py") $big $Out
