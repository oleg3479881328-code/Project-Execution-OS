# Executor Channel Acknowledgement And Publication Standard

Updated: 2026-06-09
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
- progress heartbeat;
- execution report;
- artifact URL;
- commit SHA and pull-request URL when repository changes are published;
- validation evidence.

## Mandatory Progress Heartbeat

An executor must not remain silent during a long-running task.

If execution is still in progress 20 minutes after acknowledgement, post a short progress heartbeat in the active reply surface.

After that, post another heartbeat at least every 20 minutes until the final execution report or blocker report is published.

Also post an immediate heartbeat when any of these events occurs:

- a major phase completes;
- validation starts;
- a long benchmark or model-comparison run starts;
- a branch or pull request is created;
- the estimated remaining time changes materially;
- a non-blocking failure occurs and execution continues through fallback;
- the executor changes the implementation plan inside the approved scope.

A heartbeat is a status report, not a request for permission. After publishing it, continue execution automatically unless a real blocker exists.

Do not restart completed work merely because a reviewer or owner asks for status.

### Required Heartbeat Fields

Use this compact format:

```text
PROGRESS HEARTBEAT
Status:
Current Phase:
Completed Since Last Update:
In Progress:
Still Pending:
Current Branch / PR:
Validation State:
Fallbacks Or Non-Blocking Errors:
Estimated Remaining Time:
Blocker Requiring Owner Input: none / <exact blocker>
Next Automatic Action:
```

Keep the heartbeat short and factual. Do not paste long command output, raw logs, or repeated background explanation unless it is required to explain a blocker.

### Short Task Rule

For tasks completed in under 20 minutes, the initial acknowledgement and final execution report are sufficient unless a blocker or material non-blocking failure occurs.

### Owner Visibility Rule For Heartbeats

After posting a durable heartbeat, show the owner a short linked receipt using:

`docs/OWNER_VISIBLE_CHANNEL_RECEIPT_STANDARD.md`

## Mandatory Owner-Visible Receipt

After sending any durable message, the executor must immediately show the owner a short linked receipt using:

`docs/OWNER_VISIBLE_CHANNEL_RECEIPT_STANDARD.md`

The receipt must identify:

- what was sent;
- message type;
- recipient;
- active channel;
- direct message URL or narrowest available durable channel URL;
- current state;
- what the executor is waiting for;
- next action.

Do not merely say `sent`.

## Default Publication Rule

For a bounded implementation handoff that authorizes reviewable repository edits, the executor continues through:

```text
acknowledge
-> implement
-> publish progress heartbeats while long-running
-> validate
-> minimal commit
-> push to private review branch
-> open draft pull request
-> post structured execution report in the named reply surface
-> show owner-visible linked receipt
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

If the executor cannot continue, it must post a signed blocker report immediately in the active reply surface, then show the owner a linked receipt. It must not wait silently for a manual prompt.

## Review Continuation Rule

When a reviewer posts a bounded revision request inside the approved scope, the executor continues automatically through fix, validation, publication, updated report, and owner-visible linked receipt.

## Owner Trigger Rule

The owner starts or redirects work. The owner is not the routine courier between agents.

## Final Rule

A bounded handoff is not complete when local work exists. It is complete only when the reviewable result, structured report, and owner-visible linked receipt are visible.

A long-running bounded handoff is not healthy while silent. It must remain observable through periodic progress heartbeats in the active reply surface.