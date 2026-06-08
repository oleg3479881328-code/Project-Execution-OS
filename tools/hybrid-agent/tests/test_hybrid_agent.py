from __future__ import annotations

import json
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "hybrid-agent"))

from hybrid_agent import EndpointConfig, run_hybrid_agent, validate_local_payload  # noqa: E402


class MockHandler(BaseHTTPRequestHandler):
    routes: dict[str, list[dict[str, object]]] = {}
    received_payloads: list[dict[str, object]] = []

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(length).decode("utf-8")
        payload = json.loads(raw_body)
        self.received_payloads.append(payload)
        path = self.path
        responses = self.routes.get(path)
        if not responses:
            self.send_response(404)
            self.end_headers()
            return
        response = responses.pop(0)
        status = int(response.get("status", 200))
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        body = response.get("body")
        if body == "echo-user":
            content = payload["messages"][1]["content"]
            body = {
                "id": "cloud-echo",
                "choices": [{"message": {"content": f"Echoed:{content}"}}],
                "usage": {"prompt_tokens": 111, "completion_tokens": 22, "total_tokens": 133},
            }
        self.wfile.write(json.dumps(body).encode("utf-8"))

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return


class HybridAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), MockHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_address[1]}/v1"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.thread.join(timeout=5)
        cls.server.server_close()

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workdir = Path(self.temp_dir.name)
        self.log_path = self.workdir / "runtime.jsonl"
        self.input_log = self.workdir / "sample.log"
        MockHandler.received_payloads = []
        self.input_log.write_text(
            "\n".join(
                [
                    "INFO start",
                    "ERROR failure in scripts/build_semantic_store.py",
                    "Traceback line here",
                    "WARNING downstream validation skipped",
                ]
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def local_config(self) -> EndpointConfig:
        return EndpointConfig(
            provider="local-test",
            endpoint=self.base_url,
            model="local-model",
            api_key="unused",
            timeout_seconds=5,
        )

    def cloud_config(self) -> EndpointConfig:
        return EndpointConfig(
            provider="cloud-test",
            endpoint=self.base_url,
            model="cloud-model",
            api_key="unused",
            timeout_seconds=5,
        )

    def read_logs(self) -> list[dict[str, object]]:
        return [json.loads(line) for line in self.log_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    def test_cloud_only_path(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {"body": "echo-user"},
            ]
        }
        result = run_hybrid_agent(
            task_text="Summarize the failure.",
            mode="cloud-only",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=None,
            cloud_config=self.cloud_config(),
            log_path=self.log_path,
        )
        self.assertIn("cloud", result)
        self.assertEqual(result["fallback_used"], False)
        self.assertIn("Echoed:", result["cloud"]["content"])
        logs = self.read_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]["stage"], "cloud_reasoning")

    def test_local_only_path_with_mocked_endpoint(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-1",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Failure repeats in the semantic builder.",
                                            "relevant_error_excerpts": [
                                                {
                                                    "path": str(self.input_log),
                                                    "start_line": 2,
                                                    "end_line": 4,
                                                    "reason": "Repeated failure lines.",
                                                }
                                            ],
                                            "suspected_files_modules": [
                                                {
                                                    "path": "tools/hybrid-agent/hybrid_agent.py",
                                                    "module": "hybrid-agent",
                                                    "reason": "Existing repository file used for validation.",
                                                }
                                            ],
                                            "escalation_recommendation": "cloud",
                                            "local_stage_metadata": {
                                                "confidence": "medium",
                                                "notes": "mock",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {"prompt_tokens": 90, "completion_tokens": 30, "total_tokens": 120},
                    }
                }
            ]
        }
        result = run_hybrid_agent(
            task_text="Compress this log.",
            mode="local-only",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=None,
            log_path=self.log_path,
        )
        self.assertIn("local", result)
        self.assertEqual(result["local"]["payload"]["summary"], "Failure repeats in the semantic builder.")
        logs = self.read_logs()
        self.assertEqual(logs[0]["stage"], "local_preprocess")
        self.assertIsNotNone(logs[0]["compression_ratio"])

    def test_preprocess_then_cloud_with_mocked_endpoints(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-2",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Local summary.",
                                            "relevant_error_excerpts": [],
                                            "suspected_files_modules": [],
                                            "escalation_recommendation": "cloud",
                                            "local_stage_metadata": {
                                                "confidence": "low",
                                                "notes": "mock",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {"prompt_tokens": 50, "completion_tokens": 20, "total_tokens": 70},
                    }
                },
                {"body": "echo-user"},
            ]
        }
        result = run_hybrid_agent(
            task_text="Analyze this failure.",
            mode="preprocess-then-cloud",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=self.cloud_config(),
            log_path=self.log_path,
        )
        self.assertFalse(result["fallback_used"])
        self.assertIn("Local summary.", json.dumps(result, ensure_ascii=False))
        logs = self.read_logs()
        self.assertEqual([item["stage"] for item in logs], ["local_preprocess", "cloud_reasoning"])
        cloud_prompt = MockHandler.received_payloads[1]["messages"][1]["content"]
        self.assertIn("\"compact_context\"", cloud_prompt)
        self.assertNotIn("\"bounded_evidence\"", cloud_prompt)

    def test_local_failure_fallback(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "status": 500,
                    "body": {"error": {"message": "local exploded"}},
                },
                {"body": "echo-user"},
            ]
        }
        result = run_hybrid_agent(
            task_text="Analyze with fallback.",
            mode="preprocess-then-cloud",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=self.cloud_config(),
            log_path=self.log_path,
        )
        self.assertTrue(result["fallback_used"])
        self.assertIn("local_error", result)
        logs = self.read_logs()
        self.assertEqual(logs[0]["status"], "failed_fallback_to_cloud")
        self.assertEqual(logs[1]["stage"], "cloud_reasoning")
        self.assertIn("local_preprocess_failed", logs[1]["notes"])
        cloud_prompt = MockHandler.received_payloads[1]["messages"][1]["content"]
        self.assertIn("\"bounded_evidence\"", cloud_prompt)
        self.assertNotIn("\"compact_context\"", cloud_prompt)

    def test_preprocess_then_cloud_falls_back_on_invalid_excerpt_range(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-bad-range",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Bad range.",
                                            "relevant_error_excerpts": [
                                                {
                                                    "path": str(self.input_log),
                                                    "start_line": 2,
                                                    "end_line": 99,
                                                    "reason": "invalid",
                                                }
                                            ],
                                            "suspected_files_modules": [],
                                            "escalation_recommendation": "cloud",
                                            "local_stage_metadata": {
                                                "confidence": "low",
                                                "notes": "mock",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {"prompt_tokens": 50, "completion_tokens": 20, "total_tokens": 70},
                    }
                },
                {"body": "echo-user"},
            ]
        }
        result = run_hybrid_agent(
            task_text="Analyze invalid range.",
            mode="preprocess-then-cloud",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=self.cloud_config(),
            log_path=self.log_path,
        )
        self.assertTrue(result["fallback_used"])
        self.assertIn("local_error", result)
        self.assertIn("outside the source evidence line range", result["local_error"])
        cloud_prompt = MockHandler.received_payloads[1]["messages"][1]["content"]
        self.assertIn("\"bounded_evidence\"", cloud_prompt)
        self.assertNotIn("\"compact_context\"", cloud_prompt)

    def test_preprocess_then_cloud_falls_back_on_invented_suspect_path(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-bad-path",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Invented path.",
                                            "relevant_error_excerpts": [],
                                            "suspected_files_modules": [
                                                {
                                                    "path": "missing/not-real.py",
                                                    "module": "ghost",
                                                    "reason": "invented",
                                                }
                                            ],
                                            "escalation_recommendation": "cloud",
                                            "local_stage_metadata": {
                                                "confidence": "low",
                                                "notes": "mock",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {"prompt_tokens": 50, "completion_tokens": 20, "total_tokens": 70},
                    }
                },
                {"body": "echo-user"},
            ]
        }
        result = run_hybrid_agent(
            task_text="Analyze invented path.",
            mode="preprocess-then-cloud",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=self.cloud_config(),
            log_path=self.log_path,
        )
        self.assertTrue(result["fallback_used"])
        self.assertIn("local_error", result)
        self.assertIn("references a missing path", result["local_error"])
        cloud_prompt = MockHandler.received_payloads[1]["messages"][1]["content"]
        self.assertIn("\"bounded_evidence\"", cloud_prompt)
        self.assertNotIn("\"compact_context\"", cloud_prompt)

    def test_preprocess_then_cloud_can_include_full_evidence_in_debug_mode(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-4",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Local summary.",
                                            "relevant_error_excerpts": [],
                                            "suspected_files_modules": [],
                                            "escalation_recommendation": "cloud",
                                            "local_stage_metadata": {
                                                "confidence": "low",
                                                "notes": "mock",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {"prompt_tokens": 50, "completion_tokens": 20, "total_tokens": 70},
                    }
                },
                {"body": "echo-user"},
            ]
        }
        run_hybrid_agent(
            task_text="Analyze this failure.",
            mode="preprocess-then-cloud",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=self.cloud_config(),
            log_path=self.log_path,
            include_full_evidence=True,
        )
        cloud_prompt = MockHandler.received_payloads[1]["messages"][1]["content"]
        self.assertIn("\"compact_context\"", cloud_prompt)
        self.assertIn("\"bounded_evidence\"", cloud_prompt)

    def test_structured_output_validation(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-invalid",
                        "choices": [{"message": {"content": "{\"summary\": \"missing fields\"}"}}],
                        "usage": {},
                    }
                }
            ]
        }
        with self.assertRaises(ValueError):
            run_hybrid_agent(
                task_text="Invalid payload.",
                mode="local-only",
                log_paths=[self.input_log],
                file_paths=[],
                local_config=self.local_config(),
                cloud_config=None,
                log_path=self.log_path,
            )

    def test_validate_local_payload_normalizes_live_model_variants(self) -> None:
        payload = validate_local_payload(
            {
                "summary": "Repeated SQLite lock failures detected.",
                "relevant_error_excerpts": [
                    {
                        "path": "tools\\hybrid-agent\\fixtures\\synthetic_repetitive_log.txt",
                        "start_line": 1,
                        "end_line": 2,
                        "reason": "keyword_match",
                    }
                ],
                "suspected_files_modules": [
                    {
                        "path": "tools\\hybrid-agent\\fixtures\\synthetic_repetitive_log.txt",
                        "module": "scripts/build_semantic_store.py",
                        "reason": "sqlite lock",
                    }
                ],
                "escalation_recommendation": "Local Sufficient",
                "local_stage_metadata": {
                    "confidence": "HIGH",
                    "notes": "normalized for workstation local runs",
                },
            }
        )
        self.assertEqual(payload["escalation_recommendation"], "local_sufficient")
        self.assertEqual(payload["local_stage_metadata"]["confidence"], "high")
        self.assertEqual(
            payload["relevant_error_excerpts"][0]["path"],
            str(Path("tools\\hybrid-agent\\fixtures\\synthetic_repetitive_log.txt")),
        )

    def test_local_only_rejects_unknown_excerpt_path(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-invalid-path",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Unknown excerpt path.",
                                            "relevant_error_excerpts": [
                                                {
                                                    "path": "C:/not/in/evidence.log",
                                                    "start_line": 1,
                                                    "end_line": 1,
                                                    "reason": "invented",
                                                }
                                            ],
                                            "suspected_files_modules": [],
                                            "escalation_recommendation": "cloud",
                                            "local_stage_metadata": {
                                                "confidence": "low",
                                                "notes": "mock",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {},
                    }
                }
            ]
        }
        with self.assertRaises(ValueError):
            run_hybrid_agent(
                task_text="Invalid excerpt path.",
                mode="local-only",
                log_paths=[self.input_log],
                file_paths=[],
                local_config=self.local_config(),
                cloud_config=None,
                log_path=self.log_path,
            )

    def test_local_only_repairs_embedded_excerpt_path_for_single_source_evidence(self) -> None:
        embedded_log = self.workdir / "embedded.log"
        embedded_log.write_text(
            "\n".join(
                [
                    "INFO start",
                    "ERROR sqlite3.OperationalError database is locked file=.local/semantic-index/semantic-index.sqlite3",
                    "WARNING retry pending",
                ]
            ),
            encoding="utf-8",
        )
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-embedded-path",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Embedded file path was selected instead of source evidence path.",
                                            "relevant_error_excerpts": [
                                                {
                                                    "path": ".local\\semantic-index\\semantic-index.sqlite3",
                                                    "start_line": 1,
                                                    "end_line": 3,
                                                    "reason": "mentioned inside log excerpt",
                                                }
                                            ],
                                            "suspected_files_modules": [],
                                            "escalation_recommendation": "local_sufficient",
                                            "local_stage_metadata": {
                                                "confidence": "medium",
                                                "notes": "repair single-source excerpt path",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {},
                    }
                }
            ]
        }
        result = run_hybrid_agent(
            task_text="Repair embedded excerpt path.",
            mode="local-only",
            log_paths=[embedded_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=None,
            log_path=self.log_path,
        )
        self.assertEqual(result["local"]["payload"]["relevant_error_excerpts"][0]["path"], str(embedded_log))

    def test_local_only_repairs_route_alias_suspect_path(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-route-alias",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Route alias suspect path should be normalized to the real repo file.",
                                            "relevant_error_excerpts": [
                                                {
                                                    "path": str(self.input_log),
                                                    "start_line": 2,
                                                    "end_line": 4,
                                                    "reason": "keyword_match",
                                                }
                                            ],
                                            "suspected_files_modules": [
                                                {
                                                    "path": "tools/hybrid-agent/workstation-route",
                                                    "module": "route",
                                                    "reason": "selected route alias",
                                                }
                                            ],
                                            "escalation_recommendation": "local_sufficient",
                                            "local_stage_metadata": {
                                                "confidence": "medium",
                                                "notes": "repair route alias",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {},
                    }
                }
            ]
        }
        result = run_hybrid_agent(
            task_text="Repair route alias suspect path.",
            mode="local-only",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=None,
            log_path=self.log_path,
        )
        self.assertEqual(
            result["local"]["payload"]["suspected_files_modules"][0]["path"],
            "tools\\hybrid-agent\\workstation_route.py",
        )

    def test_logging_fields_and_compression_ratio(self) -> None:
        MockHandler.routes = {
            "/v1/chat/completions": [
                {
                    "body": {
                        "id": "local-3",
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(
                                        {
                                            "summary": "Tiny summary.",
                                            "relevant_error_excerpts": [],
                                            "suspected_files_modules": [],
                                            "escalation_recommendation": "local_sufficient",
                                            "local_stage_metadata": {
                                                "confidence": "high",
                                                "notes": "mock",
                                            },
                                        }
                                    )
                                }
                            }
                        ],
                        "usage": {"prompt_tokens": 60, "completion_tokens": 10, "total_tokens": 70},
                    }
                }
            ]
        }
        run_hybrid_agent(
            task_text="Measure logging.",
            mode="local-only",
            log_paths=[self.input_log],
            file_paths=[],
            local_config=self.local_config(),
            cloud_config=None,
            log_path=self.log_path,
        )
        log_entry = self.read_logs()[0]
        self.assertIn("input_size_bytes", log_entry)
        self.assertIn("output_size_bytes", log_entry)
        self.assertIn("compression_ratio", log_entry)
        self.assertGreater(log_entry["input_size_bytes"], 0)
        self.assertGreater(log_entry["output_size_bytes"], 0)
        self.assertGreater(log_entry["compression_ratio"], 0)


if __name__ == "__main__":
    unittest.main()
