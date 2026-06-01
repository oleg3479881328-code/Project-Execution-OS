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

function Add-ErrorMessage {
    param(
        [System.Collections.Generic.List[string]]$Errors,
        [string]$ProjectName,
        [string]$Message
    )

    $Errors.Add("$ProjectName - $Message") | Out-Null
}

$errors = [System.Collections.Generic.List[string]]::new()

if (-not (Test-Path $projectsRoot)) {
    Write-Host "No projects directory found. Nothing to validate."
    exit 0
}

$projectDirs = Get-ChildItem -Path $projectsRoot -Directory

foreach ($projectDir in $projectDirs) {
    $projectPath = Join-Path $projectDir.FullName "PROJECT.md"
    $legacyEntrypointPath = Join-Path $projectDir.FullName "PROJECT_ENTRYPOINT.md"
    if (-not (Test-Path $projectPath) -and -not (Test-Path $legacyEntrypointPath)) {
        continue
    }

    if ((Test-Path $projectPath) -and (Test-Path $legacyEntrypointPath)) {
        Add-ErrorMessage $errors $projectDir.Name "both PROJECT.md and legacy PROJECT_ENTRYPOINT.md exist"
    }

    $statePath = Join-Path $projectDir.FullName "PROJECT_STATE.md"
    if (-not (Test-Path $statePath)) {
        Add-ErrorMessage $errors $projectDir.Name "missing PROJECT_STATE.md"
        continue
    }

    $stateContent = Get-Content -Raw $statePath
    $projectMode = Get-FrontmatterValue -Content $stateContent -Key "project_mode"
    $status = Get-FrontmatterValue -Content $stateContent -Key "status"

    if (-not $projectMode) {
        $projectMode = if (Test-Path (Join-Path $projectDir.FullName "PROJECT_RULES.md")) { "full" } else { "compact" }
    }

    if (-not $status) {
        Add-ErrorMessage $errors $projectDir.Name "PROJECT_STATE.md should define frontmatter key: status"
    }

    $commonRequired = @(
        "workflow-runs",
        "logs"
    )

    foreach ($item in $commonRequired) {
        if (-not (Test-Path (Join-Path $projectDir.FullName $item))) {
            Add-ErrorMessage $errors $projectDir.Name "missing $item"
        }
    }

    if ($projectMode -eq "full") {
        foreach ($item in @("PROJECT_RULES.md", "agents", "project-library")) {
            if (-not (Test-Path (Join-Path $projectDir.FullName $item))) {
                Add-ErrorMessage $errors $projectDir.Name "full-mode project missing $item"
            }
        }
    }

    $workflowRoot = Join-Path $projectDir.FullName "workflow-runs"
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

if ($errors.Count -gt 0) {
    Write-Error ("Project structure validation failed:`n- " + ($errors -join "`n- "))
}

Write-Host "Project structure validation passed."
