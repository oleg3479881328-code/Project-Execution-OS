# Telegram Block

## Purpose

This block gives `Project Execution OS` one reusable domain layer for Telegram-related product, automation, integration, and research work.

It helps an agent select the correct Telegram surface, reuse existing libraries and platform capabilities, define a safe architecture, prepare implementation handoff, and avoid confusing bots, Mini Apps, Telegram Login, Gateway API, MTProto, and TDLib.

## Status

`candidate`

## When To Use

Use this block when work involves:

- Telegram bots;
- AI assistants inside Telegram;
- Telegram Mini Apps;
- Telegram Business or Secretary Bots;
- Managed Bots and bot factories;
- inline bots, guest bots, groups, channels, or communities;
- Telegram Login;
- Telegram Gateway verification codes;
- Telegram Stars, subscriptions, payments, affiliate flows, or paid media;
- Telegram widgets;
- Bot API webhooks, polling, hosting, scaling, or local Bot API server;
- Telegram API, MTProto, TDLib, or custom Telegram clients;
- Telegram-specific security, privacy, moderation, and compliance;
- selection of frameworks, donor repositories, and reusable bot patterns.

## When Not To Use

Do not use this block for:

- generic backend work with no Telegram-specific decision;
- social-media strategy without a Telegram product surface;
- unofficial user-account automation that violates Telegram terms;
- storing bot tokens, API hashes, access tokens, or personal data in this repository;
- treating a community framework as an official Telegram product;
- building a custom client when the Bot API already solves the task.

## Core Rule

Choose the smallest Telegram surface that solves the actual job.

Use:

`goal -> user journey -> Telegram surface -> platform capability -> ready solution or framework -> data model -> security boundary -> monetization path -> hosting and operations -> validation -> project handoff`

## Required Reading Inside This Block

Open only the smallest relevant path:

1. `blocks/telegram/PRODUCT_SURFACES.md`
2. `blocks/telegram/CURRENT_CAPABILITIES_2026-06-06.md` when current Telegram features matter
3. `blocks/telegram/TELEGRAM_WORKFLOW_PIPELINE.md`
4. `blocks/telegram/READY_SOLUTIONS.md` before custom implementation
5. `blocks/telegram/TOOL_SELECTION_MATRIX.md` when choosing an implementation stack
6. `blocks/telegram/MONETIZATION_AND_PAYMENTS.md` for revenue or payment flows
7. `blocks/telegram/SECURITY_AND_COMPLIANCE.md` before implementation or production deployment
8. `blocks/telegram/VALIDATION_BACKLOG.md` when testing a capability
9. `blocks/telegram/REFERENCES.md` for the source map
10. `blocks/telegram/RESEARCH_REPORT_2026-06-06.md` for the current research snapshot

## Typical Outputs

Typical outputs:

- Telegram product-mode decision;
- bot capability map;
- Mini App specification;
- BotFather setup checklist;
- webhook or polling architecture;
- framework recommendation;
- database and queue requirements;
- payments and Stars plan;
- login or verification integration plan;
- security checklist;
- hosting and observability plan;
- Codex implementation handoff;
- recommendation to create a narrower Telegram skill after repeated use.

## Boundary

This block is the reusable central Telegram domain layer.

Keep project-specific tokens, secrets, user data, deployment credentials, production logs, and final implementation details in the approved secure project layer.

## Final Rule

Prefer official Telegram capabilities and verified donor libraries before custom invention. Validate the current Bot API version before implementation.