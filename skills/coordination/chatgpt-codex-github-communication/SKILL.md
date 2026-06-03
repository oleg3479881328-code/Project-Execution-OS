---
name: chatgpt-codex-github-communication
description: Coordinate reasoning-model work and executor-agent execution through GitHub using explicit handoff packets, compact coordination snapshots, bounded execution, and reviewable follow-up loops.
category: coordination
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
  - deepseek
inputs:
  - repository_context
  - coordination_goal
  - task_artifact_or_issue_or_pr
outputs:
  - coordination_mode
  - sync_preflight_status
  - handoff_requirements
  - github_surface_plan
  - coordination_snapshot_plan
  - execution_report_contract
  - review_loop_plan
  - sync_validation_report
safety_level: medium
source: internal_project_execution_os
review_status: approved
version: 0.2.0
---

# Purpose

Turn reasoning-model to executor-agent collaboration into a durable, reviewable GitHub workflow instead of an informal chat handoff.

# When to Use

Use this skill when:
- ChatGPT or another reasoning model must hand work to an executor agent;
- GitHub is the durable coordination layer;
- the task should flow through an issue, PR, review thread, or repository artifact;
- execution scope must stay bounded and reviewable;
- multiple AI sessions may touch the same project;
- a long coordination thread needs a compact resumable state snapshot.

# Source Of Truth

For GitHub-coordinated work:

- GitHub `main` is the only source of truth for committed project state;
- the local executor folder is an execution workspace, not the source of truth;
- Google Drive or other mirrors are inspection channels, not execution or sync authorities;
- `AI_COORDINATION_STATE.md` is the compact operational snapshot when it exists;
- the snapshot never replaces issue comments, commits, diffs, PR state, or validation evidence.

# Workflow

1. Identify the coordination surface.
2. If `AI_COORDINATION_STATE.md` exists, read it before opening the active issue, PR, or review thread.
3. Run sync preflight before any local execution.
4. Select the collaboration mode.
5. Require a deterministic handoff packet before execution.
6. Bind the executor agent to explicit scope and report contract.
7. Use GitHub comments, PR threads, or issues only as durable follow-up surfaces.
8. Update `AI_COORDINATION_STATE.md` only after meaningful state transitions.
9. Review execution against the original packet before accepting state.
10. Persist accepted knowledge back into repository memory.
11. Label each AI-to-AI GitHub message with explicit speaker and recipient identity.

# Compact Coordination Snapshot

For active GitHub-backed multi-step work, use root-level:

```text
AI_COORDINATION_STATE.md
```

Use it for:

- active channel;
- previous channels;
- current task;
- latest reviewed commit;
- accepted changes;
- open review items;
- one next step;
- required validation.

Do not copy full conversation history into the file.

Update it only after:

- channel migration;
- meaningful implementation commit;
- accepted review;
- new blocker;
- scope change;
- completed task.

Before resuming coordination, read:

```text
AI_COORDINATION_STATE.md
-> Active Channel
-> latest relevant comments
-> latest commit or PR state
-> Next Step
```

# Sync Preflight

Before local execution:

1. Run `git status`.
2. If local changes exist, report them in the coordination surface before pulling.
3. Do not commit local changes unless they are explicitly part of the current task.
4. Pull latest `main` before validation:
   - `git pull --ff-only origin main`
5. If local changes are stale, superseded, or junk, discard them explicitly before sync.

# Post-Fix Sync Rules

After any local fix:

1. Report exact changed files.
2. Run validation.
3. Commit only the minimal intended files.
4. Do not commit `.venv`, logs, `.env`, `desktop.ini`, cache files, or local junk.
5. Push to GitHub only after the fix is validated.
6. Post the commit SHA and validation report in the coordination surface.
7. Update `AI_COORDINATION_STATE.md` only when the fix changes the durable coordination state.

# Collaboration Modes

- `repository_artifact_first`
- `github_issue_to_executor`
- `pr_centered_collaboration`

# Constraints

Do not:
- leave the speaker identity implicit in mixed GitHub threads;
- send the executor vague prompts;
- treat GitHub comments as a substitute for a real handoff packet;
- allow silent scope expansion;
- accept execution without a structured execution report;
- confuse GitHub activity with reviewed project state;
- treat the local folder as the source of truth;
- validate against stale local state when `main` was not pulled first;
- commit local junk or mirror artifacts;
- treat public repositories as the default;
- use `AI_COORDINATION_STATE.md` as a full transcript;
- let a long thread become the only resumable project memory.

# Failure Modes

Possible failures:
- vague handoff and broad unintended execution;
- GitHub thread noise mistaken for approved work;
- missing traceability from issue or packet to final diff;
- review without comparison to the source packet;
- stale local workspace diverging from GitHub `main`;
- mirror or Google Drive state mistaken for execution authority;
- local junk files polluting git state;
- GitHub used as the only memory layer with no repository artifact updates;
- issue thread becomes too long for reliable connector reading;
- active channel migrates but participants continue posting into the archived thread;
- compact coordination snapshot exists but is stale or ignored.

# Validation Checklist

Before finalizing:
- `git status` was checked before execution;
- local changes were either reported, discarded, or intentionally kept;
- latest `main` was pulled before validation;
- the coordination mode is explicit;
- GitHub surface is identified;
- `AI_COORDINATION_STATE.md` was read first when present;
- active channel matches the snapshot when present;
- a handoff packet exists or is required;
- AI-to-AI GitHub comments identify `FROM`, `TO`, and message `TYPE`;
- executor scope is bounded;
- execution report requirements are explicit;
- review loop is defined;
- repository memory update path is clear;
- snapshot update path is clear for meaningful state transitions;
- commit SHA reporting path is clear when changes are pushed.

# References

See `references.md`.
