# AI Hands MVP — Isolated Ollama Adapter

This MVP proves one narrow controller-led execution loop without changing Cline or its existing DeepSeek configuration.

## Existing-solution decision

The installed Cline + Ollama donor path was tested first in Issue #97. The headless path required a TTY or hung, and therefore did not satisfy the required bounded non-interactive execution contract. The project then moved to this minimal adapter as the smallest controlled fallback. Evidence: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/97

## Role contract

- The owner defines product intent and priorities.
- ChatGPT is the controller, architect, task author, and reviewer.
- The executor runs supplied code, captures evidence, and reports blockers. It must not redesign the architecture or silently broaden scope.
- The local Ollama model performs one bounded mechanical edit proposed in structured JSON.

## Safety boundary

The adapter:

- works only inside the exact resolved workspace from the task packet;
- requires the active Git branch to equal the controller-supplied `expected_branch`;
- refuses `main`, `master`, `trunk`, detached HEAD, and non-Git workspaces;
- permits exactly one existing target file;
- rejects path traversal and attempts to change another file;
- never executes model-proposed commands;
- accepts only the exact workspace-local PowerShell validation form ending in `validate.ps1`;
- runs validation with `shell=False`;
- restores the original file if validation fails, execution errors, or the operator interrupts validation;
- includes `next_recommended_action` in every report;
- does not touch Cline settings, DeepSeek credentials, Git remotes, or external accounts.

## Run

```powershell
python projects/ai-hands/mvp/ai_hands.py C:\path\to\task.json
```

Use `--dry-run` to request and validate the model proposal without writing the file or running validation.

## Task packet

See `task.example.json`. The controller must specify:

- absolute disposable workspace path;
- already-downloaded Ollama model;
- exact target file relative to that workspace;
- exact edit instruction;
- exact non-default branch expected to be active;
- the allowlisted workspace-local `validate.ps1` command.

## Expected output

The process prints one JSON report containing status, model summary, unified diff, validation evidence, errors when present, and the next recommended action. Successful write status is `COMPLETE`. Failed or interrupted validation is rolled back.

## MVP acceptance test

1. Create a disposable Git repository.
2. Create and switch to `smoke/nondefault` before running the adapter.
3. Create `notes.txt` containing `alpha`, `beta`, and `gamma` on separate lines.
4. Create `validate.ps1` that succeeds only when `delta` is present and `beta` is absent.
5. Run the adapter with `qwen3:4b` and `expected_branch` set to `smoke/nondefault`.
6. Confirm the report says `COMPLETE`, validation says `VALIDATION_OK`, the diff changes only `notes.txt`, and Cline/DeepSeek remain unchanged.
