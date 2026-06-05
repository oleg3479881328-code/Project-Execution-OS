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

When the project also contains `AI_COORDINATION_LOG.md`, treat it as the append-only chronological journal of meaningful coordination events.

For every durable coordination note, letter, request, review, report, or acknowledgement, use signed polite message format from:

`docs/AI_COORDINATION_MESSAGE_STANDARD.md`

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

When an active GitHub-backed project contains root-level coordination files, open:

```text
AI_COORDINATION_STATE.md
AI_COORDINATION_LOG.md
```

Use:

```text
docs/AI_COORDINATION_STATE_STANDARD.md
docs/AI_COORDINATION_LOG_STANDARD.md
```

for the canonical file formats, update triggers, reading order, append-only rule, and channel-migration rule.

### Signed polite coordination messages

For durable coordination messages, open:

`docs/AI_COORDINATION_MESSAGE_STANDARD.md`

Every durable message must identify sender, recipient, subject, type, and project; include a polite greeting; state the request, decision, report, or next action clearly; and end with a signature and role.

### GitHub-based ChatGPT / Codex collaboration

Open only after GitHub has been selected as the active channel:

`docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`

This is a nested channel-specific protocol.

It is not a separate top-level route beside `Канал связи`.

### In-scope review continuation

For bounded review fixes, required validation, bookkeeping updates, and required execution reports, open:

`docs/IN_SCOPE_REVIEW_CONTINUATION_STANDARD.md`

A review follow-up that remains inside the already approved task scope is a continuation of the active task. The executor continues from the latest bounded instruction in the registered active channel without asking the owner for a second confirmation.

Return to the owner only for scope expansion, destructive action, repository visibility change, external publication, business decision, or unresolved ambiguity that cannot be resolved from repository standards.

### Codex execution payload

When the task itself is already decided and executor access is required, also open:

`docs/CODEX_HANDOFF_STANDARD.md`

The handoff packet is the payload.

The selected communication channel is the transport.

Do not confuse payload with transport.

## Commands

The meanings below are universal for all connected AI participants.

Do not reinterpret them based on role, model, project, or nearby numbered options.

### `01`

Meaning: `write / send`.

Send the relevant current message to the targeted connected AI participant through that participant's registered active channel.

Use signed polite message format for durable channel messages.

`01` is not a separate execution authorization. Do not request `01` merely because an already-authorized task was discovered after reading the channel.

### `02`

Meaning: `read / check`.

Read the latest relevant incoming message from the targeted connected AI participant through the registered active channel and respond based on its actual content.

If the latest incoming message contains an already-authorized actionable request that is within the approved scope, continue with that request immediately after reading it. Do not stop to ask for a separate `01` command.

Ask for a new explicit approval only when the newly discovered action is destructive, expands scope, changes repository visibility, publishes externally, or otherwise requires owner approval under an existing standard.

When the active project contains `AI_COORDINATION_STATE.md`, use this order:

```text
read AI_COORDINATION_STATE.md
→ open its Active Channel
→ read latest relevant incoming comments
→ inspect latest repository commit or PR state
→ read AI_COORDINATION_LOG.md only when historical context is required
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

Use signed polite messages for durable coordination.