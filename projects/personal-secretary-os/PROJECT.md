# Personal Secretary OS

## Project

- Name: `personal-secretary-os`
- Type: `personal operations and AI assistant design project`
- Short description: A central personal secretary for Oleg that accepts unstructured incoming information, helps sort it, turns it into actionable items, and keeps personal and project matters organized.

## Purpose

- Build a practical personal secretary that reduces the owner's cognitive load.
- The secretary should accept raw inputs such as ideas, tasks, links, notes, documents, and requests without requiring the owner to organize them first.
- The secretary should classify incoming material, keep order, connect related items, surface what needs attention, and help prepare next actions.
- Current-stage success means validating a simple manual operating model before adding integrations or automation.

## System Entry Point

- `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`

## Router Entry

- One canonical secretary mode exists.
- Natural aliases route to the same project: `личный секретарь`, `секретарь`, `режим секретаря`, `режим личного секретаря`, `личный помощник`, `помощник`, `режим помощника`, `personal secretary`, `personal assistant`.
- These are synonyms for one entrypoint, not separate assistants.
- A long startup prompt is not required.

## ChatGPT Propagation Boundary

- The canonical repository copy of the ChatGPT routing instruction lives in `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`.
- Editing repository files does not automatically rewrite the active Custom Instructions field inside the ChatGPT app.
- After a core-prompt change, update the app field before testing a fresh conversation.

## Operating Principle

- This project is governed by `Project Execution OS`.
- `Existing Solution First` is mandatory before designing custom tooling or integrations.
- Start simple, validate repeated manual use, and add automation only when it solves an observed problem.

## Source Of Truth

- Project definition and operating design: this project folder inside the central `Project Execution OS` repository.
- Current active execution state: `PROJECT_STATE.md`.
- Latest execution log: `logs/latest.md`.
- Raw private personal intake during v0: the active ChatGPT secretary conversation only.
- No separate GitHub repository, Notion workspace, Telegram bot, or external automation layer has been attached yet.

## Current Status

- Status: `active — routing propagation pending`
- Mode: `manual secretary routing validation`
- Implementation state: the operating contract and repository routes exist; active ChatGPT Custom Instructions still need the updated routing sentence before re-test.

## Done So Far

- Confirmed the need for a central personal secretary rather than another isolated chatbot.
- Confirmed the initial simplification: begin without Telegram.
- Confirmed that integrations and automation are deferred until the manual operating model is clear.
- Created `V0_MANUAL_OPERATING_CONTRACT.md` with the intake model, categories, response format, safety rules, persistence boundary, and validation target.
- Created `PROJECT_STATE.md` and `logs/latest.md` for transfer-ready continuation.
- Added one router entry with natural aliases and removed the requirement to paste a long startup command.
- Tested `Режим секретаря` in a fresh conversation and found that repository changes do not self-apply to ChatGPT app settings.
- Updated the canonical core prompt with explicit secretary-mode aliases.

## Current Focus

- Propagate the updated secretary routing sentence into active ChatGPT Custom Instructions.
- Re-test routing in a fresh conversation.

## Next Practical Step

- Update the active ChatGPT Custom Instructions field with the secretary routing sentence from `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`.
- Open a fresh conversation and write `Режим секретаря`.

## Key Decisions And Constraints

- Treat secretary and assistant wording as aliases for one mode.
- Do not require a long activation prompt.
- Do not assume GitHub prompt changes automatically modify ChatGPT app settings.
- Do not add Telegram at the initial stage.
- Do not add broad automation before repeated manual use proves the need.
- Do not create a parallel operating system that duplicates `Project Execution OS`.
- Keep the owner interaction simple: the owner should be able to drop raw information without pre-sorting it.
- Keep private intake out of this GitHub project folder.
- Any future external actions such as sending messages, deleting information, or making commitments on the owner's behalf require explicit approval unless a narrower safe rule is later confirmed.
- Apply `Existing Solution First` before introducing custom architecture, code, integrations, databases, or agent workflows.

## Read Next

1. `V0_MANUAL_OPERATING_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `logs/latest.md`
4. `../../docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
5. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`
6. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/PROJECT_LIFECYCLE_MODEL.md`
7. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
8. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
