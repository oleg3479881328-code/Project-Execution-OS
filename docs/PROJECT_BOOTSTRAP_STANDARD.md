# Project Bootstrap Standard

## Purpose

This standard defines the minimum safe bootstrap for a real project inside Project Execution OS.

Its job is to create only the smallest durable front door needed to begin real project work honestly.

## Constitutional Entry Order

Bootstrap must preserve this order:

```text
START_HERE.md
→ docs/ROUTER.md
→ PROJECT.md for the specific project
→ existing project index if useful
→ minimum additional files required by the task
```

`PROJECT.md` is the local front door for one project.

It does not replace `START_HERE.md` as the top-level door into the overall system.

## Bootstrap Boundary

No folder is automatically mutated merely because it is opened, selected in an IDE, or used in Codex Desktop.

Bootstrap is allowed only when the owner intentionally creates a real project.

Bootstrap is not triggered by:

- casual idea discussion;
- exploratory research;
- saving a reference without starting a project;
- opening an existing folder or workspace;
- opening an existing project;
- creating a temporary working folder.

## External Project vs Internal Subproject

### External independent project folder

When the owner intentionally creates a standalone real project folder, bootstrap it with:

```text
git init
AGENTS.md
PROJECT.md
```

### Internal subproject inside an existing Git repository

When the owner intentionally creates a project-like subfolder inside an already versioned repository:

- do not run nested `git init`;
- use the parent repository's Git history;
- create `PROJECT.md`;
- create `AGENTS.md` only when local subproject instructions are actually needed.

Inside `projects/<project-id>/` in this central repository, do not create nested Git repositories unless there is a separate explicit decision to do so.

## Zero-State Bootstrap

The valid zero-state bootstrap set is:

```text
PROJECT.md
AGENTS.md    # optional for internal subprojects; required for standalone external folders
```

Do not automatically create `PROJECT_STATE.md`, `PROJECT_CHANGE_INDEX.md`, `CONTEXT_PACK.md`, `HANDOFF.md`, `workflow-runs/`, `docs/`, `logs/`, `research/`, `architecture/`, `tasks/`, or other structure at zero state.

Unknown purpose is valid state and must not be replaced by guesses.

## First Meaningful Execution Step

After the first meaningful execution step, the active project should gain:

```text
PROJECT_STATE.md
logs/latest.md
```

Use `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` for the continuity rules that begin after zero-state bootstrap.

## File Placement Rule

Every file created during bootstrap or later execution must follow `docs/FILE_ORGANIZATION_STANDARD.md`.

Determine the correct project folder or subfolder before creating a durable artifact. Do not scatter persistent files into Drive roots, computer roots, temporary locations, or unrelated folders.

## Template Rule

Project bootstrap templates are stored as passive templates under:

- `workflow-templates/project-bootstrap/AGENTS_TEMPLATE.md`
- `workflow-templates/project-bootstrap/PROJECT_TEMPLATE.md`

Bootstrap copies them into the target project under the working names:

- `AGENTS.md`
- `PROJECT.md`

Do not keep an active template `AGENTS.md` inside the template directory itself.

## Required Zero-State Content

`PROJECT.md` at zero state must state:

- project name from the folder name or already confirmed name;
- status: `initialized — purpose not yet defined` when purpose is unknown;
- project type: not yet classified when unknown;
- that the project operates under Project Execution OS;
- that no purpose, architecture, implementation plan, storage-layer choice, tool choice, or execution decision has been confirmed;
- that no substantive work should begin until intent is confirmed;
- the next practical step: obtain the project purpose;
- that `Existing Solution First` applies once a real technical or project task exists.

If created, `AGENTS.md` must reinforce:

- the constitutional entry order;
- minimum-context reading;
- index check before mass scanning;
- continuity and transfer-readiness standards;
- canonical file placement under `docs/FILE_ORGANIZATION_STANDARD.md`;
- official communication-channel routing;
- legacy migration from `PROJECT_ENTRYPOINT.md` to `PROJECT.md` when needed.

For projects outside this repository, central-system references must use canonical absolute URLs rather than relative paths.

## Required Bootstrap Sequence

1. Confirm that the owner is intentionally creating a real project.
2. Confirm whether the target is:
   - a standalone external project folder; or
   - an internal subproject inside an existing Git repository.
3. For a standalone folder, run `git init`.
4. Copy `PROJECT_TEMPLATE.md` into the project as `PROJECT.md`.
5. Copy `AGENTS_TEMPLATE.md` into the project as `AGENTS.md` when the case requires local agent instructions.
6. Mark unconfirmed purpose explicitly as unknown when it is still unknown.
7. Obtain or continue defining the project purpose.
8. After purpose is confirmed, route into the minimal appropriate lifecycle, structure, research, or execution standards.

## Related Nodes

- `START_HERE.md` — top-level router only
- `Start New Project.md` — new-project route
- `docs/PROJECT_LIFECYCLE_MODEL.md` — layer and persistence decisions
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — ongoing entrypoint contract
- `docs/PROJECT_STRUCTURE_STANDARD.md` — file or versioned structure when justified
- `docs/FILE_ORGANIZATION_STANDARD.md` — global canonical placement rule for every durable artifact
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` — continuity after zero-state bootstrap
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` — mandatory reuse-first rule for relevant project work
