---
name: skill-runtime-router
description: Route user requests to the correct skill pipeline and determine the required workflow sequence.
category: orchestration
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - user_request
  - repository_context
  - skill_registry
outputs:
  - routing_decision
  - selected_skills
  - workflow_sequence
  - required_gates
  - next_action
safety_level: medium
source: migrated_from_3TestAgents
review_status: reviewed_with_required_improvements
version: 0.1.0
---

# Purpose

Route a user request to the correct skill or skill pipeline.

# Core Principle

Select the smallest correct workflow that satisfies the user request, repository governance, and risk level.

# Standard Pipelines

1. Raw Idea To Specification
2. Approved Design To Execution
3. Full Repository Workflow
4. Research To Reuse
5. Execution Verification Only

# Constraints

Do not:
- route directly from vague idea to implementation;
- skip review for high-risk changes;
- run memory update before verification;
- select every skill by default;
- expand scope beyond the user request;
- treat routing as execution.

# Failure Modes

Possible failures:
- over-routing simple tasks;
- under-routing risky tasks;
- skipping memory synchronization;
- routing implementation before design approval;
- treating candidate skills as fully proven.

# Validation Checklist

Before finalizing routing:
- user request summarized;
- risk level assigned;
- selected pipeline justified;
- selected skills listed in order;
- required gates identified.

# References

See `references.md`.
