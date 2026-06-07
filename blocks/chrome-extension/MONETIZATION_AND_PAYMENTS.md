# Chrome Extension Monetization and Payments

## Purpose

Provide reusable monetization and payment-provider guidance for browser-extension products.

## Important Baseline

Do not rely on Chrome Web Store Payments as the default monetization path. Plan paid extensions around external checkout, SaaS billing, or license-management services.

## Monetization Models

### Freemium

Definition: a free base product with paid advanced features.

Russian: freemium — бесплатная базовая версия и платные расширенные функции.

Use when:

- the extension can deliver value for free;
- paid features are clearly separable;
- growth and conversion matter.

### Subscription

Definition: recurring monthly or yearly payment for continued access.

Russian: subscription — регулярная оплата за доступ, обычно ежемесячно или ежегодно.

Use when:

- the product has ongoing costs;
- AI/API usage is recurring;
- the extension depends on backend services;
- users receive continuous value.

### Lifetime License

Definition: one-time payment for long-term access.

Russian: lifetime license — разовая оплата за постоянный доступ.

Use when:

- server costs are low;
- the feature set is stable;
- users dislike subscriptions.

Risk:

- lifetime pricing can become unprofitable if backend or AI costs continue.

### SaaS plus Extension

Definition: the extension is the browser interface for a paid SaaS product.

Russian: SaaS plus Extension — расширение является интерфейсом к платному веб-сервису.

Use when:

- accounts, teams, billing, storage, or AI calls matter;
- the extension is one product surface, not the whole business.

### Affiliate Model

Definition: revenue comes from partner links, referrals, or commerce attribution.

Russian: affiliate model — доход идет от партнерских ссылок, рекомендаций или комиссий.

Use when:

- the extension helps compare, discover, or select products;
- disclosure is clear;
- merchant and platform rules are respected.

### White Label / B2B

Definition: selling a customized extension or extension-backed workflow to businesses.

Russian: white label / B2B — продажа кастомизированного решения компаниям под их нужды или бренд.

Use when:

- one extension pattern can be reused for multiple clients;
- configuration and support can be productized.

## Payment Providers

### Stripe

Best for maximum control.

Use when:

- the team can build and maintain backend billing logic;
- custom subscription logic is needed;
- global tax/compliance is handled separately or with Stripe tools.

### Paddle

Best when Merchant of Record support is important.

Definition: Merchant of Record is the legal seller that handles payments, taxes, refunds, and compliance obligations for the transaction.

Russian: Merchant of Record — юридический продавец, который берет на себя платежи, налоги, возвраты и часть compliance.

Use when:

- the owner wants less operational burden around tax and global payments;
- SaaS or digital product sales are expected;
- MoR tradeoffs are acceptable.

### Lemon Squeezy

Best for lightweight digital product and software sales with MoR-style handling.

Use when:

- fast setup matters;
- digital products, licenses, or simple subscriptions are enough;
- the product does not need complex custom billing.

### PayPal

Use as an additional payment option, not usually as the core billing architecture for a serious extension SaaS.

### ExtensionPay

Specialized option for browser-extension payments.

Use when:

- speed matters;
- the project wants one-time or recurring payments without building a full billing backend first;
- lock-in and feature limits are acceptable for MVP.

## Default Recommendation

For serious paid extension products:

- use `SaaS plus Extension` architecture;
- keep billing and license checks server-side;
- use Paddle or Lemon Squeezy when MoR simplicity matters;
- use Stripe when control matters more than operational simplicity;
- consider ExtensionPay for MVP validation only.

## Payment Architecture Rule

The extension should not be the source of truth for paid access.

Preferred flow:

1. user signs in;
2. checkout happens through provider;
3. backend receives payment/subscription status;
4. extension asks backend for license state;
5. extension unlocks UI based on backend response.

## Final Rule

Choose monetization before implementation. Payment architecture changes can reshape auth, backend, storage, UI, support, and privacy obligations.