# Design Picker

## Status

`initialized — active research and MVP definition`

## Purpose

Build an internal web application for visually browsing website and product-interface design donors, importing references by URL, generating previews, selecting reusable patterns, and exporting a clear design brief for agents and frontend execution.

## Project Type

Internal web application inside `Project Execution OS`.

## Operating System

This project operates under `Project Execution OS`.

Top-level entrypoint:

`START_HERE.md`

Relevant reusable block:

`blocks/design/BLOCK.md`

Relevant design-picker specification:

`blocks/design/DESIGN_PICKER.md`

`blocks/design/DESIGN_PICKER_WEB_APP.md`

## Source Of Truth

- reusable workflow and standards: `blocks/design/`
- project-specific decisions and current state: `projects/design-picker/`
- current research evidence: `projects/design-picker/RESEARCH_REPORT_2026-06-07.md`

## Confirmed Goal

The owner should be able to paste a donor URL, see a generated visual card, browse and filter donors, mark a primary or partial selection, record which patterns to reuse, reject unsuitable directions, and export the result as a design brief.

## Existing Solution First

Before custom implementation, apply:

`docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

The first research candidates are Linkwarden and Karakeep. The project must decide whether to adapt an existing solution, integrate with one, or build a bounded custom MVP only after comparing fit, licensing, complexity, and UX gaps.

## Storage Layers

- GitHub: project files, technical decisions, code when implementation begins
- Chat: active discussion
- Notion: not attached yet
- Google Drive: not attached yet

## Next Practical Step

Complete reuse-first research and record the adaptation decision.