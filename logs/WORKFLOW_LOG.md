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

# ChatGPT Core System Prompt Added

## Summary

Added a short stable ChatGPT core system prompt that tells the model to request and follow `Start New Project.md` first, then use `Project Execution OS` as the evolving external brain.

## Executed Repository Actions

### Action 1 - Core system prompt created

Affected file:

- `docs/CHATGPT_CORE_SYSTEM_PROMPT.md`

Purpose:

Separate stable constitutional instructions from the living startup playbook and the wider central memory system.

### Action 2 - Canonical docs linked to the prompt

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`

Purpose:

Make the system-prompt layer discoverable from the main repository entry documents.

## Key Decisions

### Decision 1 - System prompt should stay short and stable

The system prompt should define the constitutional read order and behavior, not carry the full evolving operating system.

### Decision 2 - `Start New Project.md` remains the living startup contract

The core prompt points to `Start New Project.md`, and that file then leads into the wider `Project Execution OS` brain.

## Next Action

Use this core prompt in ChatGPT custom instructions or other stable system layers, while continuing to evolve `Start New Project.md` and the central repository documents separately.

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

---

# Start New Project v2 Split

## Summary

Reduced `Start New Project.md` from a heavy mixed entrypoint into a short boot-router and moved deeper operating logic into dedicated linked standards.

## Executed Repository Actions

### Action 1 - Startup entrypoint reduced to routing role

Affected files:

- `Start New Project.md`

Purpose:

Keep the startup file short, strict, and hard to ignore while preventing it from becoming a second brain.

### Action 2 - Heavy operating logic split into focused standards

Affected files:

- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `docs/DECISION_REGISTRY_STANDARD.md`

Purpose:

Move deeper rules out of the startup file so they can evolve without bloating the boot layer.

### Action 3 - Index documents updated

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`

Purpose:

Make the v2 split discoverable from the main entry documents.

## Key Decisions

### Decision 1 - Start New Project is a router, not a constitution

The startup file should force correct routing, not duplicate the whole operating system.

### Decision 2 - Deeper standards should be loaded on demand

Workflow, handoff, research, review, and decision-tracking rules now live in dedicated docs.

## Next Action

Use the new boot-router in real startup sessions and tighten any linked standard only when real usage exposes a gap.

---

# Lightweight Workflow Layer Added

## Summary

Added a lightweight operating layer so the system stays disciplined without drifting into bureaucracy on tiny or routine work.

## Executed Repository Actions

### Action 1 - Quick daily shortcut added

Affected files:

- `START_FAST.md`

Purpose:

Provide a short operational shortcut without creating a competing canonical startup entrypoint.

### Action 2 - Lightweight workflow standards added

Affected files:

- `docs/MICRO_TASK_MODE.md`
- `docs/WORKFLOW_DECISION_TABLE.md`

Purpose:

Make small-task handling and workflow selection explicit instead of leaving them implicit.

### Action 3 - Core docs updated with lightweight rules

Affected files:

- `Start New Project.md`
- `START_HERE.md`
- `README.md`
- `PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/PROJECT_ENTRY_MODES.md`

Purpose:

Promote `artifact only when useful`, `micro-task mode`, and explicit workflow selection into the main operating path.

## Key Decisions

### Decision 1 - Keep one canonical startup router

`Start New Project.md` remains the only canonical startup entrypoint for new projects.

### Decision 2 - Allow a fast operational shortcut

`START_FAST.md` is a shortcut for daily use after the system is already understood, not a replacement for the canonical startup router.

### Decision 3 - Lightweight discipline beats file ritual

Tiny safe tasks should use the smallest durable structure that still preserves useful state and evidence.

## Next Action

Use the decision table and micro-task mode in real sessions, then refine thresholds only if repeated work shows ambiguity.

---

# Compact-First Gate Tightened

## Summary

Strengthened the system so compact execution wins by default and deeper standards load only on explicit need.

## Executed Repository Actions

