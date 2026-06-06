# Telegram Product Surfaces

Updated: 2026-06-06
Status: candidate

## Purpose

Choose the smallest Telegram surface that solves the product need.

## Standard Bot API Bot

Use for chat assistants, support, notifications, digests, moderation, groups, channels, commands, buttons, and workflow automation.

Core transport:

- long polling for development and small workloads;
- webhooks for production;
- local Bot API server only when its extra capabilities are needed.

## Guest Bot

Use when a bot should be mentioned temporarily in a chat without becoming a member.

Good for AI assistants, translation, fact-checking, and contextual tools.

## Inline Bot

Use when users should call a bot from any chat, select a result, and send it themselves.

Good for search, generated content, calculations, formatting, and attachments.

## Mini App

Use when messages and buttons are not enough and a custom web interface is needed inside Telegram.

Good for SaaS interfaces, games, marketplaces, dashboards, quizzes, booking, e-commerce, and AI tools.

## Secretary Bot

Use when a user connects a bot to their account and explicitly grants access to supported chats and actions.

Good for support assistants, sales workflows, and inbox triage.

## Managed Bots

Use when a manager bot or Mini App needs to guide creation and management of additional bots through supported Telegram flows.

Good for bot builders, white-label products, vertical SaaS, and agency tooling.

## Telegram Login

Use for website or app login with Telegram.

Current paths include Telegram Login library, native mobile SDKs, and OpenID Connect with Authorization Code Flow and PKCE.

## Telegram Gateway API

Use when an external website or app needs verification codes delivered through Telegram instead of SMS.

## Telegram Widgets

Use for website share buttons, embedded posts, discussions, and login.

## Telegram API, MTProto, And TDLib

Use only when building a custom Telegram client or a client-level integration that the Bot API cannot cover.

## Final Rule

Start with Bot API. Add other Telegram surfaces only when the product requirement clearly justifies the added complexity.