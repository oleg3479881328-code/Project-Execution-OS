Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvDir = Join-Path $scriptDir '.venv'
$requirementsPath = Join-Path $scriptDir 'requirements.txt'
$runner = Join-Path $scriptDir 'run-smoke-test.ps1'

function Get-PythonCommand {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        return @('py', '-3.12')
    }

    if (Get-Command python -ErrorAction SilentlyContinue) {
        return @('python')
    }

    throw 'Python launcher was not found. Install Python 3.12 or newer.'
}

$pythonCommand = Get-PythonCommand
$versionOutput = & $pythonCommand[0] $pythonCommand[1..($pythonCommand.Length - 1)] --version 2>&1
if ($LASTEXITCODE -ne 0) {
    throw "Failed to query Python version: $versionOutput"
}

if ($versionOutput -notmatch 'Python\s+(\d+)\.(\d+)') {
    throw "Unrecognized Python version output: $versionOutput"
}

$major = [int]$Matches[1]
$minor = [int]$Matches[2]
if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 10)) {
    throw "Python 3.10 or newer is required. Found: $versionOutput"
}

Push-Location $scriptDir
try {
    & $pythonCommand[0] $pythonCommand[1..($pythonCommand.Length - 1)] -m venv $venvDir
    if ($LASTEXITCODE -ne 0) {
        throw 'Failed to create the local virtual environment.'
    }

    $venvPython = Join-Path $venvDir 'Scripts\python.exe'
    & $venvPython -m pip install --disable-pip-version-check --no-color --progress-bar off --upgrade pip
    if ($LASTEXITCODE -ne 0) {
        throw 'Failed to upgrade pip in the local virtual environment.'
    }

    & $venvPython -m pip install --disable-pip-version-check --no-color --progress-bar off -r .\requirements.txt
    if ($LASTEXITCODE -ne 0) {
        throw 'Failed to install pinned adapter requirements.'
    }

    & powershell -ExecutionPolicy Bypass -File $runner
    if ($LASTEXITCODE -ne 0) {
        throw 'Smoke test failed during bootstrap.'
    }
}
finally {
    Pop-Location
}
