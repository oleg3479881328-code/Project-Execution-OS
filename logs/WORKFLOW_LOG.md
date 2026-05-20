# Workflow Log — Project Execution OS

## Purpose

This log records executed repository actions, workflow milestones, governance decisions, and state changes for Project Execution OS.

Generated ideas without repository commits must not be treated as executed history.

---

# Foundation Initialization

## Summary

Initialized `oleg3479881328-code/Project-Execution-OS` as the root repository for a universal repository-first project operating system.

Goal:
Any human, AI assistant, coding agent, research agent, review agent, or future automation system can enter through one entrypoint and understand how to start or continue a project.

## Executed Repository Actions

### Action 1 — README initialized

Affected file:

- `README.md`

Commit:

- `6a2ee83aaaf3e109d733e2b5cc22ed01831a9198`

Purpose:

Define Project Execution OS and point all users and agents to `START_HERE.md`.

### Action 2 — Universal entrypoint created

Affected file:

- `START_HERE.md`

Commit:

- `d7125dc2da653b1cc40c992c567c178ebc9c7795`

Purpose:

Create one entrypoint for humans, ChatGPT, Codex, Claude, local models, agents, and future automation.

### Action 3 — Project index created

Affected file:

- `PROJECT_INDEX.md`

Commit:

- `8b267db251d42e8f28dce6f7b6fd249ebea2a5b3`

Purpose:

Create current-state navigation and prevent repository drift.

### Action 4 — Workflow contract created

Affected file:

- `docs/WORKFLOW_CONTRACT.md`

Commit:

- `d19e5bf2d384d38e0d0c9df8f54829f315a2eede`

Purpose:

Define the universal workflow chain for project runs.

### Action 5 — Governance created

Affected file:

- `docs/GOVERNANCE.md`

Commit:

- `39cd0614234dca864a0d99e7620f856cd053a31b`

Purpose:

Define source of truth, state separation, no fake execution, agent governance, and knowledge governance.

### Action 6 — Agent creation standard created

Affected file:

- `docs/AGENT_CREATION_STANDARD.md`

Commit:

- `c603881da7e16e620a1ee19e17b516bc3d6b0a3c`

Purpose:

Define when and how project-specific agents are created.

### Action 7 — Knowledge system created

Affected file:

- `docs/KNOWLEDGE_SYSTEM.md`

Commit:

- `d0e6a655de5ec87ea045026ce379b64a3ea94f38`

Purpose:

Define local project libraries and central reusable knowledge library.

### Action 8 — Project structure standard created

Affected file:

- `docs/PROJECT_STRUCTURE_STANDARD.md`

Commit:

- `5c3972af34a747d7cbdd66d21224f0866a10ecee`

Purpose:

Define the required structure for each project folder.

### Action 9 — Central knowledge library README created

Affected file:

- `knowledge-library/README.md`

Commit:

- `9c87751265c7f823895128f64164da22b5d59953`

Purpose:

Create central knowledge library rules and entry categories.

### Action 10 — Universal workflow template created

Affected folder:

- `workflow-templates/universal-project-v1/`

Key commits:

- `74f0fcd0b7b61b7e697167f8c8f7817c68ac8dd5` — README
- `5ad62d64863e5530e89b2a3daf3ddd6b04bf6eef` — 00_INPUT.md
- `58f2e6cb17c5204b5d1126c91d156e3da3e088af` — 01_CLARIFICATION.md
- `0fb60202898e9fcd89744f8b236388d2174d5e8c` — 02_RESEARCH.md
- `bd2c92b54ca55503a28191e0f88d369c7273e7cc` — 03_PLAN.md
- `38bffdf8d703f853b9841ecb60f85fb2a0b465d4` — 04_AGENT_DESIGN.md
- `60c389cb8c08c2b825b3e8e3a3cb4cf268075c42` — 05_EXECUTION_SPEC.md
- `0996a7005825f7133bc84cb242c5ea0946ddf1d5` — 06_REVIEW.md
- `addaadecc92cc57f3dd5ac323aa82e8356cfedcd` — 07_RESULT.md
- `d22fb5c4a4393e9ecbb1d02775f130c1a0f14cf1` — 08_KNOWLEDGE_EXTRACT.md
- `44ae0804b802863fe5620e8a586287fe9bbddf87` — 09_LOG.md

Purpose:

Create a reusable workflow template for all new projects.

## Current Foundation State

Status:

`foundation_candidate`

