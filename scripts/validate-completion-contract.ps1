$ErrorActionPreference = 'Stop'

$required = @{
    'AGENTS.md' = @(
        'docs/KNOWLEDGE_SYSTEM.md',
        'docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md',
        'Meaningful work is not complete'
    )
    'docs/KNOWLEDGE_SYSTEM.md' = @(
        'Knowledge-In-The-Flow Solve Loop',
        'final promotion/completion gate',
        'Existing Artifact First'
    )
    'docs/PROJECT_MEMORY_STANDARD.md' = @(
        'docs/KNOWLEDGE_SYSTEM.md',
        'Knowledge and state preservation are part of execution'
    )
    'docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md' = @(
        'docs/KNOWLEDGE_SYSTEM.md',
        'Do not wait until the final report'
    )
    'docs/REVIEW_STANDARD.md' = @(
        'Post-Review Promotion Gate',
        'docs/KNOWLEDGE_SYSTEM.md'
    )
}

$failures = New-Object System.Collections.Generic.List[string]

foreach ($path in $required.Keys) {
    if (-not (Test-Path -LiteralPath $path)) {
        $failures.Add("Missing required completion-contract file: $path")
        continue
    }

    $text = Get-Content -LiteralPath $path -Raw
    foreach ($needle in $required[$path]) {
        if ($text -notlike "*$needle*") {
            $failures.Add("$path is missing required completion-contract marker: $needle")
        }
    }
}

if ($failures.Count -gt 0) {
    Write-Host 'Completion contract validation FAILED:' -ForegroundColor Red
    foreach ($failure in $failures) {
        Write-Host " - $failure" -ForegroundColor Red
    }
    exit 1
}

Write-Host 'Completion contract validation passed.' -ForegroundColor Green
Write-Host 'Verified: agent instructions -> knowledge-in-flow -> project memory -> transfer-ready state -> review promotion gate.'
