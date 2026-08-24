# Worker Chat Naming Standard

## Purpose

This standard defines the canonical naming rule for all delegated worker tasks across Project Execution OS.

The goal is to make every worker chat, durable task packet, result artifact, and controller review immediately recognizable by the same stable task identity.

## Canonical Format

Every worker task must use exactly this naming pattern:

```text
TASK <number> — <clear human-readable task name>
```

Example:

```text
TASK 16 — Tusia Unresolved Weddings Identity Resolution
```

## Mandatory Identity Equality Rule

For every worker task, the following values must be identical character-for-character except where a platform does not permit control of its UI-generated chat title:

1. GitHub Issue / durable task title;
2. first heading in the task packet;
3. `WORKER CHAT TITLE` value;
4. visible task-link label given to Oleg;
5. worker execution report task name;
6. worker completion message task reference;
7. controller review task reference.

Canonical identity:

```text
TASK <number> — <task name>
```

Workers and controllers must not invent shortened, alternative, translated, decorative, or paraphrased task names.

## Worker Chat Title Rule

The required worker chat title is the canonical task identity:

```text
TASK <number> — <task name>
```

If the ChatGPT/interface environment gives the worker a capability to rename the chat, the worker must rename it to that exact title before or at the start of execution.

If the platform automatically generates the chat title and the worker cannot control or rename it, that is a UI limitation rather than permission to redefine the task identity. In that case:

- all durable artifacts must still use the canonical title;
- the first substantive worker reply should begin with or clearly reference the canonical task title;
- the execution report must use the canonical task title;
- the worker must not introduce another task name as an alternative identity.

The system must never depend on an automatically generated chat title as canonical state.

## Controller Task-Creation Rule

Before issuing a worker task, the controller must:

1. determine the next valid TASK number;
2. create one clear human-readable task name;
3. build the canonical identity `TASK <number> — <task name>`;
4. use that exact identity everywhere listed in the Mandatory Identity Equality Rule;
5. include `WORKER CHAT TITLE: TASK <number> — <task name>` near the top of the task packet;
6. give Oleg a clickable link whose visible label is the same canonical identity.

Do not issue a worker task with inconsistent titles.

## Parallel Worker Rule

When several tasks are dispatched in parallel, each must have a unique TASK number and unique canonical title.

Example:

```text
TASK 16 — Tusia Unresolved Weddings Identity Resolution
TASK 17 — Tusia Venue & Vendor Reverse Search
TASK 18 — Tusia Reddit & Community Wedding Discovery
```

Do not use names such as:

```text
Research task
Worker 2
Tusia research
Wedding search
New task
```

## Completion Rule

Worker completion should identify itself with the canonical task identity and then provide the result.

Preferred form:

```text
TASK 16 — Tusia Unresolved Weddings Identity Resolution — completed.
<one-sentence result>
[Execution report](...)
```

The durable result remains the source of truth.

## Relationship to Other Standards

This standard supplements:

- `docs/EXTERNAL_AI_NOTION_TASK_RESULT_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/PROJECT_MEMORY_STANDARD.md`

Where naming guidance conflicts, this standard controls worker-task identity and worker-chat naming.

## Final Rule

One task has one canonical identity.

```text
TASK <number> — <task name>
```

Use it everywhere. Do not paraphrase it. If the UI-generated chat title cannot be controlled, preserve the canonical identity in every controllable task and result surface.