Created core foundation artifacts:

- universal entrypoint;
- project index;
- workflow contract;
- governance;
- agent creation standard;
- knowledge system;
- project structure standard;
- central knowledge library README;
- universal project workflow template;
- workflow log.

## Current Forbidden Priorities

Do not prioritize yet:

- backend;
- frontend;
- runtime engine;
- orchestration engine;
- vector database;
- semantic search;
- automation framework;
- marketplace;
- mass agent creation;
- autonomous execution layer.

## Next Required Action

Create the first real project using this OS:

`projects/0001-project-execution-os-foundation-review/`

Purpose:

Run Project Execution OS on itself and review the foundation through the universal workflow.

---

# 3TestAgents Migration Decision

## Summary

Recorded the migration direction that treats `3TestAgents` as an experimental incubator and `Project-Execution-OS` as the canonical central system.

## Executed Repository Actions

### Action 1 — Migration map created

Affected file:

- `docs/THREETESTAGENTS_MIGRATION_MAP.md`

Purpose:

Define what should be migrated from `3TestAgents`, what should only be referenced, and what should be dropped when consolidating into the central operating system.

## Key Decisions

### Decision 1 — Canonical central system

`Project-Execution-OS` is the central brain, central governance layer, central knowledge library, and central skill hub.

### Decision 2 — 3TestAgents is an incubator

`3TestAgents` is treated as a historical experimental repository whose best ideas should be curated into the canonical central system.

### Decision 3 — Curated migration only

Migration must preserve validated standards and reusable artifacts, not copy stale repository state blindly.

## Resulting State

The repository now contains an explicit migration map for consolidating `3TestAgents` into `Project-Execution-OS`.

## Next Action

Use `docs/THREETESTAGENTS_MIGRATION_MAP.md` to migrate memory standards, skill governance, and reusable knowledge into canonical central artifacts.

---

# 3TestAgents Migration Execution — Central Layer Transfer

## Summary

Transferred the first central memory, skill-governance, and reusable-knowledge layer from `3TestAgents` into `Project-Execution-OS`.

## Executed Repository Actions

### Action 1 — Central standards added

Affected files:

- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/COMPATIBILITY_MODEL.md`

Purpose:

Create the central memory and skill-governance documents that were missing from the canonical system.

### Action 2 — Central skill layer created

Affected files:

- `skills/PROJECT_INDEX.md`
- `skills/registry.md`
- migrated candidate skills under `skills/`

Purpose:

Create the central reusable skill layer and import the incubator skills as `candidate` artifacts rather than treating them as already active.

### Action 3 — Central knowledge patterns imported

Affected files:

- `knowledge-library/PROJECT_INDEX.md`
- `knowledge-library/patterns/document-first-mvp.md`
- `knowledge-library/patterns/tool-neutral-core.md`
- `knowledge-library/patterns/state-separation-in-ai-systems.md`

Purpose:

Import the strongest reusable incubator patterns into the central knowledge layer.

### Action 4 — Entrypoints updated

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`

Purpose:

Make the central role of reusable skills and knowledge explicit in the repository entrypoints.

## Key Decisions

### Decision 1 — Incubator skills stay candidate

Migrated skills are committed into the central system, but they remain `candidate` until re-reviewed inside `Project-Execution-OS`.

### Decision 2 — Central knowledge imports also stay candidate

Migrated patterns are now available in the central library, but they are marked as central candidates rather than active rules.

### Decision 3 — Central system owns the reusable layer

`Project-Execution-OS` now explicitly owns the central repository-memory standard, central skill layer, and central reusable knowledge layer.

## Resulting State

The canonical system now contains:

- central memory standardization;
- central skill standards;
- a central skill registry and index;
- migrated candidate skills;
- migrated central knowledge patterns;
- updated entrypoints that describe the central-brain role more accurately.

## Next Action

Run the first central review pass over the migrated candidate skills and decide which can move from `candidate` toward `reviewed` or `active`.

---

# Central Skill Review Pass 001

## Summary

Completed the first central review pass for `github-repository-research` and `repository-memory-update`.

## Executed Repository Actions

### Action 1 — Central review artifacts created

Affected files:

- `skills/research/github-repository-research/validation/CENTRAL_REVIEW.md`
- `skills/memory/repository-memory-update/validation/REVIEW.md`

Purpose:

Record explicit central review results instead of relying on incubator review state.

### Action 2 — Skill lifecycle statuses updated

