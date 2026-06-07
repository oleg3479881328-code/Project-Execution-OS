# Chrome Extension Security and Compliance

## Purpose

Keep extension projects publishable, safe, and privacy-aware from the first design pass.

## Core Rules

1. Request the narrowest permissions that support the user-facing feature.
2. Prefer optional permissions when access is not always required.
3. Keep private API keys and payment secrets out of shipped extension code.
4. Use backend services for private credentials, billing, and license enforcement.
5. Disclose user data flow clearly.
6. Do not collect data unrelated to the feature.
7. Do not treat researched policy notes as legal advice.

## Permission Review

Before implementation, list:

- required Chrome APIs;
- required host permissions;
- optional host permissions;
- reason for each permission;
- user-facing explanation;
- lower-permission alternative considered.

Reject broad access when a narrow domain allowlist or user-initiated permission is enough.

## Data Review

Before publication, list:

- what data the extension reads;
- what data is stored locally;
- what data is sent to a backend;
- what data is sent to third-party services;
- how long data is retained;
- how the user can understand or control the behavior.

## AI-Specific Review

For AI extensions:

- do not expose model provider keys in extension code;
- use a backend proxy for paid provider calls;
- explain when selected content is sent outside the browser;
- avoid sending more content than the feature requires;
- keep rate limits and abuse controls server-side when relevant.

## Payment and License Review

For paid extensions:

- payment provider must be outside Chrome Web Store Payments;
- license checks should not rely only on easily editable local state;
- refund, cancellation, and subscription status must be handled by the payment provider or backend;
- user access state must fail safely.

## Store Policy Review

Before Chrome Web Store submission:

- verify Manifest V3 compliance;
- verify privacy policy presence when required;
- verify permission explanations;
- verify screenshots and description match real behavior;
- verify no misleading claims;
- verify no hidden unrelated data collection.

## Escalation

Escalate to the owner before proceeding when:

- the extension needs broad host access;
- the feature touches sensitive user data;
- monetization depends on unclear policy interpretation;
- the extension may be rejected by Chrome Web Store;
- legal, tax, or merchant-of-record decisions affect the business.

## Final Rule

Design for review first. A powerful extension that cannot pass privacy, permission, and store review is not a usable product.