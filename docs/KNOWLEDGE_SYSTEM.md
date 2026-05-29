# Knowledge System v2

## 1. Purpose

This document defines how Project Execution OS captures, reviews, promotes, activates, loads and retires reusable knowledge.

The goal is to prevent useful lessons from disappearing inside chats or one-off work without forcing every project into GitHub, ritual documentation or oversized AI context packages.

Layer selection follows `docs/PROJECT_LIFECYCLE_MODEL.md`.
Context loading follows `docs/CONTEXT_ASSEMBLY_STANDARD.md`.

## 2. Knowledge Layers

Project Execution OS uses three logical knowledge levels:

- raw reference or idea: potentially useful material not yet validated as reusable knowledge;
- project-specific knowledge: useful inside one project or one context;
- central reusable knowledge: reviewed value that should be reused across projects.

These are logical levels, not mandatory GitHub folder structures for every project.

## 3. Raw References And Ideas

Raw external references, notes, links, screenshots and outside solutions that should be preserved without being treated as active knowledge follow:

`docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`

The default external intake library is:

`oleg3479881328-code/Reference-Idea-Library`

Raw material is not an active system rule, skill, standard or implementation requirement merely because it was captured.

## 4. Project-Specific Knowledge

Store project-specific knowledge in the durable layer the project actually uses.

Examples:

- a Notion-managed project may store decisions, findings and local lessons in its Notion project space;
- a GitHub-backed technical project may store technical lessons near its versioned artifacts;
- a project with heavy source materials may link relevant Google Drive assets from its management layer.

Do not create a repository or a project-library folder merely because one useful note exists.

When a GitHub-backed project benefits from a local library, it may use a structure such as:

`project-library/`

or, for intentionally internal projects inside this repository:

`projects/<project-id>/project-library/`

These are optional patterns, not universal requirements.

## 5. Central Knowledge Library

Reviewed cross-project reusable knowledge for `Project Execution OS` lives in:

`knowledge-library/`

Purpose:

- store patterns reusable across projects;
- store anti-patterns;
- store workflow lessons;
- store architecture decisions;
- store research methods;
- store reusable execution standards;
- store verified technical solutions worth reusing.

## 6. Knowledge Lifecycle

Use this lifecycle when central reuse is being considered:

```text
captured -> researched -> candidate -> reviewed -> active -> deprecated / replaced
```

Meaning:

- `captured` = preserved so the material is not lost;
- `researched` = checked against evidence, sources or real use;
- `candidate` = plausible reusable value, but not yet active guidance;
- `reviewed` = evidence, scope and conflicts have been inspected;
- `active` = approved for reuse across relevant work;
- `deprecated` = preserved historically but no longer recommended;
- `replaced` = superseded by a newer active entry.

Do not silently treat `captured`, `researched` or `candidate` material as an active operating rule.

## 7. Promotion Rule

A project-specific lesson or external reference may be promoted to central knowledge only when:

1. it is useful beyond one project or one isolated event;
2. it does not contain irrelevant project-only noise or secrets;
3. it has clear reuse or adaptation guidance;
4. it has evidence appropriate to the active layer;
5. it has been reviewed before being treated as active system knowledge;
6. its scope limits and loading triggers are explicit enough for selective use.

Promotion does not require an `08_KNOWLEDGE_EXTRACT.md` file unless the work is already using a GitHub-backed workflow where that artifact is useful.

Do not create empty extraction artifacts by ritual.

## 8. Knowledge Entry Types

Allowed central entry types include:

- `pattern`;
- `anti-pattern`;
- `workflow-lesson`;
- `research-method`;
- `architecture-decision`;
- `execution-standard`;
- `verified-technical-solution`.

When stored in the GitHub-backed central library, useful category folders may include:

