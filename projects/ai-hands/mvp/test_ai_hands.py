import json
import tempfile
import unittest
from pathlib import Path

import ai_hands


class AdapterSafetyTests(unittest.TestCase):
    def test_rejects_target_outside_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            task = ai_hands.Task(
                workspace=workspace,
                model="test",
                instruction="test",
                target_file="../outside.txt",
                validation_command=["python", "-c", "pass"],
            )
            with self.assertRaises(ai_hands.ExecutionError):
                ai_hands.resolve_target(task)

    def test_rejects_unapproved_model_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            task = ai_hands.Task(
                workspace=Path(tmp),
                model="test",
                instruction="test",
                target_file="notes.txt",
                validation_command=["python", "-c", "pass"],
            )
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
                "validation_command": "dangerous shell string",
            }), encoding="utf-8")
            with self.assertRaises(ai_hands.ExecutionError):
                ai_hands.load_task(path)


if __name__ == "__main__":
    unittest.main()
