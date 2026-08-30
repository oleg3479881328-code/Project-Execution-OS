# Project Entrypoint Standard

## Purpose

This standard defines the canonical entrypoint artifact for a specific project while preserving the Project Execution OS rule that AI interfaces enter the overall system through one global `START_HERE.md`.

A project entrypoint is a durable project node reached through routing. It is not a competing global door.

## Core Rule

Every meaningful project should have exactly one current canonical project entrypoint in its durable workspace.

Any AI/client interface should enter Project Execution OS through the global `START_HERE.md`, follow recursive routing, and only then reach the relevant project's canonical entrypoint.

```text
global START_HERE.md
→ router
→ router / registry / index ... as needed
→ canonical project entrypoint
→ minimum current evidence
```

Routing depth is not fixed.

## Canonical Project Forms

Use the same project-entry contract in environment-specific durable forms:

- `GitHub / repository projects` -> `PROJECT.md`
- `Notion / workspace-first projects` -> `Project Entrypoint` or `START HERE` page
- another durable workspace -> one clearly identified canonical project entrypoint appropriate to that system

The medium may differ. The contract should stay the same.

## ChatGPT Projects

ChatGPT Project is an interface, not a durable project-entrypoint layer.

When an attached bootstrap file is useful or required, use the generic `START_HERE.md` pointer defined by `docs/CHATGPT_PROJECT_START_HERE_TEMPLATE.md`.

That attachment points to the global Project Execution OS `START_HERE.md`, not directly to a specific project.

Do not maintain project-specific ChatGPT attachment snapshots or parallel project-specific START_HERE contracts merely because work happens inside separate ChatGPT Projects.

Project identity is resolved through the live router tree and durable project registry/index nodes.

## Recursive Navigation Contract

A navigation node may point to:

- another router;
- a project registry;
- a domain registry;
- a collection index;
- a project entrypoint;
- another specialized navigation node;
- canonical content.

Any of those navigation nodes may route onward again.

There is no artificial maximum routing depth. Use the depth required by the real information architecture while keeping each node narrow.

Navigation nodes should not duplicate the detailed state or knowledge stored behind them.

## Required Questions The Project Entrypoint Must Answer

After reaching the canonical project entrypoint, a new human or AI should be able to answer:

1. What is this project?
2. Why does it exist?
3. What kind of project is it?
4. Where is the source of truth?
5. What has already been done?
6. What is the current state?
7. What is the next practical step?
8. Which decisions or constraints must not be ignored?
9. Where should I read next if I need deeper context?

If the entrypoint does not answer these clearly, it is incomplete.

## Required Sections

Every canonical live project entrypoint should include the following sections in compact form.

### 1. Project
- project name;
- short description;
- project type.

### 2. Purpose
- why the project exists;
- who it is for;
- what success looks like at the current stage.

If purpose is unknown, say so directly instead of guessing.

### 3. Source Of Truth
State clearly where durable truth lives.

### 4. Source Trail
Follow `docs/SOURCE_TRACEABILITY_STANDARD.md` and provide recoverable pointers to underlying sources, raw inputs, Drive files, repository paths, databases or other durable evidence.

### 5. Current Status
Summarize current mode, phase and health/confidence when relevant.

### 6. Done So Far
List only the most important completed milestones.

### 7. Current Focus
State what is actively being worked on now.

### 8. Next Practical Step
State the next useful action clearly enough that another participant can continue without guessing.

### 9. Key Decisions And Constraints
Record only decisions and constraints that materially affect future work.

### 10. Read Next
Point to the minimum deeper artifacts needed for additional context.

## Initialization-Only Entrypoint

A project entrypoint may honestly exist before the project purpose is known.

In that state, say explicitly that the project is initialized but not yet defined. Unknown fields are allowed when truthful. Invented fields are not.

## What The Project Entrypoint Must Not Become

The project entrypoint must not become:

- the global system router;
- the full project history;
- the full rules document;
- a transcript dump;
- a research archive;
- a hidden second state database.

History belongs in logs, workflow runs, databases or supporting pages. Rules belong in standards/project rules. The project entrypoint remains the shortest reliable project-level front door after routing has selected that project.

## Legacy Migration Rule

For repository projects:

- if `PROJECT.md` exists, use it as the canonical project entrypoint;
- if `PROJECT.md` is absent but `PROJECT_ENTRYPOINT.md` exists, treat it as a legacy name;
- migrate it to `PROJECT.md` at the nearest safe opportunity;
- update links and references;
- do not keep both active at the same time.

## Maintenance Rule

Update the canonical project entrypoint whenever its source of truth, source trail, current mode, current focus, next practical step, or a major decision changes what a new participant must know first.

Do not update the generic ChatGPT attachment for ordinary project changes.

## Final Rule

One Project Execution OS has one global AI door: `START_HERE.md`.

One meaningful project has one canonical durable project entrypoint.

Recursive routers connect the global door to the correct project and may use as many navigation levels as the information architecture requires.