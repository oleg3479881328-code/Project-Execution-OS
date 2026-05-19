---
name: chatgpt-codex-github-communication
description: Coordinate reasoning-model work and Codex execution through GitHub using explicit handoff packets, bounded execution, and reviewable follow-up loops.
category: coordination
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - repository_context
  - coordination_goal
  - task_artifact_or_issue_or_pr
outputs:
  - coordination_mode
  - sync_preflight_status
  - handoff_requirements
  - github_surface_plan
  - execution_report_contract
  - review_loop_plan
  - sync_validation_report
safety_level: medium
source: internal_project_execution_os
review_status: approved
version: 0.1.0
---

# Purpose

Turn ChatGPT to Codex collaboration into a durable, reviewable GitHub workflow instead of an informal chat handoff.

# When to Use

Use this skill when:
- ChatGPT or another reasoning model must hand work to Codex;
- GitHub is the durable coordination layer;
- the task should flow through an issue, PR, review thread, or repository artifact;
- execution scope must stay bounded and reviewable;
- multiple AI sessions may touch the same project.

# Source Of Truth

For GitHub-coordinated work:

- GitHub `main` is the only source of truth for committed project state;
- the local Codex folder is an execution workspace, not the source of truth;
- Google Drive or other mirrors are inspection channels, not execution or sync authorities.

# Workflow

1. Identify the coordination surface.
2. Run sync preflight before any local execution.
3. Select the collaboration mode.
4. Require a deterministic handoff packet before execution.
5. Bind Codex to explicit scope and report contract.
6. Use GitHub comments, PR threads, or issues only as durable follow-up surfaces.
7. Review execution against the original packet before accepting state.
8. Persist accepted knowledge back into repository memory.

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

# Collaboration Modes

- `repository_artifact_first`
- `github_issue_to_codex`
- `pr_centered_collaboration`

# Constraints

Do not:
- send Codex vague prompts;
- treat GitHub comments as a substitute for a real handoff packet;
- allow silent scope expansion;
- accept execution without a structured execution report;
- confuse GitHub activity with reviewed project state;
- treat the local folder as the source of truth;
- validate against stale local state when `main` was not pulled first;
- commit local junk or mirror artifacts;
- treat public repositories as the default.

# Failure Modes

Possible failures:
- vague handoff and broad unintended execution;
- GitHub thread noise mistaken for approved work;
- missing traceability from issue or packet to final diff;
- review without comparison to the source packet;
- stale local workspace diverging from GitHub `main`;
- mirror or Google Drive state mistaken for execution authority;
- local junk files polluting git state;
- GitHub used as the only memory layer with no repository artifact updates.

# Validation Checklist

Before finalizing:
- `git status` was checked before execution;
- local changes were either reported, discarded, or intentionally kept;
- latest `main` was pulled before validation;
- the coordination mode is explicit;
- GitHub surface is identified;
- a handoff packet exists or is required;
- Codex scope is bounded;
- execution report requirements are explicit;
- review loop is defined;
- repository memory update path is clear;
- commit SHA reporting path is clear when changes are pushed.

# References

See `references.md`.
