# Automatic Capture Standard

Status: Active system standard
Date: 2026-06-16

## Purpose

When the owner asks to preserve an idea, decision, lesson, or project insight, the assistant must perform durable capture instead of only summarizing it in chat.

## Trigger

Activate this workflow whenever the owner's wording clearly means: save, record, preserve, capture, remember, add to the library, add to the project, or do not lose this.

Russian examples include: зафиксируй, сохрани, запиши, чтобы не потерялось, внеси в библиотеку, добавь в проект.

The exact wording is not important. The preservation intent is the trigger.

## Required Flow

1. Classify the captured material as project-specific, system-wide, or both.
2. Check whether an active project is known.
3. Store system-wide knowledge in the Project Execution OS knowledge library.
4. Store project knowledge in the active project repository.
5. Use both locations when the material affects both the active project and future reuse.
6. Report the exact files created or updated.
7. End the response with direct links to every durable location created or updated.

## Important Rule

A chat summary alone does not count as durable capture.

## Reporting Rule

After any successful durable capture, the final user-facing response must include:

- the exact repository, document, issue, Notion page, Drive file, or other storage layer used;
- the exact path or title;
- a direct URL when the storage tool provides or allows one;
- a clear distinction between durable storage and ChatGPT memory.

Do not only say `saved`, `recorded`, or `captured` without giving the owner the location.

When multiple files or systems are updated, list every durable location separately.

## Project-Aware Default

When an active project is already being discussed, the assistant must evaluate project storage automatically. The owner should not need to issue a second reminder to save the same knowledge inside the project.

## Failure Mode To Prevent

Do not require the owner to separately remind the assistant to save first to the central library and then again to the active project.

Do not require the owner to ask where the material was saved after a capture action. The location and link belong in the completion report by default.

## Example

Owner request:

`Зафиксируй это, чтобы не потерялось.`

Expected result:

- classify the material;
- save central reusable knowledge when applicable;
- save project-specific knowledge when applicable;
- report storage locations and completion status;
- end with direct links to every created or updated durable record.