### Action 1 - Startup router tightened

Affected files:

- `Start New Project.md`
- `START_FAST.md`

Purpose:

Make `compact-first`, `1 file / 1 issue / 1 packet`, and standards-on-demand part of the default operating behavior.

### Action 2 - Workflow expansion gate formalized

Affected files:

- `docs/WORKFLOW_CONTRACT.md`
- `docs/WORKFLOW_DECISION_TABLE.md`

Purpose:

Prevent automatic escalation into heavier workflow layers when a shorter useful path is enough.

## Key Decisions

### Decision 1 - Compact-first is now the default gate

Heavier workflow is allowed only when scope, risk, review, handoff, or future continuity clearly requires it.

### Decision 2 - Standards are loaded on demand, not by ritual

Deeper standards should be opened only when the current task has a concrete reason for them.

## Next Action

Use this tighter gate in real sessions and watch for any remaining cases where the system still expands too eagerly.

---

# Mode Classifier Added

## Summary

Added an explicit first-pass classifier so the system can distinguish project start, micro-task, discussion, research-only, normalization, and Codex handoff before expanding workflow.

## Executed Repository Actions

### Action 1 - Classifier standard added

Affected files:

- `docs/MODE_CLASSIFIER.md`

Purpose:

Give the system a fast way to choose the lightest correct mode before repository or workflow expansion.

### Action 2 - Routing docs linked to classifier

Affected files:

- `Start New Project.md`
- `START_FAST.md`
- `docs/PROJECT_ENTRY_MODES.md`
- `docs/WORKFLOW_DECISION_TABLE.md`

Purpose:

Make the classifier part of the normal operating path instead of an implicit idea.

## Key Decisions

### Decision 1 - Not every request is a project

The system must distinguish new project, existing work, micro-task, discussion, research-only, normalization, and handoff before choosing workflow weight.

### Decision 2 - Classify first, expand second

The classifier exists to keep the operating system from turning small work into unnecessary process.

## Next Action

Use the classifier in live sessions and tighten the boundary cases only if repeated ambiguity appears.

---

# Startup Guardrails Tightened

## Summary

Added a few small startup guardrails without changing the overall architecture: explicit startup state, MVP lock, trigger list for deeper standards, no guessing of project idea, and a one-line Codex path.

## Executed Repository Actions

### Action 1 - Boot-router guardrails added

Affected files:

- `Start New Project.md`

Purpose:

Reduce ambiguity after `Question 1 / Question 2` without turning the startup into heavier process.

### Action 2 - Supporting rules linked

Affected files:

- `docs/MODE_CLASSIFIER.md`
- `docs/CODEX_HANDOFF_STANDARD.md`

Purpose:

Make the startup rules line up with the classifier and the handoff standard.

## Key Decisions

### Decision 1 - Do not guess the project idea

If the user asks to create a project without stating the idea, the system must ask `Question 1` instead of inventing direction.

### Decision 2 - Startup state should be short and explicit

After `Question 1` and `Question 2`, the system should preserve only the minimal startup state needed to avoid drift.

### Decision 3 - MVP lock stays active early

Before a first useful result exists, the system should not drift into scaling, abstraction, agent sprawl, or automation without a concrete reason.

## Next Action

Use these small guardrails in real startup sessions and keep them only if they reduce drift without reintroducing bureaucracy.

---

# Start New Project Contract Format

## Summary

Reformatted `Start New Project.md` into a stricter machine-readable contract while preserving the same operating logic.

## Executed Repository Actions

### Action 1 - Boot-router rewritten as contract

Affected files:

- `Start New Project.md`

Purpose:

Make the entrypoint easier for weaker models to execute by separating mode decision, required behavior, forbidden behavior, startup state, routing triggers, and output format.

### Action 2 - Workflow log updated

Affected files:

- `logs/WORKFLOW_LOG.md`

Purpose:

Record the contract-format decision and keep the operating history durable.

## Key Decisions

