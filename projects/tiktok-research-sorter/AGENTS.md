# AGENTS — TikTok Research Sorter

## Entry Order

1. Read the central system door: https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md
2. Follow the current router.
3. Read this project’s `PROJECT.md`.
4. Read `PROJECT_STATE.md` and `logs/latest.md` only when execution continuity is needed.
5. Open deeper files only for the active task.

## Working Rules

- Apply Existing Solution First before new architecture or custom tooling.
- Keep project files under `projects/tiktok-research-sorter/` while this is an internal subproject.
- Do not create a nested Git repository here.
- Keep permissions narrow and explain every new permission.
- Do not add remote executable code.
- Do not add CAPTCHA bypasses, stealth automation, credential extraction, private-profile access, or anti-bot evasion.
- Treat TikTok payload structures as adapters that may change; isolate platform-specific parsing.
- Add sanitized fixtures and tests for every payload shape fixed.
- Never commit cookies, tokens, authorization headers, browser profiles, or user-identifying raw traffic.
- Maintain `PROJECT_STATE.md` and `logs/latest.md` after meaningful execution.

## Validation

Before handoff, run:

```bash
npm install
npm run typecheck
npm test
npm run build
```

Record failures honestly. Browser behavior still requires an unpacked-extension smoke test in Chrome.
