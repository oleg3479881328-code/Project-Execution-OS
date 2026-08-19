# Project Memory Standard

## Purpose

This standard defines the universal memory architecture for every meaningful project operating under Project Execution OS.

Its goal is to give every project durable, complete, and efficient memory without treating chat history or model memory as a source of truth.

A new human or AI executor should be able to enter a project, restore only the context needed for the current task, and continue safely without asking Oleg to reconstruct the project from memory.

## Constitutional Rule

Chat is a temporary execution surface.

Durable project memory must live outside chat in explicit project artifacts and canonical connected sources.

Model memory, conversation history, and previous assistant summaries may help with orientation, but they never override the canonical project memory.

## Durable File Artifact Rule

Any valuable file artifact produced or received during work must survive the chat session.

When a ZIP, export package, document, PDF, image, media file, design extract, evidence package, backup, snapshot, source bundle, migration package, or other file may be needed later, preserve a durable copy in Google Drive before treating it as safely retained.

This is a global Project Execution OS rule. It applies to every project and to meaningful non-project work.

Routing follows `docs/FILE_ORGANIZATION_STANDARD.md`:

- project-specific files -> that project's Google Drive folder tree;
- cross-project or system-wide reusable artifacts -> global `System Artifacts` folder;
- GitHub and Notion may remain canonical for code, structured text, decisions, and live documentation, but valuable file artifacts must not exist only in chat, `/mnt/data`, or another temporary runtime.

The executor performs this persistence proactively. The owner should not need to request it repeatedly.

## Universal Memory Layers

Every active project uses four logical layers.

### L0 — Session Memory

Temporary working context inside the current chat, terminal, IDE, or executor session.

L0 may contain:

- the current conversation;
- temporary reasoning;
- terminal output;
- draft changes;
- transient working notes.

L0 is not durable project memory.

Anything that another executor may need later must be promoted to a durable layer before the work is considered safely preserved.

### L1 — Project Entrypoint

The shortest reliable front door into the project.

Canonical forms:

- repository-first project: `PROJECT.md`;
- Notion-first project: `Project Entrypoint` or `START HERE` page;
- ChatGPT Project attachment: a thin pointer file that routes to the canonical entrypoint.

L1 must stay short. It routes; it does not contain the whole project.

Follow `docs/PROJECT_ENTRYPOINT_STANDARD.md`.

### L2 — Current Operational State

The minimum current state required to continue work safely.

For repository projects after the first meaningful execution step:

```text
PROJECT_STATE.md
logs/latest.md
```

For Notion-first projects, use an equivalent current-state page or block plus a current work log.

L2 answers:

- what is happening now;
- what has been completed;
- what remains;
- what is blocked;
- what must not be repeated;
- what the next safe action is.

Follow `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`.

### L3 — Durable Knowledge

Deeper reusable project knowledge, opened only when relevant.

Examples:

- standards and rules;
- architecture and decisions;
- known bugs and fixes;
- source trail and research;
- reusable donors and templates;
- content libraries and indexes;
- archives and publication history;
- schemas, contracts, and technical references;
- migration snapshots when a project needs historical handoff records.

L3 is modular. Do not force every project to create every category.

Create a durable knowledge artifact only when the information is reusable, expensive to reconstruct, or materially affects future work.

## Canonical Re-Entry Sequence

A new executor should restore context in this order:

```text
1. thin local pointer, if present
2. canonical project entrypoint
3. current operational state
4. latest work log or checkpoint
5. only the task-relevant durable knowledge
6. raw source material only when needed
```

Do not begin by scanning the entire repository, Notion workspace, archive, or chat history.

Use the minimum sufficient context rule.

## ChatGPT Project Pointer Rule

When a project uses the ChatGPT Projects interface and its live canonical entrypoint is stored elsewhere, the attached `START_HERE.md` must be a thin, stable pointer.

The pointer must state:

1. that it is not the canonical project memory;
2. the exact durable location of the canonical entrypoint;
3. that the canonical entrypoint must be read before project work;
4. that linked required sources must be opened as directed;
5. that the canonical source overrides the pointer, chat history, and model memory.

The pointer should normally remain unchanged.

Do not duplicate the full live entrypoint inside the ChatGPT Project attachment because the copy will become stale.

## Notion-First Project Rule

When Notion is the primary durable workspace:

- maintain one canonical `START HERE` or `Project Entrypoint` page;
- keep it compact and routing-focused;
- put detailed standards in separate linked pages;
- keep current status in a dedicated current-state block or page;
- keep reusable knowledge in narrow pages or databases;
- update the canonical page when routing, priorities, source-of-truth, or required reading changes.

The entrypoint must not grow into the entire knowledge base.

## Repository-First Project Rule

When GitHub or a local repository is the primary durable workspace:

- use `PROJECT.md` as the canonical project entrypoint;
- use `PROJECT_STATE.md` and `logs/latest.md` after meaningful execution begins;
- keep detailed standards and reusable knowledge under appropriate durable paths;
- link external Notion, Drive, issue, PR, or source pages rather than duplicating them without need;
- keep source locations and stable identifiers recoverable.

## Source-Of-Truth Precedence

Each project entrypoint must explicitly declare its precedence order.

A typical order is:

```text
1. confirmed working artifact or primary source
2. canonical project standard or decision
3. canonical project entrypoint
4. current project state
5. latest durable work log or checkpoint
6. current conversation
7. model memory
```

Projects may adapt this order, but ambiguity is not allowed.

## Promotion Rules

Promote information out of L0 when it is any of the following:

- a confirmed reusable rule;
- an architectural or product decision;
- a known error and verified fix;
- a reusable donor, template, or reference;
- a source location required for reproducibility;
- a meaningful completed milestone;
- a current blocker or changed execution path;
- a result that would be expensive to reproduce;
- a new next safe action;
- a do-not-repeat constraint.

Place it in the narrowest correct durable artifact.

Do not dump entire conversations into project memory.

## Update Responsibility

After every meaningful work step, the executor must determine whether to update:

- `PROJECT.md` or the Notion entrypoint — only when the front door changed;
- `PROJECT_STATE.md` or equivalent — when current state or next action changed;
- `logs/latest.md` or equivalent — when meaningful work or validation occurred;
- a durable knowledge artifact — when reusable knowledge was created;
- a decision or error record — when a confirmed decision or fix must survive;
- source trail — when new source material or provenance became relevant;
- Google Drive — when a valuable file artifact was created, received, exported, or changed and must survive the session.

The owner should not need to request a handoff or a Drive save manually for the project to remain recoverable.

## Minimum Structures

### Zero-State Real Project

```text
PROJECT.md
AGENTS.md    # required for standalone external folders; optional for internal subprojects
```

Do not create empty memory files before meaningful work exists.

### Active Repository Project

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

Add deeper memory only when justified.

### Active Notion-First Project

```text
START HERE or Project Entrypoint
Current State
Current Work Log
linked task-relevant standards and knowledge
```

### ChatGPT Project With External Canonical Memory

```text
START_HERE.md    # thin pointer only
external canonical entrypoint
external current state and durable knowledge
```

## Migration Snapshot Rule

A migration snapshot is a historical handoff artifact, not the primary live state.

Use it when:

- a major phase or executor transition needs a frozen record;
- the project crosses environments or systems;
- the active architecture changes materially;
- preserving an exact transition state has real value.

Do not use an ever-growing sequence of snapshots as a substitute for maintaining current state.

The latest live state remains canonical.

## Anti-Bureaucracy Rule

The purpose is reliable memory, not documentation volume.

Do not:

- duplicate the same truth across multiple active files;
- maintain a full START HERE copy in every interface;
- create empty databases or folders for hypothetical future needs;
- require all projects to use Notion when the repository is sufficient;
- require all projects to use GitHub when Notion is the natural source of truth;
- preserve raw chat transcripts as project documentation;
- force a new executor to read the entire knowledge base before starting.

Use one front door, one current state, one current log, and only the deeper knowledge the project actually needs.

## Memory Health Test

A project passes the memory health test when a new executor can:

1. identify the canonical source of truth;
2. understand the project purpose and current phase;
3. find what has already been completed;
4. find the next safe action;
5. identify key constraints and do-not-repeat work;
6. open deeper standards or sources only when relevant;
7. find valuable file artifacts in durable storage without relying on old chats or temporary runtimes;
8. continue without asking Oleg to reconstruct hidden context.

If this requires reading old chats or relying on model memory, the project memory is incomplete.

## Adoption Rule For Existing Projects

For an existing project:

1. identify its real current source of truth;
2. choose exactly one canonical entrypoint;
3. replace duplicate attached START HERE copies with thin pointers when appropriate;
4. establish or repair current operational state;
5. link, do not duplicate, existing standards and knowledge;
6. record the precedence order;
7. move valuable file artifacts out of temporary/chat-only storage into their correct Google Drive location;
8. remove or clearly mark stale competing entrypoints;
9. run the memory health test.

Do not perform a destructive migration without confirming which existing artifacts are still authoritative.

## Related Standards

- `Start New Project.md`
- `docs/PROJECT_BOOTSTRAP_STANDARD.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/FILE_ORGANIZATION_STANDARD.md`
- `docs/SOURCE_TRACEABILITY_STANDARD.md`

## Final Rule

Every meaningful project must have durable memory, and every valuable file artifact must survive the chat session in durable storage, but every executor should read only the minimum durable memory needed to act safely.
