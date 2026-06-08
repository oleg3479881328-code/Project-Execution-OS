from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
from urllib import error, request

from hybrid_agent import (
    DEFAULT_LOG_PATH,
    DEFAULT_SELECTED_ROUTE,
    EndpointConfig,
    build_input_payload,
    json_size_metrics,
    run_hybrid_agent,
    utc_now_iso,
    write_log_entry,
)


DEFAULT_WORKSTATION_ROUTE = "tools/hybrid-agent/workstation-route"
DEFAULT_LOCAL_ENDPOINT = "http://localhost:11434/v1"
DEFAULT_LOCAL_MODEL = "llama3.2:3b"
DEFAULT_LOCAL_API_KEY = "ollama"
DEFAULT_TIMEOUT_SECONDS = 240.0
DEFAULT_AUTO_MIN_EVIDENCE_BYTES = 1000
DEFAULT_AUTO_MIN_EVIDENCE_COUNT = 1
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_HANDOFF_DIR = REPO_ROOT / "logs" / "api-runtime" / "hybrid-handoffs"


@dataclass(slots=True)
class WorkstationEntrypoints:
    codex_cli_path: str | None
    codex_desktop_path: str | None
    vscode_cli_path: str | None
    codex_vscode_extension_path: str | None
    codex_vscode_chat_session_type: str | None
    deepseek_vscode_config_path: str | None
    deepseek_vscode_model_id: str | None


@dataclass(slots=True)
class RouteDecision:
    requested_mode: str
    chosen_mode: str
    reason: str
    evidence_count: int
    evidence_bytes: int
    local_available: bool
    cloud_available: bool
    selected_route: str
    executor: str


@dataclass(slots=True)
class ExecutorHandoff:
    executor: str
    packet_path: str
    launch_method: str
    launch_boundary: str
    launch_status: str
    launch_target: str | None
    launch_command: list[str]


def command_path(name: str) -> str | None:
    resolved = shutil.which(name)
    return str(Path(resolved).resolve()) if resolved else None


def discover_deepseek_vscode_config() -> tuple[str | None, str | None]:
    config_path = Path(os.environ.get("APPDATA", "")) / "Code" / "User" / "chatLanguageModels.json"
    if not config_path.exists():
        return None, None

    try:
        content = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return str(config_path), None

    if not isinstance(content, list):
        return str(config_path), None

    for group in content:
        if not isinstance(group, dict):
            continue
        if group.get("name") != "DeepSeek":
            continue
        models = group.get("models")
        if not isinstance(models, list) or not models:
            return str(config_path), None
        first_model = models[0]
        if isinstance(first_model, dict):
            model_id = first_model.get("id")
            if isinstance(model_id, str):
                return str(config_path), model_id
    return str(config_path), None


