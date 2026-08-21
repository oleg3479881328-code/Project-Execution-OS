# Full Telegram Channel Audit via Telegram Desktop JSON Export

- Type: research method
- Review status: reviewed for practical reuse
- Scope: reusable across projects
- Recorded: 2026-08-21

## Problem

Public web access, Telegram previews, search engines, and third-party indexers do not guarantee a complete sequential archive of every post in a Telegram channel. This makes claims such as "I reviewed the whole channel" unreliable when only public indexing was used.

## Method

For a complete channel-level audit, prefer an owner/user-generated export from Telegram Desktop:

1. Open the target channel in Telegram Desktop.
2. Open the channel menu and choose `Export chat history`.
3. Export in machine-readable `JSON` format.
4. Text is sufficient for vacancy/content analysis unless media itself is part of the task.
5. Upload the resulting `result.json` or the export folder as a ZIP into the working chat/project.
6. Run the audit against the exported dataset, not against public previews or third-party mirrors.

## Why JSON

JSON is preferred over HTML for machine analysis because it preserves structured message data and is easier to parse, filter, deduplicate, classify, and aggregate. Telegram has also documented cases where HTML export could omit older messages while the JSON export contained them, so JSON is the safer default for completeness-sensitive audits.

## What This Enables

A full export can be converted into a structured registry such as:

`message -> date -> company/entity -> role/vacancy type -> pay model -> rate -> geography -> home time -> requirements -> links/contacts -> repeated claims -> verification status -> risk flags`

For CDL vacancy channels, this supports:

- complete vacancy inventory;
- company frequency analysis;
- Dry Van / Reefer / Flatbed / Car Hauler / Local / Regional / OTR classification;
- CPM / percentage / daily / weekly pay comparison;
- home-time and experience requirement extraction;
- detection of repeated or unusually aggressive earnings claims;
- downstream carrier verification through USDOT/MC/FMCSA and external reviews;
- ranked shortlist generation.

## When To Use

Use this method when the task requires claims about the **entire** Telegram channel or complete historical coverage.

Use especially when:

- missing even a small number of posts would distort conclusions;
- the user wants a full audit, ranking, historical trend, entity inventory, or deduplication;
- the channel is only partially visible through web search or public Telegram previews.

## When Not To Use

Do not require a full export when:

- only a few recent posts are needed;
- the user supplied the relevant messages directly;
- a spot-check or example analysis is sufficient.

## Reliability Rule

Do not say that the whole Telegram channel was reviewed unless the analysis source provides complete channel coverage, such as a full export or another source whose completeness was independently verified.

If only public indexing is available, explicitly describe the coverage as partial.

## Operational Note

Telegram may temporarily restrict exports from a newly authorized Telegram Desktop session and require waiting or confirmation from an already authorized device.

## Sources / Traceability

- Telegram issue tracker / export instructions: https://bugs.telegram.org/c/60/4
- Telegram issue tracker / HTML vs JSON export completeness example: https://bugs.telegram.org/c/42845/4
- Originating practical use case: audit of `https://t.me/top_cdl_offers` for complete CDL vacancy analysis.