### Decision 1 - Logic unchanged, execution shape tightened

The file still acts as the startup boot-router, but now uses explicit contract sections instead of narrative guidance.

### Decision 2 - Non-start modes must not trigger startup questions

The boot decision now explicitly says that discussion, micro-task, research-only, existing project work, normalization, and Codex handoff do not automatically receive `Question 1 / Question 2`.

## Next Action

Test the contract-style entrypoint with clean chats and watch whether it reduces creative interpretation without making startup heavier.

---

# Workflow Reference vs Execution Form Clarified

## Summary

Clarified that the full `00_INPUT.md -> 09_LOG.md` workflow is the reference model, while compact mode is the default execution form.

## Executed Repository Actions

### Action 1 - Workflow contract clarified

Affected files:

- `docs/WORKFLOW_CONTRACT.md`

Purpose:

Remove ambiguity between the full workflow chain and compact-first execution.

### Action 2 - Decision table clarified

Affected files:

- `docs/WORKFLOW_DECISION_TABLE.md`

Purpose:

Make the default path for a new meaningful project compact unless scope, risk, review, handoff, or reuse justifies full workflow expansion.

## Key Decision

Full workflow is a map, not mandatory bureaucracy.

Compact mode is the default execution form.

## Next Action

Watch clean-chat behavior for whether models now choose compact mode more consistently on normal startup tasks.

---

# Documentation Block Embedded

## Summary

Embedded the reusable core of `Documentation-OS` into `Project-Execution-OS` as an internal Documentation Block instead of keeping that domain capability only in a separate repository.

## Executed Repository Actions

### Action 1 - Blocks layer introduced

Affected files:

- `blocks/README.md`
- `blocks/PROJECT_INDEX.md`

Purpose:

Create a formal home for reusable domain blocks inside the central brain.

### Action 2 - Documentation Block created

Affected files:

- `blocks/documentation/BLOCK.md`
- `blocks/documentation/PROJECT_INDEX.md`
- `blocks/documentation/MIGRATION_MAP.md`
- `blocks/documentation/standards/AI_READY_DOCUMENTATION_PACKAGE_STANDARD.md`
- `blocks/documentation/standards/REPOSITORY_DOCUMENTATION_TRANSFER_STANDARD.md`
- `blocks/documentation/templates/compact-repository-documentation/`
- `blocks/documentation/examples/family-memory-book-transfer-package/EXAMPLE.md`
- `blocks/documentation/skills/repository-documentation-transfer/SKILL.md`

Purpose:

Embed only the reusable documentation layer, not the full source repository history.

### Action 3 - Central indexes updated

Affected files:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`

Purpose:

Make the new blocks layer discoverable without bloating the startup router.

## Key Decisions

### Decision 1 - Separate repository becomes source, central repo becomes canonical home

`Documentation-OS` remains useful as an incubator and history source, but the reusable documentation capability now has an embedded canonical home inside the central brain.

### Decision 2 - Reusable core only

The embedded block includes standards, templates, skill, and example, but not all one-off workflow history from the source repository.

## Next Action

Use the Documentation Block in real work inside `Project-Execution-OS` and promote or trim its assets based on actual reuse.

---

# Entry Hierarchy, Integrations Layer, And Structure Validation

## Summary

Strengthened the operating system so the top-level entry hierarchy is clearer, project state is easier for agents to parse, ChatGPT-specific docs have a dedicated integrations home, and project structure can now be checked automatically.

## Executed Repository Actions

### Action 1 - Top-level routing clarified

Affected files:

- `START_HERE.md`
- `README.md`
- `PROJECT_INDEX.md`
- `Start New Project.md`

Purpose:

Keep one top-level entry while preserving the dedicated startup router and fast shortcut as downstream paths rather than competing roots.

### Action 2 - Machine-readable project state added

Affected files:

- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `projects/20260516-green-apple/PROJECT_STATE.md`

Purpose:

Add a stable frontmatter shape so agents can recover project status, mode, current run, and next action without rereading the whole project.

### Action 3 - Integrations layer added

Affected files:

- `docs/integrations/README.md`
- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`

