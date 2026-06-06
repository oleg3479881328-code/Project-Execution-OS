# Codex Handoff Standard Addendum — 2026-06-06

## Purpose

Extend `docs/CODEX_HANDOFF_STANDARD.md` with mandatory reply-surface acknowledgement and default reviewable publication behavior.

## Required Companion Standard

Read and apply:

`docs/CODEX_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`

## Operational Effect

For bounded repository implementation work:

- Codex acknowledges the handoff immediately in the named GitHub reply surface;
- Codex posts blockers and clarifications there without waiting for manual prompting;
- Codex validates, commits, pushes to a private branch, opens a draft PR, and posts the execution report unless the packet explicitly chooses another publication mode;
- routine review fixes continue without a second owner confirmation;
- only real escalation boundaries stop execution.

## Final Rule

The owner is the trigger, not the courier. GitHub is the durable reply channel.