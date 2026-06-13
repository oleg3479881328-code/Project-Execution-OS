# Project Structure Standard v2

## Purpose

This standard defines durable file structure for a project when a file-based execution layer is actually needed.

It does not mean every idea or every project must become a GitHub repository.

Before applying this standard, use:

`docs/PROJECT_LIFECYCLE_MODEL.md`

For the exact contract of the first project-read artifact, use:

`docs/PROJECT_ENTRYPOINT_STANDARD.md`

For every file-placement decision, also follow:

`docs/FILE_ORGANIZATION_STANDARD.md`

## Constitutional Entry Order

For file-based projects, the entry order stays:

```text
START_HERE.md
→ docs/ROUTER.md
→ PROJECT.md
→ existing project index if useful
→ minimum additional files needed for the task
```

## Zero-State Bootstrap

Zero-state bootstrap is intentionally small.

### Standalone external project folder

```text
.git/
PROJECT.md
AGENTS.md
```

### Internal subproject inside an existing Git repository

```text
PROJECT.md
AGENTS.md    # optional when local subproject instructions are useful
```

Do not create `PROJECT_STATE.md`, `logs/latest.md`, `workflow-runs/`, or other extra structure at zero state unless the project has already moved into meaningful execution.

## First Meaningful Execution Step

After the first meaningful execution step, the active minimal set becomes:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

This is the minimum active continuity set.

Use `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` for the maintenance rule after that point.

## Compact Active Mode

Compact mode is preferred for small or low-risk technical projects.

It may remain as small as:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

Additional useful artifacts may be added only when justified, for example:

- `PROJECT_RULES.md`
- `PROJECT_CHANGE_INDEX.md`
- `CONTEXT_PACK.md`
- `workflow-runs/`
- `project-library/`

Do not require these ritualistically for every compact project.

## Fuller File-Execution Mode

Larger projects may add more structure when it creates real value for continuation, review, or validation, for example:

- `PROJECT_RULES.md`
- `agents/`
- `project-library/`
- `workflow-runs/`
- `logs/history/`

Create only the artifacts that materially improve continuity, evidence, or execution safety.

## Internal Subprojects

An internal subproject stored inside an existing repository must use the parent repository's Git layer by default.

Do not run nested `git init` unless a separate explicit decision authorizes it.

Inside `projects/<project-id>/` in this repository, local structure should stay lightweight unless the subproject proves it needs more.

## Source-Of-Truth Rule

There is no single universal source-of-truth medium for every project.

For a project with multiple layers:

1. `PROJECT.md` is the local project front door.
2. `PROJECT_STATE.md` and `logs/latest.md` preserve current active file-based execution state.
3. GitHub governs committed code and review history only when a GitHub layer exists.
4. Notion may govern readable status, decisions, and coordination when present.
5. Google Drive may govern heavy source assets when present.

The project entrypoint must remove ambiguity by stating these boundaries explicitly.

## No Hidden Durable State

Important durable state must not exist only in chat.

Write it into the correct active layer of the project: project files, GitHub, Notion, or Google Drive linkage, depending on what kind of truth it is.

## No Scattered Durable Files

Persistent files must not be left in Drive roots, computer roots, temporary folders, random folders, or unrelated project trees.

Choose the correct destination before creation. Keep temporary generation, editable sources, exports, and backups separated according to `docs/FILE_ORGANIZATION_STANDARD.md`.