Purpose:

Move ChatGPT-facing entrypoints into an explicit integrations layer so the root docs stay more AI-agnostic.

### Action 4 - Structure validation automated

Affected files:

- `.github/workflows/validate-project-structure.yml`
- `scripts/validate-project-structure.ps1`

Purpose:

Turn part of the project-structure governance into an executable check instead of relying only on participant discipline.

### Action 5 - Changelog added

Affected files:

- `CHANGELOG.md`

Purpose:

Provide one short high-signal place to track recent operating-system changes without rereading the whole workflow log.

## Key Decisions

### Decision 1 - One top-level entry does not require one file for every role

`START_HERE.md` is the single top-level entry, while `Start New Project.md` and `START_FAST.md` remain specialized downstream routers.

### Decision 2 - `PROJECT_STATE.md` should be readable by humans and agents

Short frontmatter is now the preferred machine-readable state layer, while the body remains the human-readable detailed state.

### Decision 3 - `CONTEXT_PACK.md` is optional and secondary

Fast recovery briefs are allowed, but they must not replace canonical project memory artifacts.

### Decision 4 - Integration-specific docs belong in an integrations layer

ChatGPT-specific routing now has a dedicated home under `docs/integrations/` even while compatibility aliases still exist elsewhere in the repository.

## Next Action

Run the new project-structure validator in normal repository work, then tighten or relax its checks only when real usage exposes false positives or missing guarantees.

---

# Reference Idea Capture Function Added

## Summary

Added a lightweight idea-capture function so a new chat can discuss an idea, avoid losing it, and optionally route it into `Reference-Idea-Library` without forcing premature project startup.

## Executed Repository Actions

### Action 1 - Idea capture standard created

Affected files:

- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`

Purpose:

Define a durable but lightweight path for ideas, references, links, and notes that are not yet project state.

### Action 2 - Startup and routing docs updated

Affected files:

- `Start New Project.md`
- `START_HERE.md`
- `docs/MODE_CLASSIFIER.md`
- `README.md`
- `PROJECT_INDEX.md`

Purpose:

Teach the system that "I have an idea, let's discuss it" can route into idea capture instead of being forced into project creation.

## Key Decisions

### Decision 1 - Idea capture is a function, not another brain

`Reference-Idea-Library` is treated as an intake, holding, and promotion layer rather than a replacement for project repositories or the central operating system.

### Decision 2 - Record only on explicit user intent

Discussion may stay ephemeral, but when the user wants the idea preserved, the system now has a canonical place and rule set for doing that.

## Next Action

Use this function in real chats where the user brings an idea or reference that should not be lost, then refine the standard only if repeated use exposes ambiguity.

---

# ChatGPT Entrypoint Fetch Rule Tightened

## Summary

Strengthened the ChatGPT integration layer so a new chat should fetch `Start New Project.md` itself when the canonical URL is already known and accessible, instead of asking the user to paste the file again.

## Executed Repository Actions

### Action 1 - Core prompt behavior tightened

Affected files:

- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- `docs/integrations/README.md`

Purpose:

Remove a passive failure mode where the model acknowledged the startup contract but still pushed the retrieval work back onto the user.

## Key Decisions

### Decision 1 - Known canonical URL should be used directly

If the exact startup entrypoint URL is already known and readable, the model should fetch it itself.

### Decision 2 - Asking the user is fallback behavior only

The user should be asked to paste or resend the file only when the canonical entrypoint truly cannot be accessed from the known URL or available context.

## Next Action

Use this tighter rule in future clean-chat tests and keep watching for any remaining passive handoff behavior around entrypoint retrieval.

---

# Startup-to-Idea Switch Behavior Tightened

## Summary

Tightened the startup behavior so if a user changes intent from project creation to idea discussion, the assistant must switch modes immediately without repeating startup ritual language or formatting the discussion as a procedural questionnaire.

## Executed Repository Actions

### Action 1 - Core prompt updated

Affected files:

- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`

