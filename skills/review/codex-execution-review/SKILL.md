---
name: codex-execution-review
description: Validate Codex execution results against the original implementation handoff packet before accepting repository changes.
category: review
status: candidate
target_agent: tool-neutral
compatibility:
  - codex
  - chatgpt
  - claude
inputs:
  - implementation_handoff_packet
  - execution_report
  - changed_files_or_diff
outputs:
  - execution_review
  - scope_drift_analysis
  - acceptance_validation
  - governance_findings
  - final_execution_verdict
safety_level: medium
source: migrated_from_3TestAgents
review_status: reviewed_with_required_improvements
version: 0.1.0
---

# Purpose

Review execution results after implementation work and before repository acceptance, merge, promotion, or memory persistence.

# Core Principle

Execution is not verification.

# When to Use

Use this skill after:
- repository files were modified by an executor;
- an execution report is returned;
- acceptance criteria must be verified.

# Workflow

1. Validate the original handoff packet.
2. Validate the execution report.
3. Review changed file scope.
4. Check each acceptance criterion.
5. Check validation evidence.
6. Scan for scope drift.
7. Review governance.
8. Review rollback safety.
9. Return one final verdict.

# Hard Constraints

Do not:
- trust execution claims without evidence;
- approve out-of-scope repository mutations silently;
- confuse generated state with executed state;
- ignore skipped validations;
- treat partial completion as full success.

# Failure Modes

Possible failures:
- reviewer trusts execution blindly;
- reviewer ignores file drift;
- hidden architecture rewrite passes review;
- governance violations ignored.

# Validation Checklist

Before finalizing review:
- original packet reviewed;
- execution report reviewed;
- changed files checked;
- acceptance criteria validated;
- validation evidence checked;
- governance reviewed;
- rollback assessed;
- verdict selected from allowed values.

# References

See `references.md`.
