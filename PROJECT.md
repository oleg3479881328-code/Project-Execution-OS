# PROJECT.md

## Project

- Name: `Project Execution OS`
- Type: `layer-aware project operating system`
- Short description: `central standards, templates, routing, and reusable artifacts for starting and running projects across the right durable layers`

## Purpose

- Create a universal operating system for starting, running, reviewing, and preserving projects without forcing every idea into the same storage model.
- Support humans and AI agents through one stable entrypoint, one live router, and minimal task-specific context loading.

## Source Of Truth

- This repository is the committed source of truth for `Project Execution OS` standards, templates, skills, and reusable repository artifacts.
- `START_HERE.md` is the stable system door.
- `docs/ROUTER.md` is the live internal map.

## Current Status

- Mode: `document-first`
- Phase: `foundation`
- Status: `index-first discovery layer, local semantic retrieval pilot, and optional hybrid local-model preprocessing prototype implemented`

## Done So Far

- Established `START_HERE.md` as the stable top-level entrypoint.
- Split live routing into `docs/ROUTER.md`.
- Built central standards for lifecycle, context assembly, repository memory, review, research, handoff, and bootstrap.
- Added a bounded structural corpus builder, local semantic SQLite runtime, and mandatory index-first agent-entry guidance.
- Added an optional hybrid local-model preprocessing prototype for bounded context compression before cloud API reasoning.

## Current Focus

- Keep central standards internally consistent while making real-project bootstrap lightweight and safe.
- Keep repository entry narrow by default through curated indexes, generated corpus files, and local semantic retrieval.
- Measure whether optional local preprocessing can reduce cloud-bound payload size without weakening traceability or making the local layer mandatory.

## Next Practical Step

- Validate semantic retrieval quality and the hybrid preprocessing prototype on additional real repository tasks before deciding what should be promoted beyond prototype scope.

## Key Decisions And Constraints

- Do not duplicate evolving system logic into ad hoc files when the repository standards already define it.
- `Existing Solution First` applies before inventing new central mechanisms.
- `PROJECT.md` is the canonical local project entrypoint for GitHub-backed and file-executed projects.
- `PROJECT_INDEX.md` remains an index and must not replace the role of `PROJECT.md`.
- Local Git is the default bootstrap for real project folders; GitHub, Notion, and Google Drive are attached only when they are actually needed.

## Read Next

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT_INDEX.md`
4. `docs/PROJECT_BOOTSTRAP_STANDARD.md`
5. `docs/PROJECT_ENTRYPOINT_STANDARD.md`
