# Executor Channel Acknowledgement And Publication Standard

Updated: 2026-06-06
Status: `active`

## Purpose

Prevent any execution agent from completing work silently, waiting for manual prompting, or treating routine publication of reviewable results as a new owner decision.

This standard applies to Codex, DeepSeek, Claude, local models, specialized agents, future connected executors, and human-assisted executor workflows when they operate through Project Execution OS.

## Mandatory Acknowledgement

When an execution agent receives a bounded handoff packet, it must immediately post a short signed acknowledgement in the exact named reply surface before starting work.

The acknowledgement must state:

- handoff received;
- active reply surface;
- execution has started;
- whether any blocker exists;
- the next expected report type.

## Active Reply Surface

The named GitHub issue, pull request, review thread, Notion comment thread, or other registered durable transport is the active bidirectional channel.

The executor must post there without waiting for the owner to relay messages:

- acknowledgement;
- clarification question;
- blocker report;
- useful status update;
- execution report;
- artifact URL;
- commit SHA and pull-request URL when repository changes are published;
- validation evidence.

## Default Publication Rule

For a bounded implementation handoff that authorizes reviewable repository edits, the executor continues through:

```text
acknowledge
-> implement
-> validate
-> minimal commit
-> push to private review branch
-> open draft pull request
-> post structured execution report in the named reply surface
```

This is routine in-scope execution. It does not require a second owner confirmation.

For a bounded non-code handoff, replace commit and PR publication with the smallest reviewable artifact appropriate to the active channel.

## Stop Boundary

The executor must stop and ask in the active reply surface before:

- destructive action;
- scope expansion;
- repository visibility change;
- external public publication;
- production deployment;
- irreversible data migration;
- business decision;
- legal, financial, or safety-critical decision outside the approved scope;
- unresolved ambiguity that cannot be resolved from repository standards.

## Blocker Rule

If the executor cannot continue, it must post a signed blocker report immediately in the active reply surface. It must not wait silently for a manual prompt.

## Review Continuation Rule

When a reviewer posts a bounded revision request inside the approved scope, the executor continues automatically through fix, validation, publication, and updated report.

## Owner Trigger Rule

The owner starts or redirects work. The owner is not the routine courier between agents.

## Final Rule

A bounded handoff is not complete when local work exists. It is complete only when the reviewable result and structured report are visible in the named durable channel.