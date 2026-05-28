# Project Bootstrap Standard

## Purpose

This standard defines the mandatory zero-state initialization of a newly created file-based project inside Project Execution OS.

A project must become a transferable, self-explaining work object immediately, even when its purpose has not yet been discussed.

This zero state must already inherit the central reuse-first rule from `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`.

## Core Invariant

An explicit project-creation event is sufficient to initialize a project.

When a user creates a new project folder or workspace through any supported interface, the folder must receive the minimal Project Execution OS bootstrap at the earliest technically enforceable moment and before substantive discussion, planning, research, architecture or implementation begins.

A newly initialized project may truthfully exist in this state:

`initialized — purpose not yet defined`

Unknown purpose is valid state and must not be replaced by guesses.

## Trigger Boundary

Bootstrap is required for an explicit new-project creation action, including creation of a local project folder, a new development workspace, or a new agent project workspace.

Bootstrap is not triggered by casual idea discussion, exploratory research, or saving a reference without starting a project.

Explicit creation and idea discussion are different lifecycle moments and must not be conflated.

## Earliest Enforceable Moment Rule

- When an interface exposes a project-created action or template mechanism, bootstrap occurs as part of creation.
- When an interface creates or selects a folder but exposes no project-created trigger, bootstrap occurs at the first controllable session start in that folder, before other project work.
- The system must not claim click-time initialization unless the project files were actually created at click time.

## Minimal Bootstrap Artifacts

For a newly created folder-based project, create only:

```text
<project-folder>/
├── AGENTS.md
└── PROJECT_ENTRYPOINT.md
```

Do not automatically create state files, rules files, logs, workflow folders, agent folders, libraries or infrastructure folders until real project work requires them.

## Artifact Roles

### `AGENTS.md`

This is the automatic agent-discovery shim for Codex-compatible work. It must be short and route the agent to `PROJECT_ENTRYPOINT.md` and the central Project Execution OS entrypoint. It must not duplicate the complete system or project history.

### `PROJECT_ENTRYPOINT.md`

This is the project front door for humans and AI participants. In zero state it records that the project exists while its purpose remains unconfirmed, identifies the central system entrypoint, blocks invented purpose or decisions, and states the next practical action.

## Required Zero-State Content

A bootstrap `PROJECT_ENTRYPOINT.md` must state:

- project name from the folder name or already confirmed name;
- status: `initialized — purpose not yet defined` when purpose is unknown;
- project type: not yet classified when unknown;
- that the project operates under Project Execution OS;
- that no purpose, architecture, implementation plan, storage-layer choice, tool choice or execution decision has been confirmed;
- that no substantive work should begin until intent is confirmed;
- the next practical step: ask what idea or project is being developed.
- that `Existing Solution First` remains mandatory once a real task exists.

A bootstrap `AGENTS.md` must state:

- read `PROJECT_ENTRYPOINT.md` before project work;
- follow the central Project Execution OS entrypoint and its selected route;
- do not infer missing project purpose, architecture or decisions.
- do not invent solutions before checking existing suitable ones;
- read `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` for the canonical rule.

## Required Bootstrap Sequence

1. Detect explicit creation of a new project folder or workspace.
2. Create `AGENTS.md` and `PROJECT_ENTRYPOINT.md` in that project root at the earliest technically enforceable moment.
3. Mark unconfirmed purpose explicitly as unknown.
4. Only after bootstrap, obtain or continue defining the project purpose.
5. After purpose is confirmed, update the project entrypoint and route into the minimal appropriate lifecycle, structure, research or execution standards.

## Transition Out Of Zero State

Zero state is not the same as a defined project.

After the project purpose is confirmed:

- update the project entrypoint with the actual project purpose, type, source-of-truth boundaries, focus and next step;
- determine required durable layers through `docs/PROJECT_LIFECYCLE_MODEL.md`;
- use `docs/PROJECT_STRUCTURE_STANDARD.md` only when a versioned or file-execution structure is justified;
- create additional artifacts only when they hold real state or constraints.

## Tool Adapters

Platform-specific adapters may implement this invariant but must not weaken it or claim capabilities that the platform does not expose.

For Codex desktop, app and IDE environments, use `docs/integrations/codex/CODEX_PROJECT_BOOTSTRAP_ADAPTER.md`.

## Related Nodes

- `START_HERE.md` — top-level router only
- `Start New Project.md` — new-project route
- `docs/PROJECT_LIFECYCLE_MODEL.md` — layer and persistence decisions
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — ongoing entrypoint contract
- `docs/PROJECT_STRUCTURE_STANDARD.md` — later file or versioned structure when justified
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` — mandatory reuse-first rule from zero state onward
