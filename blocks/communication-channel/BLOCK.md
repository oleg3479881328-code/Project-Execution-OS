# Communication Channel Block

## Display Name

`Канал связи`

## Purpose

This block is the single top-level entrypoint for communication-channel work inside `Project Execution OS`.

Use this block whenever the active request concerns:

- communication between connected AI participants;
- message transport;
- selection of a coordination channel;
- uncertainty about where an agent-to-agent message should go;
- the shorthand commands `01` or `02`;
- GitHub, Notion comments, chat, or an optional coordination hub used as a communication path.

Do not route these cases directly from `docs/ROUTER.md` into a channel-specific protocol.

## Status

`active`

## Core Rule

First select the active communication channel.

Only after the channel is selected, open the narrowest relevant nested standard or protocol.

When an active GitHub-backed project contains `AI_COORDINATION_STATE.md`, treat that file as the compact operational snapshot for channel continuation.

## Route

```text
START_HERE.md
→ docs/ROUTER.md
→ blocks/communication-channel/BLOCK.md
→ docs/AI_COORDINATION_HUB_STANDARD.md
→ selected active channel
```

## Nested Routes

### General channel selection or coordination policy

Open:

`docs/AI_COORDINATION_HUB_STANDARD.md`

Use it to choose among:

- `Chat`;
- `Notion comments`;
- the target repository's GitHub issue, pull request, or review thread;
- the optional cross-repository coordination hub.

### Compact coordination state

When an active GitHub-backed project contains a root-level coordination snapshot, open:

`AI_COORDINATION_STATE.md`

Use:

`docs/AI_COORDINATION_STATE_STANDARD.md`

for the canonical file format, update triggers, reading order, and channel-migration rule.

### GitHub-based ChatGPT / Codex collaboration

Open only after GitHub has been selected as the active channel:

`docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`

This is a nested channel-specific protocol.

It is not a separate top-level route beside `Канал связи`.

### Codex execution payload

When the task itself is already decided and executor access is required, also open:

`docs/CODEX_HANDOFF_STANDARD.md`

The handoff packet is the payload.

The selected communication channel is the transport.

Do not confuse payload with transport.

## Commands

### `01`

Send the relevant current message to the targeted connected AI participant through that participant's registered active channel.

### `02`

Read the latest relevant incoming message from the targeted connected AI participant through the registered active channel and respond based on its actual content.

When the active project contains `AI_COORDINATION_STATE.md`, use this order:

```text
read AI_COORDINATION_STATE.md
→ open its Active Channel
→ read latest relevant incoming comments
→ inspect latest repository commit or PR state
→ continue from Next Step
```

`01` and `02` control communication only.

They do not approve destructive actions, scope expansion, repository changes, or other execution by themselves.

## Boundary

This block is a routing block.

Keep detailed channel policy, agent registry, channel registry, technical protocol details and long examples in the nested standards.

## Final Rule

`Канал связи` is the one top-level communication route.

Select the transport first.

Then open only the narrowest nested protocol required by the selected channel and the active work.