Affected files:

- `skills/research/github-repository-research/SKILL.md`
- `skills/memory/repository-memory-update/SKILL.md`
- `skills/registry.md`
- `skills/PROJECT_INDEX.md`

Purpose:

Promote both skills from `candidate` to `reviewed` after successful central review while intentionally stopping short of `active`.

## Key Decisions

### Decision 1 — Reviewed, not active

Both skills passed central review, but neither is marked `active` yet because central operational use in `Project-Execution-OS` still needs to be proven by repeated practice.

### Decision 2 — Incubator review is not enough

Migration history is preserved for provenance, but central status is determined by central review artifacts created in this repository.

## Resulting State

The central skill layer now contains:

- 2 reviewed skills:
  - `github-repository-research`
  - `repository-memory-update`
- 6 remaining candidate skills awaiting central review

## Next Action

Run the next central review pass for `implementation-handoff-packet` and `codex-execution-review`.

---

# Central Operating Model Synchronization

## Summary

Synchronized the central operating model with three explicit decisions:

- default location is one dedicated GitHub repository per project;
- research may use any publicly verifiable external sources, not only open-source code;
- compact project mode is allowed when the same governance rules are preserved with fewer files.

## Executed Repository Actions

### Action 1 — New-project entrypoint updated

Affected file:

- `Start New Project.md`

Purpose:

Make the startup flow match the intended central-brain operating model.

### Action 2 — Core entrypoint documents updated

Affected files:

- `START_HERE.md`
- `README.md`
- `PROJECT_INDEX.md`

Purpose:

Align central repository messaging with the repository-per-project default and compact-mode exception.

### Action 3 — Workflow and structure standards updated

Affected files:

- `docs/WORKFLOW_CONTRACT.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`

Purpose:

Make compact mode and publicly verifiable research sources part of the written operating standard.

## Key Decisions

### Decision 1 — Repository per project by default

Every new project should use its own dedicated GitHub repository unless an explicit exception is chosen.

### Decision 2 — Publicly verifiable research is broader than open-source code

Research may use official docs, GitHub, open-source examples, and other public evidence sources appropriate to the project domain.

### Decision 3 — Compact mode is valid

Small or low-risk projects may use fewer files as long as the same governance rules still hold.

## Next Action

Use the updated `Start New Project.md` as the canonical startup entrypoint in real project runs and continue hardening the central brain in practice.

---

# Skill Universe Inventory And Graphify Gap

## Summary

Recorded the broader external skill universe and explicitly documented that Graphify is not yet fully wired into `Project-Execution-OS`.

## Executed Repository Actions

### Action 1 — Skill universe inventory created

Affected file:

- `docs/SKILL_UNIVERSE_INVENTORY.md`

Purpose:

Give the central brain one inventory document that distinguishes central skills, migration candidates, adapter candidates, project-specific skills, and environment-specific skills.

### Action 2 — Graphify standard created

Affected file:

- `docs/GRAPHIFY_STANDARD.md`

Purpose:

Record the intended role of Graphify as graph-memory and repository cognition, while stating honestly that it is not yet fully installed in this repository.

### Action 3 — Canonical indexes updated

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `skills/PROJECT_INDEX.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`

Purpose:

Make the wider skill-universe inventory and Graphify standard visible from the central documentation layer.

## Key Decisions

### Decision 1 — The central brain should know the whole universe

`Project-Execution-OS` should not only store currently migrated central skills. It should also document the wider known skill universe.

### Decision 2 — Knowing the universe is not the same as activating everything

The central inventory may list many external skills, but the central active registry must remain curated and reviewed.

### Decision 3 — Graphify is a target standard, not yet a completed installation here

Graphify is now documented as part of the intended central-brain model, but local graph outputs and local Graphify setup have not yet been installed into this repository.

## Next Action

Run the next migration wave for:

- `graphify`
- `project-experience-memory`
- `project-knowledge-sync`
- `project-documentation-architect`
- `logic-deconstruction`

---

# Migration Wave 002 And Entry-Mode Expansion

## Summary

Migrated the next central skill wave from local skill stores and expanded the operating model to cover brainstorm-only work and legacy-project normalization.

## Executed Repository Actions

### Action 1 — New central candidate skills added

Affected paths:

- `skills/graph/graphify/`
- `skills/memory/project-experience-memory/`
- `skills/knowledge/project-knowledge-sync/`
- `skills/documentation/project-documentation-architect/`
- `skills/analysis/logic-deconstruction/`

