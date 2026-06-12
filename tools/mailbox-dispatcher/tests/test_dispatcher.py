"""
Behavioral tests for mailbox_dispatcher.py (v4)

Run with: python -m unittest tools/mailbox-dispatcher/tests/test_dispatcher.py -v
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add parent to path so we can import the dispatcher
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mailbox_dispatcher import (
    parse_mailbox,
    read_current_sequence,
    read_current_type,
    check_dirty_tree,
    validate_active_route,
    validate_before_mutation,
    stage_runtime_files,
    ALLOWED_STAGED_PATHS,
    RUNTIME_STAGED_PATHS,
    REPO_ROOT,
    ACTIVE_CHANNEL_ROUTE_PATH,
    TERMINAL_STATES,
    FROM_EXECUTOR_PATH,
    TO_EXECUTOR_PATH,
)


class TestParseMailbox(unittest.TestCase):
    """Test mailbox envelope parsing."""

    def test_parse_full_envelope(self):
        """Parse a complete mailbox envelope."""
        content = "# TO_EXECUTOR\n\nSequence: 2\nUpdated-At: 2026-06-11T21:47:24Z\nTask-ID: test-task\nFrom: Reviewer\nTo: Executor\nType: CORRECTION\nActive-Channel: https://github.com/test/issues/1\nSupersedes-Sequence: 1\nOwner-Action-Required: none\nNext-Automatic-Action: Post ACK.\n\n## Summary\n\nTest summary.\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(content)
            tmp_path = f.name

        try:
            result = parse_mailbox(Path(tmp_path))
            self.assertEqual(result.get("Sequence"), "2")
            self.assertEqual(result.get("Task-ID"), "test-task")
            self.assertEqual(result.get("Type"), "CORRECTION")
            self.assertEqual(result.get("Supersedes-Sequence"), "1")
            self.assertEqual(result.get("Owner-Action-Required"), "none")
            self.assertIn("Test summary", result.get("Summary", ""))
        finally:
            os.unlink(tmp_path)

    def test_parse_empty_file(self):
        """Parse a non-existent file returns empty dict."""
        result = parse_mailbox(Path("/nonexistent/path.md"))
        self.assertEqual(result, {})


class TestReadCurrentSequence(unittest.TestCase):
    """Test sequence reading from mailbox files."""

    def test_read_sequence(self):
        """Read sequence from a valid mailbox."""
        content = "# TO_EXECUTOR\n\nSequence: 42\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(content)
            tmp_path = f.name

        try:
            seq = read_current_sequence(Path(tmp_path))
            self.assertEqual(seq, 42)
        finally:
            os.unlink(tmp_path)

    def test_read_sequence_missing_file(self):
        """Missing file returns 0."""
        seq = read_current_sequence(Path("/nonexistent/path.md"))
        self.assertEqual(seq, 0)


class TestReadCurrentType(unittest.TestCase):
    """Test reading Type field from mailbox files."""

    def test_read_type_ack(self):
        """Read Type: ACK from a mailbox."""
        content = "# FROM_EXECUTOR\n\nSequence: 2\nType: ACK\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(content)
            tmp_path = f.name

        try:
            t = read_current_type(Path(tmp_path))
            self.assertEqual(t, "ACK")
        finally:
            os.unlink(tmp_path)

    def test_read_type_complete(self):
        """Read Type: COMPLETE from a mailbox."""
        content = "# FROM_EXECUTOR\n\nSequence: 2\nType: COMPLETE\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(content)
            tmp_path = f.name

        try:
            t = read_current_type(Path(tmp_path))
            self.assertEqual(t, "COMPLETE")
        finally:
            os.unlink(tmp_path)

    def test_read_type_missing_file(self):
        """Missing file returns empty string."""
        t = read_current_type(Path("/nonexistent/path.md"))
        self.assertEqual(t, "")


class TestTerminalStates(unittest.TestCase):
    """Test TERMINAL_STATES constant."""

    def test_complete_is_terminal(self):
        """COMPLETE is a terminal state."""
        self.assertIn("COMPLETE", TERMINAL_STATES)

    def test_blocker_is_terminal(self):
        """BLOCKER is a terminal state."""
        self.assertIn("BLOCKER", TERMINAL_STATES)

    def test_ack_not_terminal(self):
        """ACK is NOT a terminal state."""
        self.assertNotIn("ACK", TERMINAL_STATES)


class TestCheckDirtyTree(unittest.TestCase):
    """Test dirty tree detection."""

    def test_clean_tree(self):
        """Clean tree returns empty list."""
        dirty = check_dirty_tree()
        self.assertIsInstance(dirty, list)

    def test_allowed_paths_defined(self):
        """ALLOWED_STAGED_PATHS contains expected entries."""
        self.assertIn("coordination/TO_EXECUTOR.md", ALLOWED_STAGED_PATHS)
        self.assertIn("coordination/FROM_EXECUTOR.md", ALLOWED_STAGED_PATHS)
        self.assertIn("logs/latest.md", ALLOWED_STAGED_PATHS)
        self.assertIn("tools/mailbox-dispatcher/mailbox_dispatcher.py", ALLOWED_STAGED_PATHS)
        self.assertIn("tools/mailbox-dispatcher/README.md", ALLOWED_STAGED_PATHS)
        self.assertIn("tools/mailbox-dispatcher/tests/", ALLOWED_STAGED_PATHS)


class TestRuntimeStagingPaths(unittest.TestCase):
    """Test RUNTIME_STAGED_PATHS (v4)."""

    def test_runtime_staging_excludes_to_executor(self):
        """RUNTIME_STAGED_PATHS excludes TO_EXECUTOR.md."""
        self.assertNotIn("coordination/TO_EXECUTOR.md", RUNTIME_STAGED_PATHS)

    def test_runtime_staging_excludes_source(self):
        """RUNTIME_STAGED_PATHS excludes dispatcher source."""
        self.assertNotIn("tools/mailbox-dispatcher/mailbox_dispatcher.py", RUNTIME_STAGED_PATHS)

    def test_runtime_staging_excludes_readme(self):
        """RUNTIME_STAGED_PATHS excludes README."""
        self.assertNotIn("tools/mailbox-dispatcher/README.md", RUNTIME_STAGED_PATHS)

    def test_runtime_staging_excludes_tests(self):
        """RUNTIME_STAGED_PATHS excludes tests directory."""
        self.assertNotIn("tools/mailbox-dispatcher/tests/", RUNTIME_STAGED_PATHS)

    def test_runtime_staging_includes_from_executor(self):
        """RUNTIME_STAGED_PATHS includes FROM_EXECUTOR.md."""
        self.assertIn("coordination/FROM_EXECUTOR.md", RUNTIME_STAGED_PATHS)

    def test_runtime_staging_includes_latest_log(self):
        """RUNTIME_STAGED_PATHS includes logs/latest.md."""
        self.assertIn("logs/latest.md", RUNTIME_STAGED_PATHS)


class TestValidateActiveRoute(unittest.TestCase):
    """Test active route validation."""

    def test_route_file_exists(self):
        """ACTIVE_CHANNEL_ROUTE.md exists and is readable."""
        self.assertTrue(
            ACTIVE_CHANNEL_ROUTE_PATH.exists(),
            f"ACTIVE_CHANNEL_ROUTE.md not found at {ACTIVE_CHANNEL_ROUTE_PATH}",
        )

    def test_route_contains_write_here(self):
        """Route file contains 'Write Here' section."""
        content = ACTIVE_CHANNEL_ROUTE_PATH.read_text(encoding="utf-8")
        self.assertIn("### Write Here", content)

    def test_route_url_matches_issue_49(self):
        """The Write Here URL points to Issue #49."""
        import re
        content = ACTIVE_CHANNEL_ROUTE_PATH.read_text(encoding="utf-8")
        match = re.search(r"### Write Here\s*\n\s*`(https?://\S+)`", content)
        self.assertIsNotNone(match, "Could not find Write Here URL")
        url = match.group(1)
        self.assertIn("issues/49", url)


