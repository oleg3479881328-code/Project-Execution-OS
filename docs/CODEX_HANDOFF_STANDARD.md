# Codex Handoff Standard v2

## Purpose

This standard defines how reasoning-model work is handed to Codex or any other executor.

Use an executor only when executor access is actually needed for:
- repository edits;
- local commands;
- validation;
- environment inspection;
- other tool-only work.

If a task is small, safe, and can be completed directly through reasoning and drafting, do it without an executor.

## Core Model

```text
Reasoning model decides and specifies.
Executor performs the specified actions.
Reviewer verifies.
Repository memory persists.
```

## Non-Thinking Executor Rule

The executor is the hands, not the head.

The reasoning model owns all analysis, architecture, choices, prioritization, naming, scope, implementation design, acceptance criteria, and validation design before the handoff is sent.

The executor must not:
- design the solution;
- choose between approaches;
- reinterpret the objective;
- invent missing requirements;
- fill an unspecified decision with an assumption;
- propose a different architecture;
- expand or reduce scope;
- decide what the owner probably meant;
- make product, UX, data, security, or workflow decisions.

The executor may inspect files, repository state, commands, and outputs only as required to perform the specified actions and collect evidence. Inspection does not authorize it to choose or redesign the solution.

Every handoff must be complete enough for the executor to follow mechanically, including exact targets, exact required changes, fixed naming and behavior, forbidden changes, validation steps, and expected outputs.

If an instruction is missing, contradictory, unsafe, impossible, or requires a decision that was not supplied, the executor must stop before improvising and report one precise blocker: what decision or input is missing and where execution stopped.

A weak or inexpensive model must be able to execute the packet correctly without independent reasoning.

## Transport Rule

The handoff packet is the payload.

GitHub issue, PR comment, or review thread is the transport when no direct runtime bridge exists.

Prefer an existing suitable project-bound GitHub channel before creating a new one.

## Exact GitHub Comment Retrieval Rule

When the owner relays a direct GitHub URL containing an exact issue-comment, PR-comment, or review-thread identifier, that exact comment is the task payload.

The executor must:
- read the exact comment directly through GitHub CLI or GitHub API using the supplied repository, issue/PR number, and comment ID;
- begin execution immediately after retrieving the payload;
- use the supplied direct URL as the authoritative transport location.

The executor must not:
- search the web for the URL;
- open or analyze the general Issue or PR page before retrieving the exact comment;
- announce that it will read, inspect, summarize, or interpret the comment;
- restate the task before execution;
- fall back to web browsing unless GitHub CLI/API returns a concrete authentication, permission, or availability error.

Every reasoning-model handoff that returns a direct GitHub comment URL must include this retrieval behavior explicitly when needed. This rule exists to avoid redundant searches, unnecessary pre-execution chatter, and avoidable executor-limit consumption.

## Owner-Facing Handoff Rule

The owner should not receive large handoff packets in chat by default.

Default behavior:

1. prepare the full execution packet inside the selected GitHub transport;
2. keep detailed instructions, constraints, acceptance criteria, and reporting format inside that transport;
3. return to the owner only the shortest useful handoff, normally a single GitHub issue, PR, or review-thread link;
4. provide the full packet in chat only when the owner explicitly asks for copy-paste text.

The purpose is to reduce chat clutter while preserving complete execution context for the executor.

## Hard Link-Only Owner Output Constraint

This is a mandatory owner-interface rule, not a stylistic preference.

When a reasoning model has created or updated a durable executor packet in GitHub or another registered durable transport, its normal owner-facing response must be link-only or link-plus-one-short-sentence.

Do not paste the execution packet, acceptance criteria, command list, implementation plan, report template, or other long executor-facing material into owner chat when a durable link can carry it.

A long pasted handoff in owner chat is considered a handoff-protocol failure unless one of these exceptions applies:

- the owner explicitly asks for the full copy-paste packet;
- no durable transport is available;
- the link itself is insufficient because the owner must manually paste content into an environment that cannot open the transport.

If none of those exceptions applies, create/update the durable packet first and return the direct link.

Before sending an owner-facing executor handoff, perform this final check:

```text
Can the executor receive the complete task from one durable link?
YES -> send the link, not the packet.
NO  -> fix the durable transport or use an explicit exception.
```

This check applies to ChatGPT, reasoning models, reviewers, coordinators, secretaries, and any future owner-facing orchestration layer.

## Canonical One-Link Relay Workflow

This is the default end-to-end workflow when the owner manually relays links between the reasoning model and the executor:

