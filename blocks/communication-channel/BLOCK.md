# Communication Channel Block

## Purpose

This block is the reusable entrypoint for choosing the communication path between connected AI participants in `Project Execution OS`.

It prevents channel ambiguity without duplicating the canonical communication policy.

## Status

`active`

## Use This Block For

- communication-channel selection;
- connected-agent coordination;
- coordination transport questions;
- repository-bound versus cross-project channel choice;
- lightweight status exchange routing.

## Core Rule

Choose the lightest durable channel that fits the active work and is available to the participants.

## Route

```text
START_HERE.md
→ docs/ROUTER.md
→ blocks/communication-channel/BLOCK.md
→ docs/AI_COORDINATION_HUB_STANDARD.md
→ selected active channel
```

## Depends On

- `docs/AI_COORDINATION_HUB_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`

## Boundary

This block selects the communication route. It does not replace project state, repository evidence, execution logs, or the canonical communication policy.

## Final Rule

Select one channel explicitly and follow `docs/AI_COORDINATION_HUB_STANDARD.md` for the detailed policy.
