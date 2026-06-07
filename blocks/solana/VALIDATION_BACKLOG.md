# Solana Validation Backlog

## Purpose

Track what must be validated before Solana Block recommendations are treated as proven operational workflow.

## Status

`candidate`

Research and structure are captured. Practical validation is still required.

## Framework Validation

- Build a simple wallet-connected frontend.
- Test wallet connect/disconnect.
- Test devnet transaction signing.
- Test `@solana/kit` in a small client flow.
- Compare current `@solana/web3.js` ecosystem examples.
- Create a minimal Anchor program.
- Run Anchor tests locally.
- Deploy a test program to devnet.

## Product Surface Validation

- Validate wallet-connected web app pattern.
- Validate token product pattern on devnet.
- Validate payment product pattern with backend order state.
- Validate AI agent transaction-preview pattern.
- Validate analytics/indexer pattern using a provider.

## Security Validation

- Produce a signer/owner/account check checklist from a real Anchor program.
- Test transaction simulation/preview UX.
- Confirm no private keys or seed phrases are stored in repo or logs.
- Validate devnet/mainnet separation.
- Review upgrade authority handling for a sample program.

## Monetization Validation

- Validate SaaS + wallet access model.
- Validate Solana payment checkout flow.
- Validate token-gated access flow.
- Validate backend license/access state after payment confirmation.

## Publishing / Launch Validation

- Define devnet acceptance checklist.
- Define mainnet readiness checklist.
- Define user support flow for failed transactions.
- Define monitoring needs after launch.

## Known Unvalidated Assumptions

- Anchor is the best default for most custom Solana program work.
- `@solana/kit` should be preferred for new TypeScript client work after checking current official guidance.
- Most owner projects should avoid custom programs unless product logic requires them.
- Solana payments can be productized cleanly with backend order state and wallet confirmation.

## Final Rule

Do not mark this block active until at least one real Solana project uses it successfully through devnet validation or production-ready review.