# AI Coordination State Standard

## Purpose

This standard defines the compact operational state file used during multi-agent project work.

The file prevents long GitHub issues, pull-request threads, or chat trails from becoming the only readable coordination memory.

## Canonical File

For an active GitHub-backed project, use a root-level file named:

```text
AI_COORDINATION_STATE.md
```

Use this file when two or more participants coordinate technical work through GitHub or another durable project channel and the active thread may become too long, fragmented, or hard to resume reliably.

## Core Split

```text
GitHub issue / PR / review thread
-> message transport and durable discussion trail

AI_COORDINATION_STATE.md
-> compact operational state snapshot
```

Do not use `AI_COORDINATION_STATE.md` as a full transcript.

Do not copy every comment into the file.

## Required Contents

The file should contain only the minimum durable coordination state:

```text
Project
Purpose
Active Channel
Previous Channels
Active Participants
Current Task
Current Repository State
Accepted Changes
Open Review Items
Next Step
Required Validation
Update Rule
Reading Rule
```

## Update Triggers

Update `AI_COORDINATION_STATE.md` only after a meaningful state transition:

- communication-channel migration;
- meaningful implementation commit;
- accepted review;
- new blocker;
- scope change;
- completed task.

Do not update it for every short coordination message.

## Reading Rule

Before resuming AI-to-AI coordination in an existing project, especially when processing shorthand command `02`, read in this order when the file exists:

```text
AI_COORDINATION_STATE.md
-> Active Channel
-> latest relevant comments in the active channel
-> latest repository commit or PR state
-> Next Step
```

Do not assume the newest issue or the longest thread is the active channel. Use the file's `Active Channel` field.

## Channel Migration Rule

When an issue, pull request, or review thread becomes too long or unreliable to read:

```text
create a new continuation channel
-> record the new channel in AI_COORDINATION_STATE.md
-> move old channel into Previous Channels
-> post a migration notice in the old channel
-> require executor acknowledgement in the new channel
```

Do not continue posting new execution reports into an archived channel.

## State Discipline

Keep generated state and executed state separate.

A file update proves that the snapshot exists in repository history.

It does not prove that code changes, validations, or runtime behavior are correct.

Record commit SHAs and validation evidence separately.

## Model-Neutral Rule

The file must remain model-neutral and vendor-neutral.

The executor may be:

- Codex;
- DeepSeek;
- Claude;
- another connected AI agent;
- automation;
- a human developer.

The reviewer may also be any explicitly named review-capable participant.

## Scope Boundary

Use this file only for active coordination state.

Do not store:

- secrets;
- raw logs;
- full conversation history;
- large patches;
- copied issue threads;
- unrelated project documentation.

Store large technical artifacts in the appropriate project files and send only short references through the active channel.

## Minimal Template

```markdown
# AI Coordination State

## Project

<project name>

## Purpose

Compact operational state for AI-to-AI coordination.

## Active Channel

<exact GitHub issue / PR / review-thread URL>

## Previous Channels

- <old channel and reason for migration>

## Active Participants

- Owner:
- Reviewer:
- Executor Agent:

## Current Task

<one bounded task>

## Current Repository State

Latest reviewed commit:

`<sha>`

Current review status:

`<status>`

## Accepted Changes

- <accepted item>

## Open Review Items

- <open item>

## Next Step

<one next action>

## Required Validation

```text
<commands and manual checks>
```

## Update Rule

Update only after a meaningful state transition.

## Reading Rule

```text
read AI_COORDINATION_STATE.md
-> open Active Channel
-> read latest relevant comments
-> inspect latest repository commit
-> continue from Next Step
```
```

## Relationship To Other Standards

Use together with:

- `blocks/communication-channel/BLOCK.md`;
- `docs/AI_COORDINATION_HUB_STANDARD.md`;
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`;
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` when durable handoff readiness matters.

## Final Rule

Use GitHub threads for transport.

Use `AI_COORDINATION_STATE.md` for compact operational state.

Do not allow a long message thread to become the only resumable project memory.
