# Chrome Extension Ready SaaS Stacks

## Purpose

Provide ready architecture bundles for paid, AI, affiliate, and account-based browser-extension products.

Use this file after `BLOCK.md`, `READY_SOLUTIONS.md`, and `TOOL_SELECTION_MATRIX.md` when the extension needs backend, auth, payments, licenses, AI, or partner monetization.

## Default Product Stack

For serious extension products, start with:

`WXT + TypeScript + React + Tailwind + SaaS backend + external payments`

Do not put private API keys, billing secrets, or provider secrets inside extension code.

## Stack 1 — WXT + Supabase + Stripe

Best for: fast SaaS MVP with custom control.

Use when:

- user accounts are needed;
- database and auth should be quick to set up;
- Stripe checkout or subscriptions are acceptable;
- the owner wants control over billing logic and product flow.

Typical pieces:

- WXT extension;
- Supabase Auth;
- Supabase Postgres;
- backend/serverless functions;
- Stripe Checkout or Billing;
- license table synced from Stripe webhooks.

Strengths:

- fast MVP;
- strong developer ecosystem;
- flexible data model;
- works well for AI or productivity extensions.

Risks:

- tax/compliance responsibility may remain more operationally complex than Merchant of Record providers;
- webhook and license sync must be implemented correctly.

Recommended for:

- QuizLight browser helper;
- study-card extension;
- AI assistant extension;
- owner-operated SaaS tools.

## Stack 2 — WXT + Firebase + Stripe

Best for: Google-native app feel and real-time app state.

Use when:

- Google login is central;
- realtime sync or Firebase ecosystem matters;
- the project benefits from Firebase hosting/functions/firestore.

Typical pieces:

- WXT extension;
- Firebase Auth;
- Firestore;
- Firebase Functions;
- Stripe Checkout or Billing;
- custom claims or backend license checks.

Strengths:

- strong Google ecosystem fit;
- good auth story;
- good for quick web plus extension projects.

Risks:

- Firestore data modeling and cost need discipline;
- Stripe integration still needs backend correctness.

Recommended for:

- Google-account-centered extensions;
- Chrome-first learning tools;
- realtime note/card sync.

## Stack 3 — WXT + Paddle

Best for: paid SaaS extension with Merchant of Record simplicity.

Use when:

- global digital-product payments matter;
- the owner wants less tax/payment operational burden;
- subscription or license management is needed;
- custom payment control is less important than business simplicity.

Typical pieces:

- WXT extension;
- backend API;
- app database;
- Paddle checkout;
- Paddle webhooks;
- license/subscription status endpoint.

Strengths:

- Merchant of Record model;
- good for SaaS and digital products;
- simplifies some global payment/tax complexity.

Risks:

- less direct control than Stripe;
- provider rules and approval requirements must be checked before launch.

Recommended for:

- serious paid extension products;
- B2C subscription extensions;
- AI tools with recurring revenue.

## Stack 4 — WXT + Lemon Squeezy

Best for: lightweight paid digital product or simple subscription extension.

Use when:

- fast checkout setup matters;
- simple licenses or subscriptions are enough;
- Merchant of Record-style simplicity is desirable;
- the project is smaller than a full Stripe billing system.

Typical pieces:

- WXT extension;
- lightweight backend;
- Lemon Squeezy checkout;
- webhook-based license table;
- extension license check endpoint.

Strengths:

- simpler than many custom Stripe setups;
- good for indie software and small paid tools;
- good MVP path for paid extension validation.

Risks:

- advanced billing needs may outgrow it;
- provider capabilities must be rechecked before choosing.

Recommended for:

- small paid productivity extension;
- lifetime-license extension;
- indie micro-SaaS extension.

## Stack 5 — WXT + ExtensionPay

Best for: fastest browser-extension payment MVP.

Use when:

- the goal is to test willingness to pay quickly;
- the team does not want to build billing infrastructure first;
- one-time or recurring extension payments are enough for MVP.

Typical pieces:

