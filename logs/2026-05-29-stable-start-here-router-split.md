# Stable START_HERE And Live ROUTER Split Log

## Date

`2026-05-29`

## Purpose

Record the executed architecture change that separates the stable external entrypoint from the evolving internal route catalogue.

## Decision

Use:

```text
START_HERE.md
→ docs/ROUTER.md
→ smallest relevant internal node
```

## Why

`START_HERE.md` may be distributed by canonical URL to many humans, agents and integrations. It must remain minimal and durable.

The growing list of internal routes must evolve separately inside `docs/ROUTER.md` so that internal system growth does not continually modify the public entry contract.

## Executed Changes

### 1. Internal router created

File:

`docs/ROUTER.md`

Commit:

`6c37027cbcb0aa81b90ac9791f407311916031da`

### 2. START_HERE reduced to stable door

File:

`START_HERE.md`

Commit:

`5d8193faf077097fdad92ca1627044aca2dd1c71`

### 3. Context assembly standard aligned

File:

`docs/CONTEXT_ASSEMBLY_STANDARD.md`

Commit:

`0b1206a7420e324a92da5716182de7a45ad90463`

### 4. ChatGPT core prompt aligned

File:

`docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`

Commit:

`4b96b07014a387d068c63fe69afa6b1be1e15ac5`

### 5. Context manifest refreshed

File:

`SYSTEM_CONTEXT_MANIFEST.md`

Commit:

`fc835e9d72c4a082e4c09846799a376c0c1296ac`

Active profile:

```text
knowledge-aware-core-v3
```

Fingerprint:

```text
1c76b4fd2e9156a2294c46873542e0202fd12f738e120e3746a188e14bbfee0d
```

### 6. Architecture decision recorded

File:

`project-library/decisions/006-stable-start-here-live-router.md`

Commit:

`e0004e5c33fb74ba5afac0bb63004a1a658172a0`

## State Separation

Implemented and committed:

- stable `START_HERE.md` door;
- live `docs/ROUTER.md` map;
- aligned context assembly standard;
- aligned ChatGPT core prompt;
- refreshed active context manifest;
- explicit architecture decision record.

Not yet validated:

- full repository-wide search for stale references that still describe `START_HERE.md` as the live route catalogue;
- runtime API orchestration behavior;
- automatic manifest regeneration.

## Next Action

Update `PROJECT_INDEX.md`, then run a bounded review for stale references and architecture drift.