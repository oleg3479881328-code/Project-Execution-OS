# Command `03` — START_HERE Topic Lookup Standard

## Purpose

`03` is a universal shorthand command for explicit re-entry into `Project Execution OS`.

Use it when the owner wants the active agent to stop relying on chat memory or ad hoc explanation and immediately consult the repository rules for the current topic.

## Meaning

`03` means:

```text
open START_HERE.md
→ open the live router named there
→ identify the active topic from the current conversation
→ follow the narrowest relevant route
→ read only the minimum required internal nodes
→ answer or continue the active work from repository rules
```

## Core Rule

Do not ask the owner to restate where the relevant rule, library, block, database, project entrypoint, or workflow is stored when the answer can be found by following `START_HERE.md` and the live router.

Do not replace repository rules with chat memory, prior assumptions, or improvised workflow.

## Topic Resolution

When the owner sends only:

```text
03
```

infer the active topic from the immediately preceding conversation context.

When the owner sends:

```text
03 <topic>
```

use the supplied topic as the lookup target.

Examples:

```text
03 библиотека промптов
03 аренда GPU-сервера
03 сохранить идею
03 QuizLight
```

## Required Behavior

1. Fetch and read `START_HERE.md`.
2. Open `docs/ROUTER.md` from the route named in `START_HERE.md`.
3. Select the smallest relevant internal route for the active topic.
4. Read the minimum required repository nodes.
5. Continue the active request without making the owner repeat system instructions already stored in the repository.
6. State briefly what route was used when that helps the owner verify the result.

## Boundary

`03` is not:

- a request to read every repository file;
- a substitute for destructive-action approval;
- a blanket authorization to modify repositories, publish externally, deploy to production, or perform irreversible migration;
- a replacement for `01` or `02` communication-channel commands.

`03` controls repository lookup and OS re-entry only.

## Relationship to Automatic Routing

Project-related work should already enter through `START_HERE.md` automatically.

`03` is the owner's explicit override and recovery command when the agent appears to be operating from memory, guesses, or an incomplete route.

## Final Rule

When `03` is invoked, go back through the stable door, follow the live map, find the repository rule for the active topic, and proceed from that rule without asking the owner to explain the system again.
