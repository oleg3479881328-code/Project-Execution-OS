# Project Bootstrap Standard

## Purpose

This standard defines the minimal project-folder initialization action inside Project Execution OS.

Use it when the owner intentionally starts a real new project folder under this system.

It is not an automatic Codex Desktop, folder-opening, workspace-opening, or session-start behavior.

## Core Rule

No folder is automatically mutated merely because it is created, opened, selected in an IDE, or used in Codex Desktop.

Real project bootstrap is automatic only when the owner intentionally creates a real new project folder.

Whenever that boundary is met, initialize the folder immediately with:

```bash
git init
```

and create:

```text
AGENTS.md
PROJECT.md
```

This narrow automatic bootstrap applies only to intentionally created real project folders. It does not create a GitHub repository, attach a remote, or promote an exploratory idea into a project. It must not create additional project artifacts beyond this minimum set.

When requested before the project purpose is known, the folder may truthfully record this state:

`initialized — purpose not yet defined`

Unknown purpose is valid state and must not be replaced by guesses.

## Trigger Boundary

Bootstrap is permitted when the owner intentionally starts a real new project folder, including cases where the purpose is still unknown.

Bootstrap is not triggered by:

- creating or opening a folder without intentionally starting a real project;
- creating or opening a Codex Desktop project;
- starting a Codex session;
- casual idea discussion;
- exploratory research;
- saving a reference without starting a project.

## Minimal Bootstrap Artifacts

When a real new project folder is intentionally created, create only:

```text
<project-folder>/
├── .git/
├── AGENTS.md
└── PROJECT.md
```

Do not automatically create `README.md`, `INDEX.md`, `PROJECT_STATE.md`, `PROJECT_CHANGE_INDEX.md`, `CONTEXT_PACK.md`, `HANDOFF.md`, `docs/`, `logs/`, `research/`, `architecture/`, `tasks/`, agent folders, libraries, or infrastructure folders until real project work requires them.

## Artifact Roles

### `AGENTS.md`

This is a short agent-compatible entry adapter. It should route the agent to `PROJECT.md` and the central Project Execution OS entrypoint, while keeping only the critical local guardrails that are often missed in the central system alone.

### `PROJECT.md`

This is the project front door for humans and AI participants. In initialization-only state it records that the folder has been initialized while its purpose remains unconfirmed, identifies the central system entrypoint, blocks invented purpose or decisions, and states the next practical action.

## Required Initialization-Only Content

An initialization-only `PROJECT.md` must state:

- project name from the folder name or already confirmed name;
- status: `initialized — purpose not yet defined` when purpose is unknown;
- project type: not yet classified when unknown;
- that the project operates under Project Execution OS;
- that no purpose, architecture, implementation plan, storage-layer choice, tool choice or execution decision has been confirmed;
- that no substantive work should begin until intent is confirmed;
- the next practical step: obtain the project purpose;
- that `Existing Solution First` applies once a real technical or project task exists.

An automatically created `AGENTS.md` should state:

- read `PROJECT.md` before project work;
- follow the central Project Execution OS entrypoint and its selected route;
- use only the minimum necessary route and project context;
- do not infer missing project purpose, architecture or decisions;
- do not invent solutions before checking existing suitable ones;
- preserve stable starts of accumulating files where practical so repeated model context remains reusable;
- use `blocks/communication-channel/BLOCK.md` as the official inter-agent communication route;
- follow `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` for the canonical rule.

If `PROJECT.md` does not exist yet but legacy `PROJECT_ENTRYPOINT.md` is present, read it as the temporary local entrypoint and migrate it to `PROJECT.md` at the nearest safe opportunity without keeping both files active.

For project folders outside this repository, references to central Project Execution OS documents must use canonical absolute URLs, not relative local paths.

## Required Bootstrap Sequence

1. Confirm that the owner is intentionally creating a real new project folder.
2. Confirm the intended target folder from the user's request or the current project context.
3. Run `git init` in that project root.
4. Create `AGENTS.md` and `PROJECT.md` in that same root.
5. Mark unconfirmed purpose explicitly as unknown when it is still unknown.
6. Obtain or continue defining the project purpose.
7. After purpose is confirmed, update the project entrypoint and route into the minimal appropriate lifecycle, structure, research or execution standards.

## Transition Out Of Initialization-Only State

After the project purpose is confirmed:

- update the project entrypoint with the actual project purpose, type, source-of-truth boundaries, focus and next step;
- determine required durable layers through `docs/PROJECT_LIFECYCLE_MODEL.md`;
- use `docs/PROJECT_STRUCTURE_STANDARD.md` only when a versioned or file-execution structure is justified;
- create additional artifacts only when they hold real state or constraints.

## Codex Desktop Rule

Automatic Codex Desktop bootstrap for every opened folder is disabled by policy.

Do not install or rely on global Codex hooks or global instructions that create project files for every opened folder, workspace, or session. Bootstrap is allowed only for an intentionally created real new project folder.

When that bootstrap boundary is met, `git init`, `AGENTS.md`, and `PROJECT.md` are the complete automatic minimum. No additional files should be created automatically.

## Related Nodes

- `START_HERE.md` — top-level router only
- `Start New Project.md` — new-project route
- `docs/PROJECT_LIFECYCLE_MODEL.md` — layer and persistence decisions
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — ongoing entrypoint contract
- `docs/PROJECT_STRUCTURE_STANDARD.md` — file or versioned structure when justified
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` — mandatory reuse-first rule for relevant project work
