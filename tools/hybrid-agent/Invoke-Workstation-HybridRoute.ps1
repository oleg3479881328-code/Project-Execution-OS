param(
    [ValidateSet('codex','deepseek')]
    [string]$Executor = 'codex',

    [ValidateSet('auto','cloud-only','local-only','preprocess-then-cloud')]
    [string]$Mode = 'auto',

    [Parameter(Mandatory = $true)]
    [string]$Task,

    [string[]]$LogPath = @(),
    [string[]]$FilePath = @(),
    [string]$RuntimeLog = 'logs/api-runtime/hybrid-agent.jsonl',
    [double]$TimeoutSeconds = 240,
    [switch]$DebugFullEvidence,
    [switch]$NoLaunchExecutor
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir '..\..')
$runner = Join-Path $scriptDir 'run_workstation_hybrid_route.py'

Push-Location $repoRoot
try {
    $arguments = @(
        $runner,
        '--executor', $Executor,
        '--mode', $Mode,
        '--task', $Task,
        '--repo-root', $repoRoot,
        '--runtime-log', $RuntimeLog,
        '--timeout-seconds', [string]$TimeoutSeconds
    )

    foreach ($path in $LogPath) {
        $arguments += @('--log-path', $path)
    }

    foreach ($path in $FilePath) {
        $arguments += @('--file-path', $path)
    }

    if ($DebugFullEvidence) {
        $arguments += '--debug-full-evidence'
    }

    if ($NoLaunchExecutor) {
        $arguments += '--no-launch-executor'
    }

    & python @arguments
}
finally {
    Pop-Location
}
