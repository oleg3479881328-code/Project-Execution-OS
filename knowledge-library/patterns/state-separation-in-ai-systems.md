# Pattern — State Separation in AI Systems

## Status

candidate

## Source

migrated_from_3TestAgents

## Purpose

Prevent hallucinated execution and operational confusion.

## Pattern

The system must distinguish:
- generated state;
- committed state;
- reviewed state;
- active state.

## Why This Exists

AI systems frequently blur ideas, drafts, executed work, and approved work.

## When to Use

Use this pattern:
- in AI agent systems;
- in workflow orchestration;
- in repository-driven systems;
- in multi-agent pipelines.

## When Not to Use

Never remove state separation in systems where AI can claim execution.
