# Universal Project Workflow Template v1

## Purpose

This template is copied into every new project workflow run.

Target location:

projects/<project-id>/workflow-runs/<run-id>/

## Workflow Files

Each run should contain:

- 00_INPUT.md
- 01_CLARIFICATION.md
- 02_RESEARCH.md
- 03_PLAN.md
- 04_AGENT_DESIGN.md
- 05_EXECUTION_SPEC.md
- 06_REVIEW.md
- 07_RESULT.md
- 08_KNOWLEDGE_EXTRACT.md
- 09_LOG.md

## Rule

Do not skip stages without recording why.

If a stage is not needed, the file must say:

Not needed for this run.

## Output

Every workflow run must end with:

- a result;
- extracted knowledge;
- a log entry;
- one concrete next action.
