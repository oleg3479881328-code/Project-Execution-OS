# External AI Task + Result Standard

> Legacy filename retained for compatibility. This standard is workspace-neutral and applies to parallel ChatGPT worker chats and other AI executors across Project Execution OS.

## Purpose

This standard defines the global Project Execution OS pattern for delegating substantial independent work to another AI worker without blocking the primary conversation and without using Oleg as a manual transport layer for context or results.

The intended operating model is:

```text
Primary chat = Controller / Architect / Reviewer
Worker chats = temporary Executors
Durable workspace = shared state and source of truth
```

The primary chat may continue discussing, planning, reviewing, or creating additional work while one or more worker chats execute independent tasks in parallel.

## Core Invariant

Use this rule:

```text
One link in -> zero extra explanation -> full execution -> durable write-back -> concise human completion summary with result link -> later review.
```

When Oleg says words equivalent to `напиши задание воркеру`, create a self-contained durable task packet whenever a shared durable workspace is available.

Oleg should normally need to do only one manual action:

1. open another ChatGPT chat/tab;
2. send ONLY the task link.

The task URL itself is the complete launch command. The worker must not require Oleg to add `открой документ`, `работай по нему`, `RUN`, project context, or any explanatory text. The task packet must contain the execution contract needed to interpret a bare task URL as: open this exact durable task, read it fully, execute it, and write the substantive result back to the designated durable destination.

He should not need to copy instructions, repeat context, explain the task, relay intermediate results, or wait in the primary chat for the worker to finish.

## Parallel Work Model

The default multi-worker flow is:

```text
Oleg <-> Primary Chat / Controller
              |
              | creates self-contained task links
              v
       TASK A   TASK B   TASK C
          |        |        |
          v        v        v
      Worker A  Worker B  Worker C
          |        |        |
          +--------+--------+
                   |
                   v
            Durable Workspace
                   |
                   v
       Primary Chat / Reviewer
          PASS / FIX / BLOCK
```

Workers are temporary execution surfaces. The durable workspace carries the task, sources, state, outputs, logs, and reviewable result.

Deleting or losing a worker chat after successful write-back must not destroy the durable result.

## Main-Conversation Continuity Rule

Delegating a task to a worker must not unnecessarily block the primary conversation.

After the owner has the worker task link, the primary chat remains available for ongoing discussion and for creating additional tasks.

Do not structure ordinary delegated work around `send task -> wait for worker -> resume conversation` when the task is independent enough to run in parallel.

Prefer:

```text
discuss -> identify independent task -> create worker packet -> owner dispatches link -> continue main conversation
```

The owner may later say `проверь`, `проверь воркера`, or identify a task by name. The primary AI should then inspect the durable result directly and perform QA without asking Oleg to paste the worker output back into chat.

## Workspace-Neutral Rule

Do not assume Notion or Google Docs specifically.

Use the project's canonical durable workspace and the data format that naturally fits the task.

Possible durable locations include:

- Google Drive folders;
- Google Sheets databases and control tables;
- Google Docs for long-form task or result material when appropriate;
- Notion pages or databases;
- GitHub repositories, issues, PRs, files, or project artifacts;
- another canonical connected workspace explicitly used by the project.

For Google-Drive-first projects, treat Google Drive as the shared state layer. Google Sheets may hold structured databases and execution control, Drive folders may hold assets, and Docs may be used only where long-form text is actually useful.

The architecture must not depend on one file type.

## Task Packet Contract

Every worker task must be self-contained enough that a capable worker can execute it from the single task link without requiring extra explanation from Oleg.

The very top of each task packet must include a link-only execution contract stating that if the document URL is the only content sent in a fresh worker chat, the URL itself is the complete instruction to open, read, execute, and write back. No separate trigger text is required.

At minimum include:

