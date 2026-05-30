# System Context Manifest — Project Execution OS

## Purpose

This manifest records stable reusable context profiles for `Project Execution OS`.

It is a version identity artifact for context assembly. It is not proof of provider-side cache persistence or cache hits.

## Manifest Version

`system-context-manifest-v2`

## Generated At

`2026-05-29`

## Profile: `knowledge-aware-core-v2`

### Purpose

Use as the stable reusable foundation for routed project-related AI work that may require selective central knowledge loading.

### Ordered Files

```text
docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md=6800f5918f09a25400d63656a1e3415071ce11f1
START_HERE.md=f315656999e3e78b1b797ad2c1c971ef64fccbf9
docs/ROUTER.md=819c36cb80e40d1bb5ce3e8439d20166fc50653f
docs/CONTEXT_ASSEMBLY_STANDARD.md=5f1a1749f6f261c6de92d1a0e79f8a53878b7afa
docs/KNOWLEDGE_SYSTEM.md=8f7336081925f182a55a6102bd8dfe1a326eecd5
```

### Canonical SHA-256 Fingerprint Input

The ordered file list above, encoded as UTF-8 with one `<path>=<git-blob-sha>` line per file and a final newline.

### SHA-256 Fingerprint

```text
4f540eac511c5a83623d0994426c1b6a061f53833f12dc9dfaa15daf3bd39116
```

### Loading Rule

This profile is a stable reusable foundation, not the whole task context.

Use:

```text
CORE_SYSTEM_PROMPT
→ START_HERE.md stable door
→ docs/ROUTER.md live internal map
→ routed standards and project evidence only when required
```

Append only the routed standard, project orientation, task-specific evidence, selected reusable modules and live instruction required by the active task.

### Status

`active — current recorded profile`

## Superseded Profile

`knowledge-aware-core-v1`

Superseded because routing was split into:

```text
START_HERE.md stable door
→ docs/ROUTER.md live internal map
```

## Update Rule

Update this manifest when a file inside an active profile changes, loading order changes, a file is added or removed, or a profile is intentionally deprecated or replaced.

Follow `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`.