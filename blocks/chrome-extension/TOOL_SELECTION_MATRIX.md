# Chrome Extension Tool Selection Matrix

## Purpose

Choose a practical extension stack without turning every new extension into a custom research project.

## Default Stack

`WXT + TypeScript + React + Tailwind + Manifest V3`

Use this unless there is a clear reason not to.

## Matrix

| Need | Recommended Path | Why |
|---|---|---|
| Serious new product extension | WXT | Best default balance of modern developer experience, MV3 support, and growth path. |
| React-heavy extension with product UI | WXT or Plasmo | Both support modern UI workflows. Compare conventions before choosing. |
| Existing Vite app adapted for extension use | CRXJS or WXT | CRXJS fits Vite-first setups; WXT fits broader extension structure. |
| Tiny proof of concept | Minimal MV3 starter | Avoid framework overhead. |
| Internal helper extension | WXT or minimal starter | Choose based on expected growth. |
| Cross-browser future | WXT or Extension.js | Validate browser targets early. |
| Extension plus SaaS backend | WXT plus backend | Keep auth, billing, license state, and heavy work server-side. |
| Paid extension without a custom backend | ExtensionPay or external checkout plus license check | Useful for speed, but validate lock-in and compliance. |

## Common Library Areas

### UI

- React for popup, options, sidebar, or content UI;
- Tailwind for fast consistent styling;
- Radix UI or shadcn-style components when building richer UI;
- browser-compatible component choices only.

### State and Storage

- `chrome.storage.local` for local extension data;
- `chrome.storage.sync` only for small sync-worthy settings;
- IndexedDB for larger structured local data;
- backend database for account, subscription, license, team, or cross-device state.

### Auth

- Google OAuth when identity is tied to Google or Chrome workflows;
- SaaS login when product account state matters;
- never store private server secrets in shipped extension code.

### AI

- do not put provider API keys directly in public extension code;
- use a backend proxy for paid AI calls;
- clearly disclose what user-provided content is sent to a backend or model provider.

### Analytics

- keep analytics minimal;
- collect only what the user-facing feature requires;
- document privacy policy before publishing.

## Selection Questions

Ask these before choosing tools:

1. Is this a toy, internal tool, or product?
2. Does it need popup, options page, side panel, content UI, or only background behavior?
3. Does it need user accounts?
4. Does it need payments?
5. Does it process page content?
6. Does it need backend AI calls?
7. Is Chrome-only acceptable?
8. Will it be published in Chrome Web Store?

## Final Rule

The stack must match the smallest product path. Do not choose a heavy framework for a one-file extension, and do not choose a toy starter for a paid product.