1. **Task name** — clear human-readable name.
2. **Task / Job ID** — stable identifier when the workflow benefits from one.
3. **Goal** — what must be accomplished.
4. **Context** — only the context required for this task.
5. **Scope** — what is included and excluded.
6. **Sources** — exact durable files, tables, folders, URLs, records, or project nodes to inspect.
7. **Method / constraints** — research rules, existing-solution-first requirements, editing boundaries, validation rules, and do-not-repeat constraints.
8. **Write targets** — exact durable destinations to update.
9. **Entity-write rule** — when shared registries are involved, search before create and use update/upsert behavior where possible to avoid duplicates.
10. **Required output** — exact expected result shape.
11. **Completion / status rule** — how to mark complete, partial, blocked, or not ready.
12. **Execution trace** — what records, files, entities, sources, or artifacts were read or changed.
13. **QA readiness** — explicit marker such as `READY_FOR_QA: YES/NO` when useful.
14. **Fallback behavior** — what to do when evidence is missing or access fails; do not silently invent missing facts.
15. **Worker completion message rule** — after durable write-back, the worker must reply in chat with a brief human-readable summary of what was done, the key outcome/status in one or two sentences, and a clickable link to the durable result or primary artifact. A bare message such as `результат записан координатору`, `done`, or `completed` is not sufficient.

## One-Link Handoff Rule

The task link itself is the handoff packet AND the launch command.

Oleg should send only the URL in the fresh worker chat. No prefix, suffix, instruction, trigger token, or explanation is required.

Oleg should not be required to separately send:

- `открой этот документ`;
- `работай только по нему`;
- `RUN`;
- a result-page link;
- repeated project context;
- copied instructions;
- source lists already present in the task;
- output templates already present in the task;
- explanation of what the task means;
- manually relayed worker results.

If a worker would need those things, the task packet is incomplete.

## Task-Link Presentation Rule

Whenever the primary AI gives Oleg a worker-task link, the visible link text must be the clear task name in normal human language.

Do not give bare or ambiguous labels such as:

```text
ссылка
открыть
task
worker
Google Drive
документ
```

Prefer:

```text
[Проверить индексацию новых wedding pages](...)
[Оформить свадьбу Matt & Morgan к публикации](...)
[Провести аудит vendor entities для Wedding W023](...)
```

The owner must be able to recognize what a link will execute without opening it.

When multiple worker links are given together, each must have a distinct task-specific title.

## Worker Ownership and Parallel Safety

Parallel workers should own separate task targets whenever possible.

Examples:

- Worker A -> Wedding W023
- Worker B -> Wedding W024
- Worker C -> Wedding W025

Avoid two workers editing the same primary record simultaneously unless the task explicitly defines safe coordination.

For shared entity registries or databases:

```text
search -> existing entity? -> enrich/update
not found -> create
```

Do not default to blind creation when concurrent workers may encounter the same venue, vendor, person, organization, URL, or other entity.

When a shared write could create a collision, the task must either:

- define an upsert/search-before-create rule;
- assign one worker as owner of the shared record;
- write candidates to a staging area for later merge;
- or avoid that shared write during parallel execution.

## Result and Execution Report Contract

A worker must leave a durable, reviewable result rather than merely saying `done` in chat.

For substantial tasks, record enough execution state to support independent QA. A useful generic structure is:

```text
JOB_ID
TASK_NAME
STATUS
STARTED / FINISHED when available
SOURCES_READ
RECORDS_OR_FILES_CHANGED
ENTITIES_CREATED
ENTITIES_UPDATED
ARTIFACTS_CREATED
MISSING_EVIDENCE
BLOCKERS
READY_FOR_QA: YES/NO
```

Use only the fields relevant to the task; do not create bureaucracy for trivial work.

The result may live directly in the target database/file or in a dedicated result/log artifact. The exact shape should follow the project's natural workspace.

## Worker Completion Message Contract

After the durable result is saved, the worker must return a short completion message in the worker chat so Oleg can immediately understand what happened without opening the document first.

The completion message should normally contain exactly three things:

1. what was completed;
2. the most important result, verdict, or blocker in one or two short sentences;
3. a clearly named clickable link to the durable result or primary artifact.