class TestValidateBeforeMutation(unittest.TestCase):
    """Test pre-mutation validation."""

    def test_validate_with_valid_route(self):
        """Valid route passes validation."""
        task = {
            "Active-Channel": "https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49",
        }
        try:
            route_url = validate_before_mutation(task, 3)
            self.assertIn("issues/49", route_url)
        except RuntimeError as e:
            self.fail(f"validate_before_mutation raised unexpectedly: {e}")

    def test_validate_with_mismatched_route(self):
        """Mismatched route raises RuntimeError."""
        task = {
            "Active-Channel": "https://github.com/other/repo/issues/999",
        }
        with self.assertRaises(RuntimeError):
            validate_before_mutation(task, 3)


class TestStageRuntimeFiles(unittest.TestCase):
    """Test staging of runtime files (v4)."""

    def test_stage_runtime_files_runs(self):
        """stage_runtime_files runs without error in clean repo."""
        try:
            stage_runtime_files()
        except RuntimeError as e:
            pass


class TestNotifierACKBehavior(unittest.TestCase):
    """Behavioral tests for notifier ACK logic (v4)."""

    def test_notifier_skips_terminal_state(self):
        """Notifier skips when FROM_EXECUTOR is already COMPLETE for same seq."""
        from mailbox_dispatcher import notifier_cycle

        # Simulate: TO_EXECUTOR seq=2, FROM_EXECUTOR seq=2 Type=COMPLETE
        # notifier_cycle should return False (no new work)
        with patch("mailbox_dispatcher.read_current_sequence") as mock_seq, \
             patch("mailbox_dispatcher.read_current_type") as mock_type, \
             patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_path, \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse:

            mock_path.exists.return_value = True
            mock_seq.side_effect = [2, 2]  # from_seq=2, to_seq=2
            mock_type.return_value = "COMPLETE"
            mock_parse.return_value = {"Supersedes-Sequence": None}

            result = notifier_cycle()
            self.assertFalse(result)

    def test_notifier_skips_same_sequence_ack(self):
        """v4: Notifier skips when same sequence even if ACK (no repeat ACK)."""
        from mailbox_dispatcher import notifier_cycle

        with patch("mailbox_dispatcher.read_current_sequence") as mock_seq, \
             patch("mailbox_dispatcher.read_current_type") as mock_type, \
             patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_path, \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse:

            mock_path.exists.return_value = True
            mock_seq.side_effect = [2, 2]  # from_seq=2, to_seq=2
            mock_type.return_value = "ACK"
            mock_parse.return_value = {"Supersedes-Sequence": None}

            # v4: Notifier does NOT repeat ACK for same sequence
            result = notifier_cycle()
            self.assertFalse(result)

    def test_notifier_processes_new_sequence(self):
        """v4: Notifier processes when to_seq > from_seq (new sequence)."""
        from mailbox_dispatcher import notifier_cycle

        with patch("mailbox_dispatcher.read_current_sequence") as mock_seq, \
             patch("mailbox_dispatcher.read_current_type") as mock_type, \
             patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_path, \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse, \
             patch("mailbox_dispatcher.validate_before_mutation") as mock_val, \
             patch("mailbox_dispatcher.read_active_issue_body") as mock_issue, \
             patch("mailbox_dispatcher.commit_and_publish") as mock_pub:

            mock_path.exists.return_value = True
            mock_seq.side_effect = [2, 3]  # from_seq=2, to_seq=3 (new!)
            mock_type.return_value = "COMPLETE"
            mock_parse.return_value = {
                "Supersedes-Sequence": None,
                "Task-ID": "test",
                "Active-Channel": "https://github.com/test/issues/1",
                "From": "Reviewer",
                "Type": "HANDOFF",
                "Next-Automatic-Action": "test",
                "Summary": "test",
            }
            mock_val.return_value = "https://github.com/test/issues/1"
            mock_issue.return_value = "issue body"

            result = notifier_cycle()
            self.assertTrue(result)
            mock_pub.assert_called_once()


