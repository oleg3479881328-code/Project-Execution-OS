# SOFT — PROJECT.md

## Project

- Name: `SOFT`
- Type: umbrella software knowledge + project coordination
- Short description: единый проект для всех наработок, связанных с программным обеспечением — как нашего собственного софта, так и чужих программ, сервисов, инструментов и решений, которые мы изучаем, тестируем или используем.

## Purpose

SOFT нужен, чтобы всё программное находилось из одного места, но без бессмысленного копирования кода и живого состояния из уже существующих проектов.

В проект входят:

- наши программы, расширения, утилиты, прототипы и внутренние системы;
- сторонние программы, SaaS, developer tools, open-source решения и доноры;
- обзоры, тесты, диагностика, баги, рабочие решения, настройки и benchmarks;
- reusable-паттерны и готовые решения;
- установочные/экспортные пакеты, ZIP, screenshots, evidence and manuals;
- legacy software and duplicate-source normalization.

## System Entry Point

- https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md

## Source Of Truth

- Canonical project entrypoint/routing: this `projects/soft/PROJECT.md`.
- Canonical SOFT Drive root: https://drive.google.com/drive/folders/1wlTvVm6UN0yYEzz_hDRCtNfu3LpXl04M
- Master software discovery index: https://docs.google.com/document/d/1yTWfazVPhs-AWdSsvS4Q6xyNd7bXKtqi6EvrmQMdAOk/edit
- Existing standalone repositories/projects remain authoritative for their own source code and live implementation state; SOFT links to them rather than duplicating them.

## Source Trail

- Google Drive parent historical software-project folder: https://drive.google.com/drive/folders/19l0KiyA70EZnTcMIztbBVOWG15geudhI
- Project Execution OS project registry: `projects/ROUTER.md`
- SOFT Drive Guide: https://docs.google.com/document/d/1DAErwDeXGAD6u7nqUn1dMFMui3LJsmbLw23cJUgsB-E/edit
- SOFT Source Map: https://docs.google.com/document/d/1qsoAXlHiZ-8W6_vzxTD2rNrZApBgfZfZRUWBNXQ0oCQ/edit
- Our Software Index: https://docs.google.com/document/d/1nzxaCsFTF7Z7VGFfYziysByeR63eMOELpDT5rBcTDHk/edit
- Third-Party Software Index: https://docs.google.com/document/d/1C-F_ukN2AlryP-_FxlJqFIKSbKjat8kzzMw8HsaSPH0/edit
- Duplicates & Legacy Cleanup Queue: https://docs.google.com/document/d/1lBpoB-bbj4ihk6VW_gny_XbdfYCVD8Im0u6z3OTaBuc/edit

## Google Drive Structure

- `00 — PROJECT GUIDE`
  - `01 — GUIDES & INDEXES`
    - `00 — READ FIRST` → `SOFT — DRIVE GUIDE — READ FIRST`
    - `SOFT — MASTER SOFTWARE INVENTORY`
    - `SOFT — DUPLICATES & LEGACY CLEANUP QUEUE`
  - `02 — SOURCE MAP` → `SOFT — SOURCE MAP`
- `01 — OUR SOFTWARE` → `SOFT — OUR SOFTWARE INDEX` + future durable artifacts when needed.
- `02 — THIRD-PARTY SOFTWARE` → `SOFT — THIRD-PARTY SOFTWARE INDEX` + future durable artifacts when needed.
- `90 — INBOX — TO SORT` — temporary intake only.

## Current Status

- Status: active
- Mode: collect + evaluate + reuse + build
- Phase: first cross-source software inventory completed; ongoing capture and legacy canonicalization.

## Done So Far

- Created and registered SOFT under Project Execution OS.
- Created the canonical Drive structure and new-chat Guide/Source Map.
- Performed the first broad software revision across PEOS GitHub projects, historical Drive software material and File Library software/reference corpora.
- Created Master Software Inventory with status labels and canonical links.
- Created separate Our Software and Third-Party Software indexes.
- Created a safe cleanup queue for duplicate/legacy material; no destructive cleanup was performed.
- Updated new-chat routing so software research starts from existing SOFT knowledge.

## Current Focus

Use SOFT as the software discovery/control plane. New chats should find what we already have before doing fresh research or creating another implementation.

## Next Practical Step

For the next software item: Master Inventory → correct index → canonical source → Existing Solution First → only then fresh research/build if needed. Promote meaningful new findings back into SOFT.

## Key Decisions And Constraints

- Existing Solution First is mandatory.
- Do not duplicate source code or live project state from standalone repositories merely to make SOFT complete.
- Durable file artifacts belong in SOFT only when a more specific canonical project folder does not already own them.
- Legacy/duplicate Drive material must not be deleted or consolidated before canonical comparison and explicit destructive approval.
- Historical machine/software inventories are evidence, not automatically current truth.
- Time-sensitive third-party facts such as pricing, licenses, features and limits must be revalidated from current official sources.
- Chat history is not canonical project memory.

## Read Next

1. `PROJECT_STATE.md`
2. SOFT Master Software Inventory: https://docs.google.com/document/d/1yTWfazVPhs-AWdSsvS4Q6xyNd7bXKtqi6EvrmQMdAOk/edit
3. SOFT Drive Guide: https://docs.google.com/document/d/1DAErwDeXGAD6u7nqUn1dMFMui3LJsmbLw23cJUgsB-E/edit
4. Our Software Index: https://docs.google.com/document/d/1nzxaCsFTF7Z7VGFfYziysByeR63eMOELpDT5rBcTDHk/edit
5. Third-Party Software Index: https://docs.google.com/document/d/1C-F_ukN2AlryP-_FxlJqFIKSbKjat8kzzMw8HsaSPH0/edit
6. Duplicates & Legacy Cleanup Queue: https://docs.google.com/document/d/1lBpoB-bbj4ihk6VW_gny_XbdfYCVD8Im0u6z3OTaBuc/edit
7. `logs/latest.md`
8. `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
9. Google Drive SOFT root: https://drive.google.com/drive/folders/1wlTvVm6UN0yYEzz_hDRCtNfu3LpXl04M
