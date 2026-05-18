---
name: implementation-handoff-packet
description: Create deterministic execution packets for handing architecture or specifications to Codex or another implementation agent.
category: implementation
status: candidate
target_agent: codex
compatibility:
  - codex
  - chatgpt
  - claude
inputs:
  - approved_design_or_specification
  - repository_context
  - intended_execution_scope
outputs:
  - execution_packet
  - acceptance_criteria
  - execution_report_contract
  - rollback_notes
  - reviewer_checklist
safety_level: medium
source: migrated_from_3TestAgents
review_status: reviewed_with_required_improvements
version: 0.1.0
---

# Purpose

Create a deterministic implementation handoff packet between a design artifact and Codex or another implementation agent.

# When to Use

Use this skill when:
- an approved design must be implemented;
- an executor needs a precise execution packet;
- repository files may be changed;
- acceptance criteria must be explicit;
- implementation work must be reviewable.

# Hard Rules

The packet must:
- be specific;
- define exact scope;
- list allowed files or file areas;
- list forbidden changes;
- define acceptance criteria;
- define execution report format;
- separate generated state from executed state;
- require blocker reporting instead of guessing.

The packet must not:
- ask the executor to redesign the system;
- allow unrelated cleanup;
- allow broad refactoring without explicit approval;
- imply completion before verification.

# Packet Types

- `FILE_CREATE`
- `FILE_UPDATE`
- `REFACTOR_LIMITED`
- `TEST_ADD_OR_UPDATE`
- `DOC_UPDATE`
- `VALIDATION_ONLY`

# Failure Modes

Possible failures:
- packet too broad;
- missing file list;
- missing acceptance criteria;
- unrelated files changed;
- success claimed without validation.

# Validation Checklist

Before finalizing a handoff packet:
- packet ID exists;
- packet type is selected;
- objective is singular;
- scope is explicit;
- out-of-scope is explicit;
- files allowed to change are listed;
- forbidden changes are listed;
- acceptance criteria are testable;
- execution report contract is included;
- rollback notes are included.

# References

See `references.md`.
