# Source Evidence — External Pattern Research Module

## Primary Donor Source

- Source: https://github.com/anthropics/knowledge-work-plugins
- Inspected: 2026-05-25
- Role: structural donor reference for file-based agent/skill modules.

## Confirmed Source Artifacts Inspected

- `product-management/.claude-plugin/plugin.json`
  - Confirmed a small manifest declaring plugin name, version, description, and author.
- `product-management/.mcp.json`
  - Confirmed a separate declaration of MCP/tool integrations.
- `product-management/skills/write-spec/SKILL.md`
  - Confirmed a skill file with frontmatter, trigger-oriented description, workflow, output expectations, constraints, and tool-aware behavior.
- `product-management/commands/brainstorm.md`
  - Confirmed an explicit command workflow separated from background skill material.

## Structural Pattern Borrowed

The following pattern is adapted into Project Execution OS:

- portable capability folders;
- small manifest file;
- explicit separation between reusable background skill guidance and directly invoked command workflows;
- optional connector declaration kept separate from skill instructions;
- Markdown-first inspectable modules that can be understood without hidden chat context.

## Deliberately Not Copied

Not copied into the internal standard or this module:

- Anthropic product naming and Claude-specific folder naming requirements;
- product-management content itself;
- specific MCP server selections;
- assumptions that a named connector is available;
- broad plugin marketplace or runtime architecture;
- role-specific workflow language not needed for Oleg's current system.

## Adaptation Decision

Decision: `adapt-candidate`.

Reason: Oleg repeatedly evaluates public repositories, public tools, workflows, and architectural patterns for adaptation into Project Execution OS, CKL, Agent Network OS, Website Design System, and product MVPs. The task is recurring and benefits from a reusable bounded skill plus an explicit command.

## Validation State

- Source pattern inspected: confirmed.
- Internal format standard created: confirmed in `docs/AGENT_MODULE_FORMAT_STANDARD.md`.
- Candidate module created: confirmed in `agent-modules/external-pattern-research/`.
- Real post-creation validation case: not yet completed.

## Promotion Requirement

Do not change this module from `candidate` to `tested` or `promoted` until it is used on one new real external-source analysis and the resulting decision/output is recorded.
