# Project Memory Standard v2

## Purpose

This standard defines the universal durable-memory architecture for meaningful projects operating under Project Execution OS.

Its goal is to preserve complete recoverable project memory while allowing every AI/client to enter through one global `START_HERE.md`, navigate recursively, and load only the minimum context needed for the current task.

## Constitutional Rule

Chat is a temporary execution surface.

Durable project memory lives outside chat in explicit project artifacts and canonical connected sources.

Model memory, conversation history, ChatGPT Project files, and assistant summaries may help with orientation, but they never override canonical durable project memory.

## Global Entry Rule

Project memory does not begin with a project-specific ChatGPT pointer.

The AI/client entry sequence begins globally:

```text
stable client instruction, when available
→ Project Execution OS START_HERE.md
→ docs/ROUTER.md
→ zero or more child routers / registries / indexes
→ canonical project entrypoint
→ current project state and only task-relevant durable memory
```

There is no fixed maximum router depth.

A project-specific `PROJECT.md`, Notion `Project Entrypoint`, or equivalent durable page remains the project's canonical local front door after the routing tree selects that project. It is not a competing global AI entrypoint.

## ChatGPT Projects Rule

ChatGPT Project is an interface/work window, not a canonical memory layer.

If stable user/system instructions already guarantee entry through the global Project Execution OS `START_HERE.md`, no ChatGPT Project attachment is required.

If an interface attachment is useful or required, use the same generic `START_HERE.md` bootstrap defined by `docs/CHATGPT_PROJECT_START_HERE_TEMPLATE.md`. It points to the global Project Execution OS entrypoint, not directly to a project-specific memory tree.

Existing project-specific ChatGPT pointers created under the old contract do not require manual replacement. They are non-authoritative compatibility artifacts. Global `START_HERE.md`, the live router path, the selected canonical project entrypoint, and current durable evidence all outrank them.

Remove or replace a legacy attachment only during convenient maintenance or when it actively causes ambiguity.

## Durable File Artifact Rule

Any valuable file artifact produced or received during work must survive the chat session.

When a ZIP, export package, document, PDF, image, media file, design extract, evidence package, backup, snapshot, source bundle, migration package, or other file may be needed later, preserve a durable copy in Google Drive before treating it as safely retained.

Routing follows `docs/FILE_ORGANIZATION_STANDARD.md`:

- project-specific files -> that project's Google Drive folder tree;
- cross-project or system-wide reusable artifacts -> global `System Artifacts` folder;
- GitHub and Notion may remain canonical for code, structured text, decisions, and live documentation;
- valuable file artifacts must not exist only in chat, `/mnt/data`, or another temporary runtime.

## Universal Memory Layers

### L0 — Session Memory

Temporary working context inside the current chat, terminal, IDE, or executor session.

L0 is not durable project memory. Anything another executor may need later must be promoted before the work is considered safely preserved.

### L1 — Canonical Project Entrypoint

The shortest reliable durable front door into the selected project.

Canonical forms:

- repository-first project -> `PROJECT.md`;
- Notion-first project -> `Project Entrypoint` or `START HERE` page;
- another durable workspace -> one clearly identified equivalent.

L1 is reached through the global router tree. It routes; it does not contain the whole project.

Follow `docs/PROJECT_ENTRYPOINT_STANDARD.md`.

### L2 — Current Operational State

The minimum current state required to continue safely.

For repository projects after meaningful execution begins:

```text
PROJECT_STATE.md
logs/latest.md
```

For Notion-first projects, use equivalent current-state and work-log artifacts.

L2 answers what is happening now, what was completed, what remains, blockers, do-not-repeat work, and the next safe action.

Follow `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`.

### L3 — Durable Knowledge

Deeper reusable project knowledge opened only when relevant: standards, architecture, decisions, verified fixes, source trails, research, donors/templates, content indexes, schemas, contracts, archives, and other expensive-to-reconstruct knowledge.

L3 is modular. Do not force every project to create every category.

## Canonical Re-Entry Sequence

```text
1. global START_HERE.md
2. live router tree
3. selected canonical project entrypoint
4. current operational state when needed
5. latest work log/checkpoint when needed
6. only task-relevant durable knowledge
7. raw source material only when needed
```

A legacy interface pointer, if physically present, is not step 1 and must not bypass this sequence.

Do not begin by scanning the entire repository, Drive tree, Notion workspace, archive, or chat history.

## Recursive Collection Memory Rule

Large projects may contain their own routers, registries, or indexes. Use them recursively rather than flattening all project memory into `PROJECT.md`.

Examples:

```text
project
→ weddings router
→ one wedding
→ vendors router
→ one vendor dossier
```

or any hierarchy justified by the project's real structure.

Create child navigation only when scale or ambiguity justifies it. Do not create empty hierarchy for hypothetical future needs.

## Notion-First Project Rule

When Notion is the primary durable workspace:

- maintain one canonical project entrypoint;
- keep it compact and routing-focused;
- put detailed standards in linked pages;
- keep current status in a dedicated current-state block/page;
- keep reusable knowledge in narrow pages/databases;
- update the entrypoint when source-of-truth, routing, priorities, or required reading changes.

