Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$manifestPath = Join-Path $repoRoot "system-manifest.json"

function Add-Problem {
    param(
        [System.Collections.Generic.List[string]]$Problems,
        [string]$Message
    )

    $Problems.Add($Message) | Out-Null
}

function Test-RequiredString {
    param(
        [System.Collections.Generic.List[string]]$Problems,
        [object]$Value,
        [string]$Label
    )

    if ($null -eq $Value -or $Value -isnot [string] -or [string]::IsNullOrWhiteSpace($Value)) {
        Add-Problem $Problems "$Label must be a non-empty string."
        return $false
    }

    return $true
}

function Test-RequiredBoolean {
    param(
        [System.Collections.Generic.List[string]]$Problems,
        [object]$Value,
        [string]$Label
    )

    if ($Value -isnot [bool]) {
        Add-Problem $Problems "$Label must be a boolean."
        return $false
    }

    return $true
}

function Test-RequiredArray {
    param(
        [System.Collections.Generic.List[string]]$Problems,
        [object]$Value,
        [string]$Label
    )

    if ($null -eq $Value) {
        Add-Problem $Problems "$Label must be an array."
        return $false
    }

    if ($Value -is [string] -or $Value -isnot [System.Collections.IEnumerable]) {
        Add-Problem $Problems "$Label must be an array."
        return $false
    }

    return $true
}

function Get-CyclePath {
    param(
        [string]$StartNode,
        [string]$RepeatedNode,
        [System.Collections.Generic.List[string]]$Stack
    )

    $startIndex = $Stack.IndexOf($RepeatedNode)
    if ($startIndex -lt 0) {
        return @($StartNode, $RepeatedNode)
    }

    $cycle = $Stack.GetRange($startIndex, $Stack.Count - $startIndex)
    $cycle.Add($RepeatedNode) | Out-Null
    return $cycle
}

function Test-AcyclicGraph {
    param(
        [hashtable]$Adjacency,
        [string]$RelationshipName
    )

    $problems = [System.Collections.Generic.List[string]]::new()
    $state = @{}
    $stack = [System.Collections.Generic.List[string]]::new()

    function Visit-Node {
        param(
            [string]$Node
        )

        $currentState = if ($state.ContainsKey($Node)) { $state[$Node] } else { 0 }
        if ($currentState -eq 1) {
            $cycle = Get-CyclePath -StartNode $Node -RepeatedNode $Node -Stack $stack
            Add-Problem $problems "$RelationshipName cycle detected: $($cycle -join ' -> ')"
            return
        }

        if ($currentState -eq 2) {
            return
        }

        $state[$Node] = 1
        $stack.Add($Node) | Out-Null

        foreach ($target in $Adjacency[$Node]) {
            if (-not $Adjacency.ContainsKey($target)) {
                continue
            }

            $targetState = if ($state.ContainsKey($target)) { $state[$target] } else { 0 }
            if ($targetState -eq 1) {
                $cycle = Get-CyclePath -StartNode $Node -RepeatedNode $target -Stack $stack
                Add-Problem $problems "$RelationshipName cycle detected: $($cycle -join ' -> ')"
                continue
            }

            Visit-Node -Node $target
        }

        [void]$stack.RemoveAt($stack.Count - 1)
        $state[$Node] = 2
    }

    foreach ($node in $Adjacency.Keys) {
        Visit-Node -Node $node
    }

    return $problems
}

$problems = [System.Collections.Generic.List[string]]::new()

if (-not (Test-Path $manifestPath)) {
    throw "System manifest not found: $manifestPath"
}

try {
    $manifest = Get-Content -Raw $manifestPath | ConvertFrom-Json -AsHashtable
}
catch {
    throw "Failed to parse system manifest JSON: $($_.Exception.Message)"
}

Test-RequiredString -Problems $problems -Value $manifest.schema_version -Label "schema_version" | Out-Null

if (-not ($manifest.system -is [hashtable])) {
    Add-Problem $problems "system must be an object."
}
else {
    Test-RequiredString -Problems $problems -Value $manifest.system.name -Label "system.name" | Out-Null
    Test-RequiredString -Problems $problems -Value $manifest.system.mode -Label "system.mode" | Out-Null
    Test-RequiredString -Problems $problems -Value $manifest.system.entrypoint -Label "system.entrypoint" | Out-Null
}

$requiredRelationshipTypes = @("route_to", "depends_on", "related_to")
$relationshipTypeNames = @()

if (-not ($manifest.relationship_types -is [hashtable])) {
    Add-Problem $problems "relationship_types must be an object."
}
else {
    $relationshipTypeNames = @($manifest.relationship_types.Keys)

    foreach ($requiredType in $requiredRelationshipTypes) {
        if (-not $manifest.relationship_types.ContainsKey($requiredType)) {
            Add-Problem $problems "relationship_types is missing '$requiredType'."
            continue
        }

        $relationshipConfig = $manifest.relationship_types[$requiredType]
        if (-not ($relationshipConfig -is [hashtable])) {
            Add-Problem $problems "relationship_types.$requiredType must be an object."
            continue
        }

        Test-RequiredString -Problems $problems -Value $relationshipConfig.meaning -Label "relationship_types.$requiredType.meaning" | Out-Null
        Test-RequiredBoolean -Problems $problems -Value $relationshipConfig.acyclic -Label "relationship_types.$requiredType.acyclic" | Out-Null
    }

    foreach ($declaredType in $relationshipTypeNames) {
        if ($requiredRelationshipTypes -notcontains $declaredType) {
            Add-Problem $problems "relationship_types contains unsupported type '$declaredType'."
        }
    }
}

