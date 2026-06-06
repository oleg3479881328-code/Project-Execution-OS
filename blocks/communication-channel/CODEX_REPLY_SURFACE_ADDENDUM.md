# Codex Reply Surface Addendum

Updated: 2026-06-06
Status: `active`

## Purpose

Clarify how Codex must use the selected GitHub channel during bounded execution.

## Rule

When GitHub is the active channel and a handoff packet names an issue, pull request, or review thread, Codex must treat that surface as the live bidirectional reply channel.

Codex must post there:

- an immediate signed acknowledgement;
- any clarification question;
- any blocker report;
- the final execution report;
- commit SHA and draft PR URL when changes are published for review.

Codex must not wait silently for the owner to prompt it after local work is complete.

## Default Flow

`handoff -> acknowledgement -> execute -> validate -> private branch -> draft PR -> report in same GitHub surface`

## Final Rule

The GitHub surface is not only storage for the task. It is the active conversation channel.