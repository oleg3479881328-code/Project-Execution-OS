# Solana Research Report — 2026-06-07

## Purpose

Capture the initial research pass behind `blocks/solana/`.

## Artifact Decision

Classification: `full block`

Reason:

Solana work is a recurring cross-project domain with multiple product surfaces, fast-changing tools, security risks, on-chain/off-chain architecture decisions, wallet flows, token/payment mechanics, and monetization paths.

A compact block would be too small because Solana work requires ready solutions, architecture patterns, security boundaries, monetization review, implementation handoff, references, and validation backlog.

## Domain Boundary

This block covers Solana product and implementation planning:

- wallet-connected apps;
- token and NFT products;
- Solana payments;
- Anchor/custom programs;
- DeFi/marketplace interfaces;
- AI-agent Solana actions;
- analytics/indexing products;
- security and compliance triage.

It does not cover price prediction, trading calls, or speculative investment advice.

## Main Research Findings

1. Official Solana documentation is the primary source for accounts, transactions, programs, PDAs, CPI, SDKs, and developer templates.
2. Solana docs currently identify official SDKs and distinguish recommended TypeScript direction from legacy TypeScript tooling.
3. Anchor remains a major framework for building Solana programs and emphasizes faster, safer program development.
4. SPL Token and related program documentation are central for token work.
5. Custom on-chain programs should not be the default path when existing programs or off-chain orchestration are enough.
6. Security risks around signer checks, account ownership, phishing-style transactions, token risk, and value movement must be first-class block concerns.

## Recommended Default

Start from product surface:

- wallet-only product when possible;
- existing programs before custom programs;
- Anchor for most custom program needs;
- backend for order state, indexing, AI calls, access control, and monetization;
- devnet validation before mainnet work.

## Files Created

- `BLOCK.md`
- `PRODUCT_SURFACES.md`
- `READY_SOLUTIONS.md`
- `ARCHITECTURE_PATTERNS.md`
- `TOOL_SELECTION_MATRIX.md`
- `SECURITY_AND_COMPLIANCE.md`
- `MONETIZATION_AND_PAYMENTS.md`
- `IMPLEMENTATION_HANDOFF.md`
- `REFERENCES.md`
- `VALIDATION_BACKLOG.md`
- `RESEARCH_REPORT_2026-06-07.md`

## Final Recommendation

Register `blocks/solana/` as a candidate full domain block and use it for the next Solana-related product discussion before creating implementation tasks.