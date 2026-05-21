# Workflow Decision Table

## Purpose

Use this table to decide how heavy the workflow should be.

Run the mode classifier first:

`docs/MODE_CLASSIFIER.md`

Default principle:

Full workflow is the reference model.

Compact mode is the default execution form.

Expand only when scope, risk, review, handoff, or reuse requires it.

## Decision Table

| Situation | Recommended mode | Typical artifacts | Codex default |
| --- | --- | --- | --- |
| Raw idea, no project yet | `brainstorm-only mode` | chat notes or optional lightweight artifact | no |
| New meaningful project | compact startup via `Start New Project.md` by default; full workflow only when justified | `00_INPUT.md` or the smallest useful startup artifact | maybe later |
| Small but durable project task | `compact mode` | one compact workflow record or a few targeted files | only if executor access is needed |
| Tiny safe task | `micro-task mode` | minimal artifact only when useful | no by default |
| Opinion, explanation, comparison, translation, or short answer | `discussion / answer-only` | answer only or optional tiny note | no |
| Research without project startup | `research-only` | research artifact only when useful | no by default |
| Existing old repo that does not match the standard | `legacy-project-normalization mode` | audit, mapping, migration artifacts | maybe |
| Narrow implementation or repo change with clear scope | `Codex handoff` or `Codex packet lite` | handoff packet, execution report, review artifact | yes |

## Selection Heuristic

Choose the lightest mode that still:
- preserves durable state when it matters;
- avoids fake execution claims;
- keeps the next action clear;
- supports review when the result will matter later.

If in doubt, start lighter and escalate only when the task proves it needs more structure.

## Standards-On-Demand Rule

Do not open deeper standards just because they exist.

Before loading a deeper standard, be able to name the reason:
- mode selection;
- handoff;
- research;
- review;
- memory;
- structure;
- graph navigation.

If no such reason exists yet, stay in the lighter mode.
