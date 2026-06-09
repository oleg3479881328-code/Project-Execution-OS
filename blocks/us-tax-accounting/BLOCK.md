# US Tax and Accounting Block

## Purpose

This block gives `Project Execution OS` a reusable workflow for United States taxation, bookkeeping, accounting operations, payroll, sales-tax routing, compliance triage, and professional handoff.

It helps an agent organize recurring tax and accounting work without treating stale memory, summaries, or AI output as authoritative.

## Status

`candidate`

## When To Use

Use this block when the task involves:

- bookkeeping or accounting setup;
- income and expense tracking;
- tax classification of a person or business;
- sole proprietorship, LLC, partnership, corporation, or S corporation questions;
- federal, state, or local tax routing;
- estimated taxes;
- self-employment income;
- gig-economy income;
- payroll, workers, contractors, W-2, 1099, or information returns;
- sales tax, indirect tax, or marketplace questions;
- monthly, quarterly, or year-end close;
- CPA, EA, bookkeeper, payroll-specialist, or tax-attorney handoff;
- tax notices, audit-readiness, or recordkeeping review;
- accounting-tool selection;
- tax-compliance workflow design for a project.

## When Not To Use

Do not use this block as a substitute for:

- current primary-source verification;
- filing a tax return without review;
- licensed professional advice where facts or risks require it;
- legal representation;
- payroll-provider execution without confirmation;
- storing confidential financial records, credentials, or tax identifiers inside the reusable block;
- assuming that federal rules automatically resolve state or local obligations.

## Core Rule

Do not answer a current tax, accounting, payroll, sales-tax, or filing question from memory alone.

Route work through:

`facts -> dates -> taxpayer -> entity -> tax classification -> jurisdictions -> activities -> income streams -> workers -> products or services -> transaction channels -> books quality -> deadlines -> primary-source verification -> action -> escalation decision -> evidence package`

## Required Reading Inside This Block

Open only the smallest relevant path:

1. `blocks/us-tax-accounting/TAX_AND_ACCOUNTING_INTAKE.md` for initial fact collection
2. `blocks/us-tax-accounting/SOURCE_HIERARCHY.md` before relying on a source
3. `blocks/us-tax-accounting/BUSINESS_ENTITY_AND_TAX_CLASSIFICATION.md` for entity and tax-treatment questions
4. `blocks/us-tax-accounting/BOOKKEEPING_STANDARD.md` for transaction capture, records, and books quality
5. `blocks/us-tax-accounting/TAX_CALENDAR_AND_DEADLINES.md` for filing and payment timing
6. `blocks/us-tax-accounting/FEDERAL_STATE_LOCAL_ROUTING.md` for jurisdiction checks
7. `blocks/us-tax-accounting/PAYROLL_CONTRACTORS_AND_INFORMATION_RETURNS.md` for workers, payroll, W-2, 1099, and information returns
8. `blocks/us-tax-accounting/SALES_TAX_AND_INDIRECT_TAX.md` for sales-tax and marketplace questions
9. `blocks/us-tax-accounting/MONTHLY_QUARTERLY_YEAR_END_CLOSE.md` for close workflows
10. `blocks/us-tax-accounting/CPA_EA_BOOKKEEPER_HANDOFF.md` for professional handoff
11. `blocks/us-tax-accounting/REVIEW_AND_ESCALATION.md` for quality review and escalation
12. `blocks/us-tax-accounting/TOOL_SELECTION_MATRIX.md` when selecting tools
13. `blocks/us-tax-accounting/READY_SOLUTIONS.md` for repeatable workflow patterns
14. `blocks/us-tax-accounting/SECURITY_AND_COMPLIANCE.md` for data handling
15. `blocks/us-tax-accounting/REFERENCES.md` for the maintained source map
16. `blocks/us-tax-accounting/VALIDATION_BACKLOG.md` for unverified assumptions and future tests
17. `blocks/us-tax-accounting/RESEARCH_REPORT_2026-06-09.md` for the initial research rationale
18. `blocks/us-law/BLOCK.md` when legal interpretation, disputes, notices, appeals, or attorney escalation become material

## Typical Modes

This block may route work into:

- individual side-income workflow;
- gig-economy workflow;
- solo-founder workflow;
- small-business bookkeeping setup;
- entity and tax-classification review;
- payroll and contractor workflow;
- sales-tax routing;
- recurring close workflow;
- year-end tax-preparer package;
- notice triage;
- accounting-tool selection;
- CPA, EA, bookkeeper, payroll-specialist, or tax-attorney handoff.

## Typical Outputs

Typical outputs:

- tax and accounting intake sheet;
- jurisdiction matrix;
- entity and tax-classification note;
- bookkeeping setup checklist;
- chart-of-accounts recommendation;
- monthly close checklist;
- deadline calendar;
- payroll and contractor checklist;
- sales-tax routing memo;
- books-quality review;
- unresolved-questions list;
- professional handoff packet;
- evidence package;
- escalation recommendation.

## Boundary

This block is a reusable organization, research, triage, and handoff layer.

Keep personal tax documents, bank records, payroll exports, Social Security numbers, EIN letters, account credentials, and final filings in the approved secure project layer.

## Final Rule

Use current primary sources, verify jurisdiction and dates, separate stable workflows from changing thresholds, preserve uncertainty, and escalate when the stakes require a qualified professional.