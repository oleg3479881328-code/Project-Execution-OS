Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

function Add-IntegrityError {
    param([string]$Message)
    $errors.Add($Message) | Out-Null
}

function Add-IntegrityWarning {
    param([string]$Message)
    $warnings.Add($Message) | Out-Null
}

function Test-RepoTarget {
    param(
        [string]$Source,
        [string]$Target
    )

    if ([string]::IsNullOrWhiteSpace($Target)) {
        return
    }

    if ($Target -match '^(https?://|skills://|sandbox:|[A-Za-z]+:)') {
        return
    }

    $normalized = $Target.Trim().TrimStart('./') -replace '/', [IO.Path]::DirectorySeparatorChar
    $fullPath = Join-Path $repoRoot $normalized

    if (-not (Test-Path $fullPath)) {
        Add-IntegrityError "$Source references missing repository target: $Target"
    }
}

# Stable entrypoint must exist and must route to the live router.
$startHerePath = Join-Path $repoRoot "START_HERE.md"
$routerPath = Join-Path $repoRoot "docs\ROUTER.md"

if (-not (Test-Path $startHerePath)) {
    Add-IntegrityError "Missing stable entrypoint: START_HERE.md"
}

if (-not (Test-Path $routerPath)) {
    Add-IntegrityError "Missing live router: docs/ROUTER.md"
}

if ((Test-Path $startHerePath) -and (Test-Path $routerPath)) {
    $startHere = Get-Content -Raw $startHerePath
    if ($startHere -notmatch [regex]::Escape('docs/ROUTER.md')) {
        Add-IntegrityError "START_HERE.md does not reference docs/ROUTER.md"
    }
}

# Validate explicit route targets in ROUTER.md.
if (Test-Path $routerPath) {
    $routerContent = Get-Content -Raw $routerPath
    $routeMatches = [regex]::Matches($routerContent, '(?m)^- .*?->\s*`([^`]+)`\s*$')

    if ($routeMatches.Count -eq 0) {
        Add-IntegrityError "No explicit repository route targets could be parsed from docs/ROUTER.md"
    }

    $targetOwners = @{}
    foreach ($match in $routeMatches) {
        $target = $match.Groups[1].Value.Trim()
        Test-RepoTarget -Source "docs/ROUTER.md" -Target $target

        if (-not $targetOwners.ContainsKey($target)) {
            $targetOwners[$target] = 0
        }
        $targetOwners[$target]++
    }

    foreach ($target in $targetOwners.Keys | Sort-Object) {
        if ($targetOwners[$target] -gt 1) {
            Add-IntegrityWarning "docs/ROUTER.md has $($targetOwners[$target]) explicit routes to the same target: $target"
        }
    }
}

# Validate the core Codex handoff entrypoint references. This catches stale
# executor routes without attempting to lint every incidental path in every doc.
$handoffEntrypointPath = Join-Path $repoRoot "docs\CODEX_HANDOFF_ENTRYPOINT.md"
if (Test-Path $handoffEntrypointPath) {
    $handoffContent = Get-Content -Raw $handoffEntrypointPath
    $backtickRefs = [regex]::Matches($handoffContent, '`((?:docs|blocks|skills)/[^`]+\.(?:md|json|ya?ml))`')
    foreach ($match in $backtickRefs) {
        Test-RepoTarget -Source "docs/CODEX_HANDOFF_ENTRYPOINT.md" -Target $match.Groups[1].Value
    }
} else {
    Add-IntegrityError "Missing docs/CODEX_HANDOFF_ENTRYPOINT.md"
}

foreach ($warning in $warnings) {
    Write-Warning $warning
}

if ($errors.Count -gt 0) {
    Write-Host "PEOS router integrity validation FAILED." -ForegroundColor Red
    foreach ($errorMessage in $errors) {
        Write-Host "- $errorMessage" -ForegroundColor Red
    }
    exit 1
}

Write-Host "PEOS router integrity validation passed." -ForegroundColor Green
Write-Host "Checked stable entrypoint, live router targets, and core Codex handoff references."
if ($warnings.Count -gt 0) {
    Write-Host "Warnings: $($warnings.Count)" -ForegroundColor Yellow
}
exit 0
