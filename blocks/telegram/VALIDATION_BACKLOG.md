# Telegram Validation Backlog

Status: candidate backlog
Updated: 2026-06-06

## Purpose

Separate promising Telegram capabilities from validated reusable workflows.

## Priority 1 — Standard Bot Baseline

Validate:

- BotFather creation flow;
- token rotation;
- long polling;
- webhook deployment;
- webhook secret verification;
- update deduplication;
- retry handling;
- command and button navigation;
- database persistence;
- background jobs;
- logging and alerting;
- rate-limit handling;
- multilingual interface.

Recommended first framework tests:

- aiogram for Python;
- grammY for TypeScript;
- python-telegram-bot as Python alternative.

## Priority 2 — AI Assistant Bot

Validate:

- private-chat assistant;
- group assistant;
- Guest Mode;
- inline mode;
- message streaming or drafts where supported;
- context limits;
- opt-in memory;
- moderation;
- cost logging;
- loop prevention;
- escalation to a human.

## Priority 3 — Mini App Baseline

Validate:

- BotFather Main Mini App setup;
- menu-button launch;
- direct-link launch;
- start parameters;
- `telegram-web-app.js` integration;
- server-side `initData` validation;
- theme and safe-area support;
- fullscreen;
- back button and bottom buttons;
- mobile-device testing;
- geolocation permission;
- sharing;
- downloads;
- Stars test payment;
- analytics.

## Priority 4 — Secretary Bot

Validate:

- BotFather Secretary Mode setup;
- BusinessConnection lifecycle;
- incoming business messages;
- permission checks;
- reply workflow;
- user-visible activity;
- data retention;
- third-party API authorization;
- disconnect workflow;
- compliance with Bot Developer Terms.

## Priority 5 — Managed Bots

Validate:

- supported manager-bot flow;
- suggested bot username and name;
- managed-bot creation;
- managed token retrieval and replacement;
- customer onboarding;
- tenant isolation;
- secret storage;
- rate limits;
- support workflow.

## Priority 6 — Telegram Login

Validate:

- allowed URLs;
- JS library;
- OIDC discovery;
- Authorization Code Flow;
- PKCE;
- ID-token verification;
- nonce;
- account linking;
- requested scopes;
- native SDK boundary.

## Priority 7 — Gateway API

Validate:

- account setup;
- access token;
- own-phone free testing;
- `checkSendAbility`;
- `sendVerificationMessage`;
- TTL;
- custom and generated codes;
- callback delivery;
- callback HMAC verification;
- fallback authentication path;
- cost monitoring.

## Priority 8 — Payments

Validate:

- Stars invoice;
- digital-goods delivery;
- recurring payment;
- channel subscription link;
- refund;
- `/paysupport`;
- physical-goods provider sandbox;
- entitlement reconciliation;
- duplicate update handling;
- terms recheck.

## Priority 9 — TDLib And Local Bot API Server

Validate only when a real project needs them:

- local Bot API server build;
- large-file workflow;
- migration from Telegram-hosted Bot API;
- TDLib build;
- user authorization;
- local storage;
- update ordering;
- version boundary;
- compliance review.

## Evidence Package

For every validation preserve:

- date;
- Telegram API version;
- library and version;
- project goal;
- setup steps;
- test bot or Mini App;
- screenshots or recordings;
- logs;
- security checks;
- limits discovered;
- current terms checked;
- result: promote, keep experimental, or reject.

## Final Rule

Validate one complete user journey at a time. Do not build a giant Telegram platform before the smallest workflow works.