"""
Behavioral tests for mailbox_dispatcher.py (v6)

Run with: python -m unittest tools/mailbox-dispatcher/tests/test_dispatcher.py -v
"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mailbox_dispatcher import (
    ACTIVE_CHANNEL_ROUTE_PATH,
    DEVELOPMENT_ALLOWED_PATHS,
    RUNTIME_STAGED_PATHS,
    AdapterResult,
    DispatchResult,
    build_comment_body,
    check_dirty_tree_runtime,
    filter_dirty_entries,
    notifier_cycle,
    parse_adapter_result,
    parse_mailbox,
    persist_blocker_locally,
    read_current_sequence,
    read_current_type,
    run_runner,
    stage_runtime_files,
    validate_active_route,
    validate_before_mutation,
    write_mailbox,
    update_latest_log,
)


class TestParseMailbox(unittest.TestCase):
    def test_parse_full_envelope(self):
        content = (
            "# TO_EXECUTOR\n\n"
            "Sequence: 8\n"
            "Task-ID: test-task\n"
            "Type: CORRECTION\n"
            "Active-Channel: https://github.com/test/issues/52\n"
            "Comment-URL: https://github.com/test/issues/52#issuecomment-1\n"
            "Result-SHA: none\n"
            "Status-Artifact-SHA: pending\n"
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
        with patch(
            "mailbox_dispatcher.validate_active_route",
            return_value="https://github.com/test/issues/52",
        ), patch("mailbox_dispatcher.check_dirty_tree_runtime", return_value=[]):
            with self.assertRaises(RuntimeError):
                validate_before_mutation(
                    {"Active-Channel": "https://github.com/test/issues/51"},
                    8,
                )


class TestDirtyTreeFiltering(unittest.TestCase):
    def test_filter_dirty_entries_blocks_source_at_runtime(self):
        offending = filter_dirty_entries(
            [" M tools/mailbox-dispatcher/mailbox_dispatcher.py"],
            RUNTIME_STAGED_PATHS,
        )
        self.assertEqual(offending, ["M tools/mailbox-dispatcher/mailbox_dispatcher.py"])

    def test_filter_dirty_entries_allows_runtime_status_files(self):
        offending = filter_dirty_entries(
            [" M coordination/FROM_EXECUTOR.md", " M logs/latest.md"],
            RUNTIME_STAGED_PATHS,
        )
        self.assertEqual(offending, [])

    def test_check_dirty_tree_runtime_uses_runtime_paths(self):
        with patch(
            "mailbox_dispatcher.get_dirty_entries",
            return_value=[" M coordination/TO_EXECUTOR.md"],
        ):
            offending = check_dirty_tree_runtime()
            self.assertEqual(offending, ["M coordination/TO_EXECUTOR.md"])


class TestRuntimeStaging(unittest.TestCase):
    def test_stage_runtime_files_only_adds_runtime_paths(self):
        with patch("mailbox_dispatcher.run_command") as mock_run, patch(
            "mailbox_dispatcher.REPO_ROOT"
        ) as mock_root:
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
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_path, patch(
            "mailbox_dispatcher.read_current_sequence",
            side_effect=[8, 8],
        ), patch(
            "mailbox_dispatcher.parse_mailbox",
            return_value={"Supersedes-Sequence": None},
        ):
            mock_path.exists.return_value = True
            self.assertFalse(notifier_cycle())

    def test_notifier_processes_new_sequence(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_path, patch(
            "mailbox_dispatcher.read_current_sequence",
            side_effect=[7, 8],
        ), patch("mailbox_dispatcher.parse_mailbox") as mock_parse, patch(
            "mailbox_dispatcher.validate_before_mutation"
        ), patch(
            "mailbox_dispatcher.read_active_issue_body",
            return_value="body",
        ), patch("mailbox_dispatcher.commit_and_publish") as mock_publish:
            mock_path.exists.return_value = True
            mock_parse.return_value = {
                "Supersedes-Sequence": None,
                "Task-ID": "dispatcher-v6",
                "Active-Channel": "https://github.com/test/issues/52",
                "Type": "CORRECTION",
                "Next-Automatic-Action": "Continue",
                "Summary": "Fix it",
            }
            self.assertTrue(notifier_cycle())
            self.assertEqual(mock_publish.call_args.kwargs["result_sha_hint"], "none")


class TestRunnerBehavior(unittest.TestCase):
    def _runner_task(self):
        return {
            "Task-ID": "dispatcher-v6",
            "Active-Channel": "https://github.com/test/issues/52",
            "Next-Automatic-Action": "Continue",
            "Summary": "Fix it",
        }

    def test_runner_same_sequence_ack_executes_once(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, patch(
            "mailbox_dispatcher.read_current_sequence",
            side_effect=[8, 8],
        ), patch(
            "mailbox_dispatcher.read_current_type",
            return_value="ACK",
        ), patch(
            "mailbox_dispatcher.parse_mailbox",
            return_value=self._runner_task(),
        ), patch("mailbox_dispatcher.validate_before_mutation"), patch(
            "mailbox_dispatcher.read_active_issue_body",
            return_value="body",
        ), patch(
            "mailbox_dispatcher.run_command",
            return_value=MagicMock(
                returncode=0,
                stdout='{"status":"COMPLETE","summary":"done","result_sha":"abc123","evidence":["ok"]}',
                stderr="",
            ),
        ) as mock_run, patch(
            "mailbox_dispatcher.check_dirty_tree_runtime",
            return_value=[],
        ), patch("mailbox_dispatcher.commit_and_publish") as mock_publish:
            mock_to.exists.return_value = True
            run_runner("python --version", 30)
            self.assertEqual(mock_run.call_count, 1)
            self.assertEqual(mock_publish.call_args.kwargs["result_sha_hint"], "abc123")

    def test_runner_same_sequence_nonterminal_non_ack_does_not_execute(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, patch(
            "mailbox_dispatcher.read_current_sequence",
            side_effect=[8, 8],
        ), patch(
            "mailbox_dispatcher.read_current_type",
            return_value="HEARTBEAT",
        ), patch(
            "mailbox_dispatcher.parse_mailbox",
            return_value=self._runner_task(),
        ), patch("mailbox_dispatcher.run_command") as mock_run:
            mock_to.exists.return_value = True
            run_runner("python --version", 30)
            mock_run.assert_not_called()

    def test_runner_never_executes_mailbox_command(self):
        task = self._runner_task()
        task["Command"] = "rm -rf /"
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, patch(
            "mailbox_dispatcher.read_current_sequence",
            side_effect=[8, 8],
        ), patch(
            "mailbox_dispatcher.read_current_type",
            return_value="ACK",
        ), patch(
            "mailbox_dispatcher.parse_mailbox",
            return_value=task,
        ), patch("mailbox_dispatcher.validate_before_mutation"), patch(
            "mailbox_dispatcher.read_active_issue_body",
            return_value="body",
        ), patch(
            "mailbox_dispatcher.run_command",
            return_value=MagicMock(
                returncode=0,
                stdout='{"status":"COMPLETE","summary":"done","result_sha":"none","evidence":["ok"]}',
                stderr="",
            ),
        ) as mock_run, patch(
            "mailbox_dispatcher.check_dirty_tree_runtime",
            return_value=[],
        ), patch("mailbox_dispatcher.commit_and_publish"):
            mock_to.exists.return_value = True
            run_runner("python --version", 30)
            self.assertEqual(mock_run.call_args.args[0], ["python", "--version"])

    def test_post_run_dirty_source_file_blocks_complete(self):
        with patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, patch(
            "mailbox_dispatcher.read_current_sequence",
            side_effect=[8, 8],
        ), patch(
            "mailbox_dispatcher.read_current_type",
            return_value="ACK",
        ), patch(
            "mailbox_dispatcher.parse_mailbox",
            return_value=self._runner_task(),
        ), patch("mailbox_dispatcher.validate_before_mutation"), patch(
            "mailbox_dispatcher.read_active_issue_body",
            return_value="body",
        ), patch(
            "mailbox_dispatcher.run_command",
            return_value=MagicMock(
                returncode=0,
                stdout='{"status":"COMPLETE","summary":"done","result_sha":"abc123","evidence":["ok"]}',
                stderr="",
            ),
        ), patch(
            "mailbox_dispatcher.check_dirty_tree_runtime",
            return_value=["M tools/mailbox-dispatcher/mailbox_dispatcher.py"],
        ), patch("mailbox_dispatcher.commit_and_publish") as mock_publish:
            mock_to.exists.return_value = True
            run_runner("python --version", 30)
            self.assertEqual(mock_publish.call_args.kwargs["msg_type"], "BLOCKER")
            self.assertIn(
                "Runner validation error",
                "\n".join(mock_publish.call_args.kwargs["evidence"]),
            )


class TestStructuredResults(unittest.TestCase):
    def test_parse_adapter_result_supports_optional_result_sha(self):
        parsed = parse_adapter_result(
            '{"status":"COMPLETE","summary":"done","result_sha":null,"evidence":["one"]}'
        )
        self.assertEqual(
            parsed,
            AdapterResult(
                status="COMPLETE",
                summary="done",
                result_sha="none",
                evidence=["one"],
            ),
        )

    def test_comment_body_includes_two_shas(self):
        body = build_comment_body(
            msg_type="COMPLETE",
            task_id="dispatcher-v6",
            sequence=8,
            summary_text="done",
            evidence=["one"],
            next_auto="next",
            result_sha="a" * 40,
            status_artifact_sha="b" * 40,
        )
        self.assertIn("Result-SHA", body)
        self.assertIn("Status-Artifact-SHA", body)

    def test_dispatch_result_dataclass(self):
        result = DispatchResult(
            result_sha="a" * 40,
            status_artifact_sha="b" * 40,
            comment_url="https://github.com/test/issues/52#issuecomment-1",
            linkback_sha="c" * 40,
            summary_text="done",
            evidence=["x"],
        )
        self.assertEqual(result.linkback_sha, "c" * 40)


class TestDurableArtifacts(unittest.TestCase):
    def test_mailbox_and_log_include_explicit_sha_fields_and_comment_url(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            mailbox_path = Path(tmpdir) / "FROM_EXECUTOR.md"
            log_path = Path(tmpdir) / "latest.md"
            with patch("mailbox_dispatcher.LATEST_LOG_PATH", log_path), patch(
                "mailbox_dispatcher.LOGS_DIR",
                Path(tmpdir),
            ):
                write_mailbox(
                    path=mailbox_path,
                    sequence=8,
                    task_id="dispatcher-v6",
                    from_role="Executor",
                    to_role="Reviewer",
                    msg_type="COMPLETE",
                    active_channel="https://github.com/test/issues/52",
                    comment_url="https://github.com/test/issues/52#issuecomment-2",
                    result_sha="a" * 40,
                    status_artifact_sha="b" * 40,
                    linkback_sha="c" * 40,
                    local_status_sha=None,
                    remote_push="ok",
                    supersedes_sequence=None,
                    owner_action_required="none",
                    next_automatic_action="wait",
                    summary="done",
                    evidence=["one"],
                )
                update_latest_log(
                    marker="COMPLETE",
                    task_id="dispatcher-v6",
                    status="done",
                    reply_surface_url="https://github.com/test/issues/52",
                    comment_url="https://github.com/test/issues/52#issuecomment-2",
                    result_sha="a" * 40,
                    status_artifact_sha="b" * 40,
                    linkback_sha="c" * 40,
                    local_status_sha=None,
                    remote_push="ok",
                    next_action="wait",
                    owner_required="none",
                )

                mailbox = mailbox_path.read_text(encoding="utf-8")
                log = log_path.read_text(encoding="utf-8")
                for text in (
                    "Result-SHA: " + "a" * 40,
                    "Status-Artifact-SHA: " + "b" * 40,
                    "Comment-URL: https://github.com/test/issues/52#issuecomment-2",
                    "Linkback-SHA: " + "c" * 40,
                ):
                    self.assertIn(text, mailbox)
                    self.assertIn(text, log)

    def test_blocker_push_failure_writes_local_pending_marker(self):
        with patch("mailbox_dispatcher.write_mailbox") as mock_write, patch(
            "mailbox_dispatcher.update_latest_log"
        ) as mock_log, patch("mailbox_dispatcher.stage_runtime_files"), patch(
            "mailbox_dispatcher.run_command"
        ) as mock_run, patch(
            "mailbox_dispatcher.get_current_commit_sha",
            return_value="c" * 40,
        ):
            mock_run.side_effect = [MagicMock(returncode=0), RuntimeError("push failed")]
            sha, push_error = persist_blocker_locally(
                task_id="dispatcher-v6",
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
            final_write = mock_write.call_args_list[-1].kwargs
            self.assertEqual(final_write["local_status_sha"], "c" * 40)
            self.assertEqual(final_write["remote_push"], "failed")
            final_log = mock_log.call_args_list[-1].kwargs
            self.assertEqual(final_log["local_status_sha"], "c" * 40)
            self.assertEqual(final_log["remote_push"], "failed")

    def test_comment_and_durable_artifacts_use_matching_sha_semantics(self):
        body = build_comment_body(
            msg_type="COMPLETE",
            task_id="dispatcher-v6",
            sequence=8,
            summary_text="done",
            evidence=["Adapter-Result-SHA: none"],
            next_auto="wait",
            result_sha="none",
            status_artifact_sha="b" * 40,
        )
        self.assertIn("- Result-SHA: none", body)
        self.assertIn("- Status-Artifact-SHA: " + "b" * 40, body)


if __name__ == "__main__":
    unittest.main()
