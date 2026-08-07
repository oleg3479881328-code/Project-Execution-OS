# External AI Task + Result Standard

## Purpose

This standard defines a reusable way to delegate substantial work to another AI without forcing the owner to shuttle text, files, partial results, and follow-up context back and forth between assistants.

The pattern is workspace-first:

1. create one durable task page;
2. create one durable result page;
3. put the exact result destination inside the task;
4. give the external AI one task link;
5. require the external AI to write results directly to the designated result page;
6. later review, verify, and continue from that same durable workspace.

This standard is project-agnostic and may be used across all projects.

## Core Pattern

```text
Owner / Primary AI
    -> creates TASK page
    -> creates RESULT page
    -> embeds RESULT destination in TASK
    -> gives only TASK link to external AI

External AI
    -> reads TASK
    -> performs work
    -> writes directly into RESULT page
    -> may create child pages only when the task explicitly permits it

Primary AI
    -> later opens RESULT page
    -> checks progress / quality / completeness
    -> records corrections or next task in the same durable workspace
```

## Default Workspace

When the project already has a canonical durable workspace, create both pages inside that project workspace.

For Notion-first projects, the default is:

- one page titled like `TASK — <short task name>`;
- one page titled like `RESULT — <short result name>` or a domain-specific persistent destination such as `MASTER CATALOG`;
- both pages live under the project’s canonical Notion area or a clearly linked child area.

Do not create task/result pages as disconnected private pages if the project already has a canonical parent.

## Task Page Contract

Every external-AI task page must contain enough information for a capable AI to execute without requiring the owner to relay additional context manually.

At minimum include:

1. **Goal** — what must be accomplished.
2. **Context** — only the project context needed for execution.
3. **Scope** — what is included and excluded.
4. **Method / constraints** — research depth, source rules, implementation rules, validation rules, etc.
5. **Required output structure** — table, report, code, catalog, checklist, artifacts, etc.
6. **Exact durable result destination** — page title + direct Notion URL.
7. **Write rule** — explicitly say to write the result directly there instead of returning the full result to the owner in chat.
8. **Child-page rule** — whether child pages are allowed and what must remain on the main result page.
9. **Completion marker** — how the external AI should indicate that the work is complete or still in progress.
10. **Source traceability** — where references, links, raw sources, or generated artifacts must be recorded.

## Result Page Contract

The result page is durable project memory, not a temporary inbox.

It should contain:

- a short purpose statement;
- a clear write rule;
- current status (`not started`, `in progress`, `complete`, or equivalent);
- the actual result or a compact index to child result pages;
- important sources and traceability;
- enough structure for the primary AI to review progress without asking the owner to copy anything back.

If the result becomes large, child pages are allowed, but the parent result page must retain:

- summary;
- status;
- index / links;
- key conclusions;
- remaining TODOs.

## Owner Handoff Rule

The owner should normally need to transfer only one thing to the external AI:

**the task-page link.**

Do not require the owner to separately send:

- a second result-page link;
- copied instructions;
- repeated project context;
- a result template already embedded in the task;
- manually relayed intermediate results.

The task page itself is the handoff packet.

## Review Rule

When the owner later asks whether there are results, the primary AI should:

1. open the designated result page directly;
2. inspect current content and child pages if needed;
3. report concrete progress;
4. distinguish finished work from TODO / partial work;
5. verify important claims when the review requires it;
6. avoid asking the owner to paste the external AI’s output if it already exists in the durable workspace.

## Reuse Across Projects

This pattern is not limited to research.

Use it when useful for:

- deep research;
- market scans;
- code audits;
- architecture reviews;
- content production;
- data extraction;
- document analysis;
- QA;
- design exploration;
- competitive analysis;
- catalog building;
- long-form drafting;
- test planning;
- implementation investigations;
- migration analysis;
- other substantial delegated work.

## When Not To Use It

Do not create this structure for trivial one-message tasks where a durable task/result workspace would add more overhead than value.

Do not use it when the external AI cannot access the designated workspace.

Do not treat chat as the canonical result location when a durable project workspace is available.

## Naming

Use clear names that are understandable without opening the page.

Examples:

```text
TASK — Deep Research — CAD and Creative Tools
RESULT — CAD and Creative Tools Research

TASK — Competitor Analysis — Local Wedding Video
RESULT — Competitor Analysis

TASK — Code Audit — Download Pipeline
RESULT — Download Pipeline Audit
```

For persistent accumulative destinations, a domain-specific name may be better than `RESULT`, for example:

```text
MASTER CATALOG — AI Program Interaction Research
RESEARCH LIBRARY — Competitors
QA REPORT — Release 0.4
```

## Final Rule

One durable task link should be enough to delegate the work.

The external AI writes into the durable result location named inside that task.

The primary AI later reviews the same result location directly.

The owner should not be used as a manual transport layer between AIs when a shared durable workspace can carry the task and result instead.