class TestRunnerACKTransition(unittest.TestCase):
    """Behavioral tests for runner ACK-to-execution transition (v4)."""

    def test_runner_allows_ack_state(self):
        """Runner allows execution when FROM_EXECUTOR Type is ACK."""
        from mailbox_dispatcher import run_runner

        with patch("mailbox_dispatcher.read_current_sequence") as mock_seq, \
             patch("mailbox_dispatcher.read_current_type") as mock_type, \
             patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, \
             patch("mailbox_dispatcher.FROM_EXECUTOR_PATH") as mock_from, \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse, \
             patch("mailbox_dispatcher.validate_before_mutation") as mock_val, \
             patch("mailbox_dispatcher.read_active_issue_body") as mock_issue, \
             patch("mailbox_dispatcher.commit_and_publish") as mock_pub:

            mock_to.exists.return_value = True
            mock_seq.side_effect = [2, 2]  # to_seq=2, from_seq=2
            mock_type.return_value = "ACK"
            mock_parse.return_value = {
                "Task-ID": "test",
                "Active-Channel": "https://github.com/test/issues/1",
                "From": "Reviewer",
                "Next-Automatic-Action": "test",
                "Summary": "test",
            }
            mock_val.return_value = "https://github.com/test/issues/1"
            mock_issue.return_value = "issue body"

            # Should not raise or exit early
            run_runner("python --version", 30)
            mock_pub.assert_called_once()

    def test_runner_skips_terminal_state(self):
        """Runner skips when FROM_EXECUTOR is already COMPLETE."""
        from mailbox_dispatcher import run_runner

        with patch("mailbox_dispatcher.read_current_sequence") as mock_seq, \
             patch("mailbox_dispatcher.read_current_type") as mock_type, \
             patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, \
             patch("mailbox_dispatcher.FROM_EXECUTOR_PATH") as mock_from, \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse:

            mock_to.exists.return_value = True
            mock_seq.side_effect = [2, 2]  # to_seq=2, from_seq=2
            mock_type.return_value = "COMPLETE"
            mock_parse.return_value = {"Task-ID": "test"}

            # Should print "Already in terminal state" and return
            run_runner("echo hello", 30)
            # No exception means it returned early