1. The owner and reasoning model discuss the task until every implementation decision is complete.
2. The reasoning model publishes one self-contained execution packet in the project-bound GitHub transport.
3. The reasoning model returns to the owner only the direct URL of that packet.
4. The owner passes that URL to the executor.
5. The executor opens the packet and begins execution immediately.
6. The executor performs the work, validates it, and publishes the complete execution report and evidence at the packet's specified `Response URL`.
7. The executor returns to the owner only the direct URL of the execution report. If blocked, it returns only the direct URL of a precise blocker report.
8. The owner passes that report URL to the reasoning model.
9. The reasoning model opens and verifies the actual report, changes, and evidence, then accepts the result or publishes the next fully specified correction packet.
10. The cycle repeats until the reasoning model accepts the result.

The normal transport is therefore:

```text
Discussion and decisions
-> one task URL
-> execution
-> one report URL
-> reasoning-model review
-> accept or next task URL
```

The owner is a link relay in this temporary manual bridge, not the implementation analyst and not the reviewer. The owner must not be asked to interpret the packet, compare technical options, inspect evidence, or decide how the executor should proceed.

Each direction uses one primary link. Do not require the owner to copy large packets, logs, reports, or multiple URLs between agents.

## No Pre-Execution Chatter

After receiving the task URL, the executor must not:

- restate or summarize the assignment;
- explain how it understood the assignment;
- announce a plan;
- describe what it is about to do;
- ask for confirmation of decisions already present in the packet;
- send conversational progress updates.

The executor's next owner-facing message must contain only:

- the direct execution-report URL after completion; or
- the direct blocker-report URL when mechanical execution cannot continue.

Detailed results, validation evidence, changed files, risks, and deviations belong inside the linked execution report, not in owner-facing chat.

## Mandatory Execution Mode

Every Codex or executor handoff must include an `Execution Mode` section.

Default behavior:

- begin implementation immediately;
- execute the packet literally and only within its stated scope;
- do not pause for optional preferences because all implementation decisions must already be supplied;
- do not resolve ambiguity, make assumptions, or choose a reasonable alternative;
- ask or report a blocker only when a missing decision, conflicting instruction, missing access, missing required credential, unsafe action, or impossible validation prevents mechanical execution;
- stop before any unspecified or out-of-scope action.

Use an interactive planning session instead only when the owner explicitly requests planning rather than execution. Planning belongs to the reasoning model, not the executor.

## Existing-Solution Responsibility

Searching for, comparing, and selecting an existing solution is reasoning work.

The reasoning model must complete that work before an implementation handoff and identify the selected solution or exact implementation design in the packet.

An executor may be assigned a bounded evidence-gathering task with exact search targets and return format. In that case it reports findings only and does not choose the solution.

## Full Packet

Use this for meaningful software execution work:

```text
IMPLEMENTATION HANDOFF PACKET

Packet Type:
Objective:
Source Decision / Design:
Decisions Already Made:
Allowed Scope:
Out Of Scope:
Repository Context:
Files Allowed To Change:
Forbidden Changes:
Selected Existing Solution Or Exact Implementation Design:
Implementation Instructions:
Execution Mode:
- Begin implementation immediately.
- Execute these instructions literally and only within the allowed scope.
- Do not make assumptions, choose alternatives, or redesign the solution.
- Stop and report the exact blocker if any required decision or input is missing.
Acceptance Criteria:
Validation Commands / Checks:
Expected Outputs:
Rollback Notes:
Execution Report Contract:
Response URL:
```

This is the default next artifact whenever the task is clearly executor-bound and executor access is now the missing step.

## Packet Lite

Use this when the task is narrow, low-risk, and bounded to a few files:

```text
CODEX PACKET LITE

Objective:
Decisions Already Made:
Files Allowed To Change:
Forbidden Changes:
Exact Changes:
Execution Mode:
- Begin implementation immediately.
- Execute these instructions literally and only within the allowed scope.
- Do not make assumptions, choose alternatives, or redesign the solution.
- Stop and report the exact blocker if any required decision or input is missing.
Acceptance Criteria:
Validation:
Expected Output:
Return:
Response URL:
```

The reasoning model must not send either packet until all choices required for mechanical execution have been made.

## Execution Report

The executor must return:

```text
EXECUTION REPORT

Status:
Files Changed:
Specified Solution Implemented:
Validation Performed:
Validation Not Performed:
Blockers:
Deviations From Packet: None / Blocked Before Deviation
Risks / Follow-Up:
Ready For Review: Yes / No
```

The executor reports evidence, not new design recommendations. Any newly discovered decision belongs back with the reasoning model.

## Evidence Rule

Do not claim `saved`, `committed`, `tested`, `executed`, `reviewed`, or `completed` without evidence.

A `commit SHA` proves a repository change exists.

It does not by itself prove full correctness.

Validation evidence and review are still required.