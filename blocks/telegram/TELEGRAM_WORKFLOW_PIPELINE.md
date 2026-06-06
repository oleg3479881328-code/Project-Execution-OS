# Telegram Workflow Pipeline

## Purpose

Use this workflow before implementing a Telegram product.

## Core Workflow

```text
1. Define the user problem and business goal.
2. Choose the smallest Telegram surface.
3. Define the user journey and entry points.
4. Capture Telegram-specific permissions and limits.
5. Choose a framework, SDK, or official API path.
6. Decide polling, webhook, or client-level architecture.
7. Define data persistence, queues, jobs, and observability.
8. Define security boundaries for tokens, webhooks, Mini App init data, and user data.
9. Define monetization and payment rules when relevant.
10. Prototype the smallest complete flow.
11. Validate in Telegram test environments and production-like conditions.
12. Prepare the implementation handoff and operations checklist.
```

## Bot API Path

Use for ordinary bots.

Capture:

- BotFather setup;
- token storage;
- commands;
- private chat, group, channel, inline, or guest behavior;
- update types;
- polling or webhook;
- webhook secret token;
- database requirements;
- rate-limit handling;
- retries and idempotency;
- moderation requirements;
- analytics and logging.

## Mini App Path

Use when a web interface is required.

Capture:

- launch method;
- direct-link start parameters;
- backend validation of `Telegram.WebApp.initData`;
- responsive layout;
- Telegram theme and safe-area handling;
- native buttons and events;
- data model;
- payment flow;
- sharing and referral flow;
- analytics;
- browser and device testing.

## Login Path

Use when a website or app needs Telegram authentication.

Capture:

- BotFather allowed URLs;
- Client ID and Client Secret storage;
- Telegram Login library, native SDK, or OIDC path;
- PKCE configuration;
- ID-token server-side validation;
- requested scopes;
- replay protection;
- account-linking behavior.

## Gateway API Path

Use for verification codes.

Capture:

- opt-in flow;
- phone-number format;
- access-token storage;
- send-ability check;
- verification-code lifecycle;
- callback URL;
- signature verification;
- TTL;
- delivery status;
- refunds;
- fallback path.

## TDLib Or MTProto Path

Use only for custom clients or client-level products.

Capture:

- why Bot API is insufficient;
- API ID and API hash handling;
- TDLib version boundary;
- user authorization flow;
- data storage;
- platform compliance;
- update handling;
- privacy review;
- operations plan.

## Final Rule

Prototype one complete user journey first. Scale only after the Telegram-specific security and operations checks pass.