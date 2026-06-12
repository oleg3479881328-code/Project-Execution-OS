param(
    [Parameter(Mandatory = $true)]
    [string]$InputFile,

    [Parameter(Mandatory = $true)]
    [string]$OutputFile,

    [int64]$MaxBytes = 52428800
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $scriptDir '.venv\Scripts\python.exe'
$runner = Join-Path $scriptDir 'scripts\convert_local.py'
$urlLikePattern = '^[a-zA-Z][a-zA-Z0-9+.-]*:'
$windowsDrivePattern = '^[a-zA-Z]:[\\/]'
$windowsNonLocalPattern = '^(\\\\|//)'

if (-not (Test-Path -LiteralPath $venvPython)) {
    throw "Virtual environment not found at $venvPython. Run bootstrap.ps1 first."
}

if ($InputFile -match $urlLikePattern -and $InputFile -notmatch $windowsDrivePattern) {
    throw 'URL-like inputs are not allowed. Local files only.'
}

if ($InputFile -match $windowsNonLocalPattern) {
    throw 'Windows network-share and device-namespace paths are not allowed. Local files only.'
}

$resolvedInput = [System.IO.Path]::GetFullPath($InputFile)
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputFile)
$outputDir = Split-Path -Parent $resolvedOutput
if ($outputDir) {
    [System.IO.Directory]::CreateDirectory($outputDir) | Out-Null
}

& $venvPython $runner --input $resolvedInput --output $resolvedOutput --max-bytes $MaxBytes
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
