# System Context Manifest — Project Execution OS

## Purpose

This manifest records stable reusable context profiles for `Project Execution OS`.

It is a version identity artifact for context assembly. It is not proof of provider-side cache persistence or cache hits.

## Manifest Version

`system-context-manifest-v1`

## Generated At

`2026-05-29`

## Profile: `knowledge-aware-core-v1`

### Purpose

Use as the stable reusable foundation for routed project-related AI work that may require selective central knowledge loading.

### Ordered Files

```text
docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md=6800f5918f09a25400d63656a1e3415071ce11f1
START_HERE.md=d62a73d1acdf0002c5f656a196149f326eb2a4de
docs/CONTEXT_ASSEMBLY_STANDARD.md=ae71043333921ac0e4dc61ee87e22ac865bf3faa
docs/KNOWLEDGE_SYSTEM.md=8f7336081925f182a55a6102bd8dfe1a326eecd5
```

### Canonical SHA-256 Fingerprint Input

The ordered file list above, encoded as UTF-8 with one `<path>=<git-blob-sha>` line per file and a final newline.

### SHA-256 Fingerprint

```text
160c2650b5658d5d977b16063c71c96d694055fb2b92be7b5d2430f33624c579
```

### Loading Rule

This profile is a stable reusable foundation, not the whole task context.

Append only the routed standard, project orientation, task-specific evidence, selected reusable modules and live instruction required by the active task.

### Status

`active — initial recorded profile`

## Update Rule

Update this manifest when a file inside an active profile changes, loading order changes, a file is added or removed, or a profile is intentionally deprecated or replaced.

Follow `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`.