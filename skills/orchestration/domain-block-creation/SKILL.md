---
name: domain-block-creation
description: Convert a recurring cross-project domain into a right-sized reusable Project Execution OS block with research, routing, knowledge capture, indexing, and validation.
category: orchestration
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - domain_request
  - expected_reuse_scope
  - existing_repository_context
  - current_router
  - relevant_sources
outputs:
  - artifact_type_decision
  - domain_block_folder
  - router_update
  - knowledge_capture
  - index_update
  - validation_report
safety_level: medium
source: extracted_from_project_execution_os_block_building_practice
review_status: reviewed_with_required_improvements
version: 0.1.0
---

# Domain Block Creation

## Purpose

Convert a recurring cross-project domain into the smallest reusable Project Execution OS block that preserves useful knowledge without turning the repository into a document dump.

This skill is for creating domain layers such as Telegram, United States law, immigration, music, or design blocks after real reuse value is demonstrated.

## When To Use

Use this skill when:

- the owner explicitly asks to create a reusable domain block;
- a topic is appearing across multiple projects or expected to recur;
- one research pass can save repeated future investigation;
- the domain has multiple product surfaces, tools, rules, risks, or execution paths;
- different agents need a shared reusable map of the domain;
- a narrow block can reduce repeated context loading and execution drift.

## When Not To Use

Do not use this skill when:

- the request is a one-off factual question;
- one reference note is enough;
- the need is project-specific rather than cross-project;
- the correct artifact is a mandatory standard rather than a domain block;
- the topic is too vague to define a stable boundary;
- a suitable existing block, skill, standard, or donor solution already covers the need;
- the block would exist only to create an appearance of progress.

## Required Inputs

- domain request;
- intended reuse scenarios;
- expected users or agents;
- known risks and freshness requirements;
- relevant existing blocks, standards, skills, and knowledge entries;
- official documentation and donor solutions when research is required;
- central router path;
- indexing and knowledge-library rules.

## Outputs

Depending on the justified level:

- explicit artifact classification decision;
- reference note, compact block, or full block;
- `BLOCK.md` entrypoint;
- optional domain-specific supporting files;
- router registration;
- block-index update;
- knowledge-library pointer or architecture decision;
- source map;
- validation backlog;
- dated capability snapshot when the domain changes over time;
- lifecycle status and review report.

## Core Principle

Create the smallest reusable domain layer that solves the recurring need.

Use:

```text
need
-> duplicate check
-> artifact classification
-> block level selection
-> research and source hierarchy
-> stable principles
-> dated snapshots
-> ready solutions
-> safety boundaries
-> router registration
-> knowledge capture
-> index refresh
-> validation backlog
-> review
```

## Artifact Classification

Before creating a block, decide whether the correct artifact is:

- `reference note` — preserve one useful idea, tool, or source;
- `skill` — one narrow reusable workflow;
- `standard` — one mandatory system rule;
- `project artifact` — one project-specific output;
- `compact block` — a reusable domain with a small but recurring surface;
- `full block` — a multi-path reusable domain layer requiring a maintained knowledge structure;
- `no new artifact` — an existing solution already covers the need.

## Block Levels

### Level 1 — Reference Note

Use when the domain is not yet proven as recurring.

Typical output:

```text
reference or knowledge entry
```

### Level 2 — Compact Domain Block

Use when a domain is recurring but still bounded.

Minimum files:

```text
blocks/<domain>/
  BLOCK.md
  REFERENCES.md
  VALIDATION_BACKLOG.md
```

### Level 3 — Full Domain Block

Use when the domain has multiple routes, changing capabilities, meaningful risks, ready-made solutions, or repeated implementation decisions.

Typical files:

```text
blocks/<domain>/
  BLOCK.md
  PRODUCT_SURFACES.md
  WORKFLOW_PIPELINE.md
  READY_SOLUTIONS.md
  TOOL_SELECTION_MATRIX.md
  SECURITY_AND_COMPLIANCE.md
  MONETIZATION_AND_PAYMENTS.md        # only when relevant
  CURRENT_CAPABILITIES_<date>.md      # when freshness matters
  VALIDATION_BACKLOG.md
  REFERENCES.md
  RESEARCH_REPORT_<date>.md
```

Use only the files justified by the domain. Do not create empty ceremony files.

## Workflow