- `knowledge-library/patterns/`;
- `knowledge-library/anti-patterns/`;
- `knowledge-library/workflow-lessons/`;
- `knowledge-library/research-methods/`;
- `knowledge-library/architecture-decisions/`;
- `knowledge-library/execution-standards/`;
- `knowledge-library/verified-technical-solutions/`.

Do not create a category folder until an accepted entry needs it.

## 9. Distinguish Knowledge From Other Artifacts

Use these boundaries:

- `reference` = captured outside material or idea not yet accepted as reusable knowledge;
- `knowledge entry` = reviewed reusable pattern, lesson or solution;
- `standard` = mandatory operating rule for the system;
- `skill/plugin` = reusable executable or instruction-backed capability;
- `agent` = role-specific AI configuration or task module;
- `project artifact` = file, decision, evidence or output belonging primarily to one project.

Do not store one artifact type under another label merely because it is convenient.

## 10. General Reusable Knowledge Entry Format

A full central knowledge entry should include only the sections that materially help reuse:

- title;
- type;
- lifecycle status;
- source and evidence;
- problem;
- reusable pattern or lesson;
- `Applies To`;
- `Triggers`;
- `Do Not Load When`;
- `Related Standards`;
- when to use;
- when not to use;
- adaptation notes;
- risks;
- review status;
- `Replaced By` when deprecated or replaced.

Use the full form for cross-project standards, architecture lessons or material requiring context.

## 11. Compact Verified Technical Solution Format

For a narrow technical problem that has been successfully resolved and verified, use the compact format adapted from legacy knowledge-base experiments:

- Date or ID;
- Problem: the exact failure, issue or task;
- Investigation: what was checked and what evidence matters;
- Solution: the working fix or instruction;
- Verification: how the successful result was confirmed;
- Source links, logs or commit references when relevant;
- Reuse limits or risks when the solution is not universal;
- Applies To / Triggers when selective loading matters;
- Lifecycle status.

Use this format only for verified technical solutions, not for speculative ideas or untested guesses.

Before solving a repeated technical error from scratch, search existing verified technical solutions and relevant project evidence first.

## 12. Search Order For New Work

Use the lightest relevant search order:

1. current project state in its active durable layer;
2. project-specific evidence or prior solutions when present;
3. central knowledge library when the issue may repeat across projects;
4. relevant current repository evidence when a GitHub layer exists;
5. external open-source projects, official documentation and other public evidence when needed.

Do not read all knowledge stores by default when a small task does not need them.

## 13. Selective Loading Rule

Central reusable knowledge must be loaded into active AI context only when the current mode, project, task or trigger makes it relevant.

Before loading a knowledge entry, check:

1. Is the entry `active`, or is the current work explicitly research/review of a candidate?
2. Does its `Applies To` scope match the task?
3. Does a listed `Trigger` apply?
4. Does `Do Not Load When` exclude the current situation?
5. Is the entry still current, or has it been deprecated or replaced?

Do not load the entire `knowledge-library/` by default.

Selective context assembly follows `docs/CONTEXT_ASSEMBLY_STANDARD.md`.

## 14. Anti-Dump Rule

The knowledge library is not a dumping ground.

Do not store:

- random chat fragments;
- unreviewed opinions as active rules;
- duplicated entries;
- project-only details in central knowledge without reusable value;
- giant unreadable prompt blobs without structure;
- empty templates created merely to make the system look complete;
- stale entries that remain active after replacement.

## 15. Review And Activation

A central knowledge item becomes active only after appropriate review.

Before review it may exist as a candidate or draft when preserving it is useful.

Review should establish:

- that the evidence is real;
- that the lesson is reusable;
- that it does not conflict with current system rules;
- that any scope limits or risks are explicit;
- that loading triggers and exclusions are usable;
- that an older active entry is deprecated or replaced when necessary.

## 16. Related Nodes

- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `knowledge-library/README.md`

## Final Rule

Capture knowledge only when it has real future value.

Store it in the layer the project actually uses.

Promote it centrally only after review proves it is reusable.

Load it into active context only when it is relevant.