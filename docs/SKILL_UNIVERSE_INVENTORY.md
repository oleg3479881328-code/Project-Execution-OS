# Skill Universe Inventory

## Purpose

This document is the central inventory of the broader skill universe available around `Project-Execution-OS`.

It exists so that:

- the central brain knows which skills already exist;
- new AI sessions can see the difference between central skills and external skills;
- migration into the central system is curated, not accidental;
- project-specific skills are not confused with universal reusable skills.

## Core Rule

Not every known skill belongs in the central active registry.

The central registry stores reviewed central skills.

This inventory stores the wider universe:

- central skills already living in `Project-Execution-OS`;
- migration candidates from local skill stores;
- domain/platform skills that may later become adapters or packs;
- project-specific or environment-specific skills that should not be treated as universal core.

## Source Locations

Current external sources:

- `C:\Users\oleg3\.codex\skills`
- `C:\Users\oleg3\.agents\skills`

Current central source:

- `skills/` inside `Project-Execution-OS`

## Status Labels

- `central_reviewed` = already lives in `Project-Execution-OS` and passed central review
- `central_candidate` = already lives in `Project-Execution-OS` but still needs central review
- `migrate_candidate` = should likely move into the central system next
- `adapter_candidate` = useful, but better treated as a domain or environment adapter
- `project_specific` = should remain outside central universal core
- `environment_specific` = tied to local machine, local tools, or local workflows
- `archive_or_ignore` = not part of the central brain roadmap right now

## Central Skills Already In Project Execution OS

| Skill | Current Status | Notes |
|---|---|---|
| `github-repository-research` | `central_reviewed` | Central research skill for repository analysis and reusable pattern extraction. |
| `repository-memory-update` | `central_reviewed` | Central memory synchronization skill. |
| `pre-architecture-brainstorming` | `central_candidate` | Strong core workflow skill. |
| `multi-agent-design-review` | `central_candidate` | Strong core review skill. |
| `codex-execution-review` | `central_candidate` | Strong execution verification skill. |
| `implementation-handoff-packet` | `central_candidate` | Strong execution handoff skill. |
| `skill-runtime-router` | `central_candidate` | Useful, but must stay lightweight. |
| `workflow-state-machine` | `central_candidate` | Useful, but must avoid bureaucracy. |

## High-Priority Migration Candidates From Local Skill Stores

These are the strongest next candidates for central-brain adoption because they support continuity, documentation, memory, or repository intelligence.

| Skill | Source | Proposed Status | Why |
|---|---|---|---|
| `graphify` | `.agents` | `central_reviewed` | Migrated and centrally reviewed; still not `active` until live operational use is proven. |
| `project-experience-memory` | `.codex` | `central_reviewed` | Migrated and centrally reviewed; still not `active` until repeated use proves the pattern. |
| `project-knowledge-sync` | `.codex` | `central_reviewed` | Migrated and centrally reviewed; still not `active` until central-library sync is proven in live projects. |
| `project-documentation-architect` | `.codex` | `central_candidate` | Migrated into the central system; useful for normalization and onboarding. |
| `logic-deconstruction` | `.codex` | `central_candidate` | Migrated into the central system; useful for reasoning quality. |

## Adapter / Domain Skill Candidates

These are useful, but they should be treated as domain packs or adapters, not as universal core workflow.