Purpose:

Move the next high-value universal skills from local skill stores into the central system as curated central candidates.

### Action 2 — Skill indexes and universe inventory updated

Affected files:

- `skills/registry.md`
- `skills/PROJECT_INDEX.md`
- `docs/SKILL_UNIVERSE_INVENTORY.md`

Purpose:

Reflect the new migration state in the central inventory and central registry.

### Action 3 — New entry modes documented

Affected files:

- `Start New Project.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`

Purpose:

Make the central brain explicitly support:
- brainstorm-only mode
- legacy-project-normalization mode

## Key Decisions

### Decision 1 — Brainstorming can be valid without project creation

The operating system must allow exploratory work without forcing repository creation too early.

### Decision 2 — Old projects must be normalizable

The operating system must be able to take older repositories that do not match the current standard and migrate them carefully into the new mode.

### Decision 3 — Graphify is now part of the central candidate layer

Graphify is no longer only a documented external candidate. It now exists as a central candidate skill and remains pending central review and full local installation.

## Next Action

Run central review passes for:

- `graphify`
- `project-experience-memory`
- `project-knowledge-sync`

---

# Central Review Pass 002 And Graphify Build Rule

## Summary

Completed central review for `graphify`, `project-experience-memory`, and `project-knowledge-sync`, and strengthened the operating rules so a new AI should build Graphify when the project justifies it.

## Executed Repository Actions

### Action 1 — Central review artifacts created

Affected files:

- `skills/graph/graphify/validation/CENTRAL_REVIEW.md`
- `skills/memory/project-experience-memory/validation/CENTRAL_REVIEW.md`
- `skills/knowledge/project-knowledge-sync/validation/CENTRAL_REVIEW.md`

Purpose:

Record explicit central review results for the next three migrated universal skills.

### Action 2 — Lifecycle states updated

Affected files:

- `skills/graph/graphify/SKILL.md`
- `skills/memory/project-experience-memory/SKILL.md`
- `skills/knowledge/project-knowledge-sync/SKILL.md`
- `skills/registry.md`
- `skills/PROJECT_INDEX.md`

Purpose:

Promote the three skills from `candidate` to `reviewed` while keeping them below `active`.

### Action 3 — Graphify build behavior strengthened

Affected files:

- `docs/GRAPHIFY_STANDARD.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `Start New Project.md`
- `START_HERE.md`

Purpose:

Make it explicit that a new AI should build Graphify when a project is broad enough and supported files exist, rather than merely knowing that Graphify exists.

## Key Decisions

### Decision 1 — Reviewed, not active

`graphify`, `project-experience-memory`, and `project-knowledge-sync` are now centrally reviewed, but not yet `active`.

### Decision 2 — Graphify should be built, not only referenced

For broad projects with supported files, the expected behavior is to build Graphify when graph outputs are missing and then use the resulting graph-memory layer.

## Next Action

Run central review passes for:

- `project-documentation-architect`
- `logic-deconstruction`
- `implementation-handoff-packet`

---

# Central Review Pass 003 And Private Repository Default

## Summary

Completed central review for `project-documentation-architect` and `logic-deconstruction`, and made private-by-default repository creation part of the canonical startup policy.

## Executed Repository Actions

### Action 1 — Central review artifacts created

Affected files:

- `skills/documentation/project-documentation-architect/validation/CENTRAL_REVIEW.md`
- `skills/analysis/logic-deconstruction/validation/CENTRAL_REVIEW.md`

Purpose:

Record explicit central review results for the next two migrated universal skills.

### Action 2 — Lifecycle states updated

Affected files:

- `skills/documentation/project-documentation-architect/SKILL.md`
- `skills/analysis/logic-deconstruction/SKILL.md`
- `skills/registry.md`
- `skills/PROJECT_INDEX.md`

Purpose:

Promote the two skills from `candidate` to `reviewed` while keeping them below `active`.

### Action 3 — Private repository default documented

Affected files:

- `Start New Project.md`
- `START_HERE.md`
- `README.md`
- `PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`

Purpose:

Make it explicit that new project repositories should be private by default unless the user intentionally chooses a public repository.

## Key Decisions

### Decision 1 — Reviewed, not active

`project-documentation-architect` and `logic-deconstruction` are now centrally reviewed, but not yet `active`.

### Decision 2 — Privacy is the default, not an afterthought

New project repositories should default to private visibility. Public repositories require an explicit user decision.

## Next Action

Run central review passes for:

- `implementation-handoff-packet`
- `codex-execution-review`
- `pre-architecture-brainstorming`

---

# GitHub Coordination Protocol Added

## Summary

Added one canonical protocol document for `ChatGPT -> GitHub -> Codex -> review -> repository memory` so the collaboration model no longer lives only as scattered notes across startup docs and skills.

## Executed Repository Actions

### Action 1 — Canonical protocol created

Affected file:

- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

Purpose:

Define one durable operating standard for reasoning-model handoff, GitHub coordination, Codex execution, PR comment loops, and review evidence.

### Action 2 — Entrypoints linked to the protocol

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `Start New Project.md`

Purpose:

Make the protocol visible from the main operating entrypoints so a new AI can discover it early.

## Key Decisions

### Decision 1 — GitHub is a coordination layer, not the source of truth by itself

GitHub PRs, issues, comments, and checks are durable communication surfaces, but they do not replace repository workflow artifacts and memory files.

### Decision 2 — ChatGPT to Codex should be packet-driven

The default collaboration model is deterministic handoff packet -> bounded Codex execution -> structured execution report -> review.

## Next Action

Run live tests with clean chats and observe where the startup flow or GitHub collaboration protocol still causes ambiguity.

---

# ChatGPT Codex Communication Skill Added

## Summary

Promoted `ChatGPT <-> Codex` communication through GitHub from a protocol-only concept into a dedicated central reviewed skill and linked it across the main operating documents.

## Executed Repository Actions

### Action 1 — Central coordination skill created

Affected files:

- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`
- `skills/coordination/chatgpt-codex-github-communication/references.md`
- `skills/coordination/chatgpt-codex-github-communication/validation/CENTRAL_REVIEW.md`

