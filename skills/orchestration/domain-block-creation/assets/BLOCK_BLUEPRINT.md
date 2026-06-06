# Domain Block Blueprint

## Level Selection

Choose one:

```text
reference note
compact block
full block
no new artifact
```

## Compact Block

```text
blocks/<domain>/
  BLOCK.md
  REFERENCES.md
  VALIDATION_BACKLOG.md
```

## Full Block

```text
blocks/<domain>/
  BLOCK.md
  PRODUCT_SURFACES.md
  WORKFLOW_PIPELINE.md
  READY_SOLUTIONS.md
  TOOL_SELECTION_MATRIX.md
  SECURITY_AND_COMPLIANCE.md
  MONETIZATION_AND_PAYMENTS.md        # only when relevant
  CURRENT_CAPABILITIES_<date>.md      # only when freshness matters
  VALIDATION_BACKLOG.md
  REFERENCES.md
  RESEARCH_REPORT_<date>.md
```

## BLOCK.md Template

```text
# <Domain> Block

## Purpose

## Status

`candidate`

## When To Use

## When Not To Use

## Core Rule

## Required Reading Inside This Block

Open only the smallest relevant path.

## Typical Outputs

## Boundary

## Final Rule
```

## Completion Checklist

```text
BLOCK.md exists
-> route registered in docs/ROUTER.md
-> blocks/PROJECT_INDEX.md updated
-> reusable knowledge captured when justified
-> generated index refresh confirmed
-> validation backlog exists
-> status remains candidate until real use validates it
```
