# Knowledge System v4

## 1. Purpose

This document defines how Project Execution OS captures, searches, reuses, improves, promotes, activates, loads and retires durable knowledge.

The goal is to make useful knowledge a normal by-product of work instead of an optional documentation task after work.

This standard adapts the mature Knowledge-Centered Service (KCS) pattern to Project Execution OS: reuse existing knowledge while solving, improve it in context, capture missing knowledge in the flow of work, and use a final promotion check as a safety net.

Layer selection follows `docs/PROJECT_LIFECYCLE_MODEL.md`.
Context loading follows `docs/CONTEXT_ASSEMBLY_STANDARD.md`.
Explicit owner preservation requests follow `docs/AUTOMATIC_CAPTURE_STANDARD.md`.

## 2. Constitutional Rule

Useful durable knowledge must not remain only in chat, model memory, terminal scrollback, or one executor's head.

Knowledge work is part of execution, not an optional follow-up activity.

For meaningful work, the executor owns both:

1. solving the active problem;
2. leaving behind the narrowest useful durable knowledge or state that prevents avoidable rework.

A chat answer alone is not durable capture.

## 3. Knowledge-In-The-Flow Solve Loop

For meaningful work, use this loop whenever existing knowledge or reusable learning may matter:

```text
understand the request
-> search early for existing project/system knowledge
-> reuse the best current canonical knowledge when applicable
-> improve or correct that knowledge in place when real use exposes a gap
-> capture new durable knowledge during the work when it would be costly or risky to reconstruct later
-> structure it in the narrowest correct existing artifact
-> continue execution
-> run the final promotion/completion gate before declaring meaningful work complete
```

The loop is intentionally lightweight. Do not perform a broad knowledge search for trivial work that clearly has no reusable context.

### Search Early, Search Often

Before solving a repeated, risky, expensive-to-reconstruct, or system-sensitive problem from scratch:

1. inspect the active project state and project-specific knowledge;
2. inspect the relevant central standard/knowledge route when cross-project reuse is plausible;
3. reuse a current canonical solution when it applies;
4. go external only when internal knowledge is absent, stale, uncertain, or insufficient.

This is compatible with `Existing Solution First`: existing internal knowledge is itself an existing solution and must be checked before reinvention.

### Reuse Is Review

When an executor actually uses a knowledge artifact, that use is also a review opportunity.

If the artifact is correct and sufficient, reuse it without ritual editing.

If real work proves that it is incomplete, stale, ambiguous, misleading, or missing an important constraint, update or flag the canonical artifact during the same work while the context is still fresh.

Do not knowingly reuse a defective instruction and leave it defective for the next executor.

### Capture In The Moment

Do not wait until the final answer when an important fact, verified failure/fix, decision, blocker, source, benchmark result, or do-not-repeat lesson emerges during a long or multi-phase task.

Preserve it when the reconstruction risk becomes material.

Examples:

- a verified fix is found after a costly investigation;
- a source-of-truth location is discovered;
- a wrong route or stale assumption is disproven;
- a benchmark establishes a reusable result;
- an architectural decision changes future execution;
- a failure mode could cause another executor to repeat expensive work;
- an interim result is valuable even if the larger task later fails.

For current-state continuity, also follow `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`.

## 4. Knowledge Layers

Project Execution OS uses three logical knowledge levels:

- raw reference or idea: potentially useful material not yet validated as reusable knowledge;
- project-specific knowledge: useful inside one project or one context;
- central reusable knowledge: reviewed value that should be reused across projects.

These are logical levels, not mandatory folder structures.

## 5. Raw References And Ideas

Raw external references, notes, links, screenshots and outside solutions that should be preserved without being treated as active knowledge follow:

`docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`

The default external intake library is:

`oleg3479881328-code/Reference-Idea-Library`

Captured material does not become an active rule merely because it was saved.

## 6. Project-Specific Knowledge

Store project-specific knowledge in the durable layer the project actually uses.

Examples:

- Notion-managed project -> decisions, findings and local lessons in its project space;
- GitHub-backed technical project -> technical lessons near versioned artifacts;
- source-heavy project -> durable source assets in Google Drive linked from the management layer.

Do not create a repository or knowledge folder merely because one useful note exists.

## 7. Central Knowledge Library

Reviewed cross-project reusable knowledge for Project Execution OS lives in:

