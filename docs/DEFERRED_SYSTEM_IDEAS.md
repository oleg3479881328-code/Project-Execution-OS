# Deferred System Ideas

## Purpose

This document preserves important `Project Execution OS` ideas that are intentionally deferred so they do not disappear between chats, reviews, or live project work.

Use this file for:

- central-brain ideas;
- system architecture ideas;
- future coordination/runtime layers;
- improvements that are clearly valuable but not justified yet.

Do not use this file for:

- active work already scheduled in a real workflow run;
- vague brainstorming noise;
- project-specific backlog items that belong inside a dedicated project repository.

Project-specific deferred work should live in that project's own repository memory.

## Status Meanings

- `deferred` = valuable, but intentionally not now
- `watch` = not approved, but worth observing
- `promoted` = moved into active planning elsewhere
- `rejected` = intentionally not part of the OS roadmap

## Required Entry Shape

Each deferred idea should capture:

- `Idea`
- `Status`
- `Why It Matters`
- `Why Deferred Now`
- `Revisit Trigger`
- `Promotion Path`

---

## 001 - Runtime Bridge Between Reasoning Model And Codex

- `Status`: `deferred`
- `Idea`: create a direct runtime bridge so a reasoning model can hand a bounded execution packet to Codex without relying only on GitHub issue or PR transport.
- `Why It Matters`: this could reduce manual coordination overhead, shorten execution latency, and make the central brain usable by more automation systems later.
- `Why Deferred Now`: the GitHub-based transport model is already working in live testing and should remain the default until repeated operational friction proves that a direct execution bridge is worth the added complexity and safety burden.
- `Revisit Trigger`: promote this idea when repeated real projects show that GitHub transport is too slow, too manual, too fragile, or too expensive in operator attention.
- `Promotion Path`: if promoted, first define a small `runtime bridge` contract and safety rules in a standalone standard before building any service, daemon, or automation layer.

## 002 - Rule For Future Additions

- `Status`: `watch`
- `Idea`: keep this document as the central parking place for validated "not now" system ideas so they survive chat resets and do not get mixed into active workflow runs prematurely.
- `Why It Matters`: the OS needs a memory layer for deferred central ideas, not only active standards and active projects.
- `Why Deferred Now`: no extra implementation is needed beyond maintaining this file consistently.
- `Revisit Trigger`: if the list grows large, split it into categories or introduce review cadence.
- `Promotion Path`: promote individual entries into active documents, workflow runs, or standards when they become justified.
