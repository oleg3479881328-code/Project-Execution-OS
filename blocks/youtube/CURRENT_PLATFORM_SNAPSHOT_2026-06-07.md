# YouTube Current Platform Snapshot — 2026-06-07

## Purpose

Capture freshness-sensitive YouTube facts separately from stable operating rules.

## YouTube Partner Program

Current higher-threshold ad-revenue eligibility paths documented by YouTube:

- 1,000 subscribers plus 4,000 valid public watch hours in the last 12 months; or
- 1,000 subscribers plus 10 million valid public Shorts views in the last 90 days.

Meeting thresholds does not guarantee acceptance. YouTube reviews the channel against monetization policies.

## Shorts Classification

For standard channels, square or vertical videos uploaded on or after 2024-10-15 with duration up to three minutes are categorized as Shorts.

Shorts can be uploaded through the YouTube app and YouTube Studio.

## Shorts Metrics

YouTube changed Shorts view counting starting 2025-03-31:

- a view counts when a Short starts to play or replay;
- the older metric is retained in Analytics as `Engaged views`;
- YPP eligibility and Shorts ad-revenue sharing remain based on engaged views.

## Shorts Monetization

Shorts monetization requires the relevant Shorts monetization terms/module.

YouTube documents that eligible Shorts revenue sharing is based on eligible engaged views in the Shorts Feed.

## Content Policy

YouTube updated terminology on 2025-07-15:

- `repetitious content` was renamed `inauthentic content`;
- repetitive or mass-produced content remains ineligible for monetization;
- reused-content policy remains separate.

## Content ID Risk For Longer Shorts

Shorts over one minute with an active Content ID claim are blocked globally and are not eligible for monetization until the claim is resolved.

## Brand Account Channels

YouTube documents Brand Account channels for cases where a channel needs a different public name from the Google Account or more than one manager/owner.

## API Uploads

YouTube Data API supports uploads through `videos.insert`.

Important current restriction:

- uploads from unverified API projects created after 2020-07-28 are restricted to private viewing mode until the API project passes an audit.

## Analytics APIs

YouTube documents:

- Analytics API for targeted queries;
- Reporting API for bulk reports and stored analysis workflows.

## Freshness Rule

Re-check official documentation before implementation, monetization planning, or scaling decisions. This snapshot is dated evidence, not a permanent rule file.