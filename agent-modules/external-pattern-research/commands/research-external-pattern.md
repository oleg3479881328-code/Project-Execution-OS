---
description: Evaluate one specified external source as a possible donor pattern for one named existing system or project and issue one adoption decision.
argument-hint: "<source URL> for <target system or project>"
status: candidate
version: 0.1.0
---

# /research-external-pattern

## Purpose

Run a bounded evidence-based review of one external source and determine the smallest justified reuse action for an existing Oleg system or project.

## Usage

```text
/research-external-pattern <source URL> for <target system or project>
```

Equivalent natural-language requests count when the user clearly asks to analyze, adapt, adopt, borrow from, or evaluate a particular outside source for an existing system.

## Preconditions

Required before producing an adoption decision:

- a specific outside source, normally a URL or named repository/product;
- a specific existing target system/project or an unambiguous target from current context;
- access to enough primary evidence to inspect the source accurately;
- the current Project Execution OS route relevant to the request.

If the target is actually a new project, route to the new-project workflow rather than running this command as though the project already exists.

## Workflow

1. Read `START_HERE.md` and the smallest relevant internal standard.
2. Define the existing target need in one sentence.
3. Inspect the outside source using primary evidence first.
4. Extract verified structural or operational patterns.
5. Exclude product-specific baggage and unjustified complexity.
6. Compare the transferable pattern with current internal artifacts.
7. Choose exactly one decision:
   - `reject`
   - `preserve-reference`
   - `adapt-candidate`
   - `test-in-real-task`
   - `promote-reusable`
   - `handoff-implementation`
8. Perform a durable write only when requested or justified by an explicit promotion/recording instruction and when tool execution confirms it.

## Output Contract

Return:

- **Target need**
- **Verified source facts**
- **Patterns worth adapting**
- **What not to copy**
- **Decision** — exactly one allowed decision
- **Single next action**
- **Record state** — chat analysis only, reference recorded, candidate artifact created, tested, promoted, or implementation confirmed

## Stop Conditions

Stop and do not overbuild when:

- the source does not solve a real current need;
- a simple reference capture is sufficient;
- a candidate artifact exists but has not yet been tested;
- the selected donor already covers the MVP need and extra searching adds no decision value;
- implementation has not been approved or cannot be confirmed through execution evidence.

## Related Skills

- `external-pattern-evaluation`

## Validation Status

`candidate` — not yet validated by a new external source evaluation performed after module creation.
