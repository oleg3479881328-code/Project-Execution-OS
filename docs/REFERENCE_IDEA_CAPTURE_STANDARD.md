# Reference Idea Capture Standard

## Purpose

This standard defines the lightest durable path for ideas, links, notes, references, screenshots, and outside solutions that should not be lost but are not yet project state.

Use this function when:

- a user says "I have an idea, let's discuss it";
- the material is interesting but not yet ready to become a project;
- a reference should be preserved without falsely promoting it into a standard, skill, block, or implementation task;
- the right next step is discussion, research, and triage rather than project startup.

## Canonical External Library

Default external intake library:

`oleg3479881328-code/Reference-Idea-Library`

Treat it as:

- idea intake;
- reference holding area;
- triage layer;
- promotion queue.

Do not treat it as:

- the central project brain;
- project source of truth;
- a replacement for project repositories;
- a replacement for `knowledge-library/` inside `Project Execution OS`.

## Core Workflow

Canonical flow:

`IDEA -> RESEARCH -> CONCLUSION -> DISCUSS -> DECIDE -> RECORD`

Short rule:

- discuss first;
- decide second;
- record only by explicit user command.

## Source Traceability Requirement

Every durable reference capture must follow:

`docs/SOURCE_TRACEABILITY_STANDARD.md`

A saved idea card is incomplete unless it includes a recoverable source trail.

Minimum acceptable source trail:

- direct source URL; or
- source file attachment / Drive URL / Notion URL; or
- repository path; or
- raw package path plus SHA256; or
- source list with filenames and hashes.

If a card says that a full package, raw bundle, archive, or research pack exists, the card must include the direct URL or path to that package.

Do not save only a summary with a vague note like "full package saved separately" unless the actual package location is included.

If the package exists only in the chat workspace and has not been uploaded to durable storage, say that explicitly and do not present the capture as fully durable.

## When To Use

Use this standard instead of project startup when:

- the user wants to explore an idea without committing to a new repository;
- the material is a reference, donor pattern, interesting product, article, workflow, or note;
- the assistant should help prevent loss of the idea without over-formalizing it into a project.

## When Not To Use

Do not use this library when:

- the work is already a real project with durable project state;
- the task already belongs in a specific project repository;
- the material is already reviewed reusable knowledge that should live in `knowledge-library/`;
- the next step is clearly Codex execution rather than idea triage.

## Operating Rule

Reference capture is optional and lightweight.

Do not record every idea automatically.

If the user only wants discussion, discussion is enough.

Record only when the user explicitly wants the idea preserved.

When recording, include source traceability before calling the record complete.

## Promotion Paths

Useful records may later be promoted into:

- a project decision;
- a project task;
- a reusable pattern;
- a central skill;
- a domain block;
- `knowledge-library/`;
- a Codex handoff packet.

## Final Rule

Capture-before-forget is good.

Premature formalization is not.

No source trail, no complete capture.