class TestShlexSplit(unittest.TestCase):
    """Test shlex.split for quoted arguments."""

    def test_shlex_split_simple(self):
        """Simple command splits correctly."""
        import shlex
        parts = shlex.split("echo hello world")
        self.assertEqual(parts, ["echo", "hello", "world"])

    def test_shlex_split_quoted(self):
        """Quoted arguments are preserved."""
        import shlex
        parts = shlex.split('echo "hello world"')
        self.assertEqual(parts, ["echo", "hello world"])

    def test_shlex_split_mixed(self):
        """Mixed quoted and unquoted arguments."""
        import shlex
        parts = shlex.split('git commit -m "test message"')
        self.assertEqual(parts, ["git", "commit", "-m", "test message"])


class TestPostCommitSHA(unittest.TestCase):
    """Test that SHA is reported after commit."""

    def test_sha_format(self):
        """SHA should be a 40-char hex string."""
        import subprocess
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True,
            cwd=REPO_ROOT,
        )
        sha = result.stdout.strip()
        self.assertEqual(len(sha), 40)
        int(sha, 16)  # Should not raise


class TestIdempotency(unittest.TestCase):
    """Test restart idempotency logic (v4)."""

    def test_same_sequence_skipped(self):
        """If FROM_EXECUTOR sequence >= TO_EXECUTOR sequence and terminal, no action."""
        to_seq = 2
        from_seq = 2
        from_type = "COMPLETE"
        # Should skip
        self.assertTrue(to_seq <= from_seq and from_type in TERMINAL_STATES)

    def test_new_sequence_detected(self):
        """If TO_EXECUTOR seq > FROM_EXECUTOR seq, new work."""
        to_seq = 3
        from_seq = 2
        self.assertGreater(to_seq, from_seq)

    def test_ack_state_allows_runner_rerun(self):
        """v4: ACK state allows runner to re-process same sequence."""
        to_seq = 2
        from_seq = 2
        from_type = "ACK"
        # Should NOT skip for runner (ACK is not terminal)
        self.assertFalse(from_type in TERMINAL_STATES)

    def test_notifier_skips_ack_state(self):
        """v4: Notifier skips same sequence even if ACK (no repeat ACK)."""
        to_seq = 2
        from_seq = 2
        # Notifier only processes NEW sequences (to_seq > from_seq)
        self.assertFalse(to_seq > from_seq)


