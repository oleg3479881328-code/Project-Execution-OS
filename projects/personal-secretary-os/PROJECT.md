# Personal Secretary OS

## Project

- Name: `personal-secretary-os`
- Type: `personal operations and AI assistant design project`
- Short description: A central personal secretary for Oleg that accepts unstructured incoming information, helps sort it, turns it into actionable items, accumulates useful personal, health and work knowledge, and keeps personal and project matters organized.

## Purpose

- Build a practical personal secretary that reduces the owner's cognitive load.
- The secretary should accept raw inputs such as ideas, tasks, links, notes, documents, and requests without requiring the owner to organize them first.
- The secretary should classify incoming material, keep order, connect related items, surface what needs attention, and help prepare next actions.
- The secretary should accumulate useful knowledge about Oleg, active work, health follow-ups, decisions, preferences, open loops and repeated workflows without storing secrets or turning memory into a dump.
- Current-stage success means validating a simple manual operating model before adding integrations or automation.

## System Entry Point

- `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`

## Router Entry

- One canonical secretary mode exists.
- Natural aliases route to the same project: `личный секретарь`, `секретарь`, `режим секретаря`, `режим личного секретаря`, `режим секретариата`, `личный помощник`, `помощник`, `режим помощника`, `personal secretary`, `personal assistant`.
- These are synonyms for one entrypoint, not separate assistants.
- A long startup prompt is not required.
- When the owner sends only a secretary activation phrase, the startup response is exactly: `Секретарь готов босс` Do not list capabilities or explain the mode in that activation reply.

## ChatGPT Propagation Boundary

- The canonical repository copy of the ChatGPT routing instruction lives in `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`.
- Editing repository files does not automatically rewrite the active Custom Instructions field inside the ChatGPT app.
- After a core-prompt change, update the app field before testing a fresh conversation.

## Operating Principle

- This project is governed by `Project Execution OS`.
- `Existing Solution First` is mandatory before designing custom tooling or integrations.
- Start simple, validate repeated manual use, and add automation only when it solves an observed problem.
- Knowledge accumulation must follow `PERSONAL_KNOWLEDGE_STANDARD.md` and must not bypass privacy or storage boundaries.
- Health-related knowledge must follow `HEALTH_KNOWLEDGE_STANDARD.md`; the secretary organizes health information but does not diagnose, prescribe, or replace a clinician.

## Source Of Truth

- Project definition and operating design: this project folder inside the central `Project Execution OS` repository.
- Current active execution state: `PROJECT_STATE.md`.
- Latest execution log: `logs/latest.md`.
- Standard procedure for personal documents: `DOCUMENT_SAVING_STANDARD.md`.
- Standard procedure for personal/work knowledge: `PERSONAL_KNOWLEDGE_STANDARD.md`.
- Standard procedure for health knowledge: `HEALTH_KNOWLEDGE_STANDARD.md`.
- Raw private personal intake during v0: the active ChatGPT secretary conversation only.
- A lightweight Notion document index is attached for validated document cards. It is not yet the general durable storage layer for all personal intake.

## Current Status

- Status: `active — first real document workflow validated; personal and health knowledge standards added`
- Mode: `manual secretary routing, intake validation, controlled knowledge accumulation, and health-continuity organization`
- Implementation state: routing works in the active ChatGPT conversation; the first personal-document intake workflow has been validated and recorded as a reusable standard; personal/work knowledge accumulation and health knowledge tracking now have project standards.

## Done So Far

- Confirmed the need for a central personal secretary rather than another isolated chatbot.
- Confirmed the initial simplification: begin without Telegram.
- Confirmed that integrations and automation are deferred until the manual operating model is clear.
- Created `V0_MANUAL_OPERATING_CONTRACT.md` with the intake model, categories, response format, safety rules, persistence boundary, and validation target.
- Created `PROJECT_STATE.md` and `logs/latest.md` for transfer-ready continuation.
- Added one router entry with natural aliases and removed the requirement to paste a long startup command.
- Tested `Режим секретаря` in a fresh conversation and found that repository changes do not self-apply to ChatGPT app settings.
- Updated the canonical core prompt with explicit secretary-mode aliases.
- Updated the canonical core prompt so personal secretary mode is the default for personal-operations intake.
- Processed the first real document intake: an Ohio vehicle registration card for a Mazda CX-5.
- Created a scan-style derivative without regenerating or changing document text.
- Created a Notion vehicle record and a user-facing document-saving procedure page.
- Added `DOCUMENT_SAVING_STANDARD.md` as the reusable default procedure for future document intake.
- Added `PERSONAL_KNOWLEDGE_STANDARD.md` as the reusable default procedure for accumulating useful knowledge about Oleg and ongoing work.
- Added `HEALTH_KNOWLEDGE_STANDARD.md` as the reusable default procedure for organizing labs, medications, exams, doctor questions and health open loops.
- Added concise activation response rule for secretary-mode startup.

## Current Focus

- Continue manual validation with real intake batches.
- Apply the document-saving standard automatically for future document photographs and scans.
- Apply the personal knowledge standard when incoming information has future value.
- Apply the health knowledge standard when incoming material concerns labs, medications, symptoms, appointments, screenings, doctor instructions or medical follow-ups.
- Observe which additional categories and storage patterns are actually needed.

## Next Practical Step

- Process additional real secretary intake batches.
- When a personal document is submitted, apply `DOCUMENT_SAVING_STANDARD.md` automatically and mention only exceptions or the next action needed from the owner.
- When reusable personal/work knowledge appears, apply `PERSONAL_KNOWLEDGE_STANDARD.md` and mention compactly what should be remembered.
- When health information appears, apply `HEALTH_KNOWLEDGE_STANDARD.md`, separate facts from assumptions, identify the next action, and mark what must be verified with a clinician or pharmacist.

## Key Decisions And Constraints

- Treat secretary and assistant wording as aliases for one mode.
- Do not require a long activation prompt.
- Do not assume GitHub prompt changes automatically modify ChatGPT app settings.
- Do not add Telegram at the initial stage.
- Do not add broad automation before repeated manual use proves the need.
- Do not create a parallel operating system that duplicates `Project Execution OS`.
- Keep the owner interaction simple: the owner should be able to drop raw information without pre-sorting it.
- Keep raw private intake out of this GitHub project folder.
- Keep secrets, raw personal documents, unredacted scans, sensitive identifiers and raw health data out of GitHub project files.
- A lightweight Notion index may store confirmed document cards; do not treat it as the storage layer for all personal intake yet.
- Durable health storage requires an owner-approved private layer; GitHub stores only health workflow rules, not personal medical records.
- Any future external actions such as sending messages, deleting information, creating medical appointments, changing information, or making commitments on the owner's behalf require explicit approval unless a narrower safe rule is later confirmed.
- Apply `Existing Solution First` before introducing custom architecture, code, integrations, databases, or agent workflows.

## Read Next

1. `V0_MANUAL_OPERATING_CONTRACT.md`
2. `PERSONAL_KNOWLEDGE_STANDARD.md`
3. `HEALTH_KNOWLEDGE_STANDARD.md`
4. `DOCUMENT_SAVING_STANDARD.md`
5. `PROJECT_STATE.md`
6. `logs/latest.md`
7. `../../docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
8. `../../docs/KNOWLEDGE_SYSTEM.md`
9. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`
10. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/PROJECT_LIFECYCLE_MODEL.md`
11. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
12. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
