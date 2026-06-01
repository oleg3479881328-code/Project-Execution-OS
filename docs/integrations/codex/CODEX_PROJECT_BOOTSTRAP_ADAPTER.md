# Codex Project Bootstrap Adapter

## Status

Automatic bootstrap for every opened folder is still withdrawn.

Intentional creation of a real new project folder now triggers the minimum project bootstrap defined by `docs/PROJECT_BOOTSTRAP_STANDARD.md`.

## Current Rule

Creating or opening a folder or Codex Desktop project does not automatically require project files.

When the owner intentionally creates a real new project folder, the minimum bootstrap creates:

```text
git init
AGENTS.md
PROJECT.md
```

## Reason

The previous broad automatic bootstrap experiment introduced unwanted overhead and complexity. The preferred model is narrow, intentional, and minimal.

## Preserved Principle

`docs/EXISTING_SOLUTION_FIRST_STANDARD.md` remains the canonical rule for relevant project, research, architecture, implementation and debugging work.

## Related Nodes

- `START_HERE.md`
- `Start New Project.md`
- `docs/PROJECT_BOOTSTRAP_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
