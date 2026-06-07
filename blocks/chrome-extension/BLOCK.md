# Chrome Extension Block

## Purpose

Provide a reusable Project Execution OS domain layer for planning, researching, designing, building, monetizing, publishing, and reviewing browser extensions, with Chrome Manifest V3 as the default baseline.

This block is for recurring extension work across projects, not for one-off Chrome Extension trivia.

## Status

`candidate`

This block is researched and ready for first real use, but remains candidate until at least one extension project validates the workflow end to end.

## When To Use

Use this block for:

- Chrome Extension product ideas;
- browser-extension architecture;
- Manifest V3 decisions;
- content scripts, background service workers, popup UI, options UI, side panel, storage, permissions, and host access;
- extension + SaaS architecture;
- AI/browser-assistant extensions;
- scraper, productivity, learning, automation, or page-enhancement extensions;
- Chrome Web Store publication;
- extension monetization, licensing, subscriptions, and payment-provider selection;
- security, privacy, and Web Store policy review for extensions.

## When Not To Use

Do not use this block for:

- general website design without an extension surface;
- Telegram, mobile apps, or desktop apps;
- a one-off question answerable from official docs;
- instructions that require bypassing website access controls, paywalls, anti-bot systems, or user consent;
- harvesting browsing data without a clear user-facing purpose and privacy basis.

## Core Rule

Existing solution first: check official Chrome documentation, ready frameworks, starter templates, and proven architecture patterns before inventing a custom extension stack.

Default stack for new product work:

`WXT + TypeScript + React + Tailwind + Manifest V3`

Use a simpler starter only when the extension is intentionally minimal.

## Required Reading Inside This Block

Smallest useful path:

1. `BLOCK.md`
2. `READY_SOLUTIONS.md`
3. `TOOL_SELECTION_MATRIX.md`
4. `ARCHITECTURE_PATTERNS.md`
5. `SECURITY_AND_COMPLIANCE.md`
6. `READY_SAAS_STACKS.md` when backend, auth, AI, affiliate, payments, or SaaS architecture matter
7. `MONETIZATION_AND_PAYMENTS.md` when monetization matters
8. `PUBLISHING.md` before Chrome Web Store work
9. `VALIDATION_BACKLOG.md` before treating research as verified
10. `REFERENCES.md` when source freshness or authority matters

Do not load every file by default. Load the smallest path that fits the task.

## Typical Outputs

- extension concept brief;
- ready-solution comparison;
- tool-selection decision;
- ready SaaS stack recommendation;
- architecture outline;
- MVP scope;
- security/privacy checklist;
- monetization model;
- payment-provider recommendation;
- Chrome Web Store readiness checklist;
- implementation handoff;
- review report.

## Boundary

This block stores reusable domain knowledge only.

Do not store API keys, payment credentials, merchant account details, customer data, private extension analytics, or project-specific confidential information here.

Keep unstable external facts in dated research reports or references, not as permanent rules.

## Final Rule

For extension work, first choose the smallest proven path. Prefer a maintained framework and narrow permissions over custom architecture and broad access.