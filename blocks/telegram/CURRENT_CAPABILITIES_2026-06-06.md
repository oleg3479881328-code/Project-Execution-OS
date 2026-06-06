# Telegram Current Capabilities Snapshot

Date checked: 2026-06-06
Status: researched snapshot; recheck before implementation

## Bot API Version

Telegram Bot API documentation reports Bot API 10.0 dated May 8, 2026.

## Recent Bot API Capabilities

### Guest Mode

Bots can receive dedicated guest updates and reply in chats where they are not members when users mention them or reply to them.

Useful for:

- AI assistants;
- translation;
- fact-checking;
- contextual tools;
- temporary utilities.

### Secretary Bots

Bots can be connected to supported user accounts and process incoming messages within user-authorized chats. Depending on granted permissions, they may reply and perform supported actions on behalf of the connected user.

Useful for:

- business support;
- sales assistants;
- inbox triage;
- CRM workflows.

### Managed Bots

Telegram supports flows where bots or Mini Apps guide creation and management of additional bots.

Useful for:

- bot builders;
- white-label bot factories;
- agency products;
- guided customer onboarding.

### Bot-To-Bot Communication

Bot API 10.0 introduced supported bot-to-bot messaging scenarios. Implement loop prevention and operational safeguards.

## Mini Apps

Mini Apps support custom web interfaces inside Telegram.

Current documented capabilities include:

- main Mini App button;
- direct links and start parameters;
- shared chat context;
- fullscreen mode;
- home-screen shortcuts;
- custom loading screens;
- theme and safe-area integration;
- native main and secondary buttons;
- geolocation;
- QR scanning;
- biometrics;
- clipboard access in supported contexts;
- device motion and orientation;
- device hardware information;
- file downloads;
- sharing media to chats and stories;
- Telegram Stars payments and subscriptions.

## Telegram Login

Telegram Login currently supports:

- JS library;
- native SDKs for iOS and Android;
- OpenID Connect;
- Authorization Code Flow;
- PKCE;
- profile scope;
- verified phone-number scope with consent;
- permission for bot direct messaging after login.

## Gateway API

Telegram Gateway supports verification-message delivery through Telegram.

Current documented capabilities include:

- phone-number verification;
- send-ability check;
- custom or generated numeric codes;
- TTL;
- status checks;
- callback URL;
- callback-signature verification;
- delivery status;
- refunds for expired undelivered messages;
- free testing with the account owner's own phone number.

## Local Bot API Server

A local Bot API server is available for advanced cases.

Extra capabilities include:

- file downloads without size limits;
- uploads up to 2000 MB;
- local file paths;
- local webhook networking;
- custom ports;
- webhook concurrency up to 100000;
- direct local file paths from `getFile`.

Most bots should use Telegram-hosted Bot API unless these capabilities are required.

## TDLib

TDLib is the preferred client library when building a custom Telegram client. It handles network details, encryption, local storage, ordered updates, and unreliable connections.

## Final Rule

Treat this file as a dated snapshot. Recheck official Telegram documentation before production implementation.