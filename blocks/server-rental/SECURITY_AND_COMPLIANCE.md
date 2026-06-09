# Security And Compliance

## Purpose

Define minimum safety and compliance checks for rented compute.

## Secrets

Never store in this block:

- API keys;
- SSH private keys;
- cloud credentials;
- billing credentials;
- provider passwords;
- private tokens.

Use a secrets manager or environment injection appropriate to the runtime.

## Baseline Controls

For every rented server:

- use key-based SSH access;
- disable password login when practical;
- restrict exposed ports;
- apply firewall rules;
- avoid public dashboards without authentication;
- rotate temporary credentials;
- separate development and production access;
- log provider, region, instance type, and lifecycle state;
- destroy unneeded instances;
- confirm that persistent volumes do not retain sensitive data unnecessarily.

## Data Handling

Before routing data to a rented server, classify:

- public;
- internal;
- confidential;
- legally sensitive;
- personally identifiable information;
- regulated data.

Do not route sensitive data to a provider or region without reviewing provider terms and applicable requirements.

## Regional Compliance

When using mainland China, Hong Kong, United States, or other regional nodes, verify:

- hosting restrictions;
- account-verification requirements;
- public-hosting requirements;
- cross-border data implications;
- sanctions and export-control exposure;
- payment restrictions;
- model-license restrictions;
- provider terms of service.

## Open-Source Model Licenses

For every deployed model, record:

- model license;
- commercial-use permission;
- redistribution rights;
- derivative-model conditions;
- output-use conditions when stated;
- attribution requirements;
- restricted-use clauses.

## Shutdown Discipline

Use automatic shutdown for expensive workers when practical.

Confirm separately whether:

- compute billing stops after shutdown;
- storage billing continues;
- public IP billing continues;
- snapshots continue to incur cost;
- idle endpoints remain billable.

## Boundary

This file is a reusable checklist, not legal advice. Unstable legal and provider-specific details belong in dated research artifacts.
