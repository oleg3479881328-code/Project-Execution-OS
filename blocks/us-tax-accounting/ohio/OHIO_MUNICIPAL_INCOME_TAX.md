# Ohio Municipal Income Tax

## Purpose

Route Ohio municipal-income-tax questions correctly. Municipal tax is a separate layer from Ohio state tax.

## Core Rule

Do not assume one statewide municipal filing path. Identify the exact municipality and collector first.

## Collector Routing

Check whether the municipality uses:

- RITA — Regional Income Tax Agency;
- CCA — Central Collection Agency;
- direct municipal collection;
- another official local collector.

## Individual Review

Ask:

- municipality of residence;
- municipalities where work was performed;
- whether local tax was withheld;
- whether the taxpayer has self-employment income;
- whether estimated municipal payments may be required;
- whether a resident credit applies;
- whether a return is required even when withholding occurred;
- whether a notice was received.

## Business Review

Ask:

- business location;
- municipalities where services were performed;
- municipalities where employees worked;
- net-profit filing obligations;
- withholding obligations;
- estimated-payment obligations;
- W-2 reporting obligations;
- collector-specific portals and forms.

## Verification

For each municipality, confirm:

- collector;
- current tax rate;
- credit factor or resident credit;
- filing requirement;
- estimated-payment rule;
- withholding rule;
- form and portal;
- due date;
- notice-response route.

## Output

Produce a municipal matrix with:

- municipality;
- collector;
- taxpayer type;
- tax category;
- withholding status;
- filing requirement;
- source URL;
- due date;
- open question.

## Final Rule

Ohio municipal tax is not optional background. Treat it as a first-class workflow.