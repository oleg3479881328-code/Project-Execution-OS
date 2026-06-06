# Executor Reply Surface Addendum

Updated: 2026-06-06
Status: `active`

## Purpose

Apply one reply-surface rule to every connected execution agent.

## Required Standard

Use:

`docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`

## Rule

When a bounded handoff names a durable reply surface, that surface becomes the active bidirectional channel for the executor.

The executor must post there:

- immediate acknowledgement;
- clarification questions;
- blocker reports;
- useful status updates;
- final report;
- reviewable artifact URL;
- commit SHA and draft PR URL when repository edits are involved;
- validation evidence.

## Default Flow

`handoff -> acknowledgement -> execution -> validation -> reviewable publication -> report in same channel`

## Final Rule

This rule applies to Codex, DeepSeek, Claude, local models, specialized agents, and future executors.