Purpose:

Make durable reasoning-model to Codex communication a first-class reusable skill instead of only a prose protocol.

### Action 2 — Registry and inventory updated

Affected files:

- `skills/registry.md`
- `skills/PROJECT_INDEX.md`
- `docs/SKILL_UNIVERSE_INVENTORY.md`

Purpose:

Register the new coordination skill and align the wider skill map with the current reviewed state.

### Action 3 — Canonical docs strengthened

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `Start New Project.md`
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

Purpose:

Make the `ChatGPT 5 <-> Codex` communication pattern visible from the main entrypoints and protocol docs.

## Key Decisions

### Decision 1 — Communication is a skill, not only a note

Durable GitHub-mediated collaboration between a reasoning model and Codex is important enough to exist as its own central reusable skill.

### Decision 2 — Protocol and skill must coexist

The protocol document explains the model. The skill gives a reusable workflow unit that new AI sessions can invoke directly.

## Next Action

Use clean chats to verify that new reasoning sessions can discover and follow this coordination skill without extra explanation.

---

# Coordination Sync Discipline Added

## Summary

Expanded the central `ChatGPT <-> Codex <-> GitHub` coordination skill and protocol to include explicit sync discipline so future sessions do not need to renegotiate source-of-truth and local-workspace rules.

## Executed Repository Actions

### Action 1 — Coordination skill expanded

Affected files:

- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`
- `skills/coordination/chatgpt-codex-github-communication/references.md`

Purpose:

Add mandatory preflight sync checks, post-fix reporting rules, and source-of-truth discipline directly into the reusable skill.

### Action 2 — Protocol strengthened

Affected file:

- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

Purpose:

Make `GitHub main` source-of-truth rules and anti-desync behavior part of the canonical protocol, not just a situational lesson.

### Action 3 — Entrypoints clarified

Affected files:

- `README.md`
- `START_HERE.md`

Purpose:

Expose the sync discipline early so new AI sessions understand the committed-state model before they execute locally.

## Key Decisions

### Decision 1 — Sync discipline is part of the skill itself

The coordination skill now includes mandatory `git status`, `pull --ff-only`, minimal-commit, and commit-SHA reporting behavior.

### Decision 2 — Local folders are execution workspaces only

This rule is now explicitly written into the reusable operating model so future chats do not drift back into treating local state or mirrors as authority.

## Next Action

Continue live testing and only expand the coordination skill further if repeated real-world failures reveal another missing invariant.

---

# Entrypoint Anti-Failure Rule Added

## Summary

Strengthened `Start New Project.md` so a new chat fed only that file understands that an existing GitHub issue or PR is already a valid way to write to Codex, instead of incorrectly saying that no direct communication path exists.

## Executed Repository Actions

### Action 1 - Start file strengthened

Affected file:

- `Start New Project.md`

Purpose:

Add an explicit anti-failure rule for the common case where the reasoning model has no direct runtime bridge but does have an existing GitHub coordination surface.

## Key Decisions

### Decision 1 - GitHub issue or PR is a valid practical bridge

If a project already defines a GitHub coordination channel, the reasoning model must use it as the practical way to write to Codex.

### Decision 2 - "I cannot write to Codex" is now explicitly disallowed in that case

That answer is treated as incorrect when a GitHub issue, PR, or review thread already exists for the project.

## Next Action

Test the revised `Start New Project.md` again in a clean chat and verify that the new chat proposes GitHub issue or PR comments as the communication path automatically.

---

# Ready Scheme Added To Single Entrypoint

## Summary

Added a direct ready-to-use scheme into `Start New Project.md` so a new chat fed only that file can understand not just the Codex handoff model, but also the transport model through GitHub.

## Executed Repository Actions

### Action 1 - Single-file scheme added

Affected file:

- `Start New Project.md`

Purpose:

Turn the one-file entrypoint into a complete operational model: source of truth, payload, transport, execution, verification, and persistence.

## Key Decisions

### Decision 1 - One file must explain both payload and transport

`Implementation handoff packet` alone is not enough. The same entrypoint must also explain where that packet goes when the chat has no direct runtime bridge.

### Decision 2 - GitHub issue or PR is now part of the ready scheme

The single entrypoint now explicitly teaches that GitHub comments and threads are the practical transport layer for Codex communication when direct bridge access is absent.

## Next Action

Run the same clean-chat test again and verify that the new chat now explains both the handoff packet and the GitHub transport layer without extra prompting.

---

# Deferred System Ideas Added

## Summary

Added a durable central place for "not now, but important" `Project Execution OS` ideas so they survive chat resets and do not get lost between live tests.

## Executed Repository Actions

### Action 1 - Central deferred-ideas document created

Affected file:

- `docs/DEFERRED_SYSTEM_IDEAS.md`

Purpose:

Preserve future-system ideas that should not be built yet but should remain part of the central brain roadmap.

### Action 2 - Canonical docs linked to the deferred-ideas layer

Affected files:

- `README.md`
- `PROJECT_INDEX.md`
- `Start New Project.md`

Purpose:

Teach humans and future AI sessions where to place important deferred system ideas instead of losing them in chat.

## Key Decisions

### Decision 1 - Central deferred ideas need their own memory artifact

System-level future ideas should not live only in transient chat text and should not be mixed into active workflow runs prematurely.

### Decision 2 - Runtime bridge is the first deferred system idea

The direct execution bridge between reasoning models and Codex is valuable, but it stays deferred until live operational evidence shows that GitHub transport is no longer enough.

## Next Action

Continue live testing and add future central-brain "not now" ideas to `docs/DEFERRED_SYSTEM_IDEAS.md` whenever they are real, reusable, and intentionally postponed.

---

# Existing Channel Preference Added

## Summary

Strengthened `Start New Project.md` so new chats prefer an already existing GitHub coordination surface and avoid turning obvious next actions into unnecessary multiple-choice prompts.

## Executed Repository Actions

### Action 1 - Existing-channel rule tightened

Affected file:

- `Start New Project.md`

Purpose:

Make the single entrypoint teach operational continuity, not just the abstract transport model.

## Key Decisions

### Decision 1 - Existing GitHub channel comes first

If a suitable issue, PR, or review thread already exists for the work, the reasoning model should continue there instead of proposing a new coordination surface by default.

### Decision 2 - Obvious next steps should not become fake choice menus

When repository state and channel context already imply the next safe action, the AI should act through that channel or propose the concrete next step directly instead of manufacturing A/B/C/D prompts.

## Next Action

Re-test the entrypoint with clean chats and verify that they now prefer the existing GitHub channel and ask fewer artificial choice questions.

---

# Codex Usage Threshold Added

## Summary

Added an explicit system rule that `Codex` should be used only when executor access is actually needed, while small safe reasoning and drafting work should stay in the reasoning chat.

## Executed Repository Actions

### Action 1 - Entry and protocol docs updated

Affected files:

- `Start New Project.md`
- `START_HERE.md`
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

Purpose:

Prevent unnecessary Codex handoffs on small tasks and preserve executor capacity for real repository work.

## Key Decisions

### Decision 1 - Small safe tasks stay in chat

If a task only requires reasoning, drafting, summarizing, planning, or text preparation, the reasoning model should do it directly.

### Decision 2 - Codex is for true executor work

Use Codex only when the work needs repository edits, local commands, validation, integration checks, or other executor-only access.

## Next Action

Continue live testing and verify that new chats stop proposing Codex for trivial doc-first or planning-only steps.

---

# Bundled Clarification Rule Added

## Summary

Added a general rule that several clarification answers for one AI-ready package may be gathered in chat first and then written into the repository as one coherent update.

## Executed Repository Actions

### Action 1 - Entry and workflow docs updated

Affected files:

- `Start New Project.md`
- `START_HERE.md`
- `docs/WORKFLOW_CONTRACT.md`

Purpose:

Prevent noisy per-answer repository updates and make clarification flow more practical for real use.

## Key Decisions

### Decision 1 - Clarification can be bundled

If five answers belong to one package, the AI may collect all five in chat before writing the repository artifact.

### Decision 2 - Repository updates should follow coherent package boundaries

The default is one meaningful repository update per completed clarification package, not one update per button click.

## Next Action

Continue live testing and verify that new chats stop proposing unnecessary per-answer repository writes during clarification-heavy startup flows.

---

# AI Message Identity Rule Added

## Summary

Added a rule that GitHub messages between AI participants should explicitly label the speaker and recipient so mixed threads do not become ambiguous.

## Executed Repository Actions

### Action 1 - Coordination docs updated

Affected files:

- `Start New Project.md`
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- `skills/coordination/chatgpt-codex-github-communication/SKILL.md`

Purpose:

Make `ChatGPT`, `Codex`, and other AI participants identify themselves clearly in GitHub issues, PR comments, and review threads.

## Key Decisions

### Decision 1 - AI-to-AI GitHub messages need explicit headers

The default lightweight header is:

`FROM: <sender>`
`TO: <recipient>`
`TYPE: <message kind>`

### Decision 2 - Thread context alone is not enough

Mixed human and AI threads should not rely on inference to determine who is speaking or who should act next.

## Next Action

Use the new identity header format in live GitHub coordination and verify that it reduces ambiguity in shared issue threads.

---

# Commit Evidence Rule Added

## Summary

Added an explicit evidence rule: `commit SHA` proves that repository files changed, but it does not replace validation or review.

## Executed Repository Actions

### Action 1 - Evidence language tightened

Affected files:

- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- `Start New Project.md`
- `START_HERE.md`

Purpose:

Prevent overclaiming correctness from commit history alone.

## Key Decisions

### Decision 1 - Commit proves change, not full correctness

A commit is strong evidence of repository state change, but not a complete proof that the resulting behavior is correct.

### Decision 2 - Validation and review remain separate gates

Behavioral confidence still requires validation evidence and review, even when the commit SHA is known.

## Next Action

Use this evidence rule in future GitHub coordination so commits, validation, and review are reported as distinct signals.

---

# Multi-Agent GitHub Identity Expanded

## Summary

Expanded the GitHub identity model so the same coordination format supports not only `ChatGPT` and `Codex`, but also other explicitly named agents.

## Executed Repository Actions

### Action 1 - Multi-agent identity docs updated

Affected files:

- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`

