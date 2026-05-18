---
name: workflow-state-machine
description: Define deterministic workflow states and valid state transitions for repository workflows.
category: orchestration
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - workflow_artifact
  - current_state
  - workflow_context
outputs:
  - state_transition_decision
  - allowed_next_states
  - blocked_transitions
  - workflow_status_summary
safety_level: medium
source: migrated_from_3TestAgents
review_status: reviewed_with_required_improvements
version: 0.1.0
---

# Purpose

Define deterministic workflow states and valid transitions for repository workflows.

# Important Rule

This is a lightweight governance layer.

It is not a BPM engine.

Keep the state model minimal.

# Standard Workflow States

- draft
- clarifying
- reviewing
- approved
- handoff_ready
- executing
- execution_review
- accepted
- persisted
- blocked
- archived

# Transition Rules

- execution is forbidden before approval or handoff readiness
- persistence is forbidden before verification
- blocked state should not be skipped silently

# Constraints

Do not:
- allow execution before approval;
- allow persistence before verification;
- silently skip blocked state;
- introduce unnecessary states;
- turn the workflow into enterprise bureaucracy.

# Failure Modes

Possible failures:
- too many states;
- too many gates;
- workflow paralysis;
- invalid transitions silently accepted;
- state confusion.

# Validation Checklist

Before finalizing:
- current state identified;
- requested transition identified;
- transition validated;
- blocked transitions explained;
- minimal workflow selected.

# References

See `references.md`.