Purpose:

Make mode switching explicit in the ChatGPT-facing system layer.

### Action 2 - Startup router and classifier updated

Affected files:

- `Start New Project.md`
- `docs/MODE_CLASSIFIER.md`

Purpose:

Prevent the assistant from continuing startup choreography after the user has clearly downgraded the request to idea discussion.

## Key Decisions

### Decision 1 - Intent change should end startup ritual immediately

Once the user switches from project start to idea discussion, the assistant should stop the startup sequence and move into the lighter mode.

### Decision 2 - Light mode should sound natural

Simple idea discussion should not be phrased as `Question 1 of 1` or wrapped in extra procedural text.

## Next Action

Keep testing clean-chat behavior and trim any remaining ritual language that survives mode switching.

---

# Brainstorm Prompt Naturalness Tightened

## Summary

Tightened the light-mode behavior again so a simple idea discussion should not be turned into a mini-questionnaire with arbitrary answer-length instructions unless the user explicitly wants a structured intake format.

## Executed Repository Actions

### Action 1 - Core prompt refined

Affected files:

- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`

Purpose:

Keep brainstorm and answer-only behavior conversational instead of bureaucratic.

### Action 2 - Startup router refined

Affected files:

- `Start New Project.md`

Purpose:

Block another residual pattern where the assistant asks for a fixed number of sentences even after correctly switching out of startup mode.

## Key Decisions

### Decision 1 - Natural discussion is the default in light modes

If the user only wants to discuss an idea, the assistant should ask naturally rather than impose a structured response shape.

### Decision 2 - Structured intake remains optional

Length or format constraints belong only in cases where the user explicitly requests a form-like intake.

## Next Action

Use this stricter natural-language rule in future clean-chat tests and keep trimming leftover questionnaire habits if they appear again.

---

# Decision Council Pressure-Test Skill Added

## Summary

Added a new candidate central review skill that adapts the reusable pattern from `tenfoldmarc/llm-council-skill` into a tool-neutral decision pressure-test capability.

## Executed Repository Actions

### Action 1 - Candidate review skill created

Affected files:

- `skills/review/decision-council-pressure-test/SKILL.md`
- `skills/review/decision-council-pressure-test/references.md`

Purpose:

Capture the reusable `LLM council` pattern without importing the source repository verbatim or treating its Claude-specific orchestration as canonical.

### Action 2 - Central skill layer updated

Affected files:

- `skills/PROJECT_INDEX.md`
- `skills/registry.md`

Purpose:

Register the new capability as a candidate central review skill with explicit external source attribution.

## Key Decisions

### Decision 1 - Steal the pattern, not the whole repository

The central skill keeps the five-lens adversarial review pattern, anonymous peer review, and chairman synthesis, but does not canonize HTML report generation or Claude-specific sub-agent mechanics.

### Decision 2 - This is a review capability, not startup logic

The council pattern belongs in the review and decision-pressure-test layer, not in project startup, memory, or idea intake.

## Next Action

Use this candidate skill on a real high-stakes decision, then review whether it deserves promotion from `candidate` toward `reviewed`.

---

# Notion Adapter Standard Added

## Summary

Added a canonical `Notion` adapter standard so the system can use `Notion` as a normal external working layer without confusing it with repository truth.

## Executed Repository Actions

### Action 1 - Notion adapter standard created

Affected files:

- `docs/integrations/notion/README.md`

Purpose:

Define exactly how `Notion` fits into `Project Execution OS` as a workspace, synthesis, and shared-visibility adapter.

### Action 2 - Integration indexes updated

Affected files:

- `docs/integrations/README.md`
- `README.md`
- `PROJECT_INDEX.md`
- `START_HERE.md`

Purpose:

Make the `Notion` adapter discoverable without moving it into the tool-neutral core or startup router.

## Key Decisions

### Decision 1 - `Notion` is a normal adapter, not a second brain

`Notion` is now explicitly allowed as a useful working surface, but it must not silently replace repository memory or become the only truth-layer.

### Decision 2 - Durable outcomes still return to the repository

Even when work is captured, synthesized, or shared through `Notion`, important committed state must still be written back into repository artifacts.

## Next Action

Use this adapter in real `Notion`-backed work and refine the standard only if repeated use exposes unclear sync boundaries.

---

# Notion Vs GitHub Usage Rule Added

## Summary

Added a short environment-choice rule clarifying when lightweight work belongs in `Notion` and when repository-driven work belongs in `GitHub`.

## Executed Repository Actions

### Action 1 - Notion adapter standard clarified

Affected files:

- `docs/integrations/notion/README.md`

Purpose:

Make the `Notion` adapter practical for everyday use by explicitly separating `light workspace` use from `durable repository execution`.

## Key Decisions

### Decision 1 - `Notion` is valid for lightweight life/workspace cases

Examples like travel planning, recipe collections, shopping comparisons, and lightweight coordination should not be forced into dedicated Git repositories.

### Decision 2 - `GitHub` stays for durable execution-grade work

Code, implementation packets, reviewable diffs, technical docs, and repository memory still belong in `GitHub`.

## Next Action

Use this rule in real routing decisions and only tighten it further if repeated borderline cases stay ambiguous.

---

# Universal Project Entrypoint Standard Added

## Summary

Added one shared `Project Entrypoint` contract so every project can have the same fast first-read surface whether it lives mainly in `GitHub` or `Notion`.

## Executed Repository Actions

### Action 1 - Universal project entrypoint standard created

Affected files:

- `docs/PROJECT_ENTRYPOINT_STANDARD.md`

Purpose:

Define the exact questions and sections a first-read project entrypoint must answer for any new human or AI participant.

### Action 2 - GitHub and Notion templates created

Affected files:

- `workflow-templates/project-entrypoint/GITHUB_PROJECT_ENTRYPOINT_TEMPLATE.md`
- `workflow-templates/project-entrypoint/NOTION_PROJECT_ENTRYPOINT_TEMPLATE.md`

Purpose:

Provide ready-to-use environment-specific forms of the same contract without splitting the system into separate project memory philosophies.

### Action 3 - Central indexes and standards linked

Affected files:

- `README.md`
- `PROJECT_INDEX.md`
- `START_HERE.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/integrations/notion/README.md`

Purpose:

Make the new contract discoverable from the central brain, project structure rules, and the Notion adapter layer.

## Key Decisions

### Decision 1 - One contract, two forms

`GitHub` projects use `PROJECT_ENTRYPOINT.md`.

`Notion` projects use a `Project Entrypoint` page or top section.

The medium changes, but the entry contract stays the same.

### Decision 2 - Entrypoint is the front door, not the full memory

The project entrypoint must stay short and answer what the project is, what matters now, and where to read next.

It must not become the full history, rules, or transcript archive.

## Next Action

Use this standard on real `GitHub` and `Notion` projects and tighten the section set only if repeated onboarding gaps still appear.

---

## 2026-06-01 - PROJECT.md bootstrap migration

Canonical local project entrypoint migrated from `PROJECT_ENTRYPOINT.md` to `PROJECT.md` across active standards, templates, and examples.

New intentionally created real project folders now receive only the minimum bootstrap set:

- `.git/`
- `AGENTS.md`
- `PROJECT.md`

Reinforced bootstrap continuity rules now also include:

- official communication-channel routing;
- minimum-context reading;
- stable-prefix behavior for accumulating files;
- legacy fallback for old `PROJECT_ENTRYPOINT.md` projects without keeping two active front doors.

Updated `SYSTEM_CONTEXT_MANIFEST.md` to `system-context-manifest-v5` after the router and context-assembly profile changes, including refreshed blob SHAs and SHA-256 fingerprint.