Purpose:

Make the GitHub coordination model reusable for broader multi-agent collaboration without losing traceability.

## Key Decisions

### Decision 1 - Named agents are first-class participants

Agents such as `Reviewer`, `Research-Agent`, `Architecture-Agent`, and `Documentation-Agent` may participate in the same durable GitHub coordination pattern.

### Decision 2 - Identity must stay explicit

Even in multi-agent threads, every AI message must still identify `FROM`, `TO`, and `TYPE`.

## Next Action

Use the same identity format when new named agents join GitHub coordination threads.

---

# Coordination Shorthand Added

## Summary

Added a short operator shorthand for GitHub coordination commands: `0` means write to the channel, and `00` means check the thread and report what is new.

## Executed Repository Actions

### Action 1 - Shorthand rule documented

Affected files:

- `docs/AI_COORDINATION_HUB_STANDARD.md`
- `AI-Coordination-Hub/docs/COORDINATION_PROTOCOL.md`

Purpose:

Make repeated coordination actions faster without re-explaining the same intent in full sentences.

## Key Decisions

### Decision 1 - `0` means write

The shorthand `0` now means: write to the active GitHub coordination channel.

### Decision 2 - `00` means check

The shorthand `00` now means: inspect the GitHub coordination thread and report updates.

## Next Action

