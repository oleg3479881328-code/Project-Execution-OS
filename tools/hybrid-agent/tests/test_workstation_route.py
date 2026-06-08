from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "hybrid-agent"))

import run_workstation_hybrid_route  # noqa: E402
from workstation_route import (  # noqa: E402
    DEFAULT_WORKSTATION_ROUTE,
    WorkstationEntrypoints,
    choose_auto_mode,
    discover_deepseek_vscode_config,
    run_workstation_route,
)
from hybrid_agent import EndpointConfig  # noqa: E402


class WorkstationRouteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workdir = Path(self.temp_dir.name)
        self.log_file = self.workdir / "runtime.jsonl"
        self.evidence_log = self.workdir / "evidence.log"
        self.evidence_log.write_text("ERROR one\nWARNING two\n" * 80, encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def fake_config(self, provider: str) -> EndpointConfig:
        return EndpointConfig(
            provider=provider,
            endpoint="http://localhost:11434/v1",
            model="llama3.2:3b",
            api_key="ollama",
            timeout_seconds=30.0,
        )

    def test_deepseek_vscode_config_detection(self) -> None:
        config_path = self.workdir / "chatLanguageModels.json"
        config_path.write_text(
            json.dumps(
                [
                    {
                        "name": "DeepSeek",
                        "models": [{"id": "deepseek-v4-pro"}],
                    }
                ]
            ),
            encoding="utf-8",
        )
        with patch.dict("os.environ", {"APPDATA": str(self.workdir)}):
            user_dir = self.workdir / "Code" / "User"
            user_dir.mkdir(parents=True, exist_ok=True)
            target = user_dir / "chatLanguageModels.json"
            target.write_text(config_path.read_text(encoding="utf-8"), encoding="utf-8")
            detected_path, model_id = discover_deepseek_vscode_config()
        self.assertEqual(detected_path, str(target))
        self.assertEqual(model_id, "deepseek-v4-pro")

    def test_auto_mode_prefers_cloud_only_for_tiny_evidence_with_cloud(self) -> None:
        tiny = self.workdir / "tiny.log"
        tiny.write_text("short\n", encoding="utf-8")
        decision = choose_auto_mode(
            task_text="tiny task",
            log_paths=[tiny],
            file_paths=[],
            selected_route=DEFAULT_WORKSTATION_ROUTE,
            executor="codex",
            local_config=self.fake_config("local-openai-compatible"),
            cloud_config=self.fake_config("cloud-openai-compatible"),
        )
        self.assertEqual(decision.chosen_mode, "cloud-only")

    def test_auto_mode_prefers_preprocess_then_cloud_for_large_evidence(self) -> None:
        decision = choose_auto_mode(
            task_text="large task",
            log_paths=[self.evidence_log],
            file_paths=[],
            selected_route=DEFAULT_WORKSTATION_ROUTE,
            executor="codex",
            local_config=self.fake_config("local-openai-compatible"),
            cloud_config=self.fake_config("cloud-openai-compatible"),
        )
        self.assertEqual(decision.chosen_mode, "preprocess-then-cloud")

    def test_auto_mode_uses_local_only_when_no_cloud_config(self) -> None:
        decision = choose_auto_mode(
            task_text="large task",
            log_paths=[self.evidence_log],
            file_paths=[],
            selected_route=DEFAULT_WORKSTATION_ROUTE,
            executor="deepseek",
            local_config=self.fake_config("local-openai-compatible"),
            cloud_config=None,
        )
        self.assertEqual(decision.chosen_mode, "local-only")

    def test_run_workstation_route_logs_decision_and_passes_mode(self) -> None:
        fake_entrypoints = WorkstationEntrypoints(
            codex_cli_path="C:/codex.exe",
            codex_desktop_path=None,
            vscode_cli_path="C:/code.cmd",
            codex_vscode_extension_path="C:/Users/test/.vscode/extensions/openai.chatgpt",
            codex_vscode_chat_session_type="openai-codex",
            deepseek_vscode_config_path="C:/chatLanguageModels.json",
            deepseek_vscode_model_id="deepseek-v4-pro",
        )
        with (
            patch("workstation_route.discover_workstation_entrypoints", return_value=fake_entrypoints),
            patch("workstation_route.build_local_config", return_value=self.fake_config("local-openai-compatible")),
            patch("workstation_route.build_cloud_config", return_value=None),
            patch(
                "workstation_route.run_hybrid_agent",
                return_value={"mode": "local-only", "fallback_used": False, "input_payload": {"evidence": []}},
            ) as run_mock,
        ):
            result = run_workstation_route(
                executor="deepseek",
                mode="auto",
                task_text="large task",
                log_paths=[self.evidence_log],
                file_paths=[],
                log_path=self.log_file,
            )
        self.assertEqual(result["route_decision"]["chosen_mode"], "local-only")
        run_mock.assert_called_once()
        log_lines = self.log_file.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(log_lines), 1)
        entry = json.loads(log_lines[0])
        self.assertEqual(entry["stage"], "route_decision")
        self.assertEqual(entry["status"], "local-only")

    def test_cloud_only_does_not_probe_local_runtime(self) -> None:
        fake_entrypoints = WorkstationEntrypoints(
            codex_cli_path="C:/codex.exe",
            codex_desktop_path="C:/Codex.exe",
            vscode_cli_path="C:/code.cmd",
            codex_vscode_extension_path="C:/Users/test/.vscode/extensions/openai.chatgpt",
            codex_vscode_chat_session_type="openai-codex",
            deepseek_vscode_config_path=None,
            deepseek_vscode_model_id=None,
        )
        with (
            patch("workstation_route.discover_workstation_entrypoints", return_value=fake_entrypoints),
            patch("workstation_route.build_local_config") as local_mock,
            patch("workstation_route.build_cloud_config", return_value=self.fake_config("cloud-openai-compatible")),
            patch(
                "workstation_route.run_hybrid_agent",
                return_value={"mode": "cloud-only", "fallback_used": False, "input_payload": {"evidence": []}},
            ) as run_mock,
        ):
            result = run_workstation_route(
                executor="codex",
                mode="cloud-only",
                task_text="cloud only task",
                log_paths=[self.evidence_log],
                file_paths=[],
                log_path=self.log_file,
            )
        local_mock.assert_not_called()
        run_mock.assert_called_once()
        self.assertFalse(result["local_config_present"])
        self.assertTrue(result["cloud_config_present"])

    def test_repo_root_resolution_keeps_relative_paths_inside_repo(self) -> None:
        repo_root = self.workdir / "repo"
        repo_root.mkdir()
        resolved_log = run_workstation_hybrid_route.resolve_cli_path("logs/api-runtime/hybrid-agent.jsonl", repo_root)
        resolved_inputs = run_workstation_hybrid_route.parse_paths(
            ["tools/hybrid-agent/fixtures/synthetic_repetitive_log.txt"],
            repo_root,
        )
        self.assertEqual(resolved_log, repo_root / "logs" / "api-runtime" / "hybrid-agent.jsonl")
        self.assertEqual(
            resolved_inputs[0],
            repo_root / "tools" / "hybrid-agent" / "fixtures" / "synthetic_repetitive_log.txt",
        )

    def test_codex_prefers_vscode_handoff_when_extension_exists(self) -> None:
        fake_entrypoints = WorkstationEntrypoints(
            codex_cli_path="C:/codex.exe",
            codex_desktop_path="C:/Codex.exe",
            vscode_cli_path="C:/code.cmd",
            codex_vscode_extension_path="C:/Users/test/.vscode/extensions/openai.chatgpt",
            codex_vscode_chat_session_type="openai-codex",
            deepseek_vscode_config_path=None,
            deepseek_vscode_model_id=None,
        )
        with (
            patch("workstation_route.discover_workstation_entrypoints", return_value=fake_entrypoints),
            patch("workstation_route.build_local_config", return_value=self.fake_config("local-openai-compatible")),
            patch("workstation_route.build_cloud_config", return_value=None),
            patch(
                "workstation_route.run_hybrid_agent",
                return_value={
                    "mode": "local-only",
                    "fallback_used": False,
                    "input_payload": {"evidence": []},
                    "local": {"payload": {"summary": "ok"}},
                },
            ),
            patch("workstation_route.subprocess.Popen") as popen_mock,
        ):
            result = run_workstation_route(
                executor="codex",
                mode="auto",
                task_text="route codex via vscode",
                log_paths=[self.evidence_log],
                file_paths=[],
                log_path=self.log_file,
                launch_executor=True,
                repo_root=self.workdir,
            )
        self.assertEqual(result["executor_handoff"]["launch_method"], "vscode-chat")
        self.assertEqual(result["executor_handoff"]["launch_status"], "launched")
        self.assertIn("code.cmd", " ".join(result["executor_handoff"]["launch_command"]))
        popen_mock.assert_called_once()

    def test_codex_falls_back_to_desktop_when_vscode_route_missing(self) -> None:
        fake_entrypoints = WorkstationEntrypoints(
            codex_cli_path="C:/codex.exe",
            codex_desktop_path="C:/Codex.exe",
            vscode_cli_path=None,
            codex_vscode_extension_path=None,
            codex_vscode_chat_session_type=None,
            deepseek_vscode_config_path=None,
            deepseek_vscode_model_id=None,
        )
        with (
            patch("workstation_route.discover_workstation_entrypoints", return_value=fake_entrypoints),
            patch("workstation_route.build_local_config", return_value=self.fake_config("local-openai-compatible")),
            patch("workstation_route.build_cloud_config", return_value=None),
            patch(
                "workstation_route.run_hybrid_agent",
                return_value={
                    "mode": "local-only",
                    "fallback_used": False,
                    "input_payload": {"evidence": []},
                    "local": {"payload": {"summary": "ok"}},
                },
            ),
            patch("workstation_route.subprocess.Popen") as popen_mock,
        ):
            result = run_workstation_route(
                executor="codex",
                mode="auto",
                task_text="route codex fallback desktop",
                log_paths=[self.evidence_log],
                file_paths=[],
                log_path=self.log_file,
                launch_executor=True,
                repo_root=self.workdir,
            )
        self.assertEqual(result["executor_handoff"]["launch_method"], "codex-desktop-wrapper")
        self.assertEqual(result["executor_handoff"]["launch_status"], "launched")
        popen_mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
