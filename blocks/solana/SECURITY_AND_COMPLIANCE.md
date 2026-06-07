# Solana Security and Compliance

## Purpose

Keep Solana products safe, reviewable, and honest before real value moves.

## Core Rules

1. Never store seed phrases or private keys in app code, logs, repo files, prompts, or central blocks.
2. Prefer existing audited programs over new custom programs.
3. Treat custom programs as high-risk until tested and reviewed.
4. Simulate or preview transactions where possible.
5. Make wallet actions understandable to the user.
6. Separate devnet testing from mainnet execution.
7. Do not present legal, tax, or securities conclusions as final advice.

## Wallet Safety

Before shipping wallet flows, verify:

- user sees what they are signing;
- transaction purpose is clear;
- network is clear;
- errors are understandable;
- no hidden value transfer is present;
- approval boundaries are explicit.

## Program Security Review

For custom programs, review:

- account ownership checks;
- signer checks;
- PDA seed correctness;
- account initialization rules;
- authority changes;
- CPI safety;
- arithmetic and overflow handling;
- rent and close-account behavior;
- upgrade authority;
- tests for failure cases.

## Token Safety

For token products, review:

- mint authority;
- freeze authority;
- supply rules;
- metadata correctness;
- distribution mechanics;
- user disclosure;
- liquidity and market assumptions;
- rug-risk optics.

## DeFi Risk Review

For DeFi-like products, review:

- slippage;
- price impact;
- oracle assumptions;
- liquidity source;
- pool risk;
- token legitimacy;
- user warnings;
- regulatory escalation need.

## AI Agent Safety

For AI + Solana products:

- AI should not silently move value;
- user approval must be explicit;
- spending limits should be defined;
- transaction preview should be shown;
- revocation path should be clear;
- audit trail should be retained where appropriate.

## Escalation

Escalate before proceeding when:

- mainnet value will move;
- custom program controls assets;
- token issuance is involved;
- financial returns are implied;
- user funds, custody, compliance, or securities risk may exist;
- legal/tax/accounting interpretation is needed.

## Final Rule

If a Solana design cannot explain who signs what, what value moves, and what can go wrong, it is not ready.