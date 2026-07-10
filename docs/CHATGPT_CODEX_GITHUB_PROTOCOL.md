# ChatGPT Codex GitHub Protocol

## Purpose

This document defines the canonical collaboration loop between a reasoning model such as ChatGPT and an execution model such as Codex when GitHub is used as the durable coordination layer.

The goal is to prevent vague handoffs, hidden state, fake completion claims, and confusion about how one AI session reports results to another.

Codex is not the default answer for every task. Use this protocol only when repository execution, local commands, validation, or other executor-only actions are actually needed.

This protocol is also operationalized as a central reusable skill:

- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`

## Core Model

Use this sequence:

```text
Reasoning model defines or reviews the work.
GitHub stores the durable task context.
Codex executes repository changes.
Codex posts its report in the GitHub coordination surface.
ChatGPT reads and reviews that report through GitHub.
GitHub stores the execution diff and review trail.
Repository memory preserves the accepted result.
```

Short form:

```text
ChatGPT thinks.
GitHub carries the task and replies.
Codex executes and reports in GitHub.
ChatGPT reads GitHub and reviews.
Repository memory persists.
```

## Role Separation

### Reasoning model

ChatGPT, Claude, Gemini, or another reasoning-oriented AI may:

- clarify the task;
- perform research;
- shape the plan;
- prepare design or execution artifacts;
- produce implementation handoff packets;
- review Codex output;
- write GitHub comments, issues, or PR guidance when the connector is available.

The reasoning model must not pretend it already executed repository changes if Codex or another executor has not done so.

The reasoning model should handle small safe tasks itself when they only require thinking, drafting, summarizing, planning, or producing text artifacts that do not require executor access.

### Codex

Codex may:

- read repository context;
- modify the repository within approved scope;
- run validations when requested and available;
- report blockers, risks, assumptions, commits, and validation evidence in the specified GitHub coordination surface;
- prepare commit-ready or PR-ready repository changes.

Codex must not redesign the task silently when the handoff packet is explicit.

Codex must not attempt to contact a separate ChatGPT chat session directly. Its reply to ChatGPT is a GitHub issue comment, PR comment, or review-thread reply on the coordination surface named in the handoff.

### Reviewer

The reviewer may be a human, ChatGPT, Codex in review mode, or another review-capable agent.

The reviewer must:

- compare execution against the original packet;
- verify scope discipline;
- verify validation evidence;
- separate passed checks from unverified claims;
- approve, request revision, or block acceptance.

## GitHub As Coordination Layer

GitHub is the default durable communication layer when the work already lives in a Git repository or when execution needs reviewable history.

GitHub may carry the collaboration through:

- repository files committed on a branch;
- issues for scoped work requests and execution-report replies;
- pull requests for execution diffs and review-report replies;
- PR descriptions for the handoff packet summary;
- PR comments and review threads for follow-up;
- GitHub Actions checks for validation evidence.

Chat messages are not durable coordination state.

Default cross-project coordination hub:

`oleg3479881328-code/AI-Coordination-Hub`

Use that hub for reusable or cross-project AI coordination threads.

Use the target project repository when the work is tightly bound to one repository's execution scope or review history.

## Transport Reality Rule

There is no required direct transport from one ChatGPT or Codex session into another ChatGPT chat window.

For repository-bound work, communication works as follows:

1. ChatGPT creates or updates a GitHub issue, pull request, review thread, or repository handoff artifact.
2. Codex Desktop (local executor) reads that GitHub surface and executes locally within the allowed scope.
3. Codex Desktop posts its `Execution Report`, clarification, blocker, commit SHA, or validation evidence as a comment in the exact GitHub surface identified in the handoff.
4. ChatGPT reads the GitHub surface through the GitHub connector and responds there with approval, requested changes, or the next packet.
5. The user is not the normal relay for AI-to-AI project coordination.

Important routing distinction:

- `Codex Desktop` / the local Codex executor is the canonical executor for this protocol.
- A GitHub mention such as `@codex` may invoke a separate GitHub/cloud connector bot and is **not** the transport used to start or address the local desktop executor.
- Handoff comments for the local executor must name the recipient in the signed message header, for example `TO: Codex Desktop — Local Executor`, without relying on `@codex` mentions.
- A cloud-bot reply requesting a Codex cloud environment does not prove that the local desktop executor is unavailable or misconfigured.

When Codex says it cannot send a message to a separate ChatGPT chat, that is not a blocker. The required reply channel is GitHub, not chat-to-chat messaging.

Every Codex handoff must explicitly include this instruction when a GitHub coordination surface exists:

```text
Do not attempt to contact another ChatGPT chat session directly.
Post your structured reply as a new comment in this GitHub issue / PR / review thread.
ChatGPT will read and review it here through GitHub.
The user should not need to manually relay the report.
```

## Sync Discipline

For GitHub-coordinated work:

- GitHub `main` is the only source of truth for committed project state.
- The local Codex folder is an execution workspace, not the source of truth.
- Google Drive and other mirrors are inspection channels only, not execution or sync authorities.

Before any local execution:

1. Run `git status`.
2. If local changes exist, report them in the GitHub coordination surface before pulling.
3. Do not commit local changes unless they are explicitly part of the current task.
4. Pull latest `main` before validation:
   - `git pull --ff-only origin main`

After any local fix:

1. Report exact changed files.
2. Run validation.
3. Commit only the minimal intended files.
4. Do not commit `.venv`, logs, `.env`, `desktop.ini`, cache files, or local junk.
5. Push only after the fix is validated.
6. Post the commit SHA and validation report in the coordination surface.

## Preferred Interaction Modes

### Mode 1 — Repository artifact first

Use when the project already follows Project Execution OS.

Flow:

1. Write the task into workflow artifacts such as `05_EXECUTION_SPEC.md` or a dedicated task artifact.
2. Give Codex the exact file paths to read and the GitHub surface where its response must be posted.
3. Let Codex execute locally in the repository.
4. Codex posts the report in the named GitHub surface.
5. Store the accepted result in repository artifacts and optionally publish to GitHub PR.

This is the preferred mode for disciplined project work.

### Mode 2 — GitHub issue to Codex

Use when the task starts from a GitHub issue or when issue-level traceability matters.

Flow:

1. Reasoning model shapes the issue into a precise objective.
2. Issue body or linked artifact defines scope, constraints, acceptance criteria, and the instruction to reply in that same issue.
3. Codex executes against that issue scope.
4. Codex posts the execution report as a comment in the issue and, when code changed, publishes a branch/PR or an explicitly permitted commit.
5. Reviewer reads the issue/PR through GitHub and checks execution against the issue and handoff packet.

### Mode 3 — PR-centered collaboration

Use when the main need is iteration on a concrete diff.

Flow:

1. Reasoning model prepares or updates the handoff packet.
2. Codex implements on a branch.
3. GitHub PR becomes the visible review and reply surface.
4. Codex posts reports and replies inside that PR or its review threads.
5. Review comments and threads drive follow-up work.
6. Reviewer confirms acceptance or requests more changes.

## Message Identity Rule

When GitHub comments or issue updates are used as the communication bridge, each AI-to-AI message should identify the speaker and intended recipient explicitly.

Minimum header:

```text
FROM: ChatGPT
TO: Codex Desktop — Local Executor
TYPE: Handoff
```

and for the return direction:

```text
FROM: Codex Desktop — Local Executor
TO: ChatGPT
TYPE: Execution Report
```

Allowed `TYPE` examples:

- `Handoff`
- `Clarification`
- `Status`
- `Execution Report`
- `Review Request`
- `Blocker`
- `Coordination Clarification`

This avoids ambiguity when issues or PRs contain messages from the user, ChatGPT, Codex, and reviewers in the same thread.

This rule also applies to other explicitly named agents such as:

- `Reviewer`
- `Research-Agent`
- `Architecture-Agent`
- `Documentation-Agent`

or any other clearly named project agent.

## Required Handoff Packet

Before Codex executes meaningful repository changes, create a deterministic packet in repository artifacts or PR or issue-linked artifacts.

Minimum structure:

```text
IMPLEMENTATION HANDOFF PACKET

