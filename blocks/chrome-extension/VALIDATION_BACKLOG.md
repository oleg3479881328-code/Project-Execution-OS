# Chrome Extension Validation Backlog

## Purpose

Track what must be validated before this researched block is treated as proven operational workflow.

## Status

`candidate`

Research has been captured. Practical validation is still required.

## Validation Items

### Framework Validation

- Create a minimal WXT extension.
- Build popup UI with React.
- Add a content script.
- Add a background service worker.
- Test message passing.
- Test storage.
- Build production package.
- Load unpacked in Chrome.

### Alternative Tool Validation

- Validate Plasmo on a small UI-heavy extension.
- Validate CRXJS on a Vite-first extension.
- Validate Extension.js on a simple cross-browser sample.
- Compare build output and project complexity.

### Security / Privacy Validation

- Produce a permission justification table for a real extension.
- Test optional permissions.
- Confirm no private keys appear in shipped build files.
- Confirm privacy policy template requirements for an AI extension.

### Monetization Validation

- Validate ExtensionPay on a toy extension.
- Validate Stripe Checkout plus backend license check.
- Validate Paddle or Lemon Squeezy checkout plus license check.
- Confirm cancellation and failed-payment behavior.
- Confirm how paid state is cached or refreshed in extension UI.

### Publishing Validation

- Submit or dry-run a Chrome Web Store listing.
- Record required screenshots and listing fields.
- Record review time and rejection reasons if any.
- Confirm update process for a new version.

### Product Pattern Validation

- Validate local utility pattern.
- Validate content UI overlay pattern.
- Validate extension plus SaaS pattern.
- Validate AI extension pattern.
- Validate affiliate or commerce helper pattern.

## Known Unvalidated Assumptions

- WXT is the best default for the owner's future extension products.
- ExtensionPay is useful enough for MVP monetization.
- Paddle or Lemon Squeezy will be preferable to Stripe when Merchant of Record simplicity matters.
- Chrome Web Store review will accept the planned permission patterns if explanations are narrow and clear.

## Final Rule

Do not mark this block active until at least one real extension uses it successfully from concept through local build and publication or publication-ready review.