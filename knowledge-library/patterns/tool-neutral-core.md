# Pattern — Tool-Neutral Core

## Status

candidate

## Source

migrated_from_3TestAgents

## Purpose

Prevent vendor lock-in.

## Pattern

The internal system format must remain independent from:
- Claude;
- Codex;
- ChatGPT;
- Cursor;
- Gemini CLI;
- any single AI ecosystem.

Environment-specific implementations are adapters, not the source of truth.

## Why This Exists

Vendor-specific architectures become fragile when tools, APIs, pricing, or execution models change.

## When to Use

Use this pattern:
- when designing skill systems;
- when building reusable workflows;
- when designing agent infrastructures;
- when supporting multiple AI ecosystems.

## When Not to Use

If a system is intentionally locked to one environment for strategic reasons.
