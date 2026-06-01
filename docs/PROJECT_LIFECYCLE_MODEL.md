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
| Notion | readable memory, status, project catalogue, coordination | when an idea or project must be remembered, managed, or revisited |
| Google Drive | optional files/assets storage | only when the project has heavy or non-versioned source materials such as images, scans, audio, video, PDFs, or large exports |

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
4. Not every project needs Google Drive.
5. Every intentionally created real project folder gets local Git unless it already lives inside an existing Git repository.
6. Internal subprojects inside an existing Git repository must not receive nested `git init` unless there is a separate explicit decision.
7. `PROJECT.md` is the local front door for a project, but `START_HERE.md` remains the top-level system door.
8. Apply `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` before new architecture, implementation, workflow invention, or custom tooling.

## Real Project Bootstrap

When the owner intentionally creates a real project, use `docs/PROJECT_BOOTSTRAP_STANDARD.md`.

That bootstrap creates only the minimum zero-state front door.

Only after purpose and storage needs are confirmed should the project gain extra durable layers such as:

- local Git for version-control continuity;
- GitHub for versioned execution and shared review;
- Notion for readable management;
- Google Drive for heavy assets.

## Minimal Routing

```text
Thought or request
→ discuss in Chat
→ apply Existing Solution First when real research or technical work begins
→ when a real project is intentionally created, bootstrap it minimally
→ when execution becomes meaningful, add PROJECT_STATE.md and logs/latest.md
→ attach GitHub only if versioned execution or shared review is required
→ attach Notion only if readable project management is needed
→ attach Google Drive only if heavy source files or assets are needed
```

## Source-of-Truth Rule

There is no universal rule that GitHub is the source of truth for every project.

The source of truth depends on the project layer:

- project status, decisions, and readable coordination: Notion when the project has a Notion layer;
- code, technical files, commits, pull requests, and Codex implementation: GitHub when the project has a GitHub layer;
- local execution history before GitHub attachment: local Git and project files when the project has only a local folder;
- heavy source assets: Google Drive when the project has a Drive layer;
- current discussion: Chat only until a durable decision is written into the proper persistent layer.

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
- `docs/RESEARCH_STANDARD.md` — evidence-backed reuse-first research
- `docs/CODEX_HANDOFF_STANDARD.md` — bounded execution transfer to Codex
