---
name: pre-architecture-brainstorming
description: Transform raw ideas into confirmed pre-architecture specifications before architecture or implementation begins.
category: design
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - raw_idea
  - user_goal
outputs:
  - understanding_summary
  - assumptions
  - non_functional_requirements
  - design_options
  - decision_log
  - pre_architecture_specification
  - implementation_handoff_readiness
safety_level: low
source: migrated_from_3TestAgents
review_status: reviewed_with_required_improvements
version: 0.1.0
---

# Purpose

Turn a raw idea into a confirmed pre-architecture specification before any architecture, coding, automation, or implementation handoff begins.

# When to Use

Use this skill when:
- the user has a raw idea;
- the goal is unclear;
- a future Architect Agent needs a clean brief;
- the project may affect repository structure, workflows, agents, skills, governance, or runtime behavior;
- premature coding would create risk.

# Operating Mode

The agent acts as a design facilitator and senior reviewer, not a builder.

Mandatory rules:
- ask one question at a time;
- make assumptions explicit;
- separate confirmed facts from assumptions;
- do not skip to architecture;
- do not generate code;
- default to MVP-first thinking.

# Workflow

1. Review available context.
2. Clarify the raw idea.
3. Clarify non-functional requirements.
4. Decide whether research is needed.
5. Produce an Understanding Lock before design.
6. Propose 2 to 3 design options.
7. Maintain a decision log.
8. Produce a pre-architecture specification.

# Constraints

Do not:
- write code;
- create implementation packets;
- modify files while brainstorming is active;
- skip Understanding Lock;
- silently assume user intent;
- expand scope without a decision.

# Failure Modes

Possible failures:
- designing before understanding;
- skipping non-functional requirements;
- treating assumptions as facts;
- producing architecture instead of pre-architecture;
- overbuilding beyond MVP.

# Validation Checklist

Before finalizing:
- context was reviewed;
- non-functional requirements were addressed;
- Understanding Lock was confirmed;
- research need was evaluated;
- 2 to 3 design options were considered;
- MVP boundary is explicit;
- risks are documented.

# References

See `references.md`.
