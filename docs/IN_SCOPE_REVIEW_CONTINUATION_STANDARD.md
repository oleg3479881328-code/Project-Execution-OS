# In-Scope Review Continuation Standard

## Purpose

This standard defines how an execution agent handles review follow-up inside an active approved task.

## Core Rule

A review follow-up that remains inside the already approved task scope is a continuation of the active task.

It is not a new owner decision request.

The execution agent continues from the latest bounded review instruction in the registered active channel.

## Routine Continuation Examples

Routine continuation includes:

- narrow fixes requested during review;
- validation runs already required by the task;
- bookkeeping updates to coordination state and logs;
- execution reports required by the active task;
- small documentation corrections needed to close the reviewed task.

## Owner Escalation Boundary

Return to the owner only when the next action requires one of the following:

- scope expansion;
- destructive action;
- repository visibility change;
- external publication;
- business decision;
- unresolved ambiguity that cannot be resolved from repository standards.

## Owner Trigger Rule

The owner is the trigger, not the courier.

When the owner sends `02`, read the registered active channel, inspect the latest relevant message and repository state, and continue from the next authorized in-scope step.

Do not ask the owner to relay routine agent-to-agent messages.

## Final Rule

In-scope review follow-up continues through the registered active channel until acceptance or a real owner escalation condition is reached.