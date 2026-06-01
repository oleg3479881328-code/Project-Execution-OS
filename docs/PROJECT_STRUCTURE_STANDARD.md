# Project Structure Standard v2

## Purpose

This standard defines the durable file structure for a project **when that project has a GitHub or versioned-file execution layer**.

It is not a rule that every idea or every project must receive a repository.

Before applying this standard, use:

`docs/PROJECT_LIFECYCLE_MODEL.md`

For the exact contract of the first project-read artifact, use:

`docs/PROJECT_ENTRYPOINT_STANDARD.md`

## Applicability

Apply this standard when a project needs one or more of the following:

- code;
- versioned files;
- technical documentation maintained as files;
- Codex execution;
- commits, branches or pull requests;
- reproducible file-based technical work.

## Optional Entrypoint Initialization vs Execution Structure

Do not confuse minimum real-project bootstrap with later execution structure.

### Minimum Real-Project Bootstrap Structure

When the owner intentionally creates a real new project folder, the minimum bootstrap uses:

```text
AGENTS.md
PROJECT.md
```

This bootstrap action is defined by `docs/PROJECT_BOOTSTRAP_STANDARD.md`.

It is not triggered automatically when a folder or Codex Desktop project is merely created or opened without intentionally starting real project work.

Do not expand a new project with empty folders or ceremonial files during bootstrap.

### Later Execution Structure

Only after the project purpose and execution needs are known should the project move into compact mode or full GitHub-backed mode.

Do not apply it automatically to:

- raw ideas;
- short discussions;
- Notion-first personal or research projects that have no versioned execution need;
- projects that only need heavy assets in Google Drive.

## Canonical Project Naming Rule

A project must keep the same canonical project name across all active layers and storage locations.

This includes:

- local project folders;
- GitHub repositories when possible;
- Notion project pages;
- Google Drive folders;
- shared archives;
- removable storage;
- execution workspaces;
- transfer artifacts.

The goal is to eliminate naming drift and ambiguity between systems.

A project should not appear under different names in different layers unless there is a hard technical limitation.

Examples:

```text
Local folder:
website-design-system

GitHub repository:
website-design-system

Notion project:
Website Design System

Google Drive folder:
website-design-system
```

Minor formatting differences are acceptable:

- kebab-case vs readable title case;
- filesystem-safe variants;
- platform-specific restrictions.

But the semantic project identity must stay identical.

## Storage Decision

A project may have:

- a Notion layer for readable management and durable status;
- a GitHub layer for versioned technical execution;
- a Google Drive layer for heavy source files and assets.

When a GitHub layer is used, the project entrypoint must state what GitHub is authoritative for and what remains authoritative in Notion or Google Drive.

## GitHub Project Root

When a project requires its own GitHub execution layer, use a dedicated repository unless there is a concrete reason to place the work inside an existing repository.

When creating a new repository, set a short clear bilingual GitHub description:

- Russian first;
- English second.

An internal folder inside `Project Execution OS` may be used only when the work belongs to the OS itself or is an explicitly chosen compact internal workstream.

Recommended internal project id format:

`YYYYMMDD-short-kebab-name`

Example:

`projects/20260516-news-telegram-bot/`

## Required Files And Folders For Full GitHub-Backed Mode

A full-mode GitHub-backed project should contain:

- `PROJECT.md`
- `PROJECT_STATE.md`
- `PROJECT_RULES.md`
- `agents/` only when agent modules are actually required
- `project-library/` when project-local reusable knowledge exists
- `workflow-runs/` when structured workflow runs are used
- `logs/` when durable execution history is required

Do not create empty folders simply to satisfy ceremony. Create only artifacts that are useful to future continuation, review or verification.

## Compact GitHub-Backed Mode

Compact mode is preferred for small or low-risk technical projects.

It may use a smaller structure, for example:

```text
PROJECT.md
PROJECT_STATE.md
logs/
```

or another minimal structure that still preserves:

- source-of-truth boundaries;
- explicit current state;
- explicit next action;
- evidence-backed research when relevant;
- review before stable acceptance when relevant;
- durable log history when execution must be recoverable.

Compact mode must not hide important durable state in chat.

## PROJECT.md

This is the single front door for the GitHub-backed project.

It must include in compact form:

- project name and purpose;
- active layers: Notion / GitHub / Google Drive, if any;
- what each active layer is authoritative for;
- current state location;
- latest relevant execution artifact;
- current next action.

Use:

`docs/PROJECT_ENTRYPOINT_STANDARD.md`

## PROJECT_STATE.md

Current technical state snapshot for the GitHub/file execution layer.

A useful short frontmatter block may be:

```yaml
---
status: in-progress
project_mode: compact
current_step: execution
last_updated: 2026-05-24
next_action: Verify the approved change and record the result.
---
```

Include only what is needed to recover current file-based work:

- current phase or task;
- confirmed technical decisions;
- active constraints;
- latest result;
- next action.

## PROJECT_RULES.md

Create project-specific rules only when they materially constrain future execution.

Possible contents:

- scope boundaries;
- forbidden actions;
- quality or evidence requirements;
- tool restrictions;
- security constraints;
- state-separation rules.

## workflow-runs/ And logs/

Use workflow runs and logs when a technical action must be durable, reviewable or recoverable.

A log may record:

- approved action;
- executed change;
- verification result;
- failure and fix;
- next action.

Do not generate large logging structures for trivial safe actions.

## Source-Of-Truth Rule

There is no single source-of-truth medium for every project.

For a project with multiple layers:

1. Notion may govern readable status, decisions and coordination.
2. GitHub governs committed code, file-based technical artifacts and implementation history.
3. Google Drive governs heavy source assets when used.
4. Chat is discussion until a durable decision is recorded in its proper persistent layer.

The project entrypoint must remove ambiguity by stating these boundaries explicitly.

## No Hidden Durable State

Important durable state must not exist only in chat.

Write it into the correct active layer of the project: Notion, GitHub or Google Drive linkage, depending on what kind of truth it is.

## CONTEXT_PACK.md

`CONTEXT_PACK.md` is optional.

Use it only when handoff between agents or sessions is frequent enough that a short re-entry brief reduces real work.

It is a briefing cache, not the source of truth.
