# Project Index — Project Execution OS

## Repository

`oleg3479881328-code/Project-Execution-OS`

## System Name

Project Execution OS

## Purpose

Create a universal layer-aware project operating system for starting, running, reviewing, and preserving projects.

The system must support humans, ChatGPT, Codex, Claude, local models, specialized agents, and future automation systems through one entrypoint and one stable project workflow.

For the canonical GitHub-based coordination loop between reasoning models and Codex, use:

`docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`

It must also support:

- brainstorm-only work without forcing project creation;
- idea capture without forcing project creation;
- normalization of older repositories into the current standard;
- durable ChatGPT to Codex communication through GitHub;
- reusable executable capability blocks that can be composed into multiple applications without copying implementation code.

## Primary Entrypoint

`START_HERE.md`

Every user, assistant, agent, or automation session must start there.

`START_HERE.md` is intentionally minimal and durable. It points to the live internal router:

`docs/ROUTER.md`

Internal route growth belongs in `docs/ROUTER.md`, not in `START_HERE.md`.

## Current Phase

Foundation phase.

Mode:

`document-first`

Status:

`transfer_ready`

## Canonical Documents

- `README.md`
- `PROJECT.md`
- `PROJECT_STATE.md`
- `logs/latest.md`
- `START_HERE.md`
- `docs/ROUTER.md`
- `Start New Project.md`
- `START_FAST.md`
- `PROJECT_INDEX.md`
- `SYSTEM_CONTEXT_MANIFEST.md`
- `project-library/DECISION_REGISTRY.md`
- `project-library/decisions/006-stable-start-here-live-router.md`
- `blocks/README.md`
- `blocks/PROJECT_INDEX.md`
- `capability-library/README.md`
- `capability-library/REGISTRY.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/WORKFLOW_DECISION_TABLE.md`
- `docs/MICRO_TASK_MODE.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/HARNESS_ENGINEERING_STANDARD.md`
- `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`
- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `docs/DECISION_REGISTRY_STANDARD.md`
- `docs/GOVERNANCE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/COMPATIBILITY_MODEL.md`
- `docs/integrations/README.md`
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`
- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- `docs/integrations/notion/README.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`
- `docs/SKILL_UNIVERSE_INVENTORY.md`
- `docs/GRAPHIFY_STANDARD.md`
- `docs/DEFERRED_SYSTEM_IDEAS.md`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/AGENT_LIBRARY_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/INCREMENTAL_REENTRY_STANDARD.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `agent-library/README.md`
- `agent-library/PROJECT_INDEX.md`
- `skills/PROJECT_INDEX.md`
- `skills/registry.md`
- `workflow-templates/universal-project-v1/README.md`
- `workflow-templates/project-entrypoint/GITHUB_PROJECT_TEMPLATE.md`
- `workflow-templates/project-entrypoint/NOTION_PROJECT_TEMPLATE.md`
- `workflow-templates/project-bootstrap/AGENTS_TEMPLATE.md`
- `workflow-templates/project-bootstrap/PROJECT_TEMPLATE.md`
- `workflow-templates/incremental-reentry/`
- `knowledge-library/README.md`
- `knowledge-library/PROJECT_INDEX.md`
- `CHANGELOG.md`
- `logs/WORKFLOW_LOG.md`

## Project Folder Standard

Default model:

Every intentionally created real project folder should receive local Git bootstrap.

GitHub, Notion, and Google Drive are attached only when the project actually needs those layers.

Internal project folders under:

`projects/<project-id>/`

are allowed for compact or intentionally internal work and must use the parent repository Git layer unless a separate explicit decision authorizes nested Git.

Public repositories should be treated as an explicit user choice, not the default.

## Entry And Context Rule

The constitutional entry order is:

```text
START_HERE.md
→ docs/ROUTER.md
→ PROJECT.md
→ existing project index if useful
→ minimum additional files needed for the task
```

## Capability Composition Rule

Reusable functionality should follow:

```text
domain block
→ capability contract
→ versioned capability implementation
→ workflow composition
→ application adapter and UI
```

The domain block decides and reviews.

The capability block performs one bounded action.

The workflow composes actions.

The application owns product-specific behavior.

## Zero-State And Active-State

Zero-state bootstrap:

```text
PROJECT.md
AGENTS.md    # optional for internal subprojects
```

After the first meaningful execution step:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

## Current Status

The central repository is an active transfer-ready project with committed continuity artifacts.

The lightweight bootstrap model was smoke-tested with temporary project `Test123`; the owner reports that the temporary test project has been deleted.

The composable capability-block architecture is recorded as `candidate_v1`. The first validation target is the media chain registered in `capability-library/REGISTRY.md`.

## Next Required Action

Implement and validate the first deterministic local capability block, preferably `media.probe`, before promoting the capability architecture beyond candidate status.