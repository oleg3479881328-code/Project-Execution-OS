# Capability Library

## Purpose

This directory is the registry and governance entrypoint for reusable executable capability blocks used across projects.

Capability blocks are different from domain blocks:

- `blocks/<domain>/` stores reusable knowledge, research, decision rules, and review guidance;
- capability implementations perform executable work behind stable contracts;
- workflows compose capabilities;
- applications provide UI, business logic, and adapters.

The canonical architecture standard is:

`docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`

## Default Integration Rule

Do not copy a capability implementation into each application.

Use a versioned package, a stable contract, and a thin application adapter.

## Registry

Executable readiness is tracked in:

`capability-library/REGISTRY.md`

A registry entry does not prove implementation. Status values must be used precisely:

```text
idea -> candidate -> validated -> production -> deprecated -> retired
```

## Current Priority

The first planned validation chain is:

```text
media.download
-> media.probe
-> media.extract_audio
-> media.transcribe
-> media.clip
```

The initial goal is to make these blocks reusable by both a short-video production workflow and another application such as QuizLight.