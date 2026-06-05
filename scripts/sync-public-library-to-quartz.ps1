param(
  [string]$PortalRoot = "",
  [string]$AllowlistPath = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot

if ([string]::IsNullOrWhiteSpace($PortalRoot)) {
  $PortalRoot = Join-Path $repoRoot "Project-Execution-OS-Library-Portal"
}
if ([string]::IsNullOrWhiteSpace($AllowlistPath)) {
  $AllowlistPath = Join-Path $repoRoot "docs\KNOWLEDGE_LIBRARY_ALLOWLIST.json"
}

$portal = [System.IO.Path]::GetFullPath($PortalRoot)
$content = Join-Path $portal "content"

if (-not (Test-Path -LiteralPath $portal)) { throw "Quartz portal folder not found: $portal" }
if (-not (Test-Path -LiteralPath $AllowlistPath)) { throw "Allowlist file not found: $AllowlistPath" }

$entries = Get-Content -Raw -Path $AllowlistPath | ConvertFrom-Json
if (-not $entries -or $entries.Count -eq 0) { throw "Allowlist is empty." }

if (Test-Path -LiteralPath $content) {
  Get-ChildItem -LiteralPath $content -Force | Remove-Item -Recurse -Force
} else {
  New-Item -ItemType Directory -Path $content | Out-Null
}

$links = @()
foreach ($entry in $entries) {
  if (-not $entry.source -or -not $entry.destination) { throw "Each allowlist entry needs source and destination." }
  $source = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $entry.source))
  $target = [System.IO.Path]::GetFullPath((Join-Path $content $entry.destination))
  if (-not $source.StartsWith($repoRoot, [System.StringComparison]::OrdinalIgnoreCase)) { throw "Source escapes repository root." }
  if (-not $target.StartsWith($content, [System.StringComparison]::OrdinalIgnoreCase)) { throw "Destination escapes Quartz content root." }
  if (-not (Test-Path -LiteralPath $source)) { throw "Missing source file: $source" }
  New-Item -ItemType Directory -Path (Split-Path -Parent $target) -Force | Out-Null
  Copy-Item -LiteralPath $source -Destination $target -Force
  $links += "- $($entry.title)"
}

$landing = @"
# Project Execution OS Library

This portal contains only reviewed allowlisted knowledge files.

## Included Pages

$($links -join "`r`n")
"@
Set-Content -Path (Join-Path $content "index.md") -Value $landing -Encoding UTF8
Write-Host "Synced $($entries.Count) allowlisted items to $content"
