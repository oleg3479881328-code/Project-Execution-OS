# Telegram Block Research Snapshot

Date: 2026-06-06
Status: completed initial research pass

## Executive Conclusion

Telegram is a modular product platform, not only a bot messenger.

Use separate lanes for:

1. standard Bot API bots;
2. inline and Guest Mode utilities;
3. Mini Apps;
4. Secretary Bots;
5. Managed Bots;
6. Telegram Login and Gateway verification;
7. Stars, subscriptions, payments, affiliates, and ads;
8. local Bot API server for advanced infrastructure;
9. TDLib for custom clients only.

## Current Snapshot

Official documentation reports Bot API 10.0 dated May 8, 2026.

Recent capabilities include Guest Mode, Secretary Bots, Managed Bots, bot-to-bot scenarios, richer Mini Apps, OIDC login, Gateway verification, and Stars monetization.

Recheck official documentation and terms before production implementation.

## Recommended Defaults

- Python custom bot: aiogram.
- TypeScript custom bot: grammY.
- Python alternative: python-telegram-bot.
- Existing suitable Node.js project: Telegraf after version review.
- Automation MVP: n8n Telegram node and trigger.
- Conversational MVP: Botpress Telegram integration.
- Mini App baseline: official `telegram-web-app.js`.
- Optional Mini App toolkit: tma.js after compatibility check.
- Advanced large-file or webhook infrastructure: local Bot API server.
- Custom Telegram client: TDLib only when Bot API is insufficient.

## Monetization Rule

Use Telegram Stars for digital goods and services inside Telegram apps.

Use supported third-party payment providers for physical goods and services.

## Security Rule

Every production implementation should include protected secrets, webhook verification, idempotent updates, queue-backed long jobs, server-side Mini App init-data validation, login-token validation, privacy policy, data minimization, retention controls, and recovery testing.

## First Practical Tests

Validate first:

1. AI assistant or digest bot;
2. webhook deployment;
3. basic Mini App with backend validation;
4. Stars test payment;
5. multilingual navigation.

Test Secretary Bots, Managed Bots, Gateway, or TDLib only when a real product requires them.

## Related Files

- `BLOCK.md`
- `PRODUCT_SURFACES.md`
- `TELEGRAM_WORKFLOW_PIPELINE.md`
- `TOOL_SELECTION_MATRIX.md`
- `READY_SOLUTIONS.md`
- `SECURITY_AND_COMPLIANCE.md`
- `MONETIZATION_AND_PAYMENTS.md`
- `CURRENT_CAPABILITIES_2026-06-06.md`
- `VALIDATION_BACKLOG.md`
- `REFERENCES.md`

## Final Rule

Start with the smallest validated Telegram surface. Add complexity only after a real requirement appears.