## Repository-First Project Rule

When GitHub or a local repository is the primary durable workspace:

- use `PROJECT.md` as canonical project entrypoint;
- use `PROJECT_STATE.md` and `logs/latest.md` after meaningful execution begins;
- keep detailed standards and reusable knowledge under appropriate durable paths;
- link external Notion, Drive, issue, PR, or source pages rather than duplicating them without need;
- keep source locations and stable identifiers recoverable.

## Source-Of-Truth Precedence

Each project entrypoint must make durable precedence unambiguous. A typical order is:

```text
1. confirmed working artifact or primary source
2. canonical project standard or decision
3. canonical project entrypoint
4. current project state
5. latest durable work log/checkpoint
6. current conversation
7. model memory
```

For AI entry/navigation, the global `START_HERE.md` and router tree determine which project artifacts to consult; they do not replace the project's own source-of-truth precedence once the project is selected.

## Promotion Rules

Promote information out of L0 when it is a confirmed reusable rule, architectural/product decision, verified error/fix, reusable donor/template/reference, reproducibility source, meaningful milestone, blocker/path change, expensive-to-reproduce result, next safe action, or do-not-repeat constraint.

Place it in the narrowest correct durable artifact. Do not dump entire conversations into project memory.

## Update Responsibility

After meaningful work, run the promotion gate in `docs/KNOWLEDGE_SYSTEM.md`, then update only the canonical artifact whose truth changed:

- `PROJECT.md` / Notion entrypoint when the project-level front door changed;
- `PROJECT_STATE.md` when current state or next action changed;
- `logs/latest.md` when meaningful execution/validation occurred;
- knowledge/decision/error/source records when reusable truth changed;
- Google Drive when a valuable file artifact must survive the session;
- router/registry/index when navigation topology changed.

Prefer updating an existing canonical artifact over creating a parallel one.

## Minimum Structures

### Zero-State Real Project

```text
PROJECT.md
AGENTS.md    # required for standalone external folders; optional for internal subprojects
```

### Active Repository Project

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

### Active Notion-First Project

```text
Project Entrypoint / START HERE
Current State
Current Work Log
linked task-relevant standards and knowledge
```

### ChatGPT Project Interface

No project-specific memory structure is required inside ChatGPT Projects.

Preferred:

```text
stable user/system instruction → global PEOS START_HERE.md
```

Optional compatibility bootstrap:

```text
generic START_HERE.md → global PEOS START_HERE.md
```

The actual project memory remains external and is selected through routing.

## Migration Snapshot Rule

A migration snapshot is a historical handoff artifact, not primary live state. Use it only when a major phase/executor/environment transition genuinely benefits from a frozen record.

Do not use ever-growing snapshots as a substitute for maintaining current state.

## Anti-Bureaucracy Rule

Do not:

- duplicate truth across multiple active files;
- maintain project-specific START HERE copies in every AI interface;
- manually replace harmless legacy ChatGPT attachments merely for architectural cleanliness;
- create empty databases/folders/routers for hypothetical needs;
- require all projects to use the same storage medium;
- preserve raw chat transcripts as project documentation;
- force a new executor to read the entire knowledge base.

Use one global AI door, one canonical project entrypoint per project, one current state, one current log, and only the deeper knowledge actually needed.

## Memory Health Test

A project passes when a new executor can, starting from global `START_HERE.md`:

1. route to the correct project without relying on hidden chat context;
2. identify the canonical source of truth;
3. understand purpose/current phase;
4. find completed work and next safe action;
5. identify constraints/do-not-repeat work;
6. open deeper knowledge only when relevant;
7. find valuable file artifacts in durable storage;
8. continue without asking the owner to reconstruct hidden context.

## Adoption Rule For Existing Projects

For an existing project:

1. identify its real current source of truth;
2. ensure exactly one canonical durable project entrypoint;
3. register or route to it from the appropriate router/index when central discovery is useful;
4. leave harmless legacy ChatGPT project pointers in place by default;
5. establish/repair current operational state;
6. link rather than duplicate standards and knowledge;
7. record precedence;
8. move valuable temporary/chat-only files to durable storage;
9. mark genuinely stale competing durable entrypoints;
10. run the memory health test.

Do not perform destructive migration merely to make interface attachments look uniform.

## Related Standards

- `START_HERE.md`
- `docs/ROUTER.md`
- `projects/ROUTER.md`
- `Start New Project.md`
- `docs/PROJECT_BOOTSTRAP_STANDARD.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/CHATGPT_PROJECT_START_HERE_TEMPLATE.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/FILE_ORGANIZATION_STANDARD.md`
- `docs/SOURCE_TRACEABILITY_STANDARD.md`

## Final Rule

Every meaningful project must have durable external memory, every valuable file artifact must survive the chat session, and every compatible AI should be able to enter through the one global `START_HERE.md`, recursively reach the correct project, and read only the minimum durable memory needed to act safely.