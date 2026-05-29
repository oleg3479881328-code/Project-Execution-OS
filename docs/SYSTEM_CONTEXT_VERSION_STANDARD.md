# System Context Version Standard v1

## Purpose

This standard defines how `Project Execution OS` records versions of the stable central context used by humans, AI agents and future API orchestrators.

The goal is to make context changes visible, reproducible and measurable without forcing every routed document into one giant prompt.

## Core Rule

A context profile is an ordered manifest of the stable files intentionally used as the reusable foundation for a class of work.

```text
stable context profile
= ordered file list
+ current Git blob SHA for each file
+ deterministic SHA-256 fingerprint of the ordered list
```

Do not treat the fingerprint as proof that an external API provider cached the content. It proves only which repository context profile was intended and recorded.

## Canonical Manifest

The current central manifest lives at:

`SYSTEM_CONTEXT_MANIFEST.md`

## Profile Types

A manifest may define multiple profiles when real work requires them.

Use the smallest profile that fits the task.

Examples:

- `core-routing` = short stable routing foundation;
- `knowledge-aware` = routing foundation plus knowledge-selection rules;
- future project-specific profiles = stable project orientation plus explicitly selected reusable modules.

Do not create profiles by ritual. Add one only when a recurring execution path benefits from a stable reproducible context package.

## Canonical Fingerprint Input

To calculate a profile fingerprint:

1. list profile files in the exact intended loading order;
2. record each path and its current Git blob SHA;
3. create a UTF-8 text block with one line per file:

```text
<path>=<git-blob-sha>
```

4. end the text block with a final newline;
5. calculate SHA-256 over that exact UTF-8 text block.

Example:

```text
START_HERE.md=<blob-sha>
docs/CONTEXT_ASSEMBLY_STANDARD.md=<blob-sha>
```

## Update Rule

Update `SYSTEM_CONTEXT_MANIFEST.md` when:

- a file inside an active profile changes;
- loading order changes;
- a file is added to or removed from an active profile;
- a new recurring profile is intentionally introduced;
- a profile is deprecated or replaced.

Do not update the manifest for unrelated repository changes outside active context profiles.

## Compatibility Rule

Future agents, orchestrators or execution logs should record the relevant profile name and fingerprint when context version affects reproducibility, cost comparison or debugging.

If a long-running project intentionally stays pinned to an older context profile, record that choice explicitly rather than silently mixing versions.

## API Cache Relationship

For prefix-caching API providers, stable ordered profiles can improve the chance of repeated prefix reuse.

However:

- provider caching may be best-effort;
- cached content may expire;
- a recorded manifest does not prove cache hit;
- runtime token usage and cache-hit/cache-miss metrics must be logged separately when available.

Use `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md` for runtime measurement.

## Review Rule

Review should check:

- whether active profile contents are actually necessary;
- whether loading order is intentional;
- whether the recorded Git blob SHAs match current files;
- whether the SHA-256 fingerprint was derived from the canonical ordered input;
- whether a context profile has grown beyond its useful minimum.

## Related Nodes

- `SYSTEM_CONTEXT_MANIFEST.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`

## Final Rule

Version the stable context foundation.

Do not confuse versioned context identity with guaranteed provider-side caching.