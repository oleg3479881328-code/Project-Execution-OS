# Project Bootstrap Standard

## Purpose

This standard defines an optional minimal project-folder initialization action inside Project Execution OS.

Use it only when the user explicitly requests a transferable project entrypoint or asks to initialize a project folder under this system.

It is not an automatic Codex Desktop, folder-creation, workspace-opening, or session-start behavior.

## Core Rule

No folder is automatically mutated merely because it is created, opened, selected in an IDE, or used in Codex Desktop.

Minimal bootstrap may be performed only by explicit user instruction.

### Local Git Initialization Exception

Whenever the owner intentionally creates a real project folder, initialize that folder immediately as a local Git repository with:

```bash
git init
```

This narrow exception is automatic for real project folders. It does not create `AGENTS.md`, `PROJECT_ENTRYPOINT.md`, state files, logs, or any other project artifacts. It does not create a GitHub repository, attach a remote, or promote an exploratory idea into a project.

When requested before the project purpose is known, the folder may truthfully record this state:

`initialized — purpose not yet defined`

Unknown purpose is valid state and must not be replaced by guesses.

## Trigger Boundary

Bootstrap is permitted when the user explicitly asks to:

- initialize a new project folder under Project Execution OS;
- create a transferable front door for a project folder;
- create minimal project entrypoint files before the purpose is defined.

Bootstrap is not triggered by:

- creating or opening a folder, except for the local `git init` rule when the folder is intentionally created as a real project folder;
- creating or opening a Codex Desktop project;
- starting a Codex session;
- casual idea discussion;
- exploratory research;
- saving a reference without starting a project.

## Minimal On-Demand Artifacts

When the user explicitly requests minimal folder bootstrap, create only:

```text
<project-folder>/
├── AGENTS.md
└── PROJECT_ENTRYPOINT.md
```

Do not automatically create state files, rules files, logs, workflow folders, agent folders, libraries or infrastructure folders until real project work requires them.

## Artifact Roles

### `AGENTS.md`

When explicitly created for a project folder, this is a short Codex-compatible entry adapter. It should route the agent to `PROJECT_ENTRYPOINT.md` and the central Project Execution OS entrypoint, without duplicating the complete system or project history.

### `PROJECT_ENTRYPOINT.md`

This is the project front door for humans and AI participants. In initialization-only state it records that the folder has been initialized on request while its purpose remains unconfirmed, identifies the central system entrypoint, blocks invented purpose or decisions, and states the next practical action.

## Required Initialization-Only Content

An initialization-only `PROJECT_ENTRYPOINT.md` must state:

- project name from the folder name or already confirmed name;
- status: `initialized — purpose not yet defined` when purpose is unknown;
- project type: not yet classified when unknown;
- that the project operates under Project Execution OS;
- that no purpose, architecture, implementation plan, storage-layer choice, tool choice or execution decision has been confirmed;
- that no substantive work should begin until intent is confirmed;
- the next practical step: obtain the project purpose;
- that `Existing Solution First` applies once a real technical or project task exists.

An explicitly created `AGENTS.md` should state:

- read `PROJECT_ENTRYPOINT.md` before project work;
- follow the central Project Execution OS entrypoint and its selected route;
- do not infer missing project purpose, architecture or decisions;
- do not invent solutions before checking existing suitable ones;
- follow `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` for the canonical rule.

For project folders outside this repository, references to central Project Execution OS documents must use canonical absolute URLs, not relative local paths.

## Required On-Demand Sequence

1. Receive an explicit request to initialize the project folder.
2. Confirm the intended target folder from the user's request or the current project context.
3. Create `AGENTS.md` and `PROJECT_ENTRYPOINT.md` only in that requested project root.
4. Mark unconfirmed purpose explicitly as unknown.
5. Obtain or continue defining the project purpose.
6. After purpose is confirmed, update the project entrypoint and route into the minimal appropriate lifecycle, structure, research or execution standards.

## Transition Out Of Initialization-Only State

After the project purpose is confirmed:

- update the project entrypoint with the actual project purpose, type, source-of-truth boundaries, focus and next step;
- determine required durable layers through `docs/PROJECT_LIFECYCLE_MODEL.md`;
- use `docs/PROJECT_STRUCTURE_STANDARD.md` only when a versioned or file-execution structure is justified;
- create additional artifacts only when they hold real state or constraints.

## Codex Desktop Rule

Automatic Codex Desktop bootstrap is disabled by policy.

Do not install or rely on global Codex hooks or global instructions that automatically create project files. When the owner wants a folder initialized, perform the minimal bootstrap only on explicit request.

The local `git init` rule is separate from project-file bootstrap. It may be executed automatically for an intentionally created real project folder because it creates version-control metadata only.

## Related Nodes

- `START_HERE.md` — top-level router only
- `Start New Project.md` — new-project route
- `docs/PROJECT_LIFECYCLE_MODEL.md` — layer and persistence decisions
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — ongoing entrypoint contract
- `docs/PROJECT_STRUCTURE_STANDARD.md` — file or versioned structure when justified
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` — mandatory reuse-first rule for relevant project work
