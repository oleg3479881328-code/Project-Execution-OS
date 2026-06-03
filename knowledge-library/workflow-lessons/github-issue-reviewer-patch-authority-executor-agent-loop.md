# Reviewer patch authority in a GitHub Issue-based executor-agent loop

- Type: `workflow-lesson`
- Lifecycle status: `active`
- Review status: `reviewed and accepted for selective reuse`
- Date: `2026-06-03`

## Terminology

Use `executor agent` — агент-исполнитель — as the generic term.

An executor agent may be:

- Codex;
- DeepSeek;
- Claude;
- another coding or tool-using AI agent;
- an automation service;
- a human developer acting inside the same protocol.

Do not hard-code this workflow to one model or vendor.

## Problem

When a reasoning model and an executor agent collaborate through GitHub, a handoff packet and execution report are not always enough.

During implementation or debugging, the reviewer may identify a precise fix faster than the executor. Without an explicit protocol, the loop can become inefficient:

- the reviewer explains the same correction repeatedly;
- the executor invents a different implementation instead of applying the known fix;
- the user manually relays code between AI sessions;
- validation evidence becomes fragmented;
- repository history no longer clearly shows which proposed patch was applied.

## Verified Workflow Pattern

For repository-bound work, use one GitHub Issue, pull request, or review thread as the durable communication channel.

The handoff packet remains the execution payload.

The GitHub thread remains the transport and review trail.

The reviewer is allowed to publish ready-to-apply code snippets, targeted patches, file replacements, or exact line-level edits directly in the active GitHub communication surface.

When such a reviewer patch is posted, the executor agent must:

1. apply it exactly unless a concrete technical conflict is found;
2. report the conflict in the same GitHub thread before inventing an alternative;
3. run the required validation commands and manual checks;
4. commit only the intended minimal files;
5. push the validated change;
6. post the commit SHA, changed files, and validation evidence in the same GitHub thread;
7. request review before treating the result as accepted.

## Default Loop

```text
Reasoning model analyzes or reviews
-> GitHub Issue / PR / review thread carries the patch
-> executor agent applies the patch locally
-> executor agent runs validation
-> executor agent commits and pushes
-> executor agent posts commit SHA and evidence in the same thread
-> reviewer verifies against the original packet and patch
-> accepted repository state is recorded
```

## Message Shape

Use explicit AI-to-AI headers in mixed GitHub threads:

```text
FROM: Reviewer
TO: Executor-Agent
TYPE: Reviewer Patch
```

The executor replies with:

```text
FROM: Executor-Agent
TO: Reviewer
TYPE: Patch Execution Report

Status:
Executor Identity:
Patch Applied Exactly: Yes / No
Conflict Found:
Files Changed:
Validation Performed:
Validation Not Performed:
Commit SHA:
Push Status:
Risks / Follow-Up:
Ready For Review: Yes / No
```

When the identities are known, use explicit names:

```text
FROM: ChatGPT
TO: DeepSeek
TYPE: Reviewer Patch
```

or:

```text
FROM: ChatGPT
TO: Codex
TYPE: Reviewer Patch
```

## Direct Reviewer Repository Edits

The reviewer may directly edit repository files only when:

- the owner explicitly requests direct correction;
- the executor agent is blocked by a repeated execution failure;
- the change is narrow, safe, and fully inspectable;
- the resulting commit SHA and validation limits are reported honestly.

Direct reviewer edits do not remove the need for validation and review.

## Applies To

- GitHub-backed software projects;
- reasoning-model <-> executor-agent collaboration loops;
- Codex, DeepSeek, Claude, automation agents, or human executors;
- debugging sessions where the reviewer identifies a concrete fix;
- issue-centered implementation work;
- PR review threads with actionable code corrections;
- multi-agent repository work requiring durable traceability.

## Triggers

Load this entry when:

- the active communication channel is a GitHub Issue, PR, or review thread;
- an executor agent is implementing a repository task from a handoff packet;
- the reviewer has a ready-to-apply code fix;
- an executor repeats the same implementation error;
- the user would otherwise need to manually relay code between AI sessions;
- execution needs a durable patch-to-commit audit trail.

## Do Not Load When

Do not use this pattern when:

- the task is only conceptual discussion or research;
- no repository execution is required;
- the patch is speculative and has not been reasoned through;
- the reviewer is trying to bypass required product decisions;
- a destructive or broad architectural change needs explicit owner approval;
- an issue comment is being used as a substitute for a real handoff packet.

## Boundaries

- GitHub comments are transport and durable follow-up surfaces, not substitutes for scoped execution packets.
- A commit SHA proves that repository changes exist; it does not prove behavioral correctness.
- Validation evidence must remain separate from execution claims.
- The executor agent must not silently redesign an explicit reviewer patch.
- The user should not be the normal relay between AI participants when the GitHub channel is available.
- The protocol must remain model-neutral and vendor-neutral.

## Evidence

Verified in project:

- Repository: `oleg3479881328-code/QuizLight`
- Active communication surface: `QuizLight` Issue `#1`
- Issue protocol comment: reviewer may publish ready-to-apply code snippets, file replacements, or targeted patches; executor must apply, validate, commit, push, and report in the same thread.
- Owner clarification: the executor is not necessarily Codex; it may be another agent such as DeepSeek.
- Owner confirmation: preserve this workflow as reusable central knowledge.

## Related Central Artifacts

- `blocks/communication-channel/BLOCK.md`
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`

## Reuse Rule

When GitHub is the selected AI-to-AI coordination channel, allow the reviewer to publish exact patches in the same durable thread and require the active executor agent — regardless of model or vendor — to return a validated patch-to-commit report there. Do not use the user as the normal relay.