Use this shorthand only where the GitHub coordination channel is already known and active.

---

# Agent Library Standard Added

## Summary

Added a central reusable agent library standard and starter templates based on public multi-agent patterns from OpenAI Agents SDK, AutoGen, and LangGraph.

## Executed Repository Actions

### Action 1 - Central standard created

Affected files:

- `docs/AGENT_LIBRARY_STANDARD.md`
- `agent-library/README.md`
- `agent-library/PROJECT_INDEX.md`

Purpose:

Create a reusable agent layer so common agent roles do not need to be reinvented for each project.

### Action 2 - Starter templates added

Affected files:

- `agent-library/templates/_TEMPLATE/AGENT.md`
- `agent-library/templates/reviewer/AGENT.md`
- `agent-library/templates/research-agent/AGENT.md`
- `agent-library/templates/documentation-agent/AGENT.md`
- `agent-library/templates/orchestrator-agent/AGENT.md`

Purpose:

Seed the library with the smallest useful reusable roles and a standard template contract.

### Action 3 - Canonical docs linked to the library

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`

Purpose:

Make the new agent-library layer discoverable from the main entry documents.

## Key Decisions

### Decision 1 - Store reusable roles, not runtime sessions

The central library keeps reusable agent templates, while project-local agents and live GitHub participants remain separate layers.

### Decision 2 - Adopt specialist-first orchestration

The default patterns now explicitly follow public best practices:

- specialist agents over one overloaded generalist
- manager/supervisor when one role should keep control
- handoff when ownership should move
- reviewer loop when acceptance quality matters

### Decision 3 - Keep context minimal

Library agents must declare the minimum context they need instead of assuming full history by default.

## Next Action

Review the starter templates in real projects and promote only the reusable ones that survive repeated use.

---

# AI Coordination Hub Created

## Summary

Created a dedicated private GitHub repository to serve as the default durable hub for `ChatGPT <-> Codex` coordination across projects and linked it back into the central standards.

## Executed Repository Actions

### Action 1 - New private coordination hub established

Repository:

- `oleg3479881328-code/AI-Coordination-Hub`

Purpose:

Keep cross-project AI coordination in one stable GitHub home instead of scattering it across unrelated repositories.

### Action 2 - Central standards linked to the hub

Affected files:

- `README.md`
- `START_HERE.md`
- `Start New Project.md`
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`

Purpose:

Define when to use the hub versus when to keep the thread inside the target project repository.

## Key Decisions

### Decision 1 - Use a hub for cross-project AI coordination

Meta-level, protocol-level, and reusable coordination threads should have one durable home.

### Decision 2 - Keep project-bound execution near the target repository

The hub does not replace project-local source of truth or repository-bound execution history.

## Next Action

Push both the new coordination hub repository and the central `Project-Execution-OS` doc updates, then use the hub for future cross-project AI communication.

---

# Repository Description Rule Added

## Summary

Added a rule that every newly created repository should receive a short clear GitHub description at creation time.

## Executed Repository Actions

### Action 1 - Repo-creation docs updated

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `Start New Project.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`

Purpose:

Make new repositories easier to identify and understand in GitHub lists, navigation, and search views.

## Key Decisions

### Decision 1 - Repository name alone is not enough

Each new repository should also have a concise description that explains its role or purpose.

### Decision 2 - Description is part of repository bootstrap

Setting a GitHub description is now treated as a standard creation-time step, not an optional later cleanup.

## Next Action

Apply this rule to future repository creation flows and keep descriptions short, specific, and human-readable.

---

# Bilingual Repository Description Rule Added

## Summary

Refined the repository-description rule: new repositories should use bilingual GitHub descriptions with Russian first and English second.

## Executed Repository Actions

### Action 1 - Repo-description docs refined

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `Start New Project.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`

Purpose:

Standardize not only the existence of descriptions, but also their language order and readability.

## Key Decisions

### Decision 1 - Repository descriptions should be bilingual

Descriptions should work for both Russian-first and English-readable navigation contexts.

### Decision 2 - Russian comes first

The default order is Russian first, English second.

## Next Action

Apply this bilingual-description rule to future repository creation and update older repositories when their descriptions are touched.
