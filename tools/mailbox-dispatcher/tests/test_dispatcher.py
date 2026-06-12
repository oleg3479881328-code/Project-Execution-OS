"""
Behavioral tests for mailbox_dispatcher.py (v5)

Run with: python -m unittest tools/mailbox-dispatcher/tests/test_dispatcher.py -v
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mailbox_dispatcher import (
    ACTIVE_CHANNEL_ROUTE_PATH,
    DEVELOPMENT_ALLOWED_PATHS,
    RUNTIME_STAGED_PATHS,
    TERMINAL_STATES,
    DispatchResult,
    build_comment_body,
    check_dirty_tree_runtime,
    filter_dirty_entries,
    notifier_cycle,
    parse_mailbox,
    persist_blocker_locally,
    read_current_sequence,
    read_current_type,
    run_runner,
    stage_runtime_files,
    validate_active_route,
    validate_before_mutation,
)


class TestParseMailbox(unittest.TestCase):
    def test_parse_full_envelope(self):
        content = (
            "# TO_EXECUTOR\n\n"
            "Sequence: 8\n"
            "Task-ID: test-task\n"
            "Type: CORRECTION\n"
            "Active-Channel: https://github.com/test/issues/52\n"
            "Owner-Action-Required: none\n"
            "Next-Automatic-Action: Continue.\n\n"
            "## Summary\n\n"
            "Test summary.\n\n"
            "## Evidence\n\n"
            "- one\n"
        )
        path = Path("test_mailbox.md")
        path.write_text(content, encoding="utf-8")
        try:
            result = parse_mailbox(path)
            self.assertEqual(result["Sequence"], "8")
            self.assertEqual(result["Task-ID"], "test-task")
            self.assertIn("Test summary", result["Summary"])
            self.assertIn("- one", result["Evidence"])
        finally:
            path.unlink(missing_ok=True)

    def test_parse_missing_file(self):
        self.assertEqual(parse_mailbox(Path("missing.md")), {})


class TestReadHelpers(unittest.TestCase):
    def test_read_current_sequence(self):
        path = Path("test_sequence.md")
        path.write_text("Sequence: 42\n", encoding="utf-8")
        try:
            self.assertEqual(read_current_sequence(path), 42)
        finally:
            path.unlink(missing_ok=True)

    def test_read_current_type(self):
        path = Path("test_type.md")
        path.write_text("Type: ACK\n", encoding="utf-8")
        try:
            self.assertEqual(read_current_type(path), "ACK")
        finally:
            path.unlink(missing_ok=True)


class TestTerminalStates(unittest.TestCase):
    def test_ack_not_terminal(self):
        self.assertNotIn("ACK", TERMINAL_STATES)

    def test_complete_blocker_terminal(self):
        self.assertIn("COMPLETE", TERMINAL_STATES)
        self.assertIn("BLOCKER", TERMINAL_STATES)


class TestAllowedPaths(unittest.TestCase):
    def test_runtime_paths_are_narrow(self):
        self.assertEqual(
            RUNTIME_STAGED_PATHS,
            {"coordination/FROM_EXECUTOR.md", "logs/latest.md"},
        )

    def test_development_paths_include_source_and_tests(self):
        self.assertIn("tools/mailbox-dispatcher/mailbox_dispatcher.py", DEVELOPMENT_ALLOWED_PATHS)
        self.assertIn("tools/mailbox-dispatcher/tests/", DEVELOPMENT_ALLOWED_PATHS)


class TestRouteValidation(unittest.TestCase):
    def test_route_file_exists(self):
        self.assertTrue(ACTIVE_CHANNEL_ROUTE_PATH.exists())

    def test_validate_active_route_returns_url(self):
        url = validate_active_route()
        self.assertTrue(url.startswith("https://github.com/"))

    def test_validate_before_mutation_rejects_mismatch(self):
        with patch("mailbox_dispatcher.validate_active_route", return_value="https://github.com/test/issues/52"):
            with patch("mailbox_dispatcher.check_dirty_tree_runtime", return_value=[]):
                with self.assertRaises(RuntimeError):
                    validate_before_mutation({"Active-Channel": "https://github.com/test/issues/51"}, 8)


class TestDirtyTreeFiltering(unittest.TestCase):
    def test_filter_dirty_entries_blocks_source_at_runtime(self):
        entries = [" M tools/mailbox-dispatcher/mailbox_dispatcher.py"]
        offending = filter_dirty_entries(entries, RUNTIME_STAGED_PATHS)
        self.assertEqual(offending, ["M tools/mailbox-dispatcher/mailbox_dispatcher.py"])

    def test_filter_dirty_entries_allows_runtime_status_files(self):
        entries = [
            " M coordination/FROM_EXECUTOR.md",
            " M logs/latest.md",
        ]
        offending = filter_dirty_entries(entries, RUNTIME_STAGED_PATHS)
        self.assertEqual(offending, [])

    def test_check_dirty_tree_runtime_uses_runtime_paths(self):
        with patch("mailbox_dispatcher.get_dirty_entries", return_value=[" M coordination/TO_EXECUTOR.md"]):
            offending = check_dirty_tree_runtime()
            self.assertEqual(offending, ["M coordination/TO_EXECUTOR.md"])


class TestRuntimeStaging(unittest.TestCase):
    def test_stage_runtime_files_only_adds_runtime_paths(self):
        with patch("mailbox_dispatcher.run_command") as mock_run, patch("mailbox_dispatcher.REPO_ROOT") as mock_root:
            def fake_join(path):
                item = MagicMock()
                item.exists.return_value = True
                return item

            mock_root.__truediv__.side_effect = fake_join
            stage_runtime_files()
            added = [call.args[0][-1] for call in mock_run.call_args_list]
            self.assertEqual(sorted(added), sorted(RUNTIME_STAGED_PATHS))


class TestNotifierBehavior(unittest.TestCase):
    def test_notifier_skips_same_sequence(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_path, \
             patch("mailbox_dispatcher.read_current_sequence", side_effect=[8, 8]), \
             patch("mailbox_dispatcher.parse_mailbox", return_value={"Supersedes-Sequence": None}):
            mock_path.exists.return_value = True
            self.assertFalse(notifier_cycle())

    def test_notifier_processes_new_sequence(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_path, \
             patch("mailbox_dispatcher.read_current_sequence", side_effect=[7, 8]), \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse, \
             patch("mailbox_dispatcher.validate_before_mutation"), \
             patch("mailbox_dispatcher.read_active_issue_body", return_value="body"), \
             patch("mailbox_dispatcher.commit_and_publish") as mock_publish:
            mock_path.exists.return_value = True
            mock_parse.return_value = {
                "Supersedes-Sequence": None,
                "Task-ID": "dispatcher-v5",
                "Active-Channel": "https://github.com/test/issues/52",
                "Type": "CORRECTION",
                "Next-Automatic-Action": "Continue",
                "Summary": "Fix it",
            }
            self.assertTrue(notifier_cycle())
            mock_publish.assert_called_once()


class TestRunnerBehavior(unittest.TestCase):
    def test_runner_allows_ack_state(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, \
             patch("mailbox_dispatcher.read_current_sequence", side_effect=[8, 8]), \
             patch("mailbox_dispatcher.read_current_type", return_value="ACK"), \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse, \
             patch("mailbox_dispatcher.validate_before_mutation"), \
             patch("mailbox_dispatcher.read_active_issue_body", return_value="body"), \
             patch("mailbox_dispatcher.run_command", return_value=MagicMock(returncode=0, stdout="ok", stderr="")), \
             patch("mailbox_dispatcher.commit_and_publish") as mock_publish:
            mock_to.exists.return_value = True
            mock_parse.return_value = {
                "Task-ID": "dispatcher-v5",
                "Active-Channel": "https://github.com/test/issues/52",
                "Next-Automatic-Action": "Continue",
                "Summary": "Fix it",
            }
            run_runner("python --version", 30)
            mock_publish.assert_called_once()

    def test_runner_skips_terminal_state(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, \
             patch("mailbox_dispatcher.read_current_sequence", side_effect=[8, 8]), \
             patch("mailbox_dispatcher.read_current_type", return_value="COMPLETE"), \
             patch("mailbox_dispatcher.parse_mailbox", return_value={"Task-ID": "dispatcher-v5"}):
            mock_to.exists.return_value = True
            run_runner("echo hello", 30)

    def test_runner_never_executes_mailbox_command(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, \
             patch("mailbox_dispatcher.read_current_sequence", side_effect=[8, 8]), \
             patch("mailbox_dispatcher.read_current_type", return_value="ACK"), \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse, \
             patch("mailbox_dispatcher.validate_before_mutation"), \
             patch("mailbox_dispatcher.read_active_issue_body", return_value="body"), \
             patch("mailbox_dispatcher.run_command", return_value=MagicMock(returncode=0, stdout="ok", stderr="")) as mock_run, \
             patch("mailbox_dispatcher.commit_and_publish"):
            mock_to.exists.return_value = True
            mock_parse.return_value = {
                "Task-ID": "dispatcher-v5",
                "Active-Channel": "https://github.com/test/issues/52",
                "Next-Automatic-Action": "Continue",
                "Summary": "Fix it",
                "Command": "rm -rf /",
            }
            run_runner("python --version", 30)
            executed = mock_run.call_args.args[0]
            self.assertEqual(executed, ["python", "--version"])


class TestStructuredPublication(unittest.TestCase):
    def test_comment_body_includes_two_shas(self):
        body = build_comment_body(
            msg_type="COMPLETE",
            task_id="dispatcher-v5",
            sequence=8,
            summary_text="done",
            evidence=["one"],
            next_auto="next",
            result_sha="a" * 40,
            status_artifact_sha="b" * 40,
        )
        self.assertIn("Result-SHA", body)
        self.assertIn("Status-Artifact-SHA", body)

    def test_persist_blocker_returns_push_failure(self):
        with patch("mailbox_dispatcher.write_mailbox"), \
             patch("mailbox_dispatcher.update_latest_log"), \
             patch("mailbox_dispatcher.stage_runtime_files"), \
             patch("mailbox_dispatcher.run_command") as mock_run, \
             patch("mailbox_dispatcher.get_current_commit_sha", return_value="c" * 40):
            mock_run.side_effect = [
                MagicMock(returncode=0),  # commit
                RuntimeError("push failed"),
            ]
            sha, push_error = persist_blocker_locally(
                task_id="dispatcher-v5",
                sequence=8,
                active_channel="https://github.com/test/issues/52",
                comment_url="none",
                summary="blocked",
                evidence=["one"],
                next_action="wait",
                owner_required="fix",
            )
            self.assertEqual(sha, "c" * 40)
            self.assertIn("push failed", push_error)

    def test_dispatch_result_dataclass(self):
        result = DispatchResult(
            result_sha="a" * 40,
            status_artifact_sha="b" * 40,
            comment_url="https://github.com/test/issues/52#issuecomment-1",
            summary_text="done",
            evidence=["x"],
        )
        self.assertEqual(result.result_sha, "a" * 40)


if __name__ == "__main__":
    unittest.main()
