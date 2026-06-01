# Existing Solution First Standard

## Purpose

This standard defines the mandatory reuse-first rule for Project Execution OS.

Before creating a new solution, the executor must first check whether an adequate existing solution already exists and can be reused or adapted.

## Core Invariant

Use this operating rule:

```text
Search before invention.
Adapt before rebuilding.
Build from scratch only when no adequate existing solution exists
or when adaptation is demonstrably worse for the current task.
```

Also use this execution refinement:

```text
Before custom diagnostics, workaround design, or low-level experimentation,
first search for an existing official or established solution and try the
standard path first.
```

Also assume:

```text
Assume that an adequate existing solution may already exist and check before creating a new one.
```

This is a mandatory working obligation, not a vague preference.

## Scope

Apply this rule to:

- architecture choices;
- new code;
- bug fixing;
- integrations;
- tool setup;
- automations;
- UI or UX patterns;
- library and framework selection;
- project workflows;
- AI skills, plugins, agent modules, and adapters;
- Codex, VS Code, GitHub, Notion, Google Drive, and related working-system setup.

## Search Order

Check in this order unless the task clearly requires a different first source:

1. existing solutions already present in the current project;
2. central reusable knowledge in Project Execution OS or CKL;
3. official product or technology documentation;
4. official examples or reference implementations;
5. relevant GitHub repositories or open-source projects;
6. GitHub Issues or Discussions showing real fixes and edge cases;
7. manuals or technical guides;
8. community sources such as Reddit as supporting evidence for practical problems and workarounds;
9. only then a new custom implementation.

For operational troubleshooting, debugging, repair, or environment issues:

1. first try the official or established standard path;
2. only after that fails, move into custom diagnostics, speculative workarounds, or low-level experimentation;
3. if the standard path requires elevated permissions, a restart, a vendor reset flow, a system repair tool, or another known maintenance procedure, prefer that documented path before inventing a custom one.

## Stop Rule

Use this stopping rule:

```text
Search seriously, but stop when a sufficiently adequate proven solution has been identified for the current MVP or task.
```

Do not keep searching for a perfect option after a sufficiently good proven donor or pattern has been found.

## Adaptation Rule

When an adequate donor exists:

- adapt the minimum necessary;
- keep the adaptation bounded to the current task or MVP;
- prefer verified simplification over speculative optimization;
- record what was reused, what was adapted, and what still had to be custom.

## When Custom Work Is Allowed

A custom implementation is justified only when at least one of these is true:

- no adequate existing solution was found;
- existing options are incompatible with the current task constraints;
- adaptation would cost more risk, complexity, or time than a bounded custom solution;
- reuse would create unacceptable maintenance, security, licensing, or correctness problems.

If custom work is chosen, record why.

## Evidence Shape

For non-trivial tasks, separate:

- confirmed facts;
- existing solutions checked;
- donor patterns selected if any;
- assumptions;
- custom work that still had to be created;
- risks or follow-up validation.

## Required Propagation

This rule must remain visible in the places where humans and AI actually enter work:

- `START_HERE.md` routes into standards that enforce it;
- `docs/PROJECT_BOOTSTRAP_STANDARD.md` ensures zero-state projects inherit it;
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` requires it in project constraints;
- `docs/RESEARCH_STANDARD.md` makes the search mandatory;
- `docs/CODEX_HANDOFF_STANDARD.md` requires explicit search expectations and reporting;
- `docs/REVIEW_STANDARD.md` checks that reuse was considered before custom work;
- project bootstrap artifacts and project `AGENTS.md` files should point to this standard briefly rather than copy it in full.