`knowledge-library/`

Use it for reusable patterns, anti-patterns, workflow lessons, architecture decisions, research methods, execution standards, and verified technical solutions.

## 8. Knowledge Lifecycle

When central reuse is being considered:

```text
captured -> researched -> candidate -> reviewed -> active -> deprecated / replaced
```

- `captured` = preserved so it is not lost;
- `researched` = checked against evidence, sources or real use;
- `candidate` = plausible reusable value, not yet active guidance;
- `reviewed` = evidence, scope and conflicts inspected;
- `active` = approved for reuse;
- `deprecated` = historical but no longer recommended;
- `replaced` = superseded by a newer active entry.

Do not silently treat `captured`, `researched` or `candidate` material as active operating truth.

## 9. Final Promotion / Completion Gate

The Solve Loop captures and improves knowledge during execution. The final gate is the safety net that prevents useful knowledge from being stranded at completion.

Before declaring any meaningful work complete, the executor must answer:

```text
Did this work create or change anything another executor, future task, project, or system decision may need?
```

If no, finish without documentation ceremony.

If yes, the work is not fully complete until the relevant durable artifact is updated or the preservation failure is explicitly reported.

Classify before creating anything new:

- current project fact, completion state, blocker, next action -> current state / current log;
- project-specific decision -> existing decision record or equivalent;
- durable architecture decision -> ADR-style artifact or existing architecture record;
- verified failure plus verified fix -> verified solution / known-fix entry / narrow runbook;
- repeatable operational procedure -> SOP / runbook / checklist / playbook;
- reusable pattern or lesson -> project knowledge first; central knowledge when cross-project value is supported;
- mandatory future rule -> update an existing standard first; create a new one only if ownership is genuinely distinct;
- reusable executable/instruction-backed behavior -> existing skill/capability path;
- raw donor/article/unverified idea -> reference capture, not active knowledge;
- valuable file artifact -> durable Drive/storage path under `docs/FILE_ORGANIZATION_STANDARD.md`.

### Hard Completion Rule

For meaningful work, `done` means both:

```text
execution result handled
AND
knowledge/state preservation gate handled
```

Do not report meaningful work as fully complete while knowingly leaving a reusable verified fix, important decision, do-not-repeat lesson, material state change, or expensive-to-reconstruct evidence only in session context.

If durable storage is unavailable, say that preservation remains incomplete instead of claiming full completion.

The owner should not need to remember to say `save this`, `make a standard`, or `do not forget this`.

## 10. Existing Artifact First

Before creating a new standard, knowledge file, runbook, checklist, ADR, skill, or project memory artifact:

1. search the current project for an artifact that already owns the subject;
2. search central Project Execution OS standards/knowledge when cross-project reuse is plausible;
3. update the existing canonical artifact when it can absorb the learning cleanly;
4. create a new artifact only when responsibility is genuinely distinct.

Do not create parallel truth.

## 11. Promotion Selection Rule

Do not use a mechanical repetition threshold such as `the second occurrence becomes a standard`.

Promotion depends on evidence, reuse value, scope, risk and stability.

A single high-cost incident may justify immediate durable capture. A frequently repeated local behavior may still belong only in a project runbook.

## 12. Standard Promotion Threshold

Promote a rule to a mandatory standard only when all are true:

1. stable enough to govern future work;
2. scope broader than one isolated incident;
3. violation creates meaningful quality, safety, continuity, or execution risk;
4. evidence or successful use supports it;
5. no current standard already owns the rule cleanly.

A successful one-off technique is not automatically a standard.

## 13. Central Promotion Rule

Project-specific knowledge or an external reference may be promoted centrally only when:

1. useful beyond one isolated project/event;
2. stripped of irrelevant project-only noise and secrets;
3. clear reuse/adaptation guidance exists;
4. evidence is appropriate to the active layer;
5. it has been reviewed before becoming active system knowledge;
6. scope limits and loading triggers are explicit enough for selective use.

## 14. Knowledge Entry Types

Allowed central entry types include:

- `pattern`;
- `anti-pattern`;
- `workflow-lesson`;
- `research-method`;
- `architecture-decision`;
- `execution-standard`;
- `verified-technical-solution`.

Useful folders may include corresponding paths under `knowledge-library/`, but do not create empty category folders by ritual.

