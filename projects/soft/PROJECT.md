# SOFT — PROJECT.md

## Project

- Name: `SOFT`
- Type: umbrella software knowledge + project coordination
- Short description: единый проект для всех наработок, связанных с программным обеспечением — как нашего собственного софта, так и чужих программ, сервисов, инструментов и решений, которые мы изучаем, тестируем или используем.

## Purpose

Проект нужен, чтобы не терять и не размазывать по разным чатам знания о софте, а собирать их в одном понятном контуре.

В проект входят:

- наши собственные программы, расширения, утилиты, прототипы и разработки;
- чужие программы, сервисы и инструменты, которые стоит сохранить, изучить, сравнить или использовать;
- обзоры, тесты, диагностика, баги, рабочие решения и полезные настройки;
- reusable-паттерны и готовые решения, которые можно применять в других проектах;
- ссылки, документация, установочные/экспортные пакеты и другие долговечные артефакты по софту.

## System Entry Point

- https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md

## Source Of Truth

- Canonical project entrypoint and routing: `projects/soft/PROJECT.md` in `oleg3479881328-code/Project-Execution-OS`.
- Canonical Google Drive project folder for durable software artifacts and collected materials: https://drive.google.com/drive/folders/1wlTvVm6UN0yYEzz_hDRCtNfu3LpXl04M
- Existing standalone software repositories/projects remain canonical for their own source code and detailed implementation state; SOFT links to them rather than duplicating them.
- The connected SOFT Google Drive source is the durable artifact/navigation layer, not a replacement for the global Project Execution OS entrypoint.

## Source Trail

- Google Drive parent software-project folder: https://drive.google.com/drive/folders/19l0KiyA70EZnTcMIztbBVOWG15geudhI
- Project Execution OS project registry: `projects/ROUTER.md`
- SOFT Drive Guide: https://docs.google.com/document/d/1DAErwDeXGAD6u7nqUn1dMFMui3LJsmbLw23cJUgsB-E/edit
- SOFT Source Map: https://docs.google.com/document/d/1qsoAXlHiZ-8W6_vzxTD2rNrZApBgfZfZRUWBNXQ0oCQ/edit

## Google Drive Structure

- `00 — PROJECT GUIDE` — project orientation and source/navigation material.
  - `01 — GUIDES & INDEXES`
    - `00 — READ FIRST`
      - `SOFT — DRIVE GUIDE — READ FIRST`
  - `02 — SOURCE MAP`
    - `SOFT — SOURCE MAP`
- `01 — OUR SOFTWARE` — durable artifacts and collected material for software we build ourselves.
- `02 — THIRD-PARTY SOFTWARE` — material about external programs, SaaS, tools and services we evaluate/use.
- `90 — INBOX — TO SORT` — temporary intake for material whose final destination is not yet clear.

Do not create product-specific subfolders until real material exists. When a specific software project already has its own canonical repository or Drive folder, keep that source authoritative and link to it from SOFT instead of duplicating it.

## Current Status

- Status: active
- Mode: collect + evaluate + reuse + build
- Phase: Drive and canonical re-entry structure initialized; ready for software intake.

## Done So Far

- Confirmed project name: `SOFT`.
- Confirmed scope: both our own software and third-party software/programs.
- Created the canonical Google Drive folder `SOFT` inside the existing software `Projects` folder.
- Created the minimum Drive classification structure for our software, third-party software and unsorted intake.
- Created a Drive Guide with explicit new-chat entry instructions and file-placement rules.
- Created a Source Map that distinguishes GitHub, Drive, official vendor sources, our verified tests and chat/model memory.
- Registered SOFT in the Project Execution OS project router.

## Current Focus

Use SOFT as the common collection and navigation layer for software-related work without duplicating canonical source repositories or existing Project Execution OS standards.

## Next Practical Step

When the next software item appears, first check whether it already belongs to an existing project/repository. If not, classify it into `01 — OUR SOFTWARE` or `02 — THIRD-PARTY SOFTWARE`; use `90 — INBOX — TO SORT` only when classification is genuinely unclear.

## Key Decisions And Constraints

- Existing Solution First is mandatory: before inventing or building, check our existing solutions, current projects, documentation, tools/integrations, then proven external solutions.
- Do not duplicate source code or canonical project state from standalone repositories merely to make SOFT look complete; link to the canonical source.
- Durable files with continuing value belong in the SOFT Google Drive folder tree unless a more specific canonical project folder already exists.
- Do not scatter SOFT artifacts into the Google Drive root.
- Keep the SOFT Drive root clean and classification-focused.
- Do not create empty product/category trees in anticipation of hypothetical future needs.
- Community claims about third-party software remain evidence until independently verified or confirmed by official sources/our own tests.
- Chat history is not canonical project memory.

## Read Next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. SOFT Drive Guide: https://docs.google.com/document/d/1DAErwDeXGAD6u7nqUn1dMFMui3LJsmbLw23cJUgsB-E/edit
4. SOFT Source Map: https://docs.google.com/document/d/1qsoAXlHiZ-8W6_vzxTD2rNrZApBgfZfZRUWBNXQ0oCQ/edit
5. `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
6. `../../docs/FILE_ORGANIZATION_STANDARD.md`
7. `../../docs/PROJECT_MEMORY_STANDARD.md`
8. Google Drive SOFT folder: https://drive.google.com/drive/folders/1wlTvVm6UN0yYEzz_hDRCtNfu3LpXl04M
