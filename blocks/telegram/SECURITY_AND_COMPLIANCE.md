# Telegram Security And Compliance

Updated: 2026-06-06
Status: candidate checklist

## Purpose

Apply Telegram-specific security and compliance checks before production deployment.

## Credentials

Never store in source control:

- bot tokens;
- Telegram Login Client Secret;
- Gateway API access token;
- API ID and API hash;
- database credentials;
- webhook secrets;
- third-party payment keys.

Use a secret manager or protected environment variables. Rotate compromised credentials immediately.

## Bot API Webhooks

For production webhooks:

- use HTTPS;
- configure `secret_token` in `setWebhook`;
- verify the `X-Telegram-Bot-Api-Secret-Token` header;
- validate payload shape;
- make handlers idempotent;
- log update IDs;
- handle retries;
- avoid slow synchronous work inside webhook handlers;
- use a queue for long-running jobs.

## Mini App Validation

Never trust `Telegram.WebApp.initDataUnsafe` on the server.

Send `Telegram.WebApp.initData` to the backend and validate its signature before using user or chat data. Check `auth_date` to reject stale data.

## Telegram Login

For Telegram Login:

- register allowed URLs in BotFather;
- store Client Secret securely;
- validate ID tokens server-side;
- validate issuer, audience, expiration, nonce, and signature;
- use PKCE where applicable;
- request only necessary scopes;
- define account-linking rules.

## Gateway API

For verification-code flows:

- collect phone numbers only with user opt-in;
- store access tokens securely;
- use E.164 phone-number format;
- validate callback signatures;
- check callback timestamps;
- handle duplicate callbacks;
- define TTL and retry rules;
- provide an authentication fallback.

## Privacy And Data Retention

Telegram Bot Platform Developer Terms require a privacy policy and careful handling of user data.

Implement:

- data minimization;
- accessible privacy policy;
- purpose limitation;
- encryption at rest;
- separation of encryption keys from stored data;
- user-data deletion workflow;
- retention limits;
- breach-response procedure;
- secure backups;
- access logging.

Do not collect or retain data beyond what is needed for the product.

## Secretary Bots

For Secretary Bots:

- clearly state what the bot does;
- process only user-authorized chats;
- define retention and purpose;
- do not disclose message contents to third-party APIs without user authorization;
- do not conceal bot activity from the account owner;
- notify users when scope changes;
- provide a simple disconnect path.

## Moderation And Messaging

Implement:

- opt-in messaging rules;
- unsubscribe or stop flow;
- spam prevention;
- rate-limit handling;
- content moderation where user-generated content exists;
- audit trail for administrative actions;
- loop prevention for bot-to-bot and Guest Mode flows.

## Persistence

Do not assume Telegram will preserve your application state indefinitely.

Store important product state in your own database and test recovery from partial data loss.

## Final Rule

Treat Telegram as an integration surface, not as your secure database. Validate every trust boundary server-side.