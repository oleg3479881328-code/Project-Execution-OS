# Graphify Standard

## Purpose

This standard defines how Graphify may be used as a graph-memory and repository-cognition layer for `Project-Execution-OS` and for projects started through it.

Graphify is an optional navigation aid for broad repositories or document corpora. It is not a required project bootstrap step and does not replace current source files or project entrypoints.

## Current Status

Graphify is not yet fully installed into this repository as an active local graph layer.

At the time of this record:

- there is no `graphify-out/` folder in this repository;
- there is no local Graphify output committed here yet;
- there are no local repo-specific Graphify instructions committed yet.

So the answer to "is graph memory already wired here?" is:

`not yet fully`

## Role In The Central Brain

Graphify may become:

- a graph-memory layer for broad repository understanding;
- a repository-cognition aid for large repos or document corpora;
- a cross-file relationship map for future AI sessions;
- a durable navigation cache that reduces repeated re-reading when its maintenance cost is justified.

It must not become a mandatory layer for every project or every session.

## Rules

### 1. Explicit Use Rule

Do not initialize Graphify automatically when a project, folder, workspace or Codex Desktop session is created or opened.

Use Graphify only when the owner explicitly requests it or when an approved project task specifically requires broad repository navigation and the use is justified by context cost.

Before building Graphify for a project:

1. check whether the repository or document corpus is broad enough to justify it;
2. skip Graphify when direct reading of a small known file set is cheaper and clearer;
3. if Graphify is justified and `graphify-out/GRAPH_REPORT.md` is missing, build it only as part of the explicit task;
4. read `graphify-out/GRAPH_REPORT.md` before broad raw-file exploration when a current report exists;
5. refresh Graphify after structural changes when feasible and needed for later use.

### 2. Broad Context Rule

Use Graphify when:

- the repository is broad or unknown;
- architecture or cross-file relationships matter;
- the project will likely receive repeated follow-up questions;
- direct file reading would create unnecessary context cost;
- the graph can be kept current enough to be trustworthy as a navigation aid.

Do not force Graphify for:

- new ideas without code or documents;
- empty or early-stage project folders;
- narrow one-file or few-file tasks;
- short sessions where the cost of graph generation exceeds the benefit.

### 3. Output Rule

When Graphify is explicitly used, its standard outputs are:

- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/graph.json`
- optional derived graph artifacts such as HTML or other exports

`graphify-out/GRAPH_REPORT.md` is a navigation cache, not the source of truth. It should identify the repository state or commit it reflects whenever possible.

### 4. Refresh Rule

After structural project changes, Graphify should be refreshed before relying on it in later broad-navigation sessions.

If it has not been refreshed, report that its findings may be stale and verify important conclusions against the current repository files.

## Integration Policy

Graphify may be referenced from project documentation only when that project has deliberately adopted it.

Do not add Graphify to the default `START_HERE.md` route, automatic project initialization, global Codex instructions or ordinary new-project workflow merely because the skill exists.

The reusable skill remains available at:

- `skills/graph/graphify/SKILL.md`

## Activation Boundary

The `graphify` skill may remain in reviewed/approved status, but should not move to active-by-default behavior until:

- `Project-Execution-OS` has used it successfully in a deliberate pilot;
- at least one live broad project has used it successfully;
- refresh discipline and context-cost benefit are demonstrated in practice.

## Next Step

When a genuinely broad live repository needs repeated architectural navigation, run one explicit Graphify pilot, measure whether it reduces repeated exploration, and decide from evidence whether to adopt it in that project.
