# AI-Ready Documentation Package Standard

## Purpose

This standard defines the default output package for repository-focused documentation work.

## Default Package

The default AI-ready documentation package contains:

- `README.md`
- `PROJECT.md`
- `PROJECT_STATE.md`
- `PROJECT_RULES.md`
- `docs/CODEX_HANDOFF.md`

## Intent

This package should help:
- a human reader understand the repository quickly;
- a maintainer recover project state;
- an AI executor avoid unsafe edits;
- a reviewer judge whether future changes are acceptable.

## Package File Roles

### README.md

The short front door.

Should explain:
- what the repository is;
- why it exists;
- the shortest useful local preview or run path when relevant;
- the highest-signal repository map;
- where deeper maintainer docs live.

### PROJECT.md

The fast maintainer entry document.

Should explain:
- what this project is;
- current stage;
- entry rules;
- current next step.

### PROJECT_STATE.md

The state recovery file.

Should preserve:
- confirmed decisions;
- generated vs committed vs reviewed vs active state;
- open questions;
- next step.

### PROJECT_RULES.md

The repository-specific constraint layer.

Should preserve:
- content preservation rules;
- sensitive-domain rules;
- tooling cautions;
- review rules;
- state rules that must survive across chats.

### docs/CODEX_HANDOFF.md

The repository-local executor handoff template.

Should define:
- allowed scope;
- forbidden changes;
- validation expectations;
- execution report expectations.

## Rule

Use the full package only when it is actually useful.

Compact documentation work may produce a subset first and expand only when the repository proves it needs more structure.
