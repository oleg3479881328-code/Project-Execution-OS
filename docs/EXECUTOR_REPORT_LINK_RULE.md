# Executor Report Link Rule

Updated: 2026-07-10
Status: `active`

## Purpose

Ensure that every executor completion can be reviewed by ChatGPT without the owner copying a long status message or acting as a manual courier.

## Core Rule

Before an executor declares a bounded task complete, the executor must create one durable detailed report addressed to the active reviewer.

The report must be stored in a durable registered surface, preferably:

1. a signed `COMPLETE` comment in the active GitHub issue or pull request; or
2. a repository report file linked from that signed `COMPLETE` comment.

## Required Report Contents

The report must include:

- project and task;
- completed scope;
- exact branch and final commit SHA;
- files or artifacts created or changed;
- tests and validation actually performed;
- CI and artifact status;
- validation not performed;
- remaining limitations and risks;
- next safe reviewer action;
- owner action required, or `none`.

The executor must reconcile conflicting SHAs, test counts, or completion claims before publishing the report.

## Final Owner-Facing Link Rule

After the executor publishes the durable report, the executor's final owner-facing message must end with exactly one standalone direct URL to that report.

Do not place any text, second link, signature, suggestion, or explanation after that URL.

The link must open the detailed report that ChatGPT should review. Do not end with a general repository URL when a direct report-comment URL exists.

## Current-Task Correction Rule

When this rule is introduced after an executor has already posted a summary without a report link, the executor must:

1. publish the missing signed detailed report in the active channel;
2. update the executor-owned mailbox and durable project state;
3. send the owner a corrected final response whose last line is the single direct report URL.

## Final Rule

The owner may forward only the final report URL to ChatGPT. The owner must not be required to copy the report body, reconstruct evidence, or explain the executor's work.
