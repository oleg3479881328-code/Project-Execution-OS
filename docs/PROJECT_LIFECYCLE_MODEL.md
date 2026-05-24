# Project Lifecycle Model

## Purpose

This document defines the minimal operating model for how an idea becomes durable work inside Project Execution OS.

It is an internal system node. Entry files should route here when lifecycle or storage decisions are needed; they must not copy this logic into the front door.

## Core Model

A project can use several layers, but it does not have to use all of them.

| Layer | Role | When to use |
| --- | --- | --- |
| Chat | thinking, discussion, decisions, commands | always available; no durable-project assumption |
| Notion | readable memory, status, project catalogue, coordination | when an idea or project must be remembered, managed or revisited |
| GitHub | versioned execution, code, durable technical artifacts, Codex work | only when code, versioned files, technical documentation or executable work exists |
| Google Drive | optional files/assets storage | only when the project has heavy or non-versioned source materials such as images, scans, audio, video, PDFs or large exports |

## Hard Rules

1. Not every thought becomes a project.
2. Not every project needs GitHub.
3. Not every project needs Google Drive.
4. Notion is the readable management layer when durable project context is needed.
5. GitHub is the execution and version-control layer only for projects that require it.
6. Google Drive is an optional files/assets layer, not the project brain and not the source of operational decisions.
7. A project may start in Chat, gain a Notion layer when it must persist, and gain GitHub or Google Drive layers only when proved necessary.

## Minimal Routing

```text
Thought or request
→ discuss in Chat
→ preserve/manage in Notion only if it must persist
→ attach GitHub only if versioned execution is required
→ attach Google Drive only if heavy source files/assets are required
```

## Source-of-Truth Rule

There is no universal rule that GitHub is the source of truth for every project.

The source of truth depends on the project layer:

- project status, decisions and readable coordination: Notion when the project has a Notion layer;
- code, technical files, commits and Codex implementation: GitHub when the project has a GitHub layer;
- heavy source assets: Google Drive when the project has a Drive layer;
- current discussion: Chat only until a durable decision is written into the proper persistent layer.

A project entrypoint must state which layers exist and where each kind of truth lives.

## Execution Split

- ChatGPT performs research, comparison, classification, architecture reasoning and decision preparation whenever it has adequate access.
- Codex performs bounded technical execution after the decision is already clear: scripts, bulk updates, file changes, commits, pull requests, verification and logs.
- Do not spend Codex execution limits on open-ended thinking that ChatGPT can complete directly.

## Current Validation Cases

### Case 1 — GitHub Repository Inventory Cleanup

Validated:

- Chat was effective for deciding the model and archive criteria;
- Notion was effective as the readable inventory and status surface;
- Codex was effective for approved batch sync and batch archive execution;
- twelve obsolete repositories were archived only after dry-run and approval.

### Case 2 — Legacy Merge Analysis

Current phase:

- ChatGPT analyzes legacy repositories classified as `Merge`;
- only approved unique findings should later be handed to Codex for technical adoption;
- no bulk import of outdated architecture or duplicated rules.

## Related Nodes

- `START_HERE.md` — top-level router only
- `Start New Project.md` — new-project route only
- `docs/MODE_CLASSIFIER.md` — choose the lightest operating mode
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — per-project front door
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md` — preserve ideas that are not projects yet
- `docs/CODEX_HANDOFF_STANDARD.md` — bounded execution transfer to Codex
