# US Tax and Accounting Block Research Report — 2026-06-09

## Purpose

Preserve the rationale and initial research conclusions behind the `us-tax-accounting` block.

## Why This Block Exists

`Project Execution OS` already contains a reusable United States law block. Tax and accounting work, however, needs an operational layer beyond legal research.

Recurring project questions include:

- how to organize books;
- which facts are needed before answering;
- how to separate entity type from tax classification;
- which federal, state, and local authorities must be checked;
- how to track deadlines;
- how to handle gig-economy income;
- how to route payroll, contractors, W-2, and 1099 workflows;
- how to review sales-tax exposure;
- how to close books monthly, quarterly, and annually;
- how to prepare a clean handoff to a bookkeeper, CPA, EA, payroll specialist, sales-tax specialist, or tax attorney.

## Research Method

The block follows the canonical domain-block process:

`Research -> Donors -> Patterns -> Ready Solutions -> Review -> Validation`

The initial donor set is based on official sources:

- IRS Small Business and Self-Employed Tax Center;
- IRS Publication 583;
- IRS business structures, EIN, estimated-tax, self-employment-tax, employment-tax, tax-calendar, forms, and gig-economy pages;
- SSA Business Services Online;
- FinCEN;
- U.S. Department of Labor;
- state revenue departments;
- secretaries of state;
- state labor and unemployment agencies;
- official local tax authorities.

## Main Conclusions

### 1. Tax answers must be date-sensitive

Rates, thresholds, due dates, forms, temporary relief, mileage amounts, credits, deductions, and reporting requirements can change. Stable workflows belong in permanent files. Current figures belong in dated snapshots or source-verified answers.

### 2. Entity and tax classification must be separated

A legal entity does not automatically answer how it is treated for tax purposes. Agents must record both.

### 3. Federal-only answers are incomplete

State and local tax, registration, payroll, sales-tax, franchise-tax, gross-receipts-tax, and municipal obligations must be routed explicitly.

### 4. Books quality is a first-class variable

A recommendation is only as reliable as the underlying transaction capture and reconciliation. The block therefore uses a books-quality scale from missing to handoff ready.

### 5. Worker classification and payroll deserve a dedicated route

Contractor and employee questions can create substantial operational and compliance risk. They should not be buried inside a generic checklist.

### 6. Sales tax deserves a dedicated route

Sales tax depends on state, activity, product, service, channel, marketplace, and date. SaaS and digital products require special caution.

### 7. The block must support professional handoff

A good agent workflow does not pretend to replace specialists. It organizes facts, records, open questions, deadlines, and source links so the correct professional can work efficiently.

## Initial Files

The initial block contains:

- `BLOCK.md`
- `SOURCE_HIERARCHY.md`
- `TAX_AND_ACCOUNTING_INTAKE.md`
- `BUSINESS_ENTITY_AND_TAX_CLASSIFICATION.md`
- `BOOKKEEPING_STANDARD.md`
- `TAX_CALENDAR_AND_DEADLINES.md`
- `FEDERAL_STATE_LOCAL_ROUTING.md`
- `PAYROLL_CONTRACTORS_AND_INFORMATION_RETURNS.md`
- `SALES_TAX_AND_INDIRECT_TAX.md`
- `MONTHLY_QUARTERLY_YEAR_END_CLOSE.md`
- `CPA_EA_BOOKKEEPER_HANDOFF.md`
- `REVIEW_AND_ESCALATION.md`
- `TOOL_SELECTION_MATRIX.md`
- `READY_SOLUTIONS.md`
- `SECURITY_AND_COMPLIANCE.md`
- `REFERENCES.md`
- `VALIDATION_BACKLOG.md`

## Current Boundary

This is a candidate reusable workflow layer. It does not contain personal records, current annual thresholds, state-by-state tax tables, or professional advice.

## Next Validation

Validate the block on:

1. W-2 employee with gig income and vehicle expenses;
2. solo SaaS founder;
3. small service business with employees;
4. ecommerce or digital-product seller;
5. taxpayer receiving a notice;
6. incomplete year-end books.

## Final Rule

Keep permanent workflow logic stable, verify current rules from primary sources, and promote narrower sub-blocks only after repeated real-world use justifies them.