```text
1. Enter through START_HERE.md and follow docs/ROUTER.md.
2. Read blocks/skill-creator/BLOCK.md and the central skill / knowledge / indexing standards that apply.
3. Search existing skills/, blocks/, docs/, knowledge-library/, and relevant official sources before creating anything.
4. Define the recurring domain boundary in one paragraph.
5. Identify intended reuse scenarios and expected agents.
6. Decide: reference note, skill, standard, project artifact, compact block, full block, or no new artifact.
7. If block creation is justified, select the minimum block level.
8. Build BLOCK.md as the stable entrypoint: purpose, status, when to use, when not to use, core rule, smallest-path reading order, outputs, boundary, final rule.
9. Add only the supporting files required by the domain.
10. Separate stable principles from dated snapshots and external-source references.
11. Add a source hierarchy and preserve official sources as the primary authority where applicable.
12. Add ready solutions before custom invention when implementation choices matter.
13. Add security, legal, privacy, or escalation boundaries when mistakes are costly.
14. Add VALIDATION_BACKLOG.md so researched possibilities are not confused with verified workflows.
15. Register the narrow route in docs/ROUTER.md.
16. Update blocks/PROJECT_INDEX.md.
17. Capture a compact reusable architecture decision or pointer in knowledge-library/ when cross-project reuse is expected.
18. Refresh generated indexes or confirm the automatic index workflow refreshed them.
19. Run review: right-sized scope, no duplication, no document dump, truthful lifecycle state, valid paths, and freshness boundaries.
20. Keep the new block in candidate status until real use validates it.
```

## BLOCK.md Contract

Every domain block entrypoint should include:

- Purpose;
- Status;
- When To Use;
- When Not To Use;
- Core Rule;
- Required Reading Inside This Block;
- Typical Outputs;
- Boundary;
- Final Rule.

The entrypoint is a router, not an encyclopedia.

## Research Rule

When research is required:

- search official documentation first;
- distinguish official sources, professional interpretation, community practice, and anecdotal signals;
- preserve source URLs in `REFERENCES.md`;
- record the research date;
- isolate unstable facts in dated snapshot files;
- avoid presenting forum reports as authoritative rules;
- stop searching when a sufficiently adequate proven map exists for the block MVP.

## Indexing Rule

After structural changes:

- update the curated block index;
- confirm router registration;
- confirm `BLOCK.md` exists;
- refresh generated indexes;
- verify no broken paths;
- use semantic-ready corpus generation when available;
- preserve canonical files as the source of truth.

## Constraints

- Do not create blocks reflexively.
- Do not duplicate existing blocks, skills, standards, or knowledge entries.
- Do not make the router store detailed domain knowledge.
- Do not load the entire block by default; define the smallest-path reading order.
- Do not treat research as operational validation.
- Do not mark a new block active merely because files were committed.
- Do not store secrets, credentials, personal case data, or project-specific confidential material in central reusable blocks.
- Do not mix stable principles with time-sensitive snapshots.
- Do not create empty placeholder files merely to imitate a full block layout.

## Failure Modes

- creating a full block for a one-off question;
- creating a reference note when a recurring domain needs routing and validation;
- duplicating an existing solution;
- turning `BLOCK.md` into a large encyclopedia;
- loading every block file for every task;
- hiding freshness-sensitive facts in undated files;
- confusing researched candidates with verified solutions;
- omitting router registration;
- omitting block index or generated-index refresh;
- storing project-specific secrets in a central block;
- creating too many files before real use proves their value;
- failing to add a validation backlog.

## Validation Checklist

- [ ] recurring cross-project need is explicit;
- [ ] duplicate check covered skills, blocks, docs, knowledge-library, and relevant external donors;
- [ ] artifact classification is recorded;
- [ ] selected block level is justified;
- [ ] `BLOCK.md` exists and acts as a router rather than a dump;
- [ ] supporting files are justified by the domain;
- [ ] stable principles are separated from dated snapshots;
- [ ] official sources are preserved when applicable;
- [ ] ready solutions were checked before custom invention;
- [ ] security and escalation boundaries are present when needed;
- [ ] validation backlog exists;
- [ ] router route is narrow and registered;
- [ ] curated block index is updated;
- [ ] knowledge-library capture is added when cross-project reuse warrants it;
- [ ] generated index refresh is confirmed;
- [ ] paths are valid;
- [ ] lifecycle status is truthful;
- [ ] the block remains candidate until real use validates it.

## References

See `references.md`.
