---
name: chrome-web-store-publication-readiness
description: Prepare Chrome extension release documents and validation gates.
category: documentation
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - extension_repository
  - manifest_file
  - behavior_evidence
outputs:
  - readiness_report
  - listing_draft
  - test_instructions
safety_level: medium
source: extracted_from_Voice-Button_issue_2
review_status: not_reviewed
version: 0.1.0
---

# Chrome Web Store Publication Readiness

## Purpose

Prepare release documents for a Chrome extension from current project evidence.

## When to Use

Use when an extension needs store preparation or tester delivery preparation.

## Inputs

- repository state;
- current manifest;
- current product behavior;
- available test results.

## Outputs

- readiness report;
- listing draft;
- asset checklist;
- test instructions;
- explicit blockers.

## Workflow

1. Inspect current project files.
2. Record actual product purpose and access needs.
3. Draft store materials from evidence.
4. Record missing inputs and manual checks.
5. Keep readiness blocked until required checks exist.

## Constraints

- Use official Chrome documentation.
- Do not invent test results or product capabilities.
- Do not claim release completion without evidence.

## Failure Modes

- Draft text exceeds actual behavior.
- Required manual checks are missing.
- A candidate skill is treated as active before review.

## Validation Checklist

- Manifest reviewed.
- Product purpose stated.
- Open blockers recorded.
- Status remains candidate until review.

## References

See `references.md`.
