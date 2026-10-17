# Project Lifecycle Model

## Purpose

This document defines the minimal operating model for how an idea becomes durable work inside Project Execution OS.

It is an internal system node. Entry files should route here when lifecycle or storage decisions are needed; they must not copy this logic into the front door.

## Core Model

A project can use several layers, but it does not have to use all of them.

| Layer | Role | When to use |
| --- | --- | --- |
| Chat | thinking, discussion, decisions, commands | always available; no durable-project assumption |
| Local Git | minimum version-control bootstrap for a real project folder | when a real project folder is intentionally created |
| GitHub | versioned execution, code, durable technical artifacts, Codex work | only when code, versioned files, technical documentation, or collaborative execution actually exists |
| Notion | optional workspace views, task coordination and linked management surfaces | when a project benefits from Notion workflows; do not create parallel truth |
| Google Drive | central durable storage for projects, catalogue, entrypoints, state, decisions, knowledge, documents and assets | default central home whenever work becomes a durable project or system-wide reusable record |

## Idea Discussion vs Project Initialization

These are different lifecycle actions:

- idea discussion may stay in chat or reference capture without becoming a durable project;
- starting project work applies the relevant standards and the `Existing Solution First` rule where relevant;
- intentionally creating a real standalone project folder bootstraps it with `git init`, `PROJECT.md`, and usually `AGENTS.md`;
- intentionally creating an internal subproject inside an existing repository bootstraps it with `PROJECT.md`, and `AGENTS.md` only if local instructions are useful.

Do not turn every idea into a project.

Do not automatically create files merely because a folder or Codex Desktop project was created or opened.

## Hard Rules

1. Not every thought becomes a project.
2. Not every project needs GitHub.
3. Not every project needs Notion.
4. Not every discussion requires a new Drive project folder; durable project and system knowledge belongs in the central Google Drive storage layer.
5. Every intentionally created real project folder gets local Git unless it already lives inside an existing Git repository.
6. Internal subprojects inside an existing Git repository must not receive nested `git init` unless there is a separate explicit decision.
7. `PROJECT.md` is the local front door for a project, but `START_HERE.md` remains the top-level system door.
8. Apply `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` before new architecture, implementation, workflow invention, or custom tooling.
9. Every durable artifact must follow `docs/FILE_ORGANIZATION_STANDARD.md`: choose the correct folder before creating the file, keep project files inside the project tree, and never scatter persistent files in Drive roots or random locations.

## Real Project Bootstrap

When the owner intentionally creates a real project, use `docs/PROJECT_BOOTSTRAP_STANDARD.md`.

That bootstrap creates only the minimum zero-state front door.

Standalone external project folders already have local Git from bootstrap.
Internal subprojects inherit the parent repository Git layer.

For durable projects, use the existing Google Drive project home and registry as the default storage/management layer, without creating duplicate folders. Attach additional layers only when justified:

- GitHub for code, versioned execution, technical documentation near the code and shared review;
- Notion for optional coordination or views linked to canonical Drive/GitHub records.

A project with a real local engineering folder still follows the appropriate local Git bootstrap. Creating only a Google Drive project folder does not itself require running `git init`.

## Minimal Routing

```text
Thought or request
→ discuss in Chat
→ apply Existing Solution First when real research or technical work begins
→ when a real project is intentionally created, bootstrap it minimally
→ when execution becomes meaningful, add PROJECT_STATE.md and logs/latest.md
→ register/persist durable project state, decisions and knowledge in the existing Google Drive project home
→ attach GitHub only if code, versioned execution or technical shared review is required
→ attach Notion only if a connected coordination/view layer adds real value
→ place every durable artifact into the correct project folder or subfolder before continuing
```

## Source-of-Truth Rule

Google Drive is the central durable storage and project-knowledge home by owner decision dated 2026-10-17. This includes project registry, entrypoints, operational status, decisions, documents, useful knowledge and assets.

Layer-specific sources of truth remain unambiguous:

- project records, status, decisions and knowledge: the verified canonical Google Drive project/system documents;
- code, commits, pull requests, tests and technical execution evidence: GitHub when that engineering layer exists;
- optional Notion coordination: links or views into canonical records, not competing project truth;
- local Git: local engineering history until committed or handed off;
- current discussion: Chat only until a durable decision is recorded.

During migration, already-canonical GitHub standards remain authoritative for their own text until promoted, linked and acceptance-checked in Drive. Never guess between Drive clones or declare a cutover solely because files were copied.

A project entrypoint, when one exists, must state which layers exist and where each kind of truth lives.

## Execution Split

- ChatGPT performs research, comparison, classification, architecture reasoning, and decision preparation whenever it has adequate access.
- Codex performs bounded technical execution after the decision is already clear: scripts, bulk updates, file changes, commits, pull requests, verification, and logs.
- Do not spend Codex execution limits on open-ended thinking that ChatGPT can complete directly.
- Do not spend Codex context on unnecessary project structure beyond the minimum required for the current lifecycle state.

## Related Nodes

- `START_HERE.md` — top-level router only
- `Start New Project.md` — new-project route only
- `docs/PROJECT_BOOTSTRAP_STANDARD.md` — minimum bootstrap for an intentionally created real project
- `docs/MODE_CLASSIFIER.md` — choose the lightest operating mode
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — per-project front door when used
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md` — preserve ideas that are not projects yet
- `docs/FILE_ORGANIZATION_STANDARD.md` — global canonical placement rule for all durable artifacts
- `docs/RESEARCH_STANDARD.md` — evidence-backed reuse-first research
- `docs/CODEX_HANDOFF_STANDARD.md` — bounded execution transfer to Codex
