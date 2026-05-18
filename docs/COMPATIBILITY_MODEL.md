# Compatibility Model — Project Execution OS

## Tool-Neutral Core

The internal skill format is the source of truth.

The core format must remain independent from:

- ChatGPT;
- Codex;
- Claude;
- Cursor;
- Gemini CLI;
- any single vendor ecosystem.

## Adapter Philosophy

Environment-specific adapters are outputs, not the source of truth.

The central system should preserve one stable internal model and translate outward only when needed.

## Current Compatibility Targets

Planned or supported targets may include:

- ChatGPT
- Codex
- Claude
- local AI agents
- project-specific agents

## Adapter Rules

Adapters must:

- preserve meaning;
- preserve constraints;
- preserve workflow boundaries;
- preserve evidence rules;
- preserve review and lifecycle semantics.

## Out-of-Scope Rule

This compatibility model does not justify premature runtime creation, automatic adapter generation, orchestration engines, or marketplaces.