Good example:

```text
Аудит завершён. Gego остаётся лучшим базовым вариантом, но локальный Windows-пилот требует Docker Desktop и проверки RAM под MongoDB/PostgreSQL/etcd.
[Результат — Gego Windows Local Deployment Audit](...)
```

Bad examples:

```text
Результат записан координатору.
Done.
Task completed.
Смотри документ.
```

The worker completion message is a convenience summary only. The durable workspace remains the source of truth.

## Controller / Reviewer Rule

When Oleg later asks to check a worker result, the primary AI should:

1. identify the task from its clear task name or Job ID;
2. open the durable task and result destinations directly;
3. inspect the actual changed state, not just a worker completion claim;
4. distinguish finished work from partial, blocked, or unverified work;
5. check compliance with the task acceptance criteria;
6. verify important factual or technical claims when appropriate;
7. check for duplicate or conflicting writes when shared registries were involved;
8. return a clear verdict such as `PASS`, `FIX`, or `BLOCK`;
9. if needed, prepare a bounded correction task for the same or another worker.

Do not ask Oleg to copy worker output back into the primary chat when the result already exists in the durable workspace.

## Relationship to Project Memory

This standard implements the Project Memory constitutional rule that chat is a temporary execution surface and durable state must live outside chat.

Worker chats are not project memory.

The project must remain recoverable from its canonical durable state even if all worker chats disappear.

Project memory, source-of-truth precedence, file persistence, and entrypoint rules continue to follow `docs/PROJECT_MEMORY_STANDARD.md` and related standards.

## Reuse Across Projects

Use this pattern when independent work can proceed while the primary conversation continues, including:

- research;
- audits;
- data enrichment;
- SEO and content production;
- wedding or event preparation;
- entity research;
- market scans;
- competitor analysis;
- document analysis;
- content drafting;
- catalog building;
- QA;
- test planning;
- implementation investigations;
- code review where the worker has the required access;
- migration analysis;
- repetitive independent batches;
- other substantial delegated work.

A single conversation may dispatch several workers when the tasks are independent enough to benefit from parallel execution.

## When Not To Use It

Do not create worker infrastructure for a trivial one-message task when delegation overhead is larger than the task.

Do not use a worker when it cannot access the required sources or durable write destination.

Do not parallelize tightly coupled work whose steps must occur sequentially unless explicit dependencies are encoded.

Do not rely on cross-chat memory as the only way a worker understands its task.

Do not treat worker chat output as canonical when a durable project workspace exists.

## Naming

Task names must be understandable without opening the task.

Good examples:

```text
TASK — Publish Wedding W023 — Matt & Morgan
TASK — Audit Cincinnati Venue Entity Duplicates
TASK — Research Zero-Click SEO Competitor Patterns
TASK — Verify Search Console Indexation After DNS Change
```

Avoid generic names such as:

```text
TASK 1
Worker task
Research
Do this
New task
```

## Adoption Direction

Project Execution OS is moving toward a controller + parallel worker operating model for suitable tasks.

The intended default is not to force every task through workers. The primary AI should identify work that is sufficiently independent, substantial, and parallelizable, then create a self-contained worker packet when the owner requests delegation.

Initial adoption may remain manually dispatched by Oleg through separate ChatGPT tabs. Automation of tab creation or orchestration is not required for the model to be valid.

The manual dispatch step is intentionally minimal:

```text
Primary AI creates task -> gives named link -> Oleg sends ONLY that link in another chat -> returns to primary conversation.
```

The system can later automate dispatch if a proven, low-friction mechanism becomes available, but manual one-link dispatch is the current acceptable baseline.

## Final Rule

The owner should be able to keep talking to the primary AI while independent workers execute elsewhere.

One clearly named durable task link — sent by itself — is enough to start each worker.

Workers write results back into shared durable state, then provide a concise completion summary with the result link in their chat.

The primary AI later reviews that durable state directly.

Oleg should not be used as the context shuttle, result shuttle, or waiting mechanism between AI sessions.
