Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $scriptDir '.venv\Scripts\python.exe'
$runner = Join-Path $scriptDir 'scripts\run_smoke_test.py'

if (-not (Test-Path -LiteralPath $venvPython)) {
    throw "Virtual environment not found at $venvPython. Run bootstrap.ps1 first."
}

Push-Location $scriptDir
try {
    & $venvPython $runner --project-root $scriptDir
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
