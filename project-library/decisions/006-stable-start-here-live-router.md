# Decision 006 — Stable START_HERE Door And Live Internal Router

## Date

`2026-05-29`

## Decision

Use a two-layer entry architecture:

```text
START_HERE.md
→ docs/ROUTER.md
→ smallest relevant internal node
```

`START_HERE.md` is the stable top-level door distributed by canonical URL to humans, agents and integrations.

`docs/ROUTER.md` is the live internal navigation map that may evolve as the internal system grows.

## Reason

A top-level file distributed to many humans, agents and integrations must remain minimal and durable. New internal standards must not continually expand the public entry contract or force redistribution of copied instructions.

The stable URL remains:

```text
https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md
```

Recipients should follow the current file at that URL rather than depend on stale copied contents.

## Boundary

`START_HERE.md` must not store:

- the growing route catalogue;
- operating procedures;
- workflow details;
- architecture details;
- tool procedures;
- execution instructions;
- project state;
- agent logic.

`docs/ROUTER.md` stores navigation only. It must not store detailed procedures, project state, logs, secrets or reusable knowledge content.

## Implementation Evidence

### Router created

File:

`docs/ROUTER.md`

Commit:

`6c37027cbcb0aa81b90ac9791f407311916031da`

### START_HERE reduced to stable door

File:

`START_HERE.md`

Commit:

`5d8193faf077097fdad92ca1627044aca2dd1c71`

### Context assembly aligned

File:

`docs/CONTEXT_ASSEMBLY_STANDARD.md`

Commit:

`0b1206a7420e324a92da5716182de7a45ad90463`

### ChatGPT core prompt aligned

File:

`docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`

Commit:

`4b96b07014a387d068c63fe69afa6b1be1e15ac5`

### Context manifest refreshed

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

## Status

`implemented — committed repository architecture`

## Follow-Up

Update central navigation documents and run a bounded review to detect any remaining references that incorrectly treat `START_HERE.md` as the live route catalogue.