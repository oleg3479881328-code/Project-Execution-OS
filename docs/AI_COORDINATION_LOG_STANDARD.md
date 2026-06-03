# AI Coordination Log Standard

## Purpose

This standard defines the append-only coordination event log used during multi-agent project work.

The goal is to preserve a readable chronological record of meaningful coordination events without turning the compact operational snapshot into a growing transcript.

## Canonical File

For an active GitHub-backed project that uses `AI_COORDINATION_STATE.md`, also use a root-level file named:

```text
AI_COORDINATION_LOG.md
```

## Core Split

```text
GitHub issue / PR / review thread
-> message transport and full durable discussion trail

AI_COORDINATION_STATE.md
-> compact current operational snapshot
-> replaced in place when state changes

AI_COORDINATION_LOG.md
-> append-only chronological event journal
-> new entries are added at the bottom only
```

## Append-Only Rule

`AI_COORDINATION_LOG.md` is append-only.

Existing event entries must not be rewritten, reordered, deleted, compressed, or silently corrected.

New events must be appended below existing content.

If an earlier entry contains an error, add a new correction entry at the bottom that references the earlier event.

Do not rewrite history.

## What To Log

Append a new event only for meaningful coordination state transitions:

- communication-channel creation;
- channel migration;
- meaningful handoff packet issued;
- executor acknowledgement;
- meaningful implementation commit;
- review accepted;
- review blocked with actionable revision;
- blocker reported;
- blocker resolved;
- scope changed;
- task completed;
- important reusable workflow lesson discovered.

Do not append every short status, chat reply, or repeated ping.

## Required Event Shape

Use this structure:

```markdown
## <YYYY-MM-DD HH:MM:SS America/New_York>

Actor: <participant>
Type: <event type>
Project: <project name>

Summary:
<short factual description>

Evidence:
- <commit SHA, issue URL, PR URL, file path, or validation result>

Next Step:
<one next action or `None`>
```

## Timestamp Rule

Use `America/New_York` timestamps.

Use a concrete timestamp, not relative wording such as `today`, `just now`, or `later`.

## Evidence Rule

Log claims must distinguish:

- generated state;
- executed state;
- reviewed state;
- accepted state.

A commit SHA proves repository history changed.

It does not prove runtime behavior is correct.

Validation and review evidence must be recorded separately when relevant.

## Write Procedure

Before appending:

1. read the current `AI_COORDINATION_LOG.md`;
2. preserve every existing byte of meaningful event content;
3. append one new event block at the bottom;
4. commit the file update;
5. verify that earlier entries remain present and unchanged.

Do not replace the file with a reconstructed summary.

## Relationship To Snapshot

After a meaningful transition:

```text
append event to AI_COORDINATION_LOG.md
-> update AI_COORDINATION_STATE.md if current operational state changed
-> keep Issue / PR / review thread as the message transport
```

The log is history.

The snapshot is current state.

The transport thread is the full discussion trail.

Do not merge these roles.

## Model-Neutral Rule

The file remains model-neutral and vendor-neutral.

Participants may include:

- ChatGPT;
- Codex;
- DeepSeek;
- Claude;
- another connected AI agent;
- automation;
- a human developer.

## Scope Boundary

Do not store:

- secrets;
- full chat transcripts;
- raw verbose logs;
- large patches;
- copied issue threads;
- sensitive credentials;
- unrelated project documentation.

Use short factual summaries and evidence links.

## Minimal Starter File

```markdown
# AI Coordination Log

## Purpose

Append-only chronological journal of meaningful AI-to-AI coordination events.

Rules:

- append new events at the bottom only;
- never rewrite, reorder, or delete prior events;
- add correction events instead of editing history;
- do not copy the full discussion trail into this file.
```

## Relationship To Other Standards

Use together with:

- `docs/AI_COORDINATION_STATE_STANDARD.md`;
- `blocks/communication-channel/BLOCK.md`;
- `docs/AI_COORDINATION_HUB_STANDARD.md`;
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`;
- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`.

## Final Rule

Append meaningful coordination events at the bottom only.

Never rewrite coordination history.

Keep the snapshot short and current.
