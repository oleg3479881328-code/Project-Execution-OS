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

function Parse-PythonVersion {
    param(
        [Parameter(Mandatory = $true)]
        [string]$VersionText
    )

    if ($VersionText -notmatch 'Python\s+(\d+)\.(\d+)') {
        throw "Unrecognized Python version output: $VersionText"
    }

    return [pscustomobject]@{
        Major = [int]$Matches[1]
        Minor = [int]$Matches[2]
    }
}

function Confirm-PythonVersion {
    param(
        [Parameter(Mandatory = $true)]
        [pscustomobject]$VersionInfo,

        [Parameter(Mandatory = $true)]
        [string]$VersionText
    )

    if ($VersionInfo.Major -lt 3 -or ($VersionInfo.Major -eq 3 -and $VersionInfo.Minor -lt 10)) {
        throw "Python 3.10 or newer is required. Found: $VersionText"
    }
}

function Get-PythonVersionText {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Command,

        [string[]]$Arguments = @()
    )

    $versionArguments = @($Arguments + @('--version'))
    $versionOutput = & $Command @versionArguments 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to query Python version: $versionOutput"
    }

    return [string]$versionOutput
}

function Get-PythonInvocation {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        $launcherOutput = & py -0p 2>$null
        if ($LASTEXITCODE -eq 0) {
            $candidates = @()
            foreach ($line in $launcherOutput) {
                if ($line -match '-V:(\d+)\.(\d+)') {
                    $major = [int]$Matches[1]
                    $minor = [int]$Matches[2]
                    if ($major -eq 3 -and $minor -ge 10 -and $minor -le 13) {
                        $candidates += [pscustomobject]@{
                            Major = $major
                            Minor = $minor
                            Selector = "-$major.$minor"
                        }
                    }
                }
            }

            $selected = $candidates |
                Sort-Object -Property @{ Expression = 'Major'; Descending = $true }, @{ Expression = 'Minor'; Descending = $true } |
                Select-Object -First 1

            if ($selected) {
                return [pscustomobject]@{
                    Command = 'py'
                    Arguments = @($selected.Selector)
                }
            }
        }
    }

    if (Get-Command python -ErrorAction SilentlyContinue) {
        return [pscustomobject]@{
            Command = 'python'
            Arguments = @()
        }
    }

    throw 'Python launcher was not found. Install Python 3.10 or newer.'
}

$pythonInvocation = Get-PythonInvocation
$versionOutput = Get-PythonVersionText -Command $pythonInvocation.Command -Arguments $pythonInvocation.Arguments
$versionInfo = Parse-PythonVersion -VersionText $versionOutput
Confirm-PythonVersion -VersionInfo $versionInfo -VersionText $versionOutput

Push-Location $scriptDir
try {
    $venvPython = Join-Path $venvDir 'Scripts\python.exe'
    $reuseExistingVenv = $false
    if (Test-Path -LiteralPath $venvPython) {
        try {
            $existingVersionOutput = Get-PythonVersionText -Command $venvPython
            $existingVersionInfo = Parse-PythonVersion -VersionText $existingVersionOutput
            Confirm-PythonVersion -VersionInfo $existingVersionInfo -VersionText $existingVersionOutput
            $reuseExistingVenv = $true
        }
        catch {
            Remove-Item -Recurse -Force $venvDir -ErrorAction Stop
        }
    }

    if (-not $reuseExistingVenv) {
        if (Test-Path -LiteralPath $venvDir) {
            Remove-Item -Recurse -Force $venvDir -ErrorAction Stop
        }

        $venvArguments = @($pythonInvocation.Arguments + @('-m', 'venv', $venvDir))
        & $pythonInvocation.Command @venvArguments
        if ($LASTEXITCODE -ne 0) {
            throw 'Failed to create the local virtual environment.'
        }
    }

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
