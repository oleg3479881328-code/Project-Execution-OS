# Chrome Extension Research Report — 2026-06-07

## Purpose

Capture the initial research pass behind `blocks/chrome-extension/`.

## Artifact Decision

Classification: `full block`

Reason:

Chrome Extension work is a recurring cross-project domain with multiple product surfaces, implementation choices, security/privacy risks, publishing rules, monetization choices, and payment architecture decisions.

A compact block would be too small because monetization, store policy, permissions, AI usage, backend architecture, and ready frameworks must be handled before implementation.

## Domain Boundary

This block covers browser extensions with Chrome Manifest V3 as the default baseline, including architecture, framework selection, permissions, security/privacy, publishing, monetization, payment providers, and donor solutions.

It does not cover general web design, Telegram apps, mobile apps, or project-specific implementation state.

## Main Research Findings

1. Chrome Manifest V3 is the current baseline for Chrome extension architecture.
2. Extensions require `manifest.json` as the central declaration file.
3. MV3 background logic is based on extension service workers rather than persistent background pages.
4. Chrome Web Store Payments should not be treated as the main monetization path.
5. Modern extension products usually need external payments, backend license checks, or SaaS architecture.
6. Permission minimization and privacy disclosure are central publishability concerns.
7. WXT is the best default candidate for new serious extension products.
8. Plasmo, CRXJS, Extension.js, and minimal MV3 starters should remain as alternatives.

## Recommended Default

`WXT + TypeScript + React + Tailwind + Manifest V3`

Use this for new productized extensions unless the project is intentionally tiny or another stack clearly fits better.

## Ready Solution Shortlist

- WXT — default candidate.
- Plasmo — strong React/product framework candidate.
- CRXJS — Vite-centered candidate.
- Extension.js — zero-config/cross-browser candidate.
- Minimal MV3 starter — learning and tiny MVP candidate.
- React + TypeScript + Vite starter — UI-heavy simple candidate.

## Monetization Shortlist

- SaaS plus extension — best serious product pattern.
- Freemium — best growth pattern when free value is real.
- Subscription — best for ongoing backend or AI costs.
- Lifetime license — only when ongoing costs are low.
- Affiliate — useful for commerce helpers when disclosure and rules are clear.
- White-label/B2B — useful for repeatable client workflows.

## Payment Shortlist

- Stripe — control.
- Paddle — Merchant of Record simplicity.
- Lemon Squeezy — lightweight digital product/MoR-style path.
- PayPal — supplemental option.
- ExtensionPay — browser-extension-specific MVP path.

## Risks

- overbroad permissions;
- unclear data handling;
- hidden third-party calls;
- exposed API keys;
- fragile content scripts that depend on changing webpages;
- store rejection because listing claims and behavior do not match;
- choosing lifetime pricing for a product with recurring AI/backend cost.

## Follow-Up Needed

Validate the block by building a small WXT extension and testing local install, production build, permissions, storage, and a basic monetization/license path.

## Final Recommendation

Create and register `blocks/chrome-extension/` as a candidate full domain block. Use it for the next browser-extension project, then update the validation backlog with real results.