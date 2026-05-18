# Graphify Standard

## Purpose

This standard defines how Graphify should be used as the graph-memory and repository-cognition layer for `Project-Execution-OS` and for projects started through it.

## Current Status

Graphify is not yet fully installed into this repository as an active local graph layer.

At the time of this record:

- there is no `graphify-out/` folder in this repository;
- there is no local Graphify output committed here yet;
- there are no local hooks or repo-specific Graphify instructions committed yet.

So the answer to "is graph memory already wired here?" is:

`not yet fully`

## Role In The Central Brain

Graphify should become:

- the graph-memory layer for broad repository understanding;
- the always-on repository cognition bootstrap for large repos or document corpora;
- the cross-file relationship map for future AI sessions;
- a durable navigation layer that reduces repeated re-reading.

## Rules

### 1. New Project Rule

When a new project repository is created through `Project-Execution-OS`, Graphify should be initialized as part of setup when the project contains supported source or docs files.

The new AI entering a project should not merely know about Graphify.

It should:

1. check whether the project is broad enough to justify Graphify;
2. if yes, build Graphify when `graphify-out/GRAPH_REPORT.md` is missing and supported files exist;
3. read `graphify-out/GRAPH_REPORT.md` before broad exploration;
4. refresh Graphify after structural changes when feasible.

### 2. Broad Context Rule

Use Graphify when:

- the repository is broad or unknown;
- architecture or cross-file relationships matter;
- the project will likely receive repeated follow-up questions;
- direct file reading would create unnecessary context cost.

Do not force Graphify for narrow one-file or few-file tasks.

### 3. Output Rule

The standard Graphify outputs are:

- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/graph.json`
- optional derived graph artifacts such as HTML or other exports

### 4. Refresh Rule

After structural project changes, Graphify should be refreshed so that later sessions do not rely on stale graph memory.

## Integration Targets

Graphify should be referenced from:

- `Start New Project.md`
- `START_HERE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- project bootstrap rules

## Next Step

Wire full local Graphify installation and project-bootstrap behavior into live repository practice.
