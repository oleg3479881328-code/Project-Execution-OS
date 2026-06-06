# AI Coordination Hub Standard Addendum — Universal Executor Reply Rule

Updated: 2026-06-06
Status: `active`

## Purpose

Extend the coordination policy from Codex-specific behavior to every connected execution agent.

## Required Standard

Apply:

`docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`

## Universal Rule

Whenever any execution agent receives a bounded handoff through a registered durable channel, that agent must:

- acknowledge receipt immediately in the named reply surface;
- post clarification questions and blockers there without waiting for the owner;
- continue routine in-scope execution through the selected publication mode;
- publish a reviewable result;
- post structured evidence in the same reply surface;
- stop only at a real escalation boundary.

## Applies To

This rule applies to:

- Codex;
- DeepSeek;
- Claude;
- local models;
- specialized project agents;
- future connected executors;
- human-assisted execution workflows.

## Final Rule

The owner is the trigger, not the courier. Agents must communicate through the registered channel directly and durably.