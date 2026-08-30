# Capability Library Layer Standard v0.1

## Status

`deprecated — historical architecture note`

## Replaced By

Use the current routed architecture instead:

- `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md` for reusable executable capability blocks;
- `skills/PROJECT_INDEX.md` and the skill lifecycle for reusable instruction-backed skills;
- `blocks/PROJECT_INDEX.md` for reusable domain blocks;
- `docs/CONTEXT_ASSEMBLY_STANDARD.md` for selective context loading;
- `docs/ROUTER.md` for live discovery and routing.

Do not revive the generic capability-record layer as a parallel registry unless a new reviewed requirement proves that the current distinct block/skill/capability architecture cannot represent the needed behavior.

The content below is retained only as historical design evidence.

## Purpose

This standard defines the lightweight middle layer between a thin agent and execution tools.

The goal is to prevent agents from becoming storage dumps for MCP servers, skills, prompts, workflows, commands, and tool procedures.

Instead, reusable capabilities live as structured records and are selected only when relevant.

## Core Model

```text
Thin Agent
  -> Capability Search
  -> Capability Record
  -> Load Minimal Relevant Context
  -> Execute / Handoff / Review
  -> Usage Log + Promotion/Demotion
```

## Definition

A capability is a reusable operational unit that helps the assistant perform a bounded class of work.

Russian definition:

Capability — это переиспользуемая рабочая единица: skill, workflow, MCP, prompt, command, agent, checklist, standard, or reference package, which can be selected by context and loaded only when needed.

## Why This Exists

Agents should keep only:

- routing logic;
- judgment logic;
- orchestration logic;
- current task context.

Agents should not permanently contain:

- every MCP server instruction;
- every skill;
- every workflow;
- every reusable prompt;
- every tool procedure;
- every project-specific operating rule.

## Capability Record Contract

Every capability record should contain:

- name
- type
- purpose
- trigger_conditions
- when_to_use
- when_not_to_use
- required_inputs
- output_contract
- tools_needed
- dependencies
- risks
- validation_method
- usage_examples
- source_url
- last_reviewed_at
- promotion_status

## Capability Types

Allowed initial types:

- skill
- MCP
- workflow
- prompt
- command
- agent
- reference
- standard
- checklist

## Selection Rule

Before starting a non-trivial project, research, review, or execution handoff, the assistant should check whether an existing capability record fits the task.

If a record fits, load only the minimum relevant instructions from that record.

If no record fits, continue without inventing a fake capability.

## Anti-Bloat Rule

Do not load the entire capability library into the prompt.

Do not attach a capability just because it is related.

Use the smallest record that changes the quality of the current task.

## Promotion Rule

Reference ideas may be promoted into capability records only after they show repeatable usefulness.

A capability record may later be promoted into:

- Project Execution OS standard;
- CKL entry;
- Codex handoff pattern;
- agent module;
- reusable skill package.

## Demotion Rule

If a capability repeatedly causes confusion, context bloat, wrong routing, or unused instructions, demote it back to reference status or archive it.

## MVP Scope

The first MVP contains only three capability records:

1. Research Capability
2. Codex Handoff Capability
3. Plugin / Skill Analysis Capability

Do not build a large universal skill system until these three records prove value in real use.

## Evidence Rule

Do not claim that a capability improves workflow quality without evidence.

Acceptable evidence:

- reduced prompt size;
- fewer repeated instructions;
- clearer routing;
- fewer Codex handoff failures;
- faster task startup;
- better execution reports;
- reusable output across multiple projects.

## Final Rule

This historical artifact is not an active operating standard.

Current PEOS routing, domain blocks, skills, executable capability blocks, and context-assembly standards own the responsibilities that this early generic capability layer attempted to combine.