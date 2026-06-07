# Solana Architecture Patterns

## Purpose

Define reusable Solana architecture choices for product and implementation planning.

## Pattern 1 — Off-Chain App + Wallet Signatures

Use when the product needs wallet identity or payments but not custom on-chain state.

Typical parts:

- web app;
- wallet connection;
- backend database;
- signed messages or transactions;
- existing Solana programs.

Good for:

- login with wallet;
- dashboards;
- gated access;
- simple payments;
- user-owned asset views.

Rule:

Do not create a custom program if signed wallet actions and existing programs are enough.

## Pattern 2 — Existing Program Integration

Use when the product can rely on established Solana programs.

Typical parts:

- SPL Token;
- Associated Token Account;
- Token Extensions when needed;
- metadata programs or marketplace protocols where appropriate;
- frontend and backend orchestration.

Good for:

- token distribution;
- payment flows;
- NFT/collectible workflows;
- simple escrow-like flows if a mature protocol exists.

## Pattern 3 — Anchor Custom Program

Use when business logic requires on-chain state transitions that existing programs do not provide.

Typical parts:

- Anchor program;
- accounts and constraints;
- PDAs;
- CPI when needed;
- TypeScript tests;
- frontend client from IDL;
- devnet validation.

Good for:

- custom marketplace logic;
- escrow;
- games;
- protocol mechanics;
- complex permission/state logic.

## Pattern 4 — Indexer + Dashboard

Use when product value comes from reading, classifying, or monitoring Solana data.

Typical parts:

- RPC/data provider;
- indexer process;
- database;
- API;
- dashboard UI;
- alerting.

Good for:

- portfolio views;
- risk detection;
- whale/activity alerts;
- token analytics;
- compliance or monitoring workflows.

## Pattern 5 — Payments Product

Use when Solana is used for checkout, settlement, or machine/agent payment.

Typical parts:

- checkout UI;
- wallet transaction request;
- confirmation listener;
- order state backend;
- receipt/support flow;
- fiat accounting bridge when needed.

Good for:

- stablecoin checkout;
- creator payments;
- digital goods;
- agent micropayments.

## Pattern 6 — AI Agent + Human Approval

Use when AI proposes or prepares Solana actions.

Typical parts:

- AI planner;
- policy engine;
- transaction builder;
- transaction preview;
- user approval;
- wallet signature;
- audit trail.

Rule:

AI may prepare actions, but user approval boundaries must be explicit when value or permissions are involved.

## Final Rule

Prefer off-chain orchestration plus existing programs. Use custom on-chain programs only when product logic truly requires decentralized state or execution.