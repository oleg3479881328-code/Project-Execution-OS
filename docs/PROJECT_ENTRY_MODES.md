# Project Entry Modes

## Purpose

This document defines the valid entry modes for work entering `Project-Execution-OS`.

The central brain must distinguish these modes early so it does not force the wrong workflow shape.

## Mode 1 — New Project

Use when:
- the user is starting a new project;
- no durable project repository exists yet;
- the project should enter the standard operating flow from zero.

Default rule:
- create a dedicated GitHub repository for the project unless an explicit exception is chosen.

## Mode 2 — Brainstorm Only

Use when:
- the user wants idea exploration only;
- the user does not want project creation yet;
- the goal is to clarify direction, options, risks, constraints, or scope before deciding whether the project should exist.

Rules:
- do not create a project repository by default;
- do not create project artifacts unless the user explicitly asks to persist the brainstorm;
- use clarification, research, reasoning, and option comparison;
- keep state clearly marked as exploratory, not operational;
- if the brainstorm becomes stable enough, explicitly ask whether to convert it into a real project.

Recommended skill path:
- `pre-architecture-brainstorming`
- `logic-deconstruction` when reasoning needs stress-testing
- `github-repository-research` when external examples matter

## Mode 3 — Existing Standard Project

Use when:
- the user points to an existing repository or project that already largely follows the current standard;
- the task is to continue work, review, or implement within that project.

Rules:
- read the existing project memory first;
- use the smallest suitable workflow;
- do not rebuild the project structure without evidence of a gap.

## Mode 4 — Legacy Project Normalization

Use when:
- the user gives an older repository or folder;
- the project does not follow the current `Project-Execution-OS` standard;
- the goal is to bring the project into the new operating model.

Rules:
- do not pretend the old project already follows the standard;
- inspect the current repository state first;
- preserve existing evidence and history;
- map old artifacts to the new structure;
- add missing project entrypoint, project state, rules, logs, and workflow records as needed;
- explicitly mark migrated versus newly created artifacts;
- avoid destructive normalization.

Typical output:
- documentation audit
- structure gap analysis
- migration plan
- normalized project entry artifacts

Recommended skill path:
- `project-documentation-architect`
- `project-experience-memory`
- `project-knowledge-sync`
- `graphify` when the legacy repo is broad

## Mode Selection Rule

At startup, the system should classify the request into one of these modes before forcing repository creation or workflow expansion.

If unclear, ask only the minimum question needed to identify the mode.
