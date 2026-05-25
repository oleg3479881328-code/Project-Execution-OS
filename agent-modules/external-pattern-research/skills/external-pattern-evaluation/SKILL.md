---
name: external-pattern-evaluation
description: Evaluate an external repository, product, public workflow, plugin collection, skill format, architecture pattern, or open-source solution when Oleg wants to know whether it is useful for an existing system or project and what should be adapted, captured, tested, promoted, or rejected.
status: candidate
version: 0.1.0
scope: external donor-pattern evaluation for existing projects and reusable system capabilities
---

# External Pattern Evaluation

## Purpose

Turn a promising outside source into a grounded reuse decision without copying blindly or creating architecture that has not earned its place.

## Use When

Use this skill when the task includes both:

1. a concrete external source or named outside solution; and
2. a question about usefulness, adaptation, integration, promotion, or reuse in an existing Oleg system/project.

Typical matches:

- “Analyze whether this GitHub repository is useful for our system.”
- “Find strong patterns in this open-source project and adapt them for our workflow.”
- “Should we use this skill/plugin architecture in Project Execution OS?”
- “Study this product and determine what can speed up our MVP.”

## Do Not Use When

Do not use this skill for:

- general explanations with no reuse/adoption decision;
- new project intake where the OS startup route applies;
- implementation of an already-decided change;
- superficial collection of links with no analysis;
- endless comparison after an adequate donor is already identified for a working MVP.

## Inputs Required

Required:

- source URL or clearly identified external source;
- named target system/project, or enough current context to identify the target accurately;
- desired decision type: understand, preserve, adapt, promote, implement, or reject.

Retrieve before deciding:

- relevant Project Execution OS route and standard for this type of work;
- current target-project entrypoint/state when the adoption decision affects a specific existing project;
- primary evidence from the external source itself;
- current public documentation or repository artifacts when the outside source may have changed.

## Workflow

### 1. Route Correctly

Read `START_HERE.md` and follow the smallest matching Project Execution OS node.

Route examples:

- interesting donor not yet promoted: reference capture route;
- actual research/evaluation: research standard route;
- candidate internal standard decision: relevant lifecycle/reusable knowledge route;
- already decided implementation: Codex handoff route.

### 2. Define the Target Need

State the specific target problem before judging the donor:

- what existing system or project would benefit;
- what problem or missing capability is being addressed;
- what smallest useful adoption decision is needed now.

Do not evaluate a donor as “good in general.” Evaluate whether it solves a real current need.

### 3. Inspect Primary Evidence

Inspect the external source directly. Focus on evidence that can support an adoption decision:

- actual file structure;
- real workflows;
- documented interfaces/configuration;
- commands, skills, templates, examples, tests, or contracts;
- license/release constraints only when publication, redistribution, or commercialization becomes relevant.

Prefer exact source artifacts over marketing claims or summaries.

### 4. Extract Transferable Patterns

Separate:

- **Source fact** — what exists in the external source;
- **Transferable pattern** — the underlying structural idea worth adapting;
- **Non-transferable baggage** — product-specific assumptions, unneeded complexity, branding, connector choices, or runtime architecture not justified for Oleg's system.

### 5. Compare Against Current System

Determine whether the pattern:

- already exists internally;
- fills a real gap;
- replaces a weaker existing approach;
- would create duplication or unnecessary architecture;
- can be adopted as a small file/document change first;
- requires later execution or runtime change.

### 6. Make One Decision

Choose one outcome:

- `reject` — no useful fit or cost exceeds value;
- `preserve-reference` — useful enough not to lose, but not ready for internal promotion;
- `adapt-candidate` — worth drafting as a candidate pattern/standard/module;
- `test-in-real-task` — draft exists; next step is one bounded real-use validation;
- `promote-reusable` — tested evidence justifies reusable internal status;
- `handoff-implementation` — decision is already clear and bounded execution is justified.

Do not blur these stages.

### 7. Record Only at the Right Layer

Use the correct durable layer only after the appropriate decision:

- external reference intake -> `Reference-Idea-Library`;
- reusable approved technical/operating pattern -> `Project Execution OS` or its CKL according to current rules;
- specific project adoption -> that project's durable source of truth;
- implementation action -> Codex/GitHub handoff and execution evidence.

## Output Contract

Provide a compact evaluation containing:

1. **Target need** — the existing problem/capability being addressed.
2. **Source facts** — only confirmed evidence from the donor source.
3. **Reusable patterns** — the parts worth adapting.
4. **What not to copy** — unnecessary or unsafe baggage.
5. **Decision** — exactly one outcome from the allowed decision list.
6. **Single next action** — the smallest action justified now.
7. **Durable record status** — not recorded, recorded reference, candidate artifact created, tested, promoted, or execution confirmed.

## Constraints and Stop Conditions

- Never claim a file, commit, setting, or project change was saved without explicit execution confirmation.
- Never treat a reference capture as a binding internal standard.
- Never treat a candidate artifact as a tested skill or promoted rule.
- Never invent external source content; inspect it or state the limitation.
- Stop donor research when one viable source already solves the immediate MVP need sufficiently.
- Do not design new runtime infrastructure unless a tested real-use problem requires it.
- Do not spend Codex execution work on open-ended evaluation that ChatGPT can finish directly.

## Evidence / References

Structural source pattern:

- https://github.com/anthropics/knowledge-work-plugins

Internal governing artifacts:

- `START_HERE.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/AGENT_MODULE_FORMAT_STANDARD.md`

## Validation Status

`candidate` — generated from a confirmed repeated workflow and the Anthropic file-module pattern, but not yet validated on a new external source after creation.