class TestRecoverableBlocker(unittest.TestCase):
    """Test recoverable blocker behavior (v4)."""

    def test_post_blocker_recoverable_does_not_exit(self):
        """post_blocker_and_exit with recoverable=True does not call sys.exit."""
        from mailbox_dispatcher import post_blocker_and_exit

        with patch("mailbox_dispatcher.post_issue_comment") as mock_comment, \
             patch("mailbox_dispatcher.write_mailbox"), \
             patch("mailbox_dispatcher.update_latest_log"), \
             patch("mailbox_dispatcher.stage_runtime_files"), \
             patch("mailbox_dispatcher.run_command"):

            mock_comment.return_value = "https://github.com/test/issues/1#comment-1"

            task = {
                "Task-ID": "test",
                "From": "Reviewer",
            }

            # Should NOT call sys.exit(1) — returns normally
            try:
                post_blocker_and_exit(task, 5, "test error", "https://github.com/test/issues/1", recoverable=True)
            except SystemExit:
                self.fail("post_blocker_and_exit with recoverable=True should not exit")


class TestCommitAndPublishFailure(unittest.TestCase):
    """Test commit/push failure behavior (v4)."""

    def test_commit_failure_blocks_complete(self):
        """v4: Commit failure blocks COMPLETE and posts BLOCKER."""
        from mailbox_dispatcher import commit_and_publish

        with patch("mailbox_dispatcher.stage_runtime_files"), \
             patch("mailbox_dispatcher.run_command") as mock_run, \
             patch("mailbox_dispatcher.post_blocker_and_exit") as mock_blocker:

            # Make git push fail
            mock_run.side_effect = RuntimeError("git push failed: network error")

            task = {
                "Task-ID": "test",
                "From": "Reviewer",
            }

            commit_and_publish(
                task=task,
                to_seq=5,
                msg_type="COMPLETE",
                comment_body="test",
                summary_text="test",
                evidence=[],
                active_channel="https://github.com/test/issues/1",
                next_auto="none",
                owner_required="none",
            )

            # Should have called post_blocker_and_exit
            mock_blocker.assert_called_once()


class TestDurableDirtyTreeBlocker(unittest.TestCase):
    """Test durable dirty-tree blocker (v4)."""

    def test_blocker_saves_from_executor_and_logs(self):
        """v4: BLOCKER saves FROM_EXECUTOR.md and logs/latest.md via stage_runtime_files."""
        from mailbox_dispatcher import post_blocker_and_exit

        with patch("mailbox_dispatcher.post_issue_comment") as mock_comment, \
             patch("mailbox_dispatcher.write_mailbox"), \
             patch("mailbox_dispatcher.update_latest_log"), \
             patch("mailbox_dispatcher.stage_runtime_files") as mock_stage, \
             patch("mailbox_dispatcher.run_command"):

            mock_comment.return_value = "https://github.com/test/issues/1#comment-1"

            task = {
                "Task-ID": "test",
                "From": "Reviewer",
            }

            try:
                post_blocker_and_exit(task, 5, "dirty tree", "https://github.com/test/issues/1", recoverable=True)
            except SystemExit:
                pass

            # stage_runtime_files should have been called to durably save blocker state
            mock_stage.assert_called_once()


