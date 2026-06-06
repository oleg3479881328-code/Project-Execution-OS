# Agent Creation Communication Addendum

Updated: 2026-06-06
Status: `active`

## Rule

Every new execution agent must inherit:

`docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`

Its contract must define:

- reply surface;
- acknowledgement behavior;
- blocker reporting;
- publication mode;
- escalation boundary;
- execution report format.

## Final Rule

An execution agent is not ready for use until its durable communication behavior is defined.