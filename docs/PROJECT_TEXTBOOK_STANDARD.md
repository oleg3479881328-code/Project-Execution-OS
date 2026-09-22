# Project Textbook Standard

## Purpose

This standard defines the durable **project textbook** used by Project Execution OS so a new chat, agent, or human does not have to rediscover already solved project knowledge.

The textbook is a reusable solution manual, not a project history.

## Core Rule

Every meaningful project must maintain exactly one current canonical project textbook once the project purpose is known and reusable project knowledge exists.

The textbook records **how the project should be done now using accepted existing solutions**.

It does not record the chronology of how those solutions were discovered.

Canonical intent:

```text
NEW CHAT / NEW EXECUTOR
-> global START_HERE.md
-> router tree
-> project entrypoint
-> project textbook for reusable project knowledge
-> current state / latest work evidence only when needed
-> execute from current accepted solution
```

## Relationship To Other Project Artifacts

The textbook complements, but does not replace:

- `PROJECT.md` / project entrypoint — what the project is and where to go;
- `PROJECT_STATE.md` / Current State — what is happening now;
- `logs/latest.md` / Work Log — what happened in the latest meaningful execution;
- research/evidence files — raw investigation and external evidence;
- decision records — scoped decisions when a separate durable decision artifact is justified.

The textbook is the project's reusable operational knowledge layer.

## What Belongs In The Textbook

Include only reusable material such as:

- accepted architecture;
- ready existing solutions;
- canonical tool roles;
- proven workflows;
- standard inputs and outputs;
- current integration routes;
- durable constraints;
- authoritative source hierarchy;
- acceptance / QA gates;
- failure-recovery rules;
- stop conditions;
- do-not-rebuild rules;
- current canonical references;
- new-chat start procedure;
- explicit status labels when a solution is externally verified but not yet locally proven.

## What Must Not Become Textbook Content

Do not use the textbook as:

- a chat transcript;
- an experiment diary;
- a chronological migration log;
- a list of every failed attempt;
- a raw research dump;
- a temporary task list;
- a duplicate of PROJECT_STATE;
- a duplicate of logs/latest.md;
- a place for unverified guesses presented as production truth.

History and experiments may exist as evidence elsewhere, but the textbook should answer:

`What is the best currently accepted way to do this project now?`

## Knowledge Promotion

Use explicit knowledge states when necessary:

1. `DISCOVERY` — lead only.
2. `EXTERNALLY VERIFIED` — confirmed by authoritative external evidence.
3. `LOCAL CANDIDATE` — selected for the project but not yet accepted in the owner's environment.
4. `LOCAL-PROVEN` — executed successfully in the intended environment with required output evidence.
5. `ACCEPTED / CANONICAL` — reusable production route that passed the project's acceptance gate.

Promotion path:

```text
EXISTING SOLUTION
-> EXTERNAL VERIFICATION
-> LOCAL TEST WHEN REQUIRED
-> OUTPUT / READBACK QA
-> LOCAL-PROVEN
-> ACCEPTED / CANONICAL
-> TEXTBOOK
```

Do not promote an experiment, one-off accident, remembered trick, marketing claim, or merely successful command as canonical project knowledge.

## Existing-Solution-First Requirement

A project textbook must embody `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`.

For every durable capability, prefer:

```text
REUSE -> CONFIGURE -> INTEGRATE -> ADAPT -> BUILD
```

The textbook should make it easy for a new executor to see which tools, workflows, templates, scripts, integrations, repositories, or services already solve the problem.

When an adequate ready route exists, record it so future chats do not redesign the capability from zero.

## Naming

Preferred human-facing naming pattern:

`Учебник <PROJECT NAME> — HARD TECHNICAL STANDARD — NEW CHAT START HERE — <YYYY-MM-DD>`

Equivalent English naming is allowed when the project is English-first.

The date identifies the initial canonical version lineage. Ordinary updates should amend the same canonical document rather than create date-stamped duplicates.

## Storage

Store the textbook in the project's canonical durable workspace.

Examples:

- Google Drive-first project -> one canonical Google Doc in the project folder;
- repository-first project -> one canonical textbook/runbook file linked from PROJECT.md;
- Notion-first project -> one canonical textbook page linked from the project entrypoint.

Follow `docs/FILE_ORGANIZATION_STANDARD.md`.

Do not keep the only authoritative textbook in chat memory or a temporary runtime workspace.

## New Project Rule

Do not create an empty ceremonial textbook while project purpose is unknown.

Once a real project purpose is confirmed and the project has its first reusable architecture, workflow, ready solution, or accepted operating rule, create the project textbook and keep it current thereafter.

For projects that already contain meaningful work when this standard is adopted, create the textbook at the next substantive project touch.

## Project Entrypoint Rule

The project entrypoint should link to the current textbook under `Read Next` or the equivalent navigation section when the textbook exists.

Do not duplicate textbook content inside the project entrypoint.

## Maintenance Rule

Update the existing textbook when reusable truth changes:

- an accepted route is replaced;
- a new capability becomes locally proven;
- an existing tool becomes obsolete;
- an integration route changes;
- a new hard constraint is accepted;
- an acceptance gate changes;
- a ready solution eliminates previously custom work.

Do not update the textbook for routine execution events that do not change reusable knowledge.

## Replacement Rule

When a new solution supersedes an accepted route:

1. preserve the old evidence/history outside the textbook when needed;
2. validate the replacement through the same required acceptance path;
3. update the canonical textbook in place;
4. clearly mark the old route obsolete or remove it from active instructions;
5. do not leave two competing active routes without an explicit selection rule.

## New Chat Reading Rule

A new chat should not scan the entire project blindly.

After routing into the project:

1. read the project entrypoint;
2. read the project textbook;
3. read current state / latest work evidence only to the extent needed for the active task;
4. use the accepted solution already documented;
5. research again only when freshness, a gap, or a failure requires it.

## Anti-Bureaucracy Rule

The textbook exists to reduce rediscovery, not create documentation overhead.

Keep it solution-oriented.

Prefer one strong canonical textbook over many overlapping how-to notes.

Do not create a separate textbook per chat, phase, executor, or experiment.

## Final Rule

A project textbook describes **the ready solution we should use now**, not the story of how we arrived there.

A future executor should be able to read it and start from the project's current accumulated competence instead of starting from zero.
