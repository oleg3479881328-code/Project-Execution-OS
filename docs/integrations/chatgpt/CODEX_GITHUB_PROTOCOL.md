# ChatGPT Codex GitHub Integration

## Purpose

This is the ChatGPT-facing nested integration entrypoint for the GitHub-based `ChatGPT <-> Codex` collaboration loop.

Do not enter this document directly from the top-level router.

First enter:

`blocks/communication-channel/BLOCK.md`

Then select GitHub as the active channel.

Use this nested protocol when:

- reasoning work is ready for Codex execution;
- GitHub issue, pull request, or review thread will carry the task;
- durable GitHub-based multi-agent coordination is needed.

## Compact Coordination State And Append-Only Log

When the target repository contains:

```text
AI_COORDINATION_STATE.md
AI_COORDINATION_LOG.md
```

read `AI_COORDINATION_STATE.md` before opening the active GitHub issue, pull request, or review thread.

Read `AI_COORDINATION_LOG.md` only when historical coordination context is required.

Use:

```text
docs/AI_COORDINATION_STATE_STANDARD.md
docs/AI_COORDINATION_LOG_STANDARD.md
```

for the canonical snapshot format, append-only log rule, update triggers, reading order, and channel-migration rule.

The snapshot does not replace GitHub comments, commits, PR diffs, or validation evidence.

The append-only log does not replace the snapshot or the active GitHub discussion surface.

After a meaningful coordination transition:

```text
append event to AI_COORDINATION_LOG.md
-> update AI_COORDINATION_STATE.md if current operational state changed
-> keep the active Issue / PR / review thread as message transport
```

## Canonical Protocol

The canonical full protocol currently lives here:

`docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

Use that document for:

- the complete role model;
- message header rules;
- handoff packet expectations;
- execution report expectations;
- fallback and default-decision behavior;
- review and validation separation.

## Related Artifacts

- `blocks/communication-channel/BLOCK.md`
- `docs/AI_COORDINATION_STATE_STANDARD.md`
- `docs/AI_COORDINATION_LOG_STANDARD.md`
- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`

## Design Rule

Keep one top-level communication route:

`Канал связи`

Keep ChatGPT-specific GitHub routing here.

Keep the deeper reusable protocol stable and reviewable in the canonical protocol artifact.
