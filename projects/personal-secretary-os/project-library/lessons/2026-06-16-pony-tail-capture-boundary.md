# Lesson: Ponytail Research Must Be Captured Durably, Not Only In ChatGPT Memory

Date: 2026-06-16
Project: `personal-secretary-os`
Type: workflow lesson
Lifecycle status: captured

## Context

The owner asked to preserve the result of a research discussion about `DietrichGebert/ponytail`, an open-source project/skill pattern for reducing coding-agent overengineering and cost.

The first response stored the note only in ChatGPT memory. The owner correctly challenged this by asking where it was recorded and then confirmed that it must be done properly.

## Lesson

For secretary mode, owner wording such as `запиши`, `сохрани`, `чтобы не забылось`, or equivalent preservation intent must trigger durable capture under `docs/AUTOMATIC_CAPTURE_STANDARD.md`.

A ChatGPT memory entry can be useful, but it is not durable project/system capture and must not be reported as if it were the proper storage layer.

## Correct Handling

When preserving reusable project or system knowledge:

1. classify the material as project-specific, system-wide, or both;
2. store central reusable knowledge in `knowledge-library/` when it has cross-project value;
3. store project-specific lessons inside the active project when it affects that project;
4. report exact files created or updated;
5. clearly distinguish ChatGPT memory from GitHub/Notion/files.

## Applied Fix

The Ponytail finding was captured centrally as:

`knowledge-library/patterns/ponytail-minimal-coding-agent-mode.md`

This project-specific lesson records the secretary workflow failure and correction.

## Reuse Trigger

Load this lesson when the owner asks the secretary to save, record, remember, preserve, or not lose a finding, idea, decision, source, or project insight.

## Boundary

Do not store secrets, raw private intake, personal documents, unredacted scans, sensitive identifiers, or raw health data in GitHub.
