# Executor Handoff Standard Addendum — 2026-06-06

## Purpose

Apply one communication rule to every execution agent.

## Required Companion Standard

Use:

`docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`

## Mandatory Handoff Fields

Every executor handoff must name:

- active reply surface;
- allowed scope;
- forbidden changes;
- required validation;
- publication mode;
- execution-report format.

## Default Publication Mode

For bounded repository implementation work:

`reviewable_repository_change`

Meaning:

`acknowledge -> implement -> validate -> minimal commit -> private review branch -> draft PR -> structured report in the same reply surface`

## Final Rule

The owner approves scope. Any executor handles routine in-scope publication and reports directly through the registered durable channel.