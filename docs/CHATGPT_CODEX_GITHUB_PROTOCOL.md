# ChatGPT Codex GitHub Protocol

## Purpose

This document defines the canonical collaboration loop between a reasoning model such as ChatGPT and an execution model such as Codex when GitHub is used as the durable coordination layer.

The goal is to prevent vague handoffs, hidden state, and fake completion claims.

This protocol is also operationalized as a central reusable skill:

- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`

## Core Model

Use this sequence:

```text
Reasoning model defines or reviews the work.
GitHub stores the durable task context.
Codex executes repository changes.
GitHub stores the execution diff and review trail.
Reviewer verifies against the original packet.
Repository memory preserves the accepted result.
```

Short form:

```text
ChatGPT thinks.
GitHub carries the task.
Codex executes.
GitHub records the change.
Reviewer verifies.
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
- draft GitHub comments, issues, or PR guidance.

The reasoning model must not pretend it already executed repository changes if Codex or another executor has not done so.

### Codex

Codex may:

- read repository context;
- modify the repository within approved scope;
- run validations when requested and available;
- report blockers, risks, and assumptions;
- prepare commit-ready or PR-ready repository changes.

Codex must not redesign the task silently when the handoff packet is explicit.

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
- issues for scoped work requests;
- pull requests for execution diffs;
- PR descriptions for the handoff packet summary;
- PR comments and review threads for follow-up;
- GitHub Actions checks for validation evidence.

Chat messages are not durable coordination state.

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
2. Give Codex the exact file paths to read.
3. Let Codex execute locally in the repository.
4. Store the result in repository artifacts and optionally publish to GitHub PR.

This is the preferred mode for disciplined project work.

### Mode 2 — GitHub issue to Codex

Use when the task starts from a GitHub issue or when issue-level traceability matters.

Flow:

1. Reasoning model shapes the issue into a precise objective.
2. Issue body or linked artifact defines scope, constraints, and acceptance criteria.
3. Codex executes against that issue scope.
4. Execution is published as a branch and PR.
5. Reviewer checks the PR against the issue and handoff packet.

### Mode 3 — PR-centered collaboration

Use when the main need is iteration on a concrete diff.

Flow:

1. Reasoning model prepares or updates the handoff packet.
2. Codex implements on a branch.
3. GitHub PR becomes the visible review surface.
4. Review comments and threads drive follow-up work.
5. Reviewer confirms acceptance or requests more changes.

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
```

See:

- `skills/implementation/implementation-handoff-packet/SKILL.md`

## Required Execution Report

Codex must return a structured execution report.

Minimum structure:

```text
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

Execution without a report is incomplete for important work.

## GitHub Comment And Review Cycle

When GitHub is the active coordination surface:

1. PR comments and review threads are treated as durable follow-up tasks.
2. Actionable comments must be grouped by file or behavior area.
3. Codex should address only the selected or approved threads.
4. Each follow-up should remain traceable to the original review request.
5. Resolved, outdated, or non-actionable threads must not be treated as fresh work by default.

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
- branch exists;
- PR exists;
- checks passed or failed;
- comments are open or resolved.
- latest `main` was pulled before local validation when required;
- the reported commit SHA exists when a fix was pushed.

If GitHub evidence is missing, do not claim that the state exists.

## What Not To Do

Do not:

- send Codex vague prompts such as `improve the project`;
- use GitHub comments as a substitute for a real execution packet;
- allow Codex to broaden scope silently;
- accept a PR because it sounds plausible without checking the diff and validations;
- treat stale local workspace state as authoritative when `main` has moved ahead;
- treat Google Drive or other mirrors as execution authority;
- claim that GitHub history replaces repository memory artifacts inside the project;
- treat chat-only decisions as committed project state.

## Practical Default

For software work, the safest default loop is:

1. clarify and research;
2. create repository artifact or execution spec;
3. create implementation handoff packet;
4. let Codex execute within explicit scope;
5. publish to a private branch and draft PR when GitHub review is needed;
6. review against the original packet;
7. update repository memory after acceptance.
