# OpenAI Codex Skills / Plugins — verified reference

Date reviewed: 2026-08-29
Status: VERIFIED EXTERNAL SOLUTION / DONOR STANDARD

## Why this is here

OpenAI now provides an official reusable capability model for Codex based on Skills and Plugins. Project Execution OS should treat this as an Existing Solution First source before inventing a new Codex capability, packaging format, or reusable agent workflow.

## Current upstream status

The former `openai/skills` repository is deprecated as the primary catalog. Its README explicitly directs users to the current `openai/plugins` repository for current Codex skill and plugin examples and to the Build plugins guidance for skill-only plugins.

Legacy source:
https://github.com/openai/skills

Current source:
https://github.com/openai/plugins

## Core concepts worth adopting

### Skill

A Skill is a modular, self-contained capability package containing instructions and, where needed, scripts/resources. OpenAI describes Skills as reusable procedural knowledge that turns a general Codex agent into a more specialized agent for repeatable tasks.

Useful donor pattern:
- one capability = one bounded skill;
- explicit `SKILL.md` instructions;
- supporting scripts/references/assets only when needed;
- reusable rather than chat-specific behavior.

### Plugin

The current OpenAI repository expands the packaging model from skills into plugins. The official plugin-creator supports a plugin root containing:

- `.codex-plugin/plugin.json` — required manifest;
- `skills/` — optional reusable skills;
- `hooks/` — optional hooks;
- `scripts/` — optional executable helpers;
- `assets/` — optional assets;
- `.mcp.json` — optional MCP configuration;
- `.app.json` — optional app configuration;
- marketplace registration through `.agents/plugins/marketplace.json`.

This is important for Project Execution OS because it gives us a ready-made upstream packaging boundary for capabilities that need more than instructions alone.

## Existing Solution First integration rule

Before designing a new Codex skill/plugin/capability:

1. Check Project Execution OS existing standards, skills, capability registry, project-specific implementation, and reusable knowledge.
2. Check current official OpenAI Codex examples in `openai/plugins`.
3. Check the legacy `openai/skills` repository only as a donor/history source when useful.
4. Prefer adapting a verified official pattern over inventing a parallel packaging convention.
5. Only create a new Project Execution OS-specific abstraction when the existing OpenAI model or an existing internal solution demonstrably does not cover the requirement.

This does NOT mean blindly copying OpenAI examples. Project Execution OS remains the orchestration/governance layer. OpenAI Skills/Plugins are a capability packaging and execution donor standard.

## Mapping to Project Execution OS

| OpenAI concept | Project Execution OS analogue / role | Action |
|---|---|---|
| `SKILL.md` | reusable execution procedure / capability instructions | ADOPT pattern where appropriate |
| skill folder | bounded reusable capability | ADOPT |
| plugin | packaged capability bundle | ADOPT as Codex-facing packaging option |
| `.codex-plugin/plugin.json` | machine-readable capability manifest | ADOPT when building plugins |
| `.agents/plugins/marketplace.json` | discoverability/availability registry | STUDY and integrate rather than duplicate |
| scripts/assets/references | implementation/support material | ALREADY compatible with OS philosophy |
| MCP configuration | external tool integration | ALREADY aligned; use official packaging where applicable |
| plugin creator | scaffolding/validation | USE rather than recreating equivalent scaffolder |

## High-value official donor examples observed

The current `openai/plugins` catalog includes integrations/capability packs such as:

- Adobe
- Airtable
- Atlassian Rovo
- build-ios-apps
- build-macos-apps
- build-web-apps
- build-web-data-visualization
- Canva
- ChatCut
- CircleCI
- ClickUp
- Cloudflare
- CodeRabbit
- Codex Security
- Consensus
- Creative Production
- Data Analytics
- Datadog

This list is not intended as a frozen catalog. The upstream repository is live and should be checked at execution time.

## Particularly important upstream system capabilities

### skill-creator

Purpose: create/update a skill that extends Codex with specialized knowledge, workflows, or tool integrations.

Project Execution OS implication: do not build our own skill scaffolding rules from scratch when this upstream skill already defines the canonical Codex-oriented pattern. Our OS may add governance, routing, provenance, testing, and promotion rules around it.

### plugin-creator

Purpose: scaffold plugin directories and manifests, optional skills/hooks/scripts/assets/MCP/apps, and marketplace entries.

Project Execution OS implication: this should be the first candidate whenever we need to package a multi-part Codex capability.

## What Project Execution OS already does beyond this upstream model

OpenAI Skills/Plugins do not replace Project Execution OS. The OS additionally governs:

- project startup/routing;
- project state and durable memory;
- Existing Solution First;
- source traceability;
- task delegation and worker coordination;
- project lifecycle;
- cross-project reusable knowledge;
- evidence/verification requirements;
- decisions about when something should become a project, reference, standard, skill, or implementation task.

Therefore the correct architecture is:

`Project Execution OS governance/orchestration -> choose/reuse capability -> OpenAI Skill/Plugin packaging when Codex-facing`

not:

`OpenAI Plugins replaces Project Execution OS`.

## Adoption decision

ADOPT the official OpenAI Skills/Plugins model as a preferred Codex-facing capability packaging donor standard.

DO NOT fork the deprecated `openai/skills` repository as our canonical dependency.

TRACK `openai/plugins` as the current upstream source.

REUSE `skill-creator` / `plugin-creator` patterns before inventing equivalent scaffolding.

PRESERVE Project Execution OS as the higher-level routing, governance, memory, evidence, and orchestration layer.

## Source traceability

Primary sources:
- https://github.com/openai/skills
- https://github.com/openai/plugins
- https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- https://github.com/openai/plugins/blob/main/.agents/skills/plugin-creator/SKILL.md

Project routing source:
- https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/Start%20New%20Project.md
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`

## Maintenance rule

Because the OpenAI catalog is actively changing, never treat the plugin inventory in this document as current truth. At execution time, inspect the current `openai/plugins` repository and official OpenAI documentation. This document records the architectural conclusion and adoption rule, not a frozen marketplace snapshot.
