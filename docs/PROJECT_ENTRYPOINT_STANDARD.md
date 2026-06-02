# Project Entrypoint Standard

## Purpose

This standard defines the single entrypoint artifact for any specific project, regardless of whether that project lives primarily in `GitHub` or `Notion`.

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

Every meaningful project should have exactly one current project entrypoint.

That entrypoint is not the full history of the project.

It is the shortest reliable way to enter the project without re-deriving context from chat, memory, or guesswork.

## Canonical Forms

Use the same contract in two environment-specific forms:

- `GitHub / repository projects` -> `PROJECT.md`
- `Notion / workspace-first projects` -> `Project Entrypoint` page or top section

The medium may differ.

The contract should stay the same.

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

After reading the entrypoint, a new human or AI should be able to answer:

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

Every project entrypoint should include the following sections in compact form:

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

### 4. Current Status

Summarize:

- current mode;
- current phase or step;
- current health or confidence if relevant.

### 5. Done So Far

List only the most important completed work or milestones.

Do not turn this into a full chronology.

### 6. Current Focus

State what is actively being worked on now.

### 7. Next Practical Step

State the next useful action as clearly as possible.

This should be concrete enough that a new participant can continue without guessing.

### 8. Key Decisions And Constraints

Record only decisions and constraints that materially affect future work.

Examples:

- chosen tool or platform;
- forbidden scope;
- visibility or privacy rule;
- source-of-truth rule;
- review or handoff rule.
- `Existing Solution First` when the project must search for adequate existing solutions before custom work.

### 9. Read Next

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

## Environment-Specific Guidance

### GitHub Form

Use `PROJECT.md` in the repository root or project root.

This form should point to:

- `PROJECT_STATE.md`
- `PROJECT_RULES.md` if present
- latest workflow run
- latest project log

In initialization-only state, those deeper artifacts may legitimately not exist yet.

## Optional Deployment Metadata

If the project is deployable and static/frontend in nature, the entrypoint may include an optional deployment metadata block.

Record these fields when they are relevant:

- `deployment_provider`
- `github_repo`
- `production_branch`
- `build_command`
- `output_directory`
- `production_url`
- `preview_url`
- `custom_domain`
- `deployment_status`

If deployment is not set up yet, unknown values may remain explicit rather than guessed.

## Legacy Migration Rule

For repository projects:

- if `PROJECT.md` exists, use it as the canonical project entrypoint;
- if `PROJECT.md` is absent but `PROJECT_ENTRYPOINT.md` exists, treat `PROJECT_ENTRYPOINT.md` as a legacy name;
- read that legacy file temporarily;
- migrate it to `PROJECT.md` at the nearest safe opportunity;
- update project links and references during that migration;
- do not keep both `PROJECT.md` and `PROJECT_ENTRYPOINT.md` active at the same time.

### Notion Form

Use a page or top section called `Project Entrypoint`.

This form should point to:

- the project page itself;
- the current state block or status field;
- the relevant task or notes databases if they matter;
- the next working area to open.

In `Notion`, the entrypoint should usually sit near the top of the page so a new participant does not need to scroll through raw notes first.

## Maintenance Rule

Update the project entrypoint whenever one of these changes:

- the source of truth changes;
- the current mode changes;
- the current focus changes;
- the next practical step changes;
- a major decision changes what a new participant must know first.

If the project evolves but the entrypoint does not, re-entry cost rises and the entrypoint stops doing its job.

## Minimum Quality Standard

A good project entrypoint is:

- short;
- explicit;
- current;
- easy to scan;
- strong enough that a new human or AI can continue with minimal confusion.

It must also be honest about unknowns.

## Related Standards

- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/integrations/notion/README.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
