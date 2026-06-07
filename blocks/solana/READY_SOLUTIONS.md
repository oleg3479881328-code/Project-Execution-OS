# Solana Ready Solutions

## Purpose

Preserve known Solana tooling, frameworks, and donor paths so future agents check proven options before inventing custom blockchain architecture.

## Default Rule

Use existing programs and maintained frameworks before writing custom on-chain logic.

## Official / Core Sources

### Solana Documentation

Use for:

- core concepts;
- accounts;
- transactions;
- fees;
- programs;
- PDAs;
- CPI;
- frontend and SDK guidance.

### Solana Developer Templates

Use for:

- dApp starter paths;
- production-ready patterns;
- faster project bootstrapping.

### Official SDKs

Use official SDKs first where possible.

Important current TypeScript direction:

- `@solana/kit` should be checked as the recommended TypeScript SDK path;
- `@solana/web3.js` remains important as legacy/common ecosystem knowledge.

## Frameworks

### Anchor

Best default for custom Solana programs.

Use when:

- custom program logic is required;
- IDL-based client integration matters;
- testing and account constraints matter;
- team needs a widely used Solana program framework.

Risk:

- Anchor reduces some complexity but does not remove the need to understand Solana accounts, signers, ownership, PDAs, CPI, and security issues.

### Native Rust Solana Program

Use when:

- maximum control is needed;
- dependency minimization matters;
- the team has deep Solana expertise.

Risk:

- more footguns and slower development.

## Common Existing Programs / Protocol Areas

Consider before custom logic:

- System Program;
- SPL Token;
- Associated Token Account;
- Token Extensions;
- Memo;
- governance/stake-pool patterns when relevant;
- marketplace/payment protocols where appropriate.

## Frontend / Wallet Layer

Use when building wallet-connected apps:

- wallet adapter patterns;
- transaction simulation/preview;
- user confirmation flow;
- clear error handling;
- network/devnet/mainnet separation.

## Data / Indexing Layer

Use providers or indexers when direct RPC is not enough.

Evaluate:

- RPC provider reliability;
- historical data access;
- webhook/alert support;
- cost;
- rate limits;
- mainnet/devnet coverage.

## Donor Evaluation Checklist

Before accepting a Solana donor repo:

- last meaningful update is recent;
- dependency versions are maintained;
- devnet run path works;
- no private key or seed phrase patterns are unsafe;
- program tests exist if on-chain code exists;
- security notes are present;
- license is compatible;
- architecture matches the intended product surface.

## Final Rule

Do not write a custom Solana program until existing programs, Anchor patterns, SDK templates, and off-chain alternatives have been considered.