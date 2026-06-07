# Solana Tool Selection Matrix

## Purpose

Choose a practical Solana stack for the product surface without overengineering.

## Default Stack By Situation

| Situation | Recommended Path | Why |
|---|---|---|
| Wallet-connected website | Next.js or Vite + wallet adapter + Solana SDK | Fastest app path without custom program. |
| Custom on-chain logic | Anchor + Rust + TypeScript tests | Best default for Solana program development. |
| Maximum control program | Native Rust Solana program | Use only with strong Solana expertise. |
| Token product | SPL Token / Token Extensions + existing tooling | Avoid unnecessary custom token code. |
| Payments | Wallet transaction flow + backend order state | Keep checkout state and support flow clear. |
| Analytics product | RPC/data provider + indexer + database + dashboard | Direct RPC alone is often not enough. |
| AI agent actions | Backend policy engine + transaction builder + wallet approval | Keep user approval and audit trail clear. |

## Frontend Choices

Use:

- Next.js for SaaS-style dApps, dashboards, SEO/product pages;
- Vite/React for lighter dApps and internal tools;
- mobile stack only when mobile wallet UX is core.

## Program Choices

Use:

- no custom program when existing programs solve the job;
- Anchor for most custom programs;
- native Rust only for specialized expert cases.

## SDK Choices

Check official Solana SDK guidance before selecting.

Current direction to verify before implementation:

- `@solana/kit` for recommended TypeScript client work;
- `@solana/web3.js` for legacy and widely used ecosystem patterns;
- Rust SDK for program and validator-level work.

## Backend Choices

Use backend when the product needs:

- user accounts;
- order state;
- indexing;
- AI calls;
- notifications;
- license or subscription logic;
- analytics;
- fiat accounting.

## RPC / Data Provider Choices

Evaluate:

- mainnet/devnet support;
- rate limits;
- reliability;
- historical data;
- webhook support;
- cost;
- indexing needs.

## Final Rule

Select the stack from the product surface, not from Web3 hype. Most Solana products should start without custom on-chain programs.