Packet Type:
Objective:
Source Decision / Design:
Allowed Scope:
Out of Scope:
Repository Context:
Files Allowed To Change:
Forbidden Changes:
Implementation Instructions:
Acceptance Criteria:
Validation Commands / Checks:
Rollback Notes:
Execution Report Contract:
Reply Surface:
```

`Reply Surface` must name the exact GitHub issue, PR, or review thread in which Codex posts its report. If there is no GitHub surface, the packet must state the explicit fallback delivery method.

See:

- `skills/implementation/implementation-handoff-packet/SKILL.md`

## Required Execution Report

Codex must return a structured execution report **as a comment in the named GitHub reply surface**, unless the packet explicitly states a different fallback.

Minimum structure:

```text
FROM: Codex Desktop — Local Executor
TO: ChatGPT
TYPE: Execution Report

EXECUTION REPORT

Status:
Files Changed:
Validation Performed:
Validation Not Performed:
Blockers:
Assumptions Made:
Risks / Follow-Up:
Ready For Review: Yes / No
```

Execution without a report in the required reply surface is incomplete for important work.

## GitHub Comment And Review Cycle

When GitHub is the active coordination surface:

1. Codex posts its structured reply in the named GitHub issue, PR, or review thread; it does not ask the user to transfer the reply into a ChatGPT chat.
2. PR comments and review threads are treated as durable follow-up tasks.
3. Actionable comments must be grouped by file or behavior area.
4. Codex should address only the selected or approved threads.
5. Each follow-up should remain traceable to the original review request.
6. Resolved, outdated, or non-actionable threads must not be treated as fresh work by default.

Relevant GitHub-oriented skills already exist for this loop:

- GitHub umbrella triage
- publish changes to branch and draft PR
- address PR review comments
- inspect failing GitHub Actions checks

## Private Repository Rule

New project repositories are private by default unless the user explicitly chooses public visibility.

Public collaboration via GitHub is allowed only when the user intentionally chooses a public repository or public review surface.

## State And Evidence Rules

Never confuse:

- planned work;
- handed-off work;
- executed work;
- reviewed work;
- merged work.

GitHub evidence should support the actual state:

- issue exists;
- reply comment exists in the named coordination surface;
- branch exists;
- PR exists;
- checks passed or failed;
- comments are open or resolved;
- latest `main` was pulled before local validation when required;
- the reported commit SHA exists when a fix was pushed.

If GitHub evidence is missing, do not claim that the state exists.

Evidence interpretation rule:

- a `commit SHA` proves that a file change exists in repository history;
- a `commit SHA` does not by itself prove full behavioral correctness;
- behavioral confidence still depends on validation evidence and review.

## What Not To Do

Do not:

- instruct Codex to send a message directly to another ChatGPT chat session;
- allow Codex to treat inability to message a ChatGPT chat as a blocker when a GitHub reply surface exists;
- use the user as the normal relay between Codex and ChatGPT for repo-bound coordination;
- send Codex vague prompts such as `improve the project`;
- use GitHub comments as a substitute for a real execution packet;
- allow Codex to broaden scope silently;
- accept a PR because it sounds plausible without checking the diff and validations;
- treat stale local workspace state as authoritative when `main` has moved ahead;
- treat Google Drive or other mirrors as execution authority;
- claim that GitHub history replaces repository memory artifacts inside the project;
- treat chat-only decisions as committed project state;
- use `@codex` as the routing mechanism for Codex Desktop unless the project explicitly opts into the separate cloud-bot workflow.

## Practical Default

For software work, the safest default loop is:

1. clarify and research;
2. if no executor access is needed, complete the small safe step directly;
3. if executor access is needed, create repository artifact or execution spec;
4. create implementation handoff packet naming the exact GitHub reply surface;
5. let Codex Desktop execute within explicit scope;
6. require Codex Desktop to post its execution report in that same GitHub surface;
7. publish to a private branch and draft PR when GitHub diff review is needed;
8. review against the original packet and GitHub-posted report;
9. update repository memory after acceptance.
