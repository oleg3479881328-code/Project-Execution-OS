# Telegram Tool Selection Matrix

Updated: 2026-06-06
Status: candidate

## Purpose

Route Telegram tasks to the smallest suitable official API, SDK, or community framework.

| Need | Default candidate | Alternative | Notes |
|---|---|---|---|
| Python bot with modern async architecture | aiogram | python-telegram-bot | aiogram tracks Bot API 10.0 and includes routers, FSM, middleware, webhook replies, and localization. |
| Python bot with broad examples and high-level conveniences | python-telegram-bot | aiogram | PTB is asynchronous, typed, and supports polling and webhooks. Confirm support for the active Bot API version before implementation. |
| TypeScript bot with strong ecosystem | grammY | Telegraf | grammY is a current TypeScript / JavaScript framework for Node.js or Deno with plugins and web-framework integrations. |
| Existing Node.js project already using Telegraf | Telegraf | grammY | Telegraf is mature and lightweight. Check Bot API version coverage before choosing it for new platform features. |
| Go bot | go-telegram/bot or gotgbot | telego | Choose after validating current Bot API coverage and examples. |
| Java bot | TelegramBots | pengrad/java-telegram-bot-api | Use official Telegram tutorial and validate version support. |
| Mini App frontend | official `telegram-web-app.js` | tma.js SDK | Use the official script as the platform baseline. tma.js is a useful community TypeScript toolkit. |
| Local Bot API server | tdlib/telegram-bot-api | Telegram-hosted Bot API | Use locally only for large files, local paths, custom webhook networking, or very high webhook concurrency. |
| Custom Telegram client | TDLib | direct MTProto | Prefer TDLib because it handles networking, encryption, local storage, ordered updates, and unreliable connections. |
| Website or app authentication | Telegram Login OIDC | Telegram Login JS library or native SDKs | Prefer OIDC when integrating with an existing identity platform. |
| Phone verification codes | Telegram Gateway API | SMS provider fallback | Use opt-in, callback signature verification, delivery status, and fallback strategy. |
| Digital goods inside bots or Mini Apps | Telegram Stars | none inside Telegram apps | Use `XTR` currency. Digital goods and services inside Telegram apps must use Stars. |
| Physical goods and services | Bot Payments API with third-party provider | external checkout where appropriate | Telegram does not process card data; payment providers do. |

## Official Library Directory

Telegram maintains a community-library directory:

https://core.telegram.org/bots/samples

Important boundary:

Libraries listed there are community projects and are not maintained by Telegram.

## Selection Rules

1. Prefer the official Bot API and official Mini App documentation as the source of truth.
2. Check active Bot API support before choosing a framework.
3. Prefer a framework that matches the project language and deployment model.
4. Do not choose TDLib or direct MTProto unless Bot API is insufficient.
5. Validate community SDKs before treating them as production dependencies.
6. Record the selected version and the Bot API version used by the project.

## Final Rule

Select by required Telegram capability, current API coverage, maintainability, and team stack — not by popularity alone.