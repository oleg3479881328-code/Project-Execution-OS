# Project Entrypoint Standard

## Purpose

This standard defines the single entrypoint artifact for any specific project, regardless of whether that project lives primarily in `GitHub`, `Notion`, or another durable workspace.

The goal is simple:

Any human or AI entering a project should be able to read one short artifact and quickly understand:

- what this project is;
- why it exists;
- where the source of truth lives;
- what has already been done;
- what is happening now;
- what should happen next;
- which constraints or decisions already matter;
- where to read deeper only if needed.

## Core Rule

Every meaningful project should have exactly one current canonical project entrypoint.

That entrypoint is not the full history of the project.

It is the shortest reliable way to enter the project without re-deriving context from chat, memory, or guesswork.

If an interface such as ChatGPT Projects requires an attached local file, that file is not a second canonical entrypoint. It is a thin stable pointer to the canonical live entrypoint.

## Canonical Forms

Use the same contract in environment-specific forms:

- `GitHub / repository projects` -> `PROJECT.md`
- `Notion / workspace-first projects` -> `Project Entrypoint` or `START HERE` page
- `ChatGPT Project with external live project memory` -> attached `START_HERE.md` pointer only

The medium may differ.

The contract should stay the same.

## ChatGPT Project Attachment Standard

When a project is used inside ChatGPT Projects and the live project evolves in GitHub, Notion, Drive, or another durable external workspace, provide ChatGPT with exactly one stable attached entry file:

```text
START_HERE.md
```

This attached file must be a pointer, not a snapshot of project state.

It must contain only enough information to route the executor into the live project, including:

1. project identity;
2. the exact durable URL or path of the canonical live entrypoint;
3. the required re-entry sequence;
4. an instruction to follow the live router / current-state links rather than reconstructing state from chat;
5. source-of-truth precedence stating that the live project overrides the attachment, chat history, and model memory;
6. the Project Execution OS reference when applicable.

The pointer should normally remain unchanged for the lifetime of the project.

Project evolution must happen behind the pointer in the canonical live project memory.

Do not require the owner to re-upload or replace the ChatGPT Project attachment merely because project state, roadmap, research, architecture, tasks, or current focus changed.

Replace the attached pointer only when the canonical entrypoint location itself changes or the routing contract materially changes.

### Required Behavior After Attachment

Once the pointer file is attached to the ChatGPT Project:

```text
ChatGPT Project START_HERE.md
→ canonical live project entrypoint
→ project ROUTER, if present
→ current operational state
→ latest work log/checkpoint
→ only task-relevant durable knowledge
```

The assistant must not treat the attached pointer as the current project state.

The assistant must not ask the owner to paste migration context again when that context is recoverable through the canonical project memory.

The assistant must not create a fresh full START_HERE snapshot inside ChatGPT as a substitute for maintaining the live project.

## Initialization-Only Entrypoint

An entrypoint may honestly exist before the project purpose is known.

This initialization-only form is valid for a newly bootstrapped project and should not be treated as incomplete merely because some fields are still unknown.

In that zero state, the entrypoint should explicitly say:

- status: `initialized — purpose not yet defined`;
- type: `not yet classified`;
- purpose is not yet confirmed;
- architecture, stack, storage layers, scope, and implementation plan are not yet confirmed;
- no substantive implementation should begin yet;
- next practical step is to obtain the project purpose from the owner.

Unknown fields are allowed when they are truthful.

Invented fields are not allowed.

## Required Questions The Entrypoint Must Answer

After reading the canonical live entrypoint, a new human or AI should be able to answer:

1. What is this project?
2. Why does it exist?
3. What kind of project is it?
4. Where is the source of truth?
5. What has already been done?
6. What is the current state?
7. What is the next practical step?
8. Which decisions or constraints must not be ignored?
9. Where should I read next if I need deeper context?

If the entrypoint does not answer these clearly, it is incomplete.

## Required Sections

Every canonical live project entrypoint should include the following sections in compact form:

### 1. Project

- project name;
- short description;
- project type.

### 2. Purpose

- why the project exists;
- who it is for;
- what success looks like at the current stage.

If purpose is unknown, say so directly instead of guessing.

### 3. Source Of Truth

State clearly where durable truth lives.

