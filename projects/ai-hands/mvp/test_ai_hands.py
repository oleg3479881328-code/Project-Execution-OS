import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import ai_hands


def make_task(workspace: Path, **overrides):
    values = {
        "workspace": workspace,
        "model": "test",
        "instruction": "test",
        "target_file": "notes.txt",
        "expected_branch": "smoke/nondefault",
        "validation_command": [
            "powershell", "-ExecutionPolicy", "Bypass", "-File", ".\\validate.ps1"
        ],
    }
    values.update(overrides)
    return ai_hands.Task(**values)


class AdapterSafetyTests(unittest.TestCase):
    def test_rejects_target_outside_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            task = make_task(Path(tmp), target_file="../outside.txt")
            with self.assertRaises(ai_hands.ExecutionError):
                ai_hands.resolve_target(task)

    def test_rejects_unapproved_model_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            task = make_task(Path(tmp))
            with self.assertRaises(ai_hands.ExecutionError):
                ai_hands.validate_proposal(
                    task,
                    {"target_file": "other.txt", "new_content": "x", "summary": "x"},
                )

    def test_load_task_requires_argv_validation_command(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "task.json"
            path.write_text(json.dumps({
                "workspace": tmp,
                "model": "test",
                "instruction": "test",
                "target_file": "notes.txt",
                "expected_branch": "smoke/nondefault",
                "validation_command": "dangerous shell string",
            }), encoding="utf-8")
            with self.assertRaises(ai_hands.ExecutionError):
                ai_hands.load_task(path)

    def test_parses_standard_response_field(self):
        proposal = {"target_file": "notes.txt", "new_content": "x", "summary": "done"}
        self.assertEqual(ai_hands.parse_ollama_proposal({"response": json.dumps(proposal)}), proposal)

    def test_parses_reasoning_field_when_response_is_empty(self):
        proposal = {"target_file": "notes.txt", "new_content": "x", "summary": "done"}
        self.assertEqual(
            ai_hands.parse_ollama_proposal({"response": "", "thinking": json.dumps(proposal)}),
            proposal,
        )

    def test_rejects_non_json_reasoning_output(self):
        with self.assertRaises(ai_hands.ExecutionError):
            ai_hands.parse_ollama_proposal({"response": "", "thinking": "not-json"})

    def test_rejects_non_allowlisted_validation_executable(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            (workspace / "validate.ps1").write_text("exit 0", encoding="utf-8")
            task = make_task(workspace, validation_command=["python", "-c", "pass"])
            with self.assertRaises(ai_hands.ExecutionError):
                ai_hands.validate_validation_command(task)

    def test_rejects_default_branch(self):
        with tempfile.TemporaryDirectory() as tmp:
            task = make_task(Path(tmp), expected_branch="main")
            with mock.patch("ai_hands.git_output", side_effect=["true", "main"]):
                with self.assertRaises(ai_hands.ExecutionError):
                    ai_hands.verify_isolated_branch(task)

    def test_report_always_gets_next_action(self):
        report = {"status": "FAILED"}
        ai_hands.set_next_action(report)
        self.assertTrue(report["next_recommended_action"])


if __name__ == "__main__":
    unittest.main()
