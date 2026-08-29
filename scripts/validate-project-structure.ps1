Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$projectsRoot = Join-Path $repoRoot "projects"

function Get-FrontmatterValue {
    param(
        [string]$Content,
        [string]$Key
    )

    if ($Content -match '(?s)^---\r?\n(.*?)\r?\n---') {
        $frontmatter = $Matches[1]
        if ($frontmatter -match "(?m)^\s*$Key\s*:\s*(.+?)\s*$") {
            return $Matches[1].Trim()
        }
    }

    return $null
}

function Get-StateValue {
    param(
        [string]$Content,
        [string]$FrontmatterKey,
        [string]$LegacyLabel
    )

    $frontmatterValue = Get-FrontmatterValue -Content $Content -Key $FrontmatterKey
    if ($frontmatterValue) {
        return $frontmatterValue
    }

    $escapedLabel = [regex]::Escape($LegacyLabel)
    $legacyPattern = '(?mi)^\s*(?:[-*]\s*)?' + $escapedLabel + '\s*:\s*`?([^`\r\n]+)`?\s*$'
    if ($Content -match $legacyPattern) {
        return $Matches[1].Trim()
    }

    return $null
}

function Add-ErrorMessage {
    param(
        [System.Collections.Generic.List[string]]$Errors,
        [string]$ProjectName,
        [string]$Message
    )

    $Errors.Add("$ProjectName - $Message") | Out-Null
}

$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

if (-not (Test-Path $projectsRoot)) {
    Write-Host "No projects directory found. Nothing to validate."
    exit 0
}

$projectDirs = Get-ChildItem -Path $projectsRoot -Directory

foreach ($projectDir in $projectDirs) {
    $projectPath = Join-Path $projectDir.FullName "PROJECT.md"
    $legacyEntrypointPath = Join-Path $projectDir.FullName "PROJECT_ENTRYPOINT.md"
    $agentsPath = Join-Path $projectDir.FullName "AGENTS.md"
    $statePath = Join-Path $projectDir.FullName "PROJECT_STATE.md"
    $logsLatestPath = Join-Path $projectDir.FullName "logs\latest.md"
    $workflowRoot = Join-Path $projectDir.FullName "workflow-runs"

    $hasProject = Test-Path $projectPath
    $hasLegacy = Test-Path $legacyEntrypointPath
    $hasAgents = Test-Path $agentsPath
    $hasState = Test-Path $statePath
    $hasLatestLog = Test-Path $logsLatestPath

    if (-not $hasProject -and -not $hasLegacy) {
        continue
    }

    if ($hasProject -and $hasLegacy) {
        Add-ErrorMessage $errors $projectDir.Name "both PROJECT.md and legacy PROJECT_ENTRYPOINT.md exist"
        continue
    }

    if ($hasLegacy -and -not $hasProject) {
        $warnings.Add("$($projectDir.Name) - legacy PROJECT_ENTRYPOINT.md is still in use; migrate to PROJECT.md when the project is next maintained") | Out-Null
    }

    if (-not $hasState -and -not $hasLatestLog) {
        if ($hasProject -or $hasLegacy) {
            if ($hasAgents) {
                Write-Host "$($projectDir.Name): valid zero-state bootstrap (PROJECT + optional AGENTS only)." -ForegroundColor DarkGray
            } else {
                Write-Host "$($projectDir.Name): valid zero-state bootstrap or lightweight internal subproject entrypoint." -ForegroundColor DarkGray
            }
        }
        continue
    }

    if ($hasState -xor $hasLatestLog) {
        Add-ErrorMessage $errors $projectDir.Name "active project state must include both PROJECT_STATE.md and logs/latest.md"
        continue
    }

    $stateContent = Get-Content -Raw $statePath
    if ([string]::IsNullOrWhiteSpace($stateContent)) {
        Add-ErrorMessage $errors $projectDir.Name "PROJECT_STATE.md is empty"
        continue
    }

    $projectMode = Get-FrontmatterValue -Content $stateContent -Key "project_mode"
    $status = Get-StateValue -Content $stateContent -FrontmatterKey "status" -LegacyLabel "Status"

    # A dedicated status field is useful, but PROJECT_STRUCTURE_STANDARD.md does
    # not require one. Some valid projects express state through sections such as
    # Current Mode / Current Objective. Keep this as a diagnostic, not a hard gate.
    if (-not $status) {
        $warnings.Add("$($projectDir.Name) - PROJECT_STATE.md has no dedicated status field; state is accepted if the file remains meaningful and current") | Out-Null
    }

    if ($projectMode -eq "full" -and -not (Test-Path (Join-Path $projectDir.FullName "PROJECT_RULES.md"))) {
        Add-ErrorMessage $errors $projectDir.Name "full-mode project missing PROJECT_RULES.md"
    }

    if (Test-Path $workflowRoot) {
        $runDirs = Get-ChildItem -Path $workflowRoot -Directory
        foreach ($runDir in $runDirs) {
            $inputPath = Join-Path $runDir.FullName "00_INPUT.md"
            if (-not (Test-Path $inputPath)) {
                Add-ErrorMessage $errors $projectDir.Name "workflow run $($runDir.Name) missing 00_INPUT.md"
            }
        }
    }
}

foreach ($warning in $warnings) {
    Write-Warning $warning
}

if ($errors.Count -gt 0) {
    Write-Error ("Project structure validation failed:`n- " + ($errors -join "`n- "))
}

Write-Host "Project structure validation passed."
if ($warnings.Count -gt 0) {
    Write-Host "Warnings: $($warnings.Count)" -ForegroundColor Yellow
}