| Skill | Source | Proposed Status | Why |
|---|---|---|---|
| `telegram-bot` | `.codex` | `adapter_candidate` | Strong domain-specific implementation skill. |
| `transcribe` | `.codex` | `adapter_candidate` | Useful capability skill, but not core workflow. |
| `speech` | `.codex` | `adapter_candidate` | Output capability, not central workflow. |
| `screenshot` | `.codex` | `adapter_candidate` | Utility skill, not central workflow. |
| `android-development` | `.codex` | `adapter_candidate` | Platform-specific pack. |
| `android-developers-docs` | `.codex` | `adapter_candidate` | Docs router for Android domain. |
| `android-publisher-api` | `.codex` | `adapter_candidate` | Platform-specific publishing pack. |
| `google-play` | `.codex` | `adapter_candidate` | Platform-specific publishing pack. |
| `google-play-docs-navigator` | `.codex` | `adapter_candidate` | Docs router for Play domain. |
| `chrome-devtools-browse` | `.codex` | `adapter_candidate` | Browser tooling adapter. |
| `chrome-remote-debug` | `.codex` | `adapter_candidate` | Browser tooling adapter. |
| `chrome-page-capture` | `.codex` | `adapter_candidate` | Browser tooling adapter. |
| `chrome-extension-mv3` | `.codex` | `adapter_candidate` | Domain-specific engineering pack. |
| `chrome-extension-publication-system-v3` | `.codex` | `adapter_candidate` | Domain-specific publication pack. |
| `aws-ec2-ssm-access` | `.codex` | `adapter_candidate` | Infrastructure-specific pack. |
| `bublup-public-read` | `.codex` | `adapter_candidate` | Narrow external platform reader. |
| `notebooklm` | `.agents` | `adapter_candidate` | External product integration, not universal core. |
| `pinokio` | `.agents` | `adapter_candidate` | Tool-launch environment adapter. |
| `gepeto` | `.agents` | `adapter_candidate` | Pinokio launcher/project adapter. |

## Project-Specific Or Environment-Specific Skills

These should not be treated as central universal skills by default.

| Skill | Source | Proposed Status | Why |
|---|---|---|---|
| `voice-chat-extension-dev` | `.codex` | `project_specific` | Tied to one concrete local project. |
| `static-family-archive-site` | `.codex` | `project_specific` | Narrow repository family-archive domain. |
| `family-archive-admin-workflow` | `.codex` | `project_specific` | Local domain workflow, not universal core. |
| `photo-album-diff-sync` | `.codex` | `project_specific` | Narrow project-family workflow. |
| `codex-chat-rename` | `.codex` | `environment_specific` | Local Codex environment helper. |
| `document-scan-rename` | `.codex` | `environment_specific` | Local document-processing utility. |
| `local-qwen-usage-status` | `.codex` | `environment_specific` | Local model-governance helper. |
| `notion-memory-ritual` | `.codex` | `environment_specific` | Strong workflow, but tied to one private memory OS. |
| `notion-knowledge-capture` | `.codex` | `adapter_candidate` | Useful adapter if generalized later. |
| `notion-meeting-intelligence` | `.codex` | `adapter_candidate` | Useful adapter if generalized later. |
| `notion-research-documentation` | `.codex` | `adapter_candidate` | Useful adapter if generalized later. |
| `notion-spec-to-implementation` | `.codex` | `adapter_candidate` | Useful adapter if generalized later. |

## Utility / Narrow Capability Skills

These may remain external until there is a clear reason to create central capability packs.

| Skill | Source | Proposed Status |
|---|---|---|
| `google-play-docs-navigator` | `.codex` | `adapter_candidate` |
| `local-qwen-usage-status` | `.codex` | `environment_specific` |
| `screenshot` | `.codex` | `adapter_candidate` |
| `speech` | `.codex` | `adapter_candidate` |
| `transcribe` | `.codex` | `adapter_candidate` |

## Immediate Next Migration Wave

Recommended next central migration wave:

1. Central review `project-documentation-architect`
2. Central review `logic-deconstruction`
3. Central review `implementation-handoff-packet`
4. Central review `codex-execution-review`
5. Central review `pre-architecture-brainstorming`

## Rules For The Universe

- The central brain should know the whole universe.
- The central active registry should stay curated and reviewed.
- Project-specific skills must not pollute the universal core.
- Environment-specific helpers should be documented, but not mistaken for universal standards.
- New AI sessions should read this inventory when they need the bigger skill map, not by default for every small task.
