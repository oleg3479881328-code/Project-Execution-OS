Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$manifestPath = Join-Path $repoRoot "SYSTEM_CONTEXT_MANIFEST.md"

$manifestContent = Get-Content -Raw $manifestPath

if ($manifestContent -notmatch '(?s)### Ordered Files\s+```text\s*(.*?)\s*```') {
    throw "Could not parse ordered files block from SYSTEM_CONTEXT_MANIFEST.md"
}

$orderedBlock = $Matches[1].Trim()
$orderedLines = $orderedBlock -split "\r?\n" | Where-Object { $_.Trim() -ne "" }

$calculatedLines = [System.Collections.Generic.List[string]]::new()

foreach ($line in $orderedLines) {
    $parts = $line -split "=", 2
    if ($parts.Count -ne 2) {
        throw "Invalid ordered-files line: $line"
    }

    $relativePath = $parts[0].Trim()
    $filePath = Join-Path $repoRoot $relativePath

    if (-not (Test-Path $filePath)) {
        throw "Manifest file missing: $relativePath"
    }

    $blobSha = (git hash-object $filePath).Trim()
    $calculatedLines.Add("$relativePath=$blobSha") | Out-Null

    if ($blobSha -ne $parts[1].Trim()) {
        throw "Manifest blob SHA mismatch for $relativePath. Recorded=$($parts[1].Trim()) Calculated=$blobSha"
    }
}

$fingerprintInput = (($calculatedLines -join "`n") + "`n")
$sha256 = [System.Security.Cryptography.SHA256]::Create()
try {
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($fingerprintInput)
    $hash = $sha256.ComputeHash($bytes)
    $fingerprint = -join ($hash | ForEach-Object { $_.ToString("x2") })
} finally {
    $sha256.Dispose()
}

if ($manifestContent -notmatch '(?s)### SHA-256 Fingerprint\s+```text\s*(.*?)\s*```') {
    throw "Could not parse fingerprint block from SYSTEM_CONTEXT_MANIFEST.md"
}

$recordedFingerprint = $Matches[1].Trim()

if ($fingerprint -ne $recordedFingerprint) {
    throw "Manifest fingerprint mismatch. Recorded=$recordedFingerprint Calculated=$fingerprint"
}

Write-Host "System context manifest validation passed."
Write-Host "Fingerprint: $fingerprint"
