# Notion Agent Workspace Research Report — 2026-06-09

## Research Question

What existing Notion, GitHub, MCP, and automation solutions can serve as donors for a Project Execution OS Notion layer where any authorized agent can connect to any project through a stable project identity and standard workspace contract?

## Confirmed Existing Project State

Project Execution OS already treated Notion as an optional readable management layer rather than as a universal mandatory layer.

The repository already contained:

- `docs/integrations/notion/README.md`
- `workflow-templates/project-entrypoint/NOTION_PROJECT_TEMPLATE.md`
- layer-aware source-of-truth rules in `docs/PROJECT_LIFECYCLE_MODEL.md`
- mandatory reuse-first rules in `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

This new block extends those existing rules. It does not replace them.

## Confirmed External Donors

### Official Notion API

Notion provides an official API for pages, databases or data sources, blocks, comments, users, search, properties, and controlled writes.

Implication:

Use native Notion properties and keep schemas simple enough for reliable agent writes.

### Official Notion MCP

Notion provides an official MCP path for AI-agent access. Hosted OAuth and Markdown-oriented editing are suitable donors for agent re-entry and low-friction updates.

Implication:

Support MCP and raw API as alternative access paths, but validate exact runtime capabilities before promising parity across clients.

### Native Notion GitHub Integration

Notion provides a GitHub integration for issue and pull-request visibility.

Implication:

Start with native visibility before custom two-way synchronization.

### Donor Automation Patterns

Useful donor patterns exist through:

- Unito GitHub and Notion sync;
- GitHub Marketplace action `Notion 2 Issue`;
- n8n GitHub and Notion workflows;
- official and community MCP repositories.

Implication:

Do not build custom synchronization first. Define field ownership and conflict behavior before automation.

## Architectural Decision

Create a reusable `blocks/notion/` candidate block inside Project Execution OS.

The block must preserve the existing layer-aware model:

- Notion owns readable management truth when attached;
- GitHub owns code, technical files, commits, pull requests, and Codex implementation evidence when attached;
- local Git owns local execution history before GitHub attachment;
- asset layers own heavy source files;
- Chat owns current discussion only until a durable update is written.

## Implemented MVP

### GitHub Reusable Block

Created:

- `blocks/notion/BLOCK.md`
- `blocks/notion/WORKSPACE_CONTRACT.md`
- `blocks/notion/DATABASE_SCHEMA.md`
- `blocks/notion/AGENT_RULES.md`
- `blocks/notion/READY_SOLUTIONS.md`
- `blocks/notion/VALIDATION_BACKLOG.md`
- `blocks/notion/REFERENCES.md`
- this research report

### Live Notion Scaffold

Created live Notion workspace page:

- `Project Execution OS — Agent Workspace`

Created live Notion databases:

- Projects
- Tasks
- Research
- Decisions
- Assets
- Links
- Logs
- Knowledge Extracted
- Agent Notes

Created initial Projects record:

- `PROJECT_ID = project-execution-os`

## What Was Reused

- existing Project Execution OS layer-aware lifecycle model;
- existing Notion integration standard;
- existing Notion project entrypoint template;
- official Notion API and MCP;
- native Notion GitHub integration;
- donor sync patterns from Unito, n8n, and GitHub Marketplace.

## What Was Adapted

- standardized `PROJECT_ID` as the stable cross-system key;
- added workspace contract for fresh-agent re-entry;
- added explicit truth-map field instead of forcing one global source of truth;
- added lightweight central databases and an `Agent Notes` extension;
- delayed complex relations and two-way sync until a real project validates the basic flow.

## Risks

- MCP and connector capabilities differ across clients.
- Two-way sync can create conflicts and duplicate truth.
- Overly complex database relations can make agent writes fragile.
- Workspace-wide permissions can be broader than necessary.
- Notion API and MCP behavior can change over time.

## Recommended Next Test

1. Review and merge the GitHub block PR.
2. Use the live Notion `Projects` database to enter `project-execution-os` by `PROJECT_ID`.
3. Ask a fresh agent to find the project, read the truth map, and identify the next safe action.
4. Add one real task and one log entry.
5. Decide whether native GitHub visibility is enough before adding sync automation.

## Final Recommendation

Proceed with Notion as the universal readable agent workspace layer for projects that need it.

Do not create a separate Notion operating system.

Project Execution OS remains the operating system.