## 15. Distinguish Knowledge From Other Artifacts

- `reference` = captured outside material or idea not yet accepted as reusable knowledge;
- `knowledge entry` = reviewed reusable pattern, lesson or solution;
- `standard` = mandatory operating rule;
- `skill/plugin` = reusable executable or instruction-backed capability;
- `agent` = role-specific AI configuration/task module;
- `project artifact` = evidence/output belonging primarily to one project.

Do not store one artifact type under another label merely for convenience.

## 16. Reusable Knowledge Entry Structure

Use only sections that materially help reuse:

- title;
- type;
- lifecycle status;
- source/evidence;
- problem/context;
- reusable pattern/solution;
- `Applies To`;
- `Triggers`;
- `Do Not Load When`;
- related standards;
- adaptation notes;
- risks;
- verification/review status;
- `Replaced By` when applicable.

Keep structure simple enough that capture can occur during real work.

## 17. Compact Verified Technical Solution

For a narrow successfully resolved technical problem:

- Date or ID;
- Problem;
- Investigation/evidence;
- Solution;
- Verification;
- Source links/logs/commit references when relevant;
- Reuse limits/risks;
- Applies To / Triggers when useful;
- Lifecycle status.

Do not use this format for guesses or untested fixes.

Before solving a repeated technical error from scratch, search existing verified solutions and project evidence first.

## 18. Search Order For New Work

Use the lightest relevant order:

1. current project state;
2. project-specific prior solutions/evidence;
3. central knowledge/standards when reuse is plausible;
4. current repository evidence when applicable;
5. external official/open-source/public evidence when internal knowledge is absent or insufficient.

Do not scan every knowledge store by default.

## 19. Selective Loading Rule

Load central knowledge only when the current mode/project/task/trigger makes it relevant.

Before loading an entry, check status, scope, triggers, exclusions, and whether it has been replaced.

Follow `docs/CONTEXT_ASSEMBLY_STANDARD.md`.

## 20. Evolve Loop — Knowledge Health

Individual work uses the Solve Loop. Periodically, repeated Solve Loop evidence should improve the system itself.

Review aggregated patterns when there is enough evidence to justify it:

- repeated searches with no good result -> knowledge gap;
- repeated reuse of the same entry -> candidate for stronger routing, standardization, skill/capability extraction, or better indexing;
- repeated corrections to one entry -> quality or scope problem;
- many near-duplicate entries -> consolidation problem;
- frequently ignored/stale entries -> deprecation or routing problem;
- repeated incidents despite an existing standard -> enforcement/discoverability problem, not automatically a need for another standard.

Use this evidence to improve content health, routing, standards, tools, skills and workflow integration.

Do not create metrics or review ceremonies until they support a real decision.

## 21. Anti-Dump / Anti-Bureaucracy Rule

Do not store random chat fragments, unreviewed opinions as active rules, duplicates, giant prompt blobs, project-only noise in central knowledge, empty templates, or stale active entries.

Do not force documentation where no future value exists.

The goal is less repeated thinking and fewer repeated mistakes, not more files.

## 22. Review And Activation

Before central knowledge becomes active, establish that:

- evidence is real;
- the lesson is reusable;
- it does not conflict with current rules;
- scope limits/risks are explicit;
- triggers/exclusions are usable;
- superseded material is deprecated or replaced.

## 23. Related Nodes

- `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `docs/PROJECT_MEMORY_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `knowledge-library/README.md`

## 24. External Pattern Adopted

This standard intentionally adapts the Knowledge-Centered Service (KCS) operating pattern from the Consortium for Service Innovation, especially:

- knowledge as a by-product of interaction;
- search early, search often;
- reuse existing knowledge before recreating it;
- reuse is review;
- capture and improve in the workflow, while context is fresh;
- structure for reuse;
- use aggregated reuse/gap evidence to improve the knowledge system over time.

KCS is used as a donor pattern, not copied as an organizational bureaucracy. Project Execution OS keeps its own artifact types, routing, lifecycle and storage boundaries.

## Final Rule

Search before reinventing.

Reuse and review what already exists.

Capture or improve durable knowledge while solving when reconstruction risk is material.

Before meaningful work is called complete, verify that no valuable decision, fix, lesson, state change or evidence is stranded only in session context.

Store the result in the narrowest correct canonical artifact and load it again only when relevant.