Examples:

- `GitHub repository`
- `Notion project page`
- `GitHub repo for execution + Notion for readable workspace`

This section must remove ambiguity.

### 4. Source Trail

Follow `docs/SOURCE_TRACEABILITY_STANDARD.md`.

State where the underlying sources, references, uploaded files, raw packets, or research inputs can be opened again.

This section should include at least one recoverable pointer such as:

- source URL;
- Notion page URL;
- Google Drive file URL;
- GitHub repository path;
- attached file link;
- raw package path plus SHA256;
- source list with filenames and checksums.

If no durable external source exists yet, say so explicitly.

Do not imply that a source package is saved if the artifact only contains a summary.

### 5. Current Status

Summarize:

- current mode;
- current phase or step;
- current health or confidence if relevant.

### 6. Done So Far

List only the most important completed work or milestones.

Do not turn this into a full chronology.

### 7. Current Focus

State what is actively being worked on now.

### 8. Next Practical Step

State the next useful action as clearly as possible.

This should be concrete enough that a new participant can continue without guessing.

### 9. Key Decisions And Constraints

Record only decisions and constraints that materially affect future work.

Examples:

- chosen tool or platform;
- forbidden scope;
- visibility or privacy rule;
- source-of-truth rule;
- source-traceability rule;
- review or handoff rule;
- `Existing Solution First` when the project must search for adequate existing solutions before custom work.

### 10. Read Next

Point to the minimum deeper artifacts needed for deeper context.

Examples:

- `PROJECT_STATE.md`
- latest workflow run
- latest log
- relevant knowledge entry
- linked Notion database or subpage

In initialization-only state, those deeper artifacts may legitimately not exist yet.

## What The Entrypoint Must Not Become

The project entrypoint must not become:

- the full project history;
- the full rules document;
- a transcript dump;
- a research archive;
- a hidden second state file.

History belongs in logs, workflow runs, databases, or supporting pages.

Rules belong in project rules or system standards.

The entrypoint remains the front door.

A ChatGPT Project pointer must not become a duplicated live entrypoint.

## Environment-Specific Guidance

### GitHub Form

Use `PROJECT.md` in the repository root or project root.

This form should point to:

- `PROJECT_STATE.md`
- `PROJECT_RULES.md` if present
- latest workflow run
- latest project log
- source trail / raw input package when relevant

In initialization-only state, those deeper artifacts may legitimately not exist yet.

## Legacy Migration Rule

For repository projects:

- if `PROJECT.md` exists, use it as the canonical project entrypoint;
- if `PROJECT.md` is absent but `PROJECT_ENTRYPOINT.md` exists, treat `PROJECT_ENTRYPOINT.md` as a legacy name;
- read that legacy file temporarily;
- migrate it to `PROJECT.md` at the nearest safe opportunity;
- update project links and references during that migration;
- do not keep both `PROJECT.md` and `PROJECT_ENTRYPOINT.md` active at the same time.

### Notion Form

Use a page or top section called `Project Entrypoint` or `START HERE`.

This form should point to:

- the project page itself;
- the current state block or status field;
- the relevant task or notes databases if they matter;
- the next working area to open;
- the source trail / raw input package when relevant.

In `Notion`, the entrypoint should usually sit near the top of the page so a new participant does not need to scroll through raw notes first.

### ChatGPT Projects Form

If the project has external canonical memory, attach one `START_HERE.md` pointer file to the ChatGPT Project.

Do not attach a periodically regenerated full project snapshot as the entrypoint.

The file should be designed so the owner can attach it once and continue the project in future chats without repeating migration or replacing the file after ordinary project changes.

## Maintenance Rule

Update the canonical live project entrypoint whenever one of these changes:

- the source of truth changes;
- the source trail changes;
- the current mode changes;
- the current focus changes;
- the next practical step changes;
- a major decision changes what a new participant must know first.

Update a ChatGPT Project pointer only when its target or routing contract changes.

If the project evolves but the live entrypoint does not, re-entry cost rises and the entrypoint stops doing its job.

## Final Rule

One project has one live canonical front door.

Interface-specific files such as ChatGPT Project attachments are stable pointers to that front door, not competing copies of it.

A project entrypoint without a recoverable source trail is incomplete.