$nodes = @()

if (-not (Test-RequiredArray -Problems $problems -Value $manifest.nodes -Label "nodes")) {
    $nodes = @()
}
else {
    $nodes = @($manifest.nodes)
}

$nodeMap = @{}
$duplicatePaths = [System.Collections.Generic.List[string]]::new()

for ($index = 0; $index -lt $nodes.Count; $index++) {
    $node = $nodes[$index]
    $label = "nodes[$index]"

    if (-not ($node -is [hashtable])) {
        Add-Problem $problems "$label must be an object."
        continue
    }

    $hasPath = Test-RequiredString -Problems $problems -Value $node.path -Label "$label.path"
    Test-RequiredString -Problems $problems -Value $node.kind -Label "$label.kind" | Out-Null
    Test-RequiredString -Problems $problems -Value $node.status -Label "$label.status" | Out-Null
    Test-RequiredArray -Problems $problems -Value $node.owns -Label "$label.owns" | Out-Null

    foreach ($relationshipType in $requiredRelationshipTypes) {
        Test-RequiredArray -Problems $problems -Value $node[$relationshipType] -Label "$label.$relationshipType" | Out-Null
    }

    foreach ($propertyName in $node.Keys) {
        if ($requiredRelationshipTypes -contains $propertyName) {
            continue
        }

        if (@("path", "kind", "status", "owns") -contains $propertyName) {
            continue
        }

        if ($propertyName -match "_to$|_on$") {
            Add-Problem $problems "$label uses undeclared relationship field '$propertyName'."
        }
    }

    if (-not $hasPath) {
        continue
    }

    if ($nodeMap.ContainsKey($node.path)) {
        $duplicatePaths.Add($node.path) | Out-Null
        continue
    }

    $nodeMap[$node.path] = $node
}

foreach ($duplicatePath in $duplicatePaths) {
    Add-Problem $problems "Duplicate node path detected: $duplicatePath"
}

$entrypoint = $manifest.system.entrypoint
if ($entrypoint -is [string] -and -not [string]::IsNullOrWhiteSpace($entrypoint)) {
    $entrypointAbsolutePath = Join-Path $repoRoot $entrypoint
    if (-not (Test-Path $entrypointAbsolutePath)) {
        Add-Problem $problems "system.entrypoint does not exist on disk: $entrypoint"
    }

    if (-not $nodeMap.ContainsKey($entrypoint)) {
        Add-Problem $problems "system.entrypoint is not registered as a node: $entrypoint"
    }
}

$adjacency = @{}

foreach ($nodePath in $nodeMap.Keys) {
    $node = $nodeMap[$nodePath]
    $absolutePath = Join-Path $repoRoot $nodePath

    if (-not (Test-Path $absolutePath)) {
        Add-Problem $problems "Registered node path does not exist on disk: $nodePath"
    }

    foreach ($relationshipType in $requiredRelationshipTypes) {
        if (-not $adjacency.ContainsKey($relationshipType)) {
            $adjacency[$relationshipType] = @{}
        }

        $targets = @()
        if (Test-RequiredArray -Problems $problems -Value $node[$relationshipType] -Label "$nodePath.$relationshipType") {
            $targets = @($node[$relationshipType])
        }

        $validatedTargets = [System.Collections.Generic.List[string]]::new()

        foreach ($target in $targets) {
            if ($target -isnot [string] -or [string]::IsNullOrWhiteSpace($target)) {
                Add-Problem $problems "$nodePath.$relationshipType contains a non-string or empty target."
                continue
            }

            if (-not $nodeMap.ContainsKey($target)) {
                Add-Problem $problems "$nodePath.$relationshipType references unregistered target: $target"
                continue
            }

            $targetAbsolutePath = Join-Path $repoRoot $target
            if (-not (Test-Path $targetAbsolutePath)) {
                Add-Problem $problems "$nodePath.$relationshipType references missing on-disk target: $target"
                continue
            }

            $validatedTargets.Add($target) | Out-Null
        }

        $adjacency[$relationshipType][$nodePath] = @($validatedTargets)
    }
}

if ($problems.Count -eq 0) {
    foreach ($relationshipType in $requiredRelationshipTypes) {
        if (-not $manifest.relationship_types.ContainsKey($relationshipType)) {
            continue
        }

        $relationshipConfig = $manifest.relationship_types[$relationshipType]
        if ($relationshipConfig.acyclic) {
            $cycleProblems = Test-AcyclicGraph -Adjacency $adjacency[$relationshipType] -RelationshipName $relationshipType
            foreach ($cycleProblem in $cycleProblems) {
                Add-Problem $problems $cycleProblem
            }
        }
    }
}

if ($problems.Count -gt 0) {
    Write-Error ("System integrity validation failed:`n- " + ($problems -join "`n- "))
}

$validatedNodeCount = $nodeMap.Count
Write-Host "System integrity validation passed."
Write-Host "Validated $validatedNodeCount nodes from system-manifest.json."
Write-Host "route_to and depends_on cycle checks passed."
