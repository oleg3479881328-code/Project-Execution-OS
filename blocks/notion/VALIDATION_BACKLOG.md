# Validation Backlog

## Purpose

Track what must be proven before the Notion agent workspace block can move from `candidate` to `active`.

## Required Validation

- Create one real test Notion project page with `PROJECT_ID`.
- Create the eight workspace databases.
- Verify that an agent can find the project by `PROJECT_ID`.
- Verify that an agent can read only the smallest relevant database slice.
- Verify that a Notion project page and any attached GitHub entrypoint cross-link cleanly.
- Verify conflict handling when two layers disagree.
- Test native Notion GitHub integration for issue and pull-request visibility.
- Test Notion MCP or connector availability in each target agent environment.
- Test that required database properties can be written reliably.
- Decide whether initial automation should remain manual, use native integration, use n8n, use a GitHub Action, or use custom code.
- Confirm that no secrets or confidential documents are stored in the reusable block.

## Open Questions

- Should the central Projects database become the canonical Notion registry for all Notion-connected projects?
- Should each project entrypoint store its Notion project URL even when the project is GitHub-backed?
- Should approved Notion task intake be allowed to create GitHub issues automatically?
- Which fields should be mirrored and which should remain single-layer only?
- What is the minimum MCP capability set for agent re-entry?
- Should Bublup links be stored directly on Projects, or only through Assets and Links?

## Activation Criteria

This block can become `active` only after:

1. one real project uses the workspace contract;
2. at least one fresh agent re-enters through `PROJECT_ID` without owner explanation;
3. source-of-truth conflict handling is tested;
4. the database schema is reviewed after practical use;
5. the owner approves activation.

## Final Rule

Do not mark the Notion layer solved until it works across a real project without creating duplicate truth.