- WXT extension;
- ExtensionPay integration;
- minimal backend or no backend for first validation;
- later migration plan if the product grows.

Strengths:

- browser-extension-specific;
- fast validation;
- lower initial engineering burden.

Risks:

- lock-in;
- less flexibility than SaaS backend architecture;
- validate provider limits before building business-critical workflows.

Recommended for:

- quick paid MVP;
- small utility extension;
- early market validation.

## Stack 6 — WXT + AI Backend

Best for: AI-powered extension with paid model/provider usage.

Use when:

- AI provider calls cost money;
- prompts, rate limits, and usage accounting matter;
- provider API keys must stay private;
- monetization may depend on usage tiers.

Typical pieces:

- WXT extension;
- backend API;
- auth;
- AI provider proxy;
- usage metering;
- payment provider;
- prompt/version logging where appropriate.

Strengths:

- protects provider keys;
- supports rate limits and billing;
- supports experimentation with multiple models;
- fits learning, summarization, writing, and research tools.

Risks:

- privacy policy must clearly explain data flow;
- AI cost can destroy margins if pricing is wrong;
- output quality and latency need validation.

Recommended for:

- YouTube-to-card extension;
- language learning extension;
- ChatGPT/browser research helper;
- page summarizer.

## Stack 7 — WXT + Affiliate Extension Backend

Best for: commerce, product research, deal, or creator-affiliate extensions.

Use when:

- revenue comes from partner links or attribution;
- merchant rules and disclosure can be handled clearly;
- the extension needs remote configuration of merchants, offers, or rules.

Typical pieces:

- WXT extension;
- content script on allowed merchant domains;
- backend configuration service;
- affiliate-link generation or redirect service;
- disclosure UI;
- analytics limited to necessary product/business events.

Strengths:

- direct monetization without charging the user;
- can fit product-discovery and shopping workflows;
- remote config allows quick business changes.

Risks:

- trust and disclosure are critical;
- merchant/platform rules may change;
- overbroad host access can create store-review risk.

Recommended for:

- gadget affiliate helper;
- shopping comparison extension;
- creator commerce tools.

## Stack 8 — WXT + B2B / White-Label Backend

Best for: repeatable client-specific browser workflow products.

Use when:

- the same extension pattern can be configured for multiple clients;
- admin configuration matters;
- client data isolation matters;
- revenue comes from setup fee plus recurring support/license.

Typical pieces:

- WXT extension;
- multi-tenant backend;
- admin dashboard;
- client-specific config;
- per-client branding;
- subscription or invoice-based billing.

Strengths:

- higher revenue per customer;
- reusable architecture;
- fits automation and internal workflow products.

Risks:

- support burden;
- tenant isolation must be designed carefully;
- each client may create custom scope creep.

Recommended for:

- internal browser assistants;
- agency/client tools;
- operator workflow extensions.

## Fast Selection Guide

| Situation | Choose |
|---|---|
| Fastest paid MVP | WXT + ExtensionPay |
| Serious AI extension | WXT + AI Backend + Paddle/Stripe |
| Simple indie paid tool | WXT + Lemon Squeezy |
| Maximum billing control | WXT + Supabase + Stripe |
| Google-native sync | WXT + Firebase + Stripe |
| Global SaaS with less tax burden | WXT + Paddle |
| Commerce/affiliate product | WXT + Affiliate Extension Backend |
| Client/workflow business | WXT + B2B / White-Label Backend |

## Default Owner Recommendation

For the owner's likely future products:

1. QuizLight / language-learning extension: `WXT + Supabase + Stripe` or `WXT + AI Backend + Paddle`.
2. YouTube-to-card extension: `WXT + AI Backend + subscription billing`.
3. Gadget/affiliate extension: `WXT + Affiliate Extension Backend`.
4. Fast small paid tool: `WXT + ExtensionPay`, then migrate if validated.
5. Client browser workflow tools: `WXT + B2B / White-Label Backend`.

## Final Rule

Do not select payments separately from architecture. Auth, backend, pricing model, license checks, AI cost, and store policy must be decided together.