# Executor Channel Acknowledgement And Publication Standard

Updated: 2026-06-11
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

The acknowledgement must start with the exact first-line marker:

```text
ACK
```

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

## Durable Status Snapshot Mirror

The active reply surface is the communication transport, but it must not be the only readable current-state surface.

After every `ACK`, `HEARTBEAT`, `BLOCKER`, or `COMPLETE` comment, the executor must also update the current project's durable status mirror when the project contains one:

```text
projects/<project>/logs/latest.md
```

The mirror update must include:

- timestamp;
- active task;
- first-line marker used;
- short factual status;
- exact reply-surface URL;
- direct comment URL when available;
- current commit SHA when available;
- next automatic action;
- whether owner action is required.

After every meaningful state transition, also update:

```text
projects/<project>/PROJECT_STATE.md
```

Use this for:

- accepted plan change;
- blocker that changes route;
- resource creation or cleanup;
- completed phase;
- paused state;
- restart point;
- final completion.

This mirror rule exists because connector reads can lag, truncate, or omit the newest long-thread comments. A project must remain resumable from repository state even when the transport read path is imperfect.

## Mandatory Status Markers

Every durable executor status comment must begin with exactly one marker on the first line:

```text
ACK
HEARTBEAT
BLOCKER
COMPLETE
```

Use:

- `ACK` for handoff receipt and execution start;
- `HEARTBEAT` for progress updates;
- `BLOCKER` for a real stop condition requiring input or route change;
- `COMPLETE` for reviewable completion evidence.

Do not use vague first lines such as `Task Completed`, `Status Update`, or an unmarked summary when one of the canonical markers applies.

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
HEARTBEAT
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

After sending any durable message, the sender must immediately show the owner a short linked receipt using:

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
-> update durable status mirror
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

If the executor cannot continue, it must post a signed blocker report immediately in the active reply surface, update the durable status mirror, then show the owner a linked receipt. It must not wait silently for a manual prompt.

A blocker report must begin with:

```text
BLOCKER
```

## Completion Rule

A final execution report must begin with:

```text
COMPLETE
```

It must include:

- completed scope;
- files changed or artifacts created;
- commit SHA when applicable;
- validation performed;
- validation not performed;
- cleanup state when runtime resources were used;
- remaining risks;
- next safe action.

After posting it, update the durable status mirror before declaring completion to the owner.

## Review Continuation Rule

When a reviewer posts a bounded revision request inside the approved scope, the executor continues automatically through fix, validation, publication, updated report, durable mirror update, and owner-visible linked receipt.

## Readback Reliability Rule

When a reasoning agent checks for an incoming reply, it must not rely on one connector read of a long issue thread alone.

Use this order:

```text
read ACTIVE_CHANNEL_ROUTE.md
-> read current project's logs/latest.md
-> read current project's PROJECT_STATE.md when state changed materially
-> open active reply surface
-> inspect latest issue metadata and latest relevant comments
-> inspect latest commit when the executor reported one
-> reconcile transport comment and durable mirror
```

If the connector response is truncated, stale, or missing the newest comment:

- do not claim that no reply exists;
- report that the connector read is inconclusive;
- use the durable mirror and issue metadata as fallback evidence;
- ask for manual relay only as the last resort.

## Automatic Continuation Rule

For already-authorized bounded work, the executor continues automatically after posting `ACK`, `HEARTBEAT`, review-fix updates, and non-blocking status reports.

Do not wait for:

- a second `01`;
- a second owner ping;
- a repeated handoff;
- manual relay of the same instruction.

Stop only at the defined stop boundary or a real blocker.

## Owner Trigger Rule

The owner starts or redirects work. The owner is not the routine courier between agents.

## Final Rule

A bounded handoff is not complete when local work exists. It is complete only when the reviewable result, structured report, durable status mirror, and owner-visible linked receipt are visible.

A long-running bounded handoff is not healthy while silent. It must remain observable through periodic progress heartbeats in the active reply surface and durable project mirror.