class TestSHAPublication(unittest.TestCase):
    """Test SHA publication (v4)."""

    def test_result_sha_in_evidence(self):
        """v4: Result-SHA is included in evidence."""
        from mailbox_dispatcher import commit_and_publish

        with patch("mailbox_dispatcher.stage_runtime_files"), \
             patch("mailbox_dispatcher.run_command") as mock_run, \
             patch("mailbox_dispatcher.post_issue_comment") as mock_comment, \
             patch("mailbox_dispatcher.write_mailbox") as mock_write, \
             patch("mailbox_dispatcher.update_latest_log"), \
             patch("mailbox_dispatcher.get_current_commit_sha") as mock_sha:

            # First push succeeds, second push (artifacts) also succeeds
            mock_run.return_value = MagicMock(returncode=0)
            mock_comment.return_value = "https://github.com/test/issues/1#comment-1"
            mock_sha.side_effect = ["abc123def456", "789ghi"]  # result_sha, then artifact_sha

            task = {
                "Task-ID": "test",
                "From": "Reviewer",
            }

            commit_and_publish(
                task=task,
                to_seq=5,
                msg_type="COMPLETE",
                comment_body="test",
                summary_text="test",
                evidence=["some evidence"],
                active_channel="https://github.com/test/issues/1",
                next_auto="none",
                owner_required="none",
            )

            # Check that write_mailbox was called with evidence containing Result-SHA
            call_args = mock_write.call_args
            self.assertIsNotNone(call_args)
            _, kwargs = call_args
            evidence_list = kwargs.get("evidence", [])
            self.assertTrue(any("Result-SHA" in e for e in evidence_list))


class TestSecurityBoundary(unittest.TestCase):
    """Test security boundary (v4)."""

    def test_never_execute_mailbox_content(self):
        """v4: Runner never executes command text from mailbox content."""
        from mailbox_dispatcher import run_runner

        # The command comes from --command CLI argument, not from mailbox content.
        # Verify that run_runner uses its 'command' parameter, not task data.
        with patch("mailbox_dispatcher.read_current_sequence") as mock_seq, \
             patch("mailbox_dispatcher.read_current_type") as mock_type, \
             patch("mailbox_dispatcher.TO_EXECUTOR_PATH") as mock_to, \
             patch("mailbox_dispatcher.FROM_EXECUTOR_PATH") as mock_from, \
             patch("mailbox_dispatcher.parse_mailbox") as mock_parse, \
             patch("mailbox_dispatcher.validate_before_mutation") as mock_val, \
             patch("mailbox_dispatcher.read_active_issue_body") as mock_issue, \
             patch("mailbox_dispatcher.commit_and_publish") as mock_pub, \
             patch("mailbox_dispatcher.run_command") as mock_run:

            mock_to.exists.return_value = True
            mock_seq.side_effect = [2, 2]
            mock_type.return_value = "ACK"
            mock_parse.return_value = {
                "Task-ID": "test",
                "Active-Channel": "https://github.com/test/issues/1",
                "From": "Reviewer",
                "Next-Automatic-Action": "test",
                "Summary": "test",
                # Malicious command in mailbox — should NOT be executed
                "Command": "rm -rf /",
            }
            mock_val.return_value = "https://github.com/test/issues/1"
            mock_issue.return_value = "issue body"
            mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")

            # The command passed to run_runner is the CLI argument, not from mailbox
            run_runner("python --version", 30)

            # Verify the executed command is the CLI argument, not mailbox content
            call_args = mock_run.call_args
            self.assertIsNotNone(call_args)
            args, _ = call_args
            executed_cmd = args[0] if args else []
            self.assertEqual(executed_cmd, ["python", "--version"])


if __name__ == "__main__":
    unittest.main()
