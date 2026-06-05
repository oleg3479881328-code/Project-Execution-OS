# Channel Transition Handshake Standard

## Purpose

This standard prevents silent channel switches during AI-to-AI coordination.

A new GitHub issue, pull request, or review thread must not become the active coordination channel without an explicit handoff trail.

## Core Rule

Never switch channels silently.

When work moves from one durable GitHub surface to another, complete the following handshake:

```text
post redirect notice in previous active channel
-> post origin notice in new channel
-> update AI_COORDINATION_STATE.md Active Channel
-> move the old surface into Previous Channels
-> append a Channel Transition event to AI_COORDINATION_LOG.md
-> require executor acknowledgement in the new channel
```

## Redirect Notice

The previous active channel must receive a short signed message that states:

- the previous channel is no longer active for routine execution reporting;
- the exact new active channel URL;
- the executor should continue in the new channel.

## Origin Notice

The new channel must receive a short signed message that states:

- this is the active durable coordination channel;
- the previous relevant channels;
- the current bounded task;
- where acknowledgements, blockers, commits, validation evidence, and execution reports must be posted.

## Snapshot Rule

`AI_COORDINATION_STATE.md` must be updated as part of the transition.

The snapshot must clearly identify:

- the new `Active Channel`;
- the previous channel in `Previous Channels`;
- the current task;
- the next step;
- the requirement that routine follow-up continues in the new channel.

## Log Rule

Append a meaningful `Channel Transition` event to `AI_COORDINATION_LOG.md`.

Do not rewrite previous events.

## Acknowledgement Rule

The executor must post acknowledgement in the new channel before continuing routine execution reporting there.

## Scope Boundary

This standard applies whenever the active durable transport changes, including:

- long-thread continuation;
- transition from implementation issue to PR review;
- transition from merged PR to the next implementation issue;
- project phase change;
- migration between issue, PR, review thread, or cross-repository coordination hub.

## Final Rule

A new channel is not active until the redirect, origin notice, snapshot update, log append, and executor acknowledgement are all part of the durable coordination trail.