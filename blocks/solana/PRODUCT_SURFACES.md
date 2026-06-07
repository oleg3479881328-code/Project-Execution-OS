# Solana Product Surfaces

## Purpose

Map common Solana product surfaces so agents choose the right architecture before choosing tools.

## Surface 1 — Wallet-Connected Web App

Use when the product only needs users to connect a wallet and sign transactions.

Typical parts:

- website frontend;
- wallet adapter;
- RPC provider;
- off-chain backend if needed;
- existing Solana programs.

Good for:

- dashboards;
- claim pages;
- marketplace interfaces;
- account viewers;
- token utility apps.

## Surface 2 — Token Product

Use when the product involves fungible tokens, gated access, rewards, points-to-token conversion, or treasury mechanics.

Decisions:

- SPL Token vs Token Extensions;
- mint authority;
- freeze authority;
- metadata;
- distribution mechanics;
- compliance review.

## Surface 3 — NFT / Digital Collectible Product

Use when product value is represented by collectible assets, membership passes, certificates, media, or identity items.

Decisions:

- collection structure;
- metadata;
- marketplace compatibility;
- royalties or creator settings;
- storage approach;
- transfer rules.

## Surface 4 — Solana Payments

Use when the product uses Solana for checkout, settlement, QR payments, stablecoin payments, or machine/agent payments.

Decisions:

- wallet checkout;
- stablecoin or SOL;
- payment request format;
- confirmation policy;
- refund/support flow;
- fiat accounting bridge.

## Surface 5 — Custom On-Chain Program

Use only when existing programs cannot support the product safely.

Good for:

- custom escrow;
- custom marketplace logic;
- custom game mechanics;
- protocol logic;
- complex state transitions.

Rule:

Custom programs require stronger security review than wallet-only dApps.

## Surface 6 — DeFi / Trading Interface

Use when the product interacts with swaps, liquidity, lending, staking, or yield products.

Risks:

- price impact;
- slippage;
- malicious tokens;
- oracle risk;
- pool risk;
- regulatory and disclosure risk.

## Surface 7 — AI Agent + Solana

Use when AI agents create, read, or initiate Solana actions.

Decisions:

- human approval boundary;
- wallet delegation model;
- spending limits;
- transaction preview;
- audit trail;
- revocation path.

## Surface 8 — Analytics / Indexing Product

Use when the product reads Solana chain data for dashboards, risk detection, user history, or market intelligence.

Typical parts:

- indexer;
- RPC or data provider;
- database;
- UI;
- alerting;
- risk labels.

## Final Rule

Choose the product surface first. The surface determines wallet flow, on-chain need, security review, backend need, and monetization path.