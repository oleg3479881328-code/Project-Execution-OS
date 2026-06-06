# Telegram Product Stack

Type: `architecture-decision`
Lifecycle status: `candidate`
Captured: 2026-06-06

## Reusable Lesson

Telegram products should be routed by the smallest suitable platform surface rather than treated as one generic bot implementation.

Use:

`goal -> user journey -> Telegram surface -> existing solution -> security review -> validation -> handoff`

## Entry Point

Use:

`blocks/telegram/BLOCK.md`

## Applies To

Telegram bots, Mini Apps, Telegram Login, Gateway verification, Stars payments, business workflows, bot builders, and custom-client decisions.

## Final Rule

Reuse official Telegram capabilities and validated donor solutions before custom implementation.