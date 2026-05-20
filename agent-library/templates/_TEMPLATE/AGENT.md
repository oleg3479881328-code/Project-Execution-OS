name: TEMPLATE
role_type: TEMPLATE
purpose: TEMPLATE
when_to_use:
  - TEMPLATE
when_not_to_use:
  - TEMPLATE
default_orchestration_mode: single_agent
inputs:
  - repository_context
outputs:
  - artifact_or_decision
context_needed:
  - minimum_required_context_only
context_not_needed:
  - full_history_by_default
constraints:
  - no_fake_execution
  - evidence_first
handoff_rules:
  - state_if_this_agent_can_handoff
review_rules:
  - state_if_output_requires_review
evidence_rules:
  - separate_facts_assumptions_recommendations
failure_modes:
  - vague_scope
  - excess_context
lifecycle_state: candidate
version: 0.1.0
