# Telegram Monetization And Payments

Updated: 2026-06-06
Status: candidate guide

## Purpose

Choose the correct monetization path for Telegram bots and Mini Apps.

## Digital Goods And Services

Inside Telegram apps, digital goods and services must use Telegram Stars.

Use:

- currency `XTR`;
- invoices through Bot API;
- Stars subscriptions where appropriate;
- paid media where appropriate;
- refund flow through Bot API;
- `/paysupport` handling;
- transaction logging;
- delivery confirmation;
- dispute workflow.

Examples:

- premium bot features;
- AI credits;
- digital content;
- subscriptions;
- paid access;
- virtual items;
- Mini App upgrades.

## Physical Goods And Services

For physical goods and services, use Bot Payments API with supported third-party payment providers.

Telegram does not process or store card details. Payment providers handle sensitive payment information.

Examples:

- delivery orders;
- bookings;
- consulting;
- physical products;
- local services.

## Subscriptions

Potential subscription paths include:

- recurring Stars payments for bot or Mini App services;
- channel subscription invite links paid in Stars;
- external subscription management where allowed for the relevant product surface and goods category.

Record:

- billing period;
- price;
- entitlement state;
- renewal state;
- cancellation path;
- refund rules;
- failed-delivery handling.

## Affiliate Programs

Telegram Bot API includes affiliate-related transaction data.

Use only after validating:

- product eligibility;
- commission logic;
- refund behavior;
- attribution window;
- reporting;
- tax treatment;
- current Telegram terms.

## Ads And Revenue Sharing

Bots may participate in revenue sharing from Telegram Ads shown in bot chats. Treat this as an additional monetization channel, not the default business model.

## Stars Operations

Before launching a Stars-based product, verify the current Telegram Bot Platform Developer Terms.

Current terms describe:

- Stars-based rewards;
- advertising credits;
- possible holding periods;
- dispute-related debits;
- higher broadcast limits paid in Stars;
- expiry rules;
- geography and Fragment availability limits;
- tax responsibility remaining with the developer.

Do not hard-code business assumptions without rechecking current terms.

## Payment Checklist

Before production:

- classify the product as digital or physical;
- choose the allowed payment method;
- test invoice flow;
- test successful delivery;
- test failed delivery;
- test refund;
- implement `/paysupport`;
- store transaction IDs;
- handle duplicate updates idempotently;
- reconcile entitlements;
- document taxes and customer-support responsibilities;
- confirm current Telegram terms.

## Final Rule

Classify the product first. Use Stars for digital goods inside Telegram apps and third-party providers for physical goods and services.