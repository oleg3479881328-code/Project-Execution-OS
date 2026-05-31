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

## Idea Discussion vs Project Initialization

These are different lifecycle actions:

- idea discussion may stay in chat or reference capture without becoming a durable project;
- starting project work applies the relevant standards and the `Existing Solution First` rule where relevant;
- initializing a project folder with `AGENTS.md` and `PROJECT_ENTRYPOINT.md` happens only when the owner explicitly requests that durable folder entrypoint.

Do not turn every idea into a project.

Do not automatically create files merely because a folder or Codex Desktop project was created or opened.

Whenever the owner intentionally creates a real project folder, initialize it immediately as a local Git repository with `git init`. Local Git metadata is the narrow automatic exception; it does not create project files, a GitHub repository, or a remote connection.

## Hard Rules

1. Not every thought becomes a project.
2. Not every project needs GitHub.
3. Not every project needs Google Drive.
4. Not every new folder needs project-entrypoint files.
5. Notion is the readable management layer when durable project context is needed.
6. GitHub is the execution and version-control layer only for projects that require it.
7. Google Drive is an optional files/assets layer, not the project brain and not the source of operational decisions.
8. A project may start in Chat, gain a Notion layer when it must persist, and gain GitHub or Google Drive layers only when proved necessary.
9. Do not design an ideal system before obtaining the smallest working result when a usable existing solution can be adapted first.
10. Apply `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` before new architecture, implementation, workflow invention, or custom tooling.
11. Every intentionally created real project folder starts as a local Git repository through `git init`, even when no GitHub layer is attached.

## Optional Folder Entrypoint Initialization

When the owner explicitly requests a transferable project folder entrypoint, use `docs/PROJECT_BOOTSTRAP_STANDARD.md`.

That on-demand action creates only minimal front-door artifacts and may honestly record unknown purpose.

Only after purpose and storage needs are confirmed should the project gain extra durable layers such as:

- Notion for readable management;
- GitHub for versioned execution;
- Google Drive for heavy assets.

GitHub is not mandatory for every project, and no project receives extra layers simply because a folder exists.

Local Git is separate from the optional GitHub layer. A real project folder receives local version-control metadata through `git init`; a GitHub repository is attached only when justified.

## Minimal Routing

```text
Thought or request
→ discuss in Chat
→ apply Existing Solution First when real research / technical work begins
→ when a real project folder is intentionally created, run `git init`
→ initialize folder entrypoint only by explicit request
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

A project entrypoint, when one exists, must state which layers exist and where each kind of truth lives.

## Execution Split

- ChatGPT performs research, comparison, classification, architecture reasoning and decision preparation whenever it has adequate access.
- Codex performs bounded technical execution after the decision is already clear: scripts, bulk updates, file changes, commits, pull requests, verification and logs.
- Do not spend Codex execution limits on open-ended thinking that ChatGPT can complete directly.
- Do not spend Codex context on automatic project-file bootstrap behavior when explicit instruction is enough.
- Local `git init` for an intentionally created real project folder is the only narrow automatic bootstrap exception.

## Reference-Led MVP Route

Purpose: reach a working MVP faster by adapting proven solutions before inventing architecture from scratch.

Use this route when the proposed product, workflow, interface or automation is likely to have close existing analogues, reusable open-source foundations, proven templates or transferable patterns.

### Default Use Context

The default initial mode is personal, non-commercial experimentation and local MVP use by Oleg.

In this mode, do not slow down research, copying for local testing, adaptation, reverse engineering or prototype assembly merely because a future commercial or public-distribution question may exist.

A dedicated licensing, attribution, distribution and branding review becomes required only before one of these transitions:

- public publication or public release;
- sale, monetization or commercial deployment;
- redistribution to other users;
- transfer to a client or third party;
- incorporation of copied materials into a publicly represented original product.

Immediate hard limits still apply even in personal mode: do not use stolen secrets or credentials, bypass unauthorized access, distribute unlawfully obtained materials, or publicly misrepresent another product as original work.

### Operating Sequence

1. Define the smallest working result that would prove the idea useful.
2. Search for existing products, open-source projects, templates, libraries or workflows that already solve a substantial part of that result.
3. Select a viable donor when it covers roughly 60–80% of the needed MVP and is technically usable for the current personal testing purpose.
4. Stop searching once an adequate donor exists; do not turn donor search into a new perfection loop.
5. Adapt only what is required to produce the working MVP.
6. Test the working result in real use.
7. Only after the MVP works, extract reusable rules, architecture, standards or library entries justified by evidence.
8. Perform deeper licensing and release review only when the work is about to cross from personal experimentation into publication, redistribution or commercialization.

### Adoption Rules

- Prefer adaptation of a working foundation over greenfield construction when it materially shortens time to a usable result.
- Reuse product flows, interaction patterns, data models, technical patterns and code/components appropriate for personal MVP testing when they fit the target result.
- Do not pre-emptively block local experimentation because public-release obligations may arise later; record any obvious future release concern and keep building the personal MVP.
- Before public distribution, commercialization or delivery to another person, verify licensing, attribution obligations, asset ownership, branding restrictions, secret exposure and deployment constraints.
- Do not use secrets, unauthorized access, or copied materials in a way that creates an immediate legal or security problem even during personal testing.
- Do not build a full reusable platform before the first adapted product has proved which parts actually deserve standardization.

### Stop Conditions

Do not continue donor research when:

- a usable solution already covers most of the MVP;
- additional comparison delays implementation without changing the core choice;
- the candidate is technically adequate for personal local testing and the remaining work is bounded.

Build minimally from scratch only when no suitable reusable foundation exists or when adaptation would introduce greater practical risk than implementation.

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
- `docs/PROJECT_BOOTSTRAP_STANDARD.md` — optional folder-entrypoint initialization only on explicit request
- `docs/MODE_CLASSIFIER.md` — choose the lightest operating mode
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — per-project front door when used
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md` — preserve ideas that are not projects yet
- `docs/RESEARCH_STANDARD.md` — evidence-backed reuse-first research
- `docs/CODEX_HANDOFF_STANDARD.md` — bounded execution transfer to Codex
