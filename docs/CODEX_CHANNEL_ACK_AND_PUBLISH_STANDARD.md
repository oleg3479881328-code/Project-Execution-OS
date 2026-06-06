# Codex Channel Acknowledgement And Publication Standard

Updated: 2026-06-06
Status: `active`

## Purpose

Prevent Codex from completing local work silently, waiting for manual prompting, or treating routine publication of reviewable changes as a new owner decision.

## Mandatory Acknowledgement

When Codex receives a bounded GitHub handoff packet, it must immediately post a short signed acknowledgement in the exact named reply surface before starting work.

The acknowledgement must state:

- handoff received;
- active reply surface;
- execution has started;
- whether any blocker exists;
- the next expected report type.

## Active Reply Surface

The named GitHub issue, pull request, or review thread is the active bidirectional channel.

Codex must post all of the following there without waiting for the owner to relay messages:

- acknowledgement;
- clarification question;
- blocker report;
- status update when useful;
- execution report;
- commit SHA;
- pull-request URL;
- validation evidence.

## Default Publication Rule

For a bounded implementation handoff that authorizes repository edits and reviewable publication, Codex must continue through:

```text
local implementation
-> validation
-> minimal commit
-> push to private branch
-> open draft pull request
-> post execution report in the named reply surface
```

This is routine in-scope execution. It does not require a second owner confirmation.

## Stop Boundary

Codex must stop and ask in the active reply surface before:

- destructive action;
- scope expansion;
- repository visibility change;
- external public publication;
- production deployment;
- irreversible data migration;
- business decision;
- unresolved ambiguity that cannot be resolved from repository standards.

## Blocker Rule

If Codex cannot continue, it must post a signed blocker report immediately in the active reply surface. It must not wait silently for a manual prompt.

## Review Continuation Rule

When ChatGPT posts a bounded revision request inside the active scope, Codex continues automatically through fix, validation, commit, push, and updated report.

## Final Rule

A bounded GitHub handoff is not complete when local files exist. It is complete only when the reviewable branch or PR and the structured report are visible in the named GitHub channel.