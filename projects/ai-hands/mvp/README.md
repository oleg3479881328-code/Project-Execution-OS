# AI Hands MVP — Isolated Ollama Adapter

This MVP proves one narrow controller-led execution loop without changing Cline or its existing DeepSeek configuration.

## Role contract

- The owner defines product intent and priorities.
- ChatGPT is the controller, architect, task author, and reviewer.
- The executor runs the supplied code, captures evidence, and reports blockers. It must not redesign the architecture or silently broaden scope.
- The local Ollama model performs one bounded mechanical edit proposed in structured JSON.

## Safety boundary

The adapter:

- works only inside the exact resolved workspace from the task packet;
- permits exactly one existing target file;
- rejects path traversal and attempts to change another file;
- never executes model-proposed commands;
- runs only the controller-supplied validation command as an argv array with `shell=False`;
- restores the original file if validation fails or execution raises an error;
- does not touch Cline settings, DeepSeek credentials, Git remotes, branches, or external accounts.

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
- one deterministic allowlisted validation command.

## Expected output

The process prints one JSON report containing status, model summary, unified diff, validation command, exit code, stdout, stderr, or a precise error. Successful write status is `COMPLETE`. Failed validation is `VALIDATION_FAILED_ROLLED_BACK`.

## MVP acceptance test

1. Create a disposable directory and Git repository.
2. Create `notes.txt` containing `alpha`, `beta`, and `gamma` on separate lines.
3. Create a deterministic validation script that succeeds only when `delta` is present and `beta` is absent.
4. Run the adapter with `qwen3:4b`.
5. Confirm the report says `COMPLETE`, the diff changes only `notes.txt`, and the existing Cline/DeepSeek configuration remains unchanged.
