# System Context Manifest — Project Execution OS

## Purpose

This manifest records stable reusable context profiles for `Project Execution OS`.

It is a version identity artifact for context assembly. It is not proof of provider-side cache persistence or cache hits.

## Manifest Version

`system-context-manifest-v3`

## Generated At

`2026-05-29`

## Profile: `knowledge-aware-core-v3`

### Purpose

Use as the stable reusable foundation for routed project-related AI work that may require selective central knowledge loading.

### Ordered Files

```text
docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md=ffa44bccdd2e24dd96c1b6ee726c0726712f1e1a
START_HERE.md=f315656999e3e78b1b797ad2c1c971ef64fccbf9
docs/ROUTER.md=819c36cb80e40d1bb5ce3e8439d20166fc50653f
docs/CONTEXT_ASSEMBLY_STANDARD.md=5f1a1749f6f261c6de92d1a0e79f8a53878b7afa
docs/KNOWLEDGE_SYSTEM.md=8f7336081925f182a55a6102bd8dfe1a326eecd5
```

### Canonical SHA-256 Fingerprint Input

The ordered file list above, encoded as UTF-8 with one `<path>=<git-blob-sha>` line per file and a final newline.

### SHA-256 Fingerprint

```text
1c76b4fd2e9156a2294c46873542e0202fd12f738e120e3746a188e14bbfee0d
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

## Superseded Profiles

- `knowledge-aware-core-v1`
- `knowledge-aware-core-v2`

`knowledge-aware-core-v1` was superseded because routing was split into:

```text
START_HERE.md stable door
→ docs/ROUTER.md live internal map
```

`knowledge-aware-core-v2` was superseded because the ChatGPT core prompt was aligned with that split.

## Update Rule

Update this manifest when a file inside an active profile changes, loading order changes, a file is added or removed, or a profile is intentionally deprecated or replaced.

Follow `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`.