def discover_codex_vscode_extension() -> tuple[str | None, str | None]:
    extensions_root = Path.home() / ".vscode" / "extensions"
    matches = sorted(extensions_root.glob("openai.chatgpt-*"), reverse=True)
    if not matches:
        return None, None

    package_json = matches[0] / "package.json"
    if not package_json.exists():
        return str(matches[0]), None

    try:
        content = json.loads(package_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return str(matches[0]), None

    sessions = content.get("contributes", {}).get("chatSessions")
    if isinstance(sessions, list):
        for item in sessions:
            if isinstance(item, dict) and item.get("type") == "openai-codex":
                return str(matches[0]), "openai-codex"
    return str(matches[0]), None


def discover_workstation_entrypoints() -> WorkstationEntrypoints:
    deepseek_config_path, deepseek_model_id = discover_deepseek_vscode_config()
    codex_extension_path, codex_chat_session_type = discover_codex_vscode_extension()
    codex_cli = command_path("codex")
    vscode_cli = command_path("code")
    codex_desktop = None
    if codex_cli:
        codex_cli_path = Path(codex_cli)
        candidate = codex_cli_path.parents[2] / "app" / "Codex.exe"
        if candidate.exists():
            codex_desktop = str(candidate)

    return WorkstationEntrypoints(
        codex_cli_path=codex_cli,
        codex_desktop_path=codex_desktop,
        vscode_cli_path=vscode_cli,
        codex_vscode_extension_path=codex_extension_path,
        codex_vscode_chat_session_type=codex_chat_session_type,
        deepseek_vscode_config_path=deepseek_config_path,
        deepseek_vscode_model_id=deepseek_model_id,
    )


def local_endpoint_available(endpoint: str, timeout_seconds: float) -> bool:
    url = endpoint.rstrip("/") + "/models"
    req = request.Request(url, headers={"Authorization": f"Bearer {DEFAULT_LOCAL_API_KEY}"}, method="GET")
    try:
        with request.urlopen(req, timeout=timeout_seconds) as response:
            return response.status == 200
    except (error.HTTPError, error.URLError, TimeoutError):
        return False


def ollama_model_available(endpoint: str, model: str, timeout_seconds: float) -> bool:
    url = endpoint.rstrip("/") + "/models"
    req = request.Request(url, headers={"Authorization": f"Bearer {DEFAULT_LOCAL_API_KEY}"}, method="GET")
    try:
        with request.urlopen(req, timeout=timeout_seconds) as response:
            body = json.loads(response.read().decode("utf-8"))
    except (error.HTTPError, error.URLError, TimeoutError, json.JSONDecodeError):
        return False

    data = body.get("data")
    if not isinstance(data, list):
        return False
    for item in data:
        if isinstance(item, dict) and item.get("id") == model:
            return True
    return False


def build_local_config(timeout_seconds: float) -> EndpointConfig | None:
    endpoint = os.environ.get("HYBRID_AGENT_LOCAL_ENDPOINT", DEFAULT_LOCAL_ENDPOINT)
    model = os.environ.get("HYBRID_AGENT_LOCAL_MODEL", DEFAULT_LOCAL_MODEL)
    api_key = os.environ.get("HYBRID_AGENT_LOCAL_API_KEY", DEFAULT_LOCAL_API_KEY)
    if endpoint.endswith(":11434"):
        endpoint = endpoint + "/v1"
    if not local_endpoint_available(endpoint, timeout_seconds):
        endpoint = DEFAULT_LOCAL_ENDPOINT
        if not local_endpoint_available(endpoint, timeout_seconds):
            return None
    if not ollama_model_available(endpoint, model, timeout_seconds):
        return None
    return EndpointConfig(
        provider="local-openai-compatible",
        endpoint=endpoint,
        model=model,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
    )


def build_codex_cloud_config(timeout_seconds: float) -> EndpointConfig | None:
    endpoint = os.environ.get("HYBRID_AGENT_CLOUD_ENDPOINT")
    model = os.environ.get("HYBRID_AGENT_CLOUD_MODEL")
    api_key = os.environ.get("HYBRID_AGENT_CLOUD_API_KEY")
    if endpoint and model and api_key:
        return EndpointConfig(
            provider="cloud-openai-compatible",
            endpoint=endpoint,
            model=model,
            api_key=api_key,
            timeout_seconds=timeout_seconds,
        )

    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        return None
    openai_model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
    return EndpointConfig(
        provider="openai",
        endpoint="https://api.openai.com/v1",
        model=openai_model,
        api_key=openai_api_key,
        timeout_seconds=timeout_seconds,
    )


def build_deepseek_cloud_config(timeout_seconds: float) -> EndpointConfig | None:
    endpoint = os.environ.get("HYBRID_AGENT_CLOUD_ENDPOINT")
    model = os.environ.get("HYBRID_AGENT_CLOUD_MODEL")
    api_key = os.environ.get("HYBRID_AGENT_CLOUD_API_KEY")
    if endpoint and model and api_key:
        return EndpointConfig(
            provider="cloud-openai-compatible",
            endpoint=endpoint,
            model=model,
            api_key=api_key,
            timeout_seconds=timeout_seconds,
        )

    deepseek_api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not deepseek_api_key:
        return None
    deepseek_endpoint = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    deepseek_model = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")
    return EndpointConfig(
        provider="deepseek",
        endpoint=deepseek_endpoint,
        model=deepseek_model,
        api_key=deepseek_api_key,
        timeout_seconds=timeout_seconds,
    )


def build_cloud_config(executor: str, timeout_seconds: float) -> EndpointConfig | None:
    if executor == "deepseek":
        return build_deepseek_cloud_config(timeout_seconds)
    return build_codex_cloud_config(timeout_seconds)


def should_probe_local(mode: str) -> bool:
    return mode in {"auto", "local-only", "preprocess-then-cloud"}


def choose_auto_mode(
    *,
    task_text: str,
    log_paths: list[Path],
    file_paths: list[Path],
    selected_route: str,
    executor: str,
    local_config: EndpointConfig | None,
    cloud_config: EndpointConfig | None,
) -> RouteDecision:
    input_payload = build_input_payload(
        task_text=task_text,
        log_paths=log_paths,
        file_paths=file_paths,
        selected_route=selected_route,
    )
    evidence = input_payload["evidence"]
    evidence_count = len(evidence)
    evidence_bytes = json_size_metrics(evidence)["bytes"]
    local_available = local_config is not None
    cloud_available = cloud_config is not None

    if evidence_count < DEFAULT_AUTO_MIN_EVIDENCE_COUNT or evidence_bytes < DEFAULT_AUTO_MIN_EVIDENCE_BYTES:
        if cloud_available:
            return RouteDecision(
                requested_mode="auto",
                chosen_mode="cloud-only",
                reason="tiny_or_no_meaningful_bounded_evidence",
                evidence_count=evidence_count,
                evidence_bytes=evidence_bytes,
                local_available=local_available,
                cloud_available=cloud_available,
                selected_route=selected_route,
                executor=executor,
            )
        if local_available:
            return RouteDecision(
                requested_mode="auto",
                chosen_mode="local-only",
                reason="tiny_evidence_but_no_cloud_config_present",
                evidence_count=evidence_count,
                evidence_bytes=evidence_bytes,
                local_available=local_available,
                cloud_available=cloud_available,
                selected_route=selected_route,
                executor=executor,
            )

    if local_available and cloud_available:
        return RouteDecision(
            requested_mode="auto",
            chosen_mode="preprocess-then-cloud",
            reason="bounded_evidence_large_enough_for_local_compression_before_cloud",
            evidence_count=evidence_count,
            evidence_bytes=evidence_bytes,
            local_available=local_available,
            cloud_available=cloud_available,
            selected_route=selected_route,
            executor=executor,
        )

    if local_available:
        return RouteDecision(
            requested_mode="auto",
            chosen_mode="local-only",
            reason="bounded_evidence_present_but_no_safe_cloud_config",
            evidence_count=evidence_count,
            evidence_bytes=evidence_bytes,
            local_available=local_available,
            cloud_available=cloud_available,
            selected_route=selected_route,
            executor=executor,
        )

    if cloud_available:
        return RouteDecision(
            requested_mode="auto",
            chosen_mode="cloud-only",
            reason="local_runtime_unavailable_fallback_to_cloud",
            evidence_count=evidence_count,
            evidence_bytes=evidence_bytes,
            local_available=local_available,
            cloud_available=cloud_available,
            selected_route=selected_route,
            executor=executor,
        )

    raise RuntimeError("Neither local Ollama nor a safe cloud configuration is available for auto mode.")


def log_route_decision(log_path: Path, decision: RouteDecision, entrypoints: WorkstationEntrypoints) -> None:
    entry = {
        "timestamp_utc": utc_now_iso(),
        "provider": "workstation-route",
        "model": None,
        "request_id": None,
        "project_id": "project-execution-os",
        "task_id": None,
        "context_profile": None,
        "context_fingerprint": None,
        "selected_route": decision.selected_route,
        "loaded_modules": [],
        "input_tokens_total": None,
        "input_tokens_cache_hit": None,
        "input_tokens_cache_miss": None,
        "output_tokens": None,
        "total_tokens": None,
        "estimated_cost_usd": None,
        "billed_cost_usd": None,
        "latency_ms": 0.0,
        "status": decision.chosen_mode,
        "stage": "route_decision",
        "input_size_bytes": decision.evidence_bytes,
        "input_size_chars": decision.evidence_bytes,
        "output_size_bytes": 0,
        "output_size_chars": 0,
        "compression_ratio": None,
        "notes": json.dumps(
            {
                "requested_mode": decision.requested_mode,
                "reason": decision.reason,
                "executor": decision.executor,
                "entrypoints": asdict(entrypoints),
            },
            ensure_ascii=False,
            sort_keys=True,
        ),
    }
    write_log_entry(log_path, entry)


def compact_context_summary(result: dict[str, Any]) -> str:
    local_payload = result.get("local", {}).get("payload") if isinstance(result.get("local"), dict) else None
    if isinstance(local_payload, dict):
        summary = local_payload.get("summary")
        if isinstance(summary, str) and summary.strip():
            return summary.strip()

    cloud_content = result.get("cloud", {}).get("content") if isinstance(result.get("cloud"), dict) else None
    if isinstance(cloud_content, str) and cloud_content.strip():
        return cloud_content.strip()

    return "No structured compact summary was produced. Use the attached bounded packet and evidence paths directly."


def build_handoff_packet_text(
    *,
    executor: str,
    task_text: str,
    chosen_mode: str,
    selected_route: str,
    result: dict[str, Any],
    log_paths: list[Path],
    file_paths: list[Path],
) -> str:
    route_decision = result.get("route_decision", {})
    compact_summary = compact_context_summary(result)
    evidence_paths = [str(path) for path in [*log_paths, *file_paths]]
    local_payload = result.get("local", {}).get("payload") if isinstance(result.get("local"), dict) else None
    cloud_content = result.get("cloud", {}).get("content") if isinstance(result.get("cloud"), dict) else None

    lines = [
        "# Workstation Hybrid Executor Handoff",
        "",
        f"- executor: `{executor}`",
        f"- chosen_mode: `{chosen_mode}`",
        f"- selected_route: `{selected_route}`",
        f"- repo_root: `{REPO_ROOT}`",
        "",
        "## Task",
        "",
        task_text,
        "",
        "## Compact Context",
        "",
        compact_summary,
        "",
    ]

    if isinstance(local_payload, dict):
        lines.extend(
            [
                "## Local Payload",
                "",
                "```json",
                json.dumps(local_payload, ensure_ascii=False, indent=2, sort_keys=True),
                "```",
                "",
            ]
        )

    if isinstance(cloud_content, str) and cloud_content.strip():
        lines.extend(
            [
                "## Cloud Output",
                "",
                cloud_content.strip(),
                "",
            ]
        )

    evidence_lines = [f"- `{path}`" for path in evidence_paths] if evidence_paths else ["- none"]
    lines.extend(
        [
            "## Evidence Paths",
            "",
            *evidence_lines,
            "",
            "## Route Metadata",
            "",
            "```json",
            json.dumps(route_decision, ensure_ascii=False, indent=2, sort_keys=True),
            "```",
            "",
            "## Execution Boundary",
            "",
        ]
    )

    if executor == "deepseek":
        lines.extend(
            [
                "DeepSeek handoff is launched through VS Code chat with this packet attached as context.",
                "The actual model/provider remains governed by the installed VS Code DeepSeek configuration on this workstation.",
            ]
        )
    else:
        lines.extend(
            [
                "Codex handoff is launched through the locally registered Codex desktop entrypoint with this packet written inside the repository.",
                "A direct prompt-injection CLI contract was not discoverable on this workstation, so the saved packet is the explicit handoff boundary.",
            ]
        )

    return "\n".join(lines) + "\n"


def write_handoff_packet(
    *,
    executor: str,
    task_text: str,
    chosen_mode: str,
    selected_route: str,
    result: dict[str, Any],
    log_paths: list[Path],
    file_paths: list[Path],
    handoff_dir: Path,
) -> Path:
    handoff_dir.mkdir(parents=True, exist_ok=True)
    safe_executor = executor.replace(" ", "-")
    packet_path = handoff_dir / f"{utc_now_iso().replace(':', '-').replace('+00:00', 'Z')}-{safe_executor}.md"
    packet_text = build_handoff_packet_text(
        executor=executor,
        task_text=task_text,
        chosen_mode=chosen_mode,
        selected_route=selected_route,
        result=result,
        log_paths=log_paths,
        file_paths=file_paths,
    )
    packet_path.write_text(packet_text, encoding="utf-8")
    return packet_path


def launch_deepseek_handoff(
    *,
    entrypoints: WorkstationEntrypoints,
    packet_path: Path,
    repo_root: Path,
    evidence_paths: list[Path],
) -> ExecutorHandoff:
    if not entrypoints.vscode_cli_path:
        return ExecutorHandoff(
            executor="deepseek",
            packet_path=str(packet_path),
            launch_method="vscode-chat",
            launch_boundary="VS Code CLI was not available, so the handoff packet was written but not launched.",
            launch_status="not_available",
            launch_target=None,
            launch_command=[],
        )

    command = [
        entrypoints.vscode_cli_path,
        "chat",
        "--mode",
        "agent",
        "--reuse-window",
        "--add-file",
        str(packet_path),
    ]
    for path in evidence_paths[:4]:
        command.extend(["--add-file", str(path)])
    command.append("Continue from the attached workstation hybrid handoff packet and execute within that bounded scope.")
    subprocess.Popen(command, cwd=repo_root)
    return ExecutorHandoff(
        executor="deepseek",
        packet_path=str(packet_path),
        launch_method="vscode-chat",
        launch_boundary="Prompt and packet were injected through VS Code chat; the actual provider selection remains controlled by the installed DeepSeek VS Code configuration.",
        launch_status="launched",
        launch_target=entrypoints.vscode_cli_path,
        launch_command=command,
    )


def launch_codex_vscode_handoff(
    *,
    entrypoints: WorkstationEntrypoints,
    packet_path: Path,
    repo_root: Path,
    evidence_paths: list[Path],
) -> ExecutorHandoff:
    if not entrypoints.vscode_cli_path or not entrypoints.codex_vscode_extension_path:
        return ExecutorHandoff(
            executor="codex",
            packet_path=str(packet_path),
            launch_method="vscode-chat",
            launch_boundary="VS Code Codex integration was not available, so this handoff path could not be launched.",
            launch_status="not_available",
            launch_target=entrypoints.vscode_cli_path,
            launch_command=[],
        )

    command = [
        entrypoints.vscode_cli_path,
        "chat",
        "--mode",
        "agent",
        "--reuse-window",
        "--add-file",
        str(packet_path),
    ]
    for path in evidence_paths[:4]:
        command.extend(["--add-file", str(path)])
    command.append(
        "Continue from the attached workstation hybrid handoff packet in the installed OpenAI Codex VS Code integration and execute within that bounded scope."
    )
    subprocess.Popen(command, cwd=repo_root)
    return ExecutorHandoff(
        executor="codex",
        packet_path=str(packet_path),
        launch_method="vscode-chat",
        launch_boundary="Codex handoff is launched through the installed OpenAI Codex VS Code integration. The extension registers chat session type `openai-codex`, but the public `code chat` CLI does not expose deterministic provider-selection flags, so provider targeting remains extension/UI-managed on this workstation.",
        launch_status="launched",
        launch_target=entrypoints.vscode_cli_path,
        launch_command=command,
    )


def launch_codex_handoff(
    *,
    entrypoints: WorkstationEntrypoints,
    packet_path: Path,
    repo_root: Path,
) -> ExecutorHandoff:
    launch_target = entrypoints.codex_desktop_path or "codex://"
    command: list[str] = []
    try:
        if entrypoints.codex_desktop_path:
            command = [entrypoints.codex_desktop_path, str(repo_root), str(packet_path)]
            subprocess.Popen(command, cwd=repo_root)
            status = "launched"
        else:
            os.startfile("codex://")  # type: ignore[attr-defined]
            status = "launched"
    except Exception:  # noqa: BLE001
        status = "not_available"

    return ExecutorHandoff(
        executor="codex",
        packet_path=str(packet_path),
        launch_method="codex-desktop-wrapper",
        launch_boundary="VS Code Codex integration was unavailable for deterministic launch, so the packet was written inside the repository and the registered Codex desktop entrypoint was launched as a fallback. A documented prompt-injection CLI contract for Codex Desktop was not discoverable on this workstation, so the packet file remains the explicit handoff boundary.",
        launch_status=status,
        launch_target=launch_target,
        launch_command=command,
    )


def maybe_launch_executor_handoff(
    *,
    executor: str,
    entrypoints: WorkstationEntrypoints,
    task_text: str,
    chosen_mode: str,
    selected_route: str,
    result: dict[str, Any],
    log_paths: list[Path],
    file_paths: list[Path],
    repo_root: Path,
) -> ExecutorHandoff:
    packet_path = write_handoff_packet(
        executor=executor,
        task_text=task_text,
        chosen_mode=chosen_mode,
        selected_route=selected_route,
        result=result,
        log_paths=log_paths,
        file_paths=file_paths,
        handoff_dir=DEFAULT_HANDOFF_DIR,
    )
    evidence_paths = [*log_paths, *file_paths]
    if executor == "deepseek":
        return launch_deepseek_handoff(
            entrypoints=entrypoints,
            packet_path=packet_path,
            repo_root=repo_root,
            evidence_paths=evidence_paths,
        )
    codex_vscode = launch_codex_vscode_handoff(
        entrypoints=entrypoints,
        packet_path=packet_path,
        repo_root=repo_root,
        evidence_paths=evidence_paths,
    )
    if codex_vscode.launch_status == "launched":
        return codex_vscode
    return launch_codex_handoff(
        entrypoints=entrypoints,
        packet_path=packet_path,
        repo_root=repo_root,
    )


def run_workstation_route(
    *,
    executor: str,
    mode: str,
    task_text: str,
    log_paths: list[Path],
    file_paths: list[Path],
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    log_path: Path = DEFAULT_LOG_PATH,
    selected_route: str = DEFAULT_WORKSTATION_ROUTE,
    include_full_evidence: bool = False,
    launch_executor: bool = False,
    repo_root: Path = REPO_ROOT,
) -> dict[str, Any]:
    entrypoints = discover_workstation_entrypoints()
    local_config = build_local_config(timeout_seconds) if should_probe_local(mode) else None
    cloud_config = build_cloud_config(executor, timeout_seconds)
    chosen_mode = mode
    route_decision: RouteDecision | None = None

    if mode == "auto":
        route_decision = choose_auto_mode(
            task_text=task_text,
            log_paths=log_paths,
            file_paths=file_paths,
            selected_route=selected_route,
            executor=executor,
            local_config=local_config,
            cloud_config=cloud_config,
        )
        chosen_mode = route_decision.chosen_mode
        log_route_decision(log_path, route_decision, entrypoints)

    result = run_hybrid_agent(
        task_text=task_text,
        mode=chosen_mode,
        log_paths=log_paths,
        file_paths=file_paths,
        local_config=local_config,
        cloud_config=cloud_config,
        log_path=log_path,
        selected_route=selected_route,
        include_full_evidence=include_full_evidence,
    )
    result["executor"] = executor
    result["entrypoints"] = asdict(entrypoints)
    result["local_config_present"] = local_config is not None
    result["cloud_config_present"] = cloud_config is not None
    if local_config is not None:
        result["local_model"] = local_config.model
        result["local_endpoint"] = local_config.endpoint
    if cloud_config is not None:
        result["cloud_model"] = cloud_config.model
        result["cloud_endpoint"] = cloud_config.endpoint
    if route_decision is not None:
        result["route_decision"] = asdict(route_decision)
    else:
        result["route_decision"] = {
            "requested_mode": mode,
            "chosen_mode": chosen_mode,
            "reason": "explicit_mode_override",
            "executor": executor,
            "selected_route": selected_route,
        }
    if launch_executor:
        result["executor_handoff"] = asdict(
            maybe_launch_executor_handoff(
                executor=executor,
                entrypoints=entrypoints,
                task_text=task_text,
                chosen_mode=chosen_mode,
                selected_route=selected_route,
                result=result,
                log_paths=log_paths,
                file_paths=file_paths,
                repo_root=repo_root,
            )
        )
    return result
