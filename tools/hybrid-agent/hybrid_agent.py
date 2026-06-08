from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, request


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LOG_PATH = REPO_ROOT / "logs" / "api-runtime" / "hybrid-agent.jsonl"
DEFAULT_SELECTED_ROUTE = "docs/CONTEXT_ASSEMBLY_STANDARD.md -> issue-27-hybrid-agent"
ERROR_PATTERN = re.compile(r"(error|exception|traceback|fail|warning)", re.IGNORECASE)


@dataclass(slots=True)
class EndpointConfig:
    provider: str
    endpoint: str
    model: str
    api_key: str
    timeout_seconds: float = 60.0


@dataclass(slots=True)
class EvidenceExcerpt:
    start_line: int
    end_line: int
    text: str
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "start_line": self.start_line,
            "end_line": self.end_line,
            "text": self.text,
            "reason": self.reason,
        }


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_endpoint(endpoint: str) -> str:
    return endpoint.rstrip("/")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def slice_excerpt(lines: list[str], start: int, end: int) -> str:
    return "\n".join(lines[start:end]).strip()


def collect_matching_windows(lines: list[str], max_windows: int, context: int) -> list[tuple[int, int]]:
    windows: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        if not ERROR_PATTERN.search(line):
            continue
        start = max(0, index - context)
        end = min(len(lines), index + context + 1)
        if windows and start <= windows[-1][1]:
            windows[-1] = (windows[-1][0], max(windows[-1][1], end))
        else:
            windows.append((start, end))
        if len(windows) >= max_windows:
            break
    return windows


def build_evidence_item(
    path: Path,
    *,
    kind: str,
    max_excerpts: int = 4,
    context_lines: int = 2,
    max_excerpt_chars: int = 900,
) -> dict[str, Any]:
    text = read_text(path)
    lines = text.splitlines() or [text]
    windows = collect_matching_windows(lines, max_excerpts, context_lines)
    reason = "keyword_match"
    if not windows:
        reason = "leading_context"
        windows = [(0, min(len(lines), 40))]

    excerpts: list[EvidenceExcerpt] = []
    for start, end in windows:
        excerpt = slice_excerpt(lines, start, end)
        if len(excerpt) > max_excerpt_chars:
            excerpt = excerpt[: max_excerpt_chars - 3].rstrip() + "..."
        excerpts.append(
            EvidenceExcerpt(
                start_line=start + 1,
                end_line=end,
                text=excerpt,
                reason=reason,
            )
        )

    return {
        "path": str(path),
        "kind": kind,
        "total_lines": len(lines),
        "total_chars": len(text),
        "excerpts": [item.as_dict() for item in excerpts],
    }


def build_input_payload(
    *,
    task_text: str,
    log_paths: list[Path],
    file_paths: list[Path],
    selected_route: str,
) -> dict[str, Any]:
    evidence: list[dict[str, Any]] = []
    for path in log_paths:
        evidence.append(build_evidence_item(path, kind="log"))
    for path in file_paths:
        evidence.append(build_evidence_item(path, kind="file"))
    return {
        "task_text": task_text,
        "selected_route": selected_route,
        "generated_at_utc": utc_now_iso(),
        "evidence": evidence,
    }


def json_size_metrics(payload: Any) -> dict[str, int]:
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    encoded = text.encode("utf-8")
    return {
        "chars": len(text),
        "bytes": len(encoded),
    }


def make_local_prompt(payload: dict[str, Any]) -> str:
    return (
        "Return one JSON object only.\n"
        "You are a bounded local preprocessing worker, not the final architect.\n"
        "Summarize the task and evidence compactly while preserving source references.\n"
        "Required JSON schema:\n"
        "{\n"
        '  "summary": "string",\n'
        '  "relevant_error_excerpts": [\n'
        '    {"path": "string", "start_line": 1, "end_line": 1, "reason": "string"}\n'
        "  ],\n"
        '  "suspected_files_modules": [\n'
        '    {"path": "string", "module": "string", "reason": "string"}\n'
        "  ],\n"
        '  "escalation_recommendation": "cloud" | "local_sufficient",\n'
        '  "local_stage_metadata": {\n'
        '    "confidence": "low|medium|high",\n'
        '    "notes": "string"\n'
        "  }\n"
        "}\n"
        "Do not invent source paths or line numbers. Use only evidence that exists in the payload.\n"
        "Payload:\n"
        f"{json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)}"
    )


def make_cloud_prompt(
    *,
    task_text: str,
    selected_route: str,
    evidence_payload: dict[str, Any],
    local_payload: dict[str, Any] | None,
    fallback_reason: str | None,
    include_full_evidence: bool,
) -> str:
    payload = {
        "task_text": task_text,
        "selected_route": selected_route,
        "fallback_reason": fallback_reason,
    }
    if local_payload is not None:
        payload["compact_context"] = local_payload
        payload["traceability_mode"] = "local_payload_references"
        if include_full_evidence:
            payload["bounded_evidence"] = evidence_payload["evidence"]
    else:
        payload["bounded_evidence"] = evidence_payload["evidence"]
        payload["traceability_mode"] = "bounded_evidence"
    return (
        "You are the cloud reasoning stage for a bounded hybrid agent prototype.\n"
        "Use the provided task and evidence only. Keep traceability to source paths and line ranges.\n"
        "If local preprocessing exists, treat it as the primary compact context rather than absolute truth.\n"
        "Return a concise actionable answer in plain text.\n"
        "Payload:\n"
        f"{json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)}"
    )


def extract_text_content(message_content: Any) -> str:
    if isinstance(message_content, str):
        return message_content
    if isinstance(message_content, list):
        chunks: list[str] = []
        for item in message_content:
            if isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text")
                if isinstance(text, str):
                    chunks.append(text)
        return "\n".join(chunks).strip()
    return ""


def extract_json_object(text: str) -> dict[str, Any]:
    candidate = text.strip()
    if not candidate:
        raise ValueError("Model returned empty content")
    try:
        parsed = json.loads(candidate)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    start = candidate.find("{")
    end = candidate.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("Model did not return a JSON object")
    parsed = json.loads(candidate[start : end + 1])
    if not isinstance(parsed, dict):
        raise ValueError("Model returned JSON but not an object")
    return parsed


def normalize_evidence_path(path: str) -> str:
    return str(Path(path))


def normalize_local_payload(payload: dict[str, Any]) -> dict[str, Any]:
    recommendation = payload.get("escalation_recommendation")
    if isinstance(recommendation, str):
        normalized = recommendation.strip().lower().replace("-", "_").replace(" ", "_")
        if normalized in {"cloud", "local_sufficient"}:
            payload["escalation_recommendation"] = normalized

    metadata = payload.get("local_stage_metadata")
    if isinstance(metadata, dict):
        confidence = metadata.get("confidence")
        if isinstance(confidence, str):
            metadata["confidence"] = confidence.strip().lower()

    excerpts = payload.get("relevant_error_excerpts")
    if isinstance(excerpts, list):
        for item in excerpts:
            if isinstance(item, dict):
                path = item.get("path")
                if isinstance(path, str) and path:
                    item["path"] = normalize_evidence_path(path)

    suspects = payload.get("suspected_files_modules")
    if isinstance(suspects, list):
        for item in suspects:
            if isinstance(item, dict):
                path = item.get("path")
                if isinstance(path, str) and path:
                    item["path"] = normalize_evidence_path(path)
    return payload


def validate_local_payload(payload: dict[str, Any]) -> dict[str, Any]:
    payload = normalize_local_payload(payload)
    summary = payload.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        raise ValueError("Local payload is missing a string summary")

    excerpts = payload.get("relevant_error_excerpts")
    suspects = payload.get("suspected_files_modules")
    metadata = payload.get("local_stage_metadata")
    recommendation = payload.get("escalation_recommendation")
    if not isinstance(excerpts, list):
        raise ValueError("Local payload is missing relevant_error_excerpts")
    if not isinstance(suspects, list):
        raise ValueError("Local payload is missing suspected_files_modules")
    if recommendation not in {"cloud", "local_sufficient"}:
        raise ValueError("Local payload has invalid escalation_recommendation")
    if not isinstance(metadata, dict):
        raise ValueError("Local payload is missing local_stage_metadata")
    return payload


def evidence_index(input_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw_evidence = input_payload.get("evidence")
    if not isinstance(raw_evidence, list):
        raise ValueError("Input payload is missing evidence")

    index: dict[str, dict[str, Any]] = {}
    for item in raw_evidence:
        if not isinstance(item, dict):
            continue
        path = item.get("path")
        if isinstance(path, str) and path:
            index[path] = item
    return index


def repair_excerpt_path(path: str, evidence_by_path: dict[str, dict[str, Any]]) -> str:
    if path in evidence_by_path:
        return path
    if len(evidence_by_path) != 1:
        return path

    only_path, only_item = next(iter(evidence_by_path.items()))
    excerpts = only_item.get("excerpts")
    if not isinstance(excerpts, list):
        return path

    normalized = path.replace("\\", "/")
    for excerpt in excerpts:
        if not isinstance(excerpt, dict):
            continue
        text = excerpt.get("text")
        if isinstance(text, str) and normalized in text.replace("\\", "/"):
            return only_path
    return path


def validate_excerpt_references(
    excerpts: list[Any],
    evidence_by_path: dict[str, dict[str, Any]],
) -> None:
    for index, excerpt in enumerate(excerpts, start=1):
        if not isinstance(excerpt, dict):
            raise ValueError(f"Local payload excerpt #{index} is not an object")

        path = excerpt.get("path")
        start_line = excerpt.get("start_line")
        end_line = excerpt.get("end_line")
        if not isinstance(path, str) or not path:
            raise ValueError(f"Local payload excerpt #{index} is missing a valid path")
        repaired_path = repair_excerpt_path(path, evidence_by_path)
        if repaired_path != path:
            excerpt["path"] = repaired_path
            path = repaired_path
        if path not in evidence_by_path:
            raise ValueError(f"Local payload excerpt #{index} references unknown evidence path: {path}")
        if not isinstance(start_line, int) or not isinstance(end_line, int):
            raise ValueError(f"Local payload excerpt #{index} has invalid line-range types")
        if start_line < 1 or end_line < start_line:
            raise ValueError(f"Local payload excerpt #{index} has an invalid line range")

        total_lines = evidence_by_path[path].get("total_lines")
        if not isinstance(total_lines, int) or end_line > total_lines:
            raise ValueError(
                f"Local payload excerpt #{index} points outside the source evidence line range for {path}"
            )


def validate_suspected_paths(
    suspects: list[Any],
    evidence_by_path: dict[str, dict[str, Any]],
) -> None:
    for index, suspect in enumerate(suspects, start=1):
        if not isinstance(suspect, dict):
            raise ValueError(f"Local payload suspect #{index} is not an object")

        path = suspect.get("path")
        if not isinstance(path, str) or not path:
            raise ValueError(f"Local payload suspect #{index} is missing a valid path")

        if path in evidence_by_path:
            continue

        resolved_path = REPO_ROOT / Path(path)
        if not resolved_path.exists():
            raise ValueError(f"Local payload suspect #{index} references a missing path: {path}")


def validate_local_references(
    payload: dict[str, Any],
    input_payload: dict[str, Any],
) -> dict[str, Any]:
    evidence_by_path = evidence_index(input_payload)
    validate_excerpt_references(payload["relevant_error_excerpts"], evidence_by_path)
    validate_suspected_paths(payload["suspected_files_modules"], evidence_by_path)
    return payload


def call_chat_completion(
    config: EndpointConfig,
    *,
    system_prompt: str,
    user_prompt: str,
) -> tuple[dict[str, Any], float]:
    base_url = normalize_endpoint(config.endpoint)
    url = f"{base_url}/chat/completions"
    body = {
        "model": config.model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
    }
    payload = json.dumps(body).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.api_key}",
    }
    started = time.perf_counter()
    req = request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with request.urlopen(req, timeout=config.timeout_seconds) as response:
            response_text = response.read().decode("utf-8")
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        exc.close()
        raise RuntimeError(f"{config.provider} request failed with HTTP {exc.code}: {detail}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"{config.provider} request failed: {exc.reason}") from exc
    latency_ms = (time.perf_counter() - started) * 1000.0
    parsed = json.loads(response_text)
    return parsed, latency_ms


def response_text_and_usage(response: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        raise ValueError("Response does not contain choices")
    first = choices[0]
    message = first.get("message") if isinstance(first, dict) else None
    if not isinstance(message, dict):
        raise ValueError("Response choice does not contain a message")
    text = extract_text_content(message.get("content"))
    usage = response.get("usage") if isinstance(response.get("usage"), dict) else {}
    return text, usage


def map_usage_fields(usage: dict[str, Any]) -> dict[str, Any]:
    prompt_tokens = usage.get("prompt_tokens")
    completion_tokens = usage.get("completion_tokens")
    total_tokens = usage.get("total_tokens")
    prompt_details = usage.get("prompt_tokens_details") if isinstance(usage.get("prompt_tokens_details"), dict) else {}
    cache_hit = prompt_details.get("cached_tokens")
    cache_miss = None
    if isinstance(prompt_tokens, int) and isinstance(cache_hit, int):
        cache_miss = prompt_tokens - cache_hit
    return {
        "input_tokens_total": prompt_tokens,
        "input_tokens_cache_hit": cache_hit,
        "input_tokens_cache_miss": cache_miss,
        "output_tokens": completion_tokens,
        "total_tokens": total_tokens,
    }


def compression_ratio(input_bytes: int, output_bytes: int) -> float | None:
    if input_bytes <= 0:
        return None
    return round(output_bytes / input_bytes, 6)


def write_log_entry(log_path: Path, entry: dict[str, Any]) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


def build_log_entry(
    *,
    stage: str,
    provider: str,
    model: str,
    task_id: str | None,
    project_id: str | None,
    selected_route: str,
    loaded_modules: list[str],
    request_id: str | None,
    usage: dict[str, Any],
    input_metrics: dict[str, int],
    output_metrics: dict[str, int],
    latency_ms: float,
    status: str,
    notes: str | None,
) -> dict[str, Any]:
    usage_fields = map_usage_fields(usage)
    return {
        "timestamp_utc": utc_now_iso(),
        "provider": provider,
        "model": model,
        "request_id": request_id,
        "project_id": project_id,
        "task_id": task_id,
        "context_profile": None,
        "context_fingerprint": None,
        "selected_route": selected_route,
        "loaded_modules": loaded_modules,
        "input_tokens_total": usage_fields["input_tokens_total"],
        "input_tokens_cache_hit": usage_fields["input_tokens_cache_hit"],
        "input_tokens_cache_miss": usage_fields["input_tokens_cache_miss"],
        "output_tokens": usage_fields["output_tokens"],
        "total_tokens": usage_fields["total_tokens"],
        "estimated_cost_usd": None,
        "billed_cost_usd": None,
        "latency_ms": round(latency_ms, 3),
        "status": status,
        "stage": stage,
        "input_size_bytes": input_metrics["bytes"],
        "input_size_chars": input_metrics["chars"],
        "output_size_bytes": output_metrics["bytes"],
        "output_size_chars": output_metrics["chars"],
        "compression_ratio": compression_ratio(input_metrics["bytes"], output_metrics["bytes"]),
        "notes": notes,
    }


def run_local_stage(
    *,
    config: EndpointConfig,
    input_payload: dict[str, Any],
    task_id: str | None,
    project_id: str | None,
    selected_route: str,
    log_path: Path,
) -> dict[str, Any]:
    system_prompt = "You are a precise local preprocessing worker."
    prompt = make_local_prompt(input_payload)
    input_metrics = json_size_metrics({"system": system_prompt, "user": prompt})
    response, latency_ms = call_chat_completion(config, system_prompt=system_prompt, user_prompt=prompt)
    text, usage = response_text_and_usage(response)
    parsed = validate_local_payload(extract_json_object(text))
    parsed = validate_local_references(parsed, input_payload)
    output_metrics = json_size_metrics(parsed)
    log_entry = build_log_entry(
        stage="local_preprocess",
        provider=config.provider,
        model=config.model,
        task_id=task_id,
        project_id=project_id,
        selected_route=selected_route,
        loaded_modules=[item["path"] for item in input_payload["evidence"]],
        request_id=response.get("id"),
        usage=usage,
        input_metrics=input_metrics,
        output_metrics=output_metrics,
        latency_ms=latency_ms,
        status="success",
        notes=None,
    )
    write_log_entry(log_path, log_entry)
    return {
        "payload": parsed,
        "log_entry": log_entry,
        "latency_ms": latency_ms,
        "request_id": response.get("id"),
    }


def run_cloud_stage(
    *,
    config: EndpointConfig,
    task_text: str,
    input_payload: dict[str, Any],
    local_payload: dict[str, Any] | None,
    fallback_reason: str | None,
    include_full_evidence: bool,
    task_id: str | None,
    project_id: str | None,
    selected_route: str,
    log_path: Path,
) -> dict[str, Any]:
    system_prompt = "You are a careful cloud reasoning stage."
    prompt = make_cloud_prompt(
        task_text=task_text,
        selected_route=selected_route,
        evidence_payload=input_payload,
        local_payload=local_payload,
        fallback_reason=fallback_reason,
        include_full_evidence=include_full_evidence,
    )
    input_metrics = json_size_metrics({"system": system_prompt, "user": prompt})
    response, latency_ms = call_chat_completion(config, system_prompt=system_prompt, user_prompt=prompt)
    text, usage = response_text_and_usage(response)
    output_metrics = json_size_metrics({"content": text})
    notes = fallback_reason if fallback_reason else None
    log_entry = build_log_entry(
        stage="cloud_reasoning",
        provider=config.provider,
        model=config.model,
        task_id=task_id,
        project_id=project_id,
        selected_route=selected_route,
        loaded_modules=[item["path"] for item in input_payload["evidence"]],
        request_id=response.get("id"),
        usage=usage,
        input_metrics=input_metrics,
        output_metrics=output_metrics,
        latency_ms=latency_ms,
        status="success",
        notes=notes,
    )
    write_log_entry(log_path, log_entry)
    return {
        "content": text,
        "usage": usage,
        "log_entry": log_entry,
        "latency_ms": latency_ms,
        "request_id": response.get("id"),
    }


def run_hybrid_agent(
    *,
    task_text: str,
    mode: str,
    log_paths: list[Path],
    file_paths: list[Path],
    local_config: EndpointConfig | None,
    cloud_config: EndpointConfig | None,
    log_path: Path = DEFAULT_LOG_PATH,
    selected_route: str = DEFAULT_SELECTED_ROUTE,
    task_id: str | None = None,
    project_id: str | None = "project-execution-os",
    include_full_evidence: bool = False,
) -> dict[str, Any]:
    input_payload = build_input_payload(
        task_text=task_text,
        log_paths=log_paths,
        file_paths=file_paths,
        selected_route=selected_route,
    )
    result: dict[str, Any] = {
        "mode": mode,
        "selected_route": selected_route,
        "fallback_used": False,
        "input_payload": input_payload,
    }

    if mode == "cloud-only":
        if cloud_config is None:
            raise ValueError("cloud-only mode requires cloud configuration")
        result["cloud"] = run_cloud_stage(
            config=cloud_config,
            task_text=task_text,
            input_payload=input_payload,
            local_payload=None,
            fallback_reason=None,
            include_full_evidence=include_full_evidence,
            task_id=task_id,
            project_id=project_id,
            selected_route=selected_route,
            log_path=log_path,
        )
        return result

    if mode == "local-only":
        if local_config is None:
            raise ValueError("local-only mode requires local configuration")
        result["local"] = run_local_stage(
            config=local_config,
            input_payload=input_payload,
            task_id=task_id,
            project_id=project_id,
            selected_route=selected_route,
            log_path=log_path,
        )
        return result

    if mode != "preprocess-then-cloud":
        raise ValueError(f"Unsupported mode: {mode}")
    if cloud_config is None:
        raise ValueError("preprocess-then-cloud mode requires cloud configuration")

    local_payload = None
    fallback_reason = None
    if local_config is not None:
        try:
            local_result = run_local_stage(
                config=local_config,
                input_payload=input_payload,
                task_id=task_id,
                project_id=project_id,
                selected_route=selected_route,
                log_path=log_path,
            )
            result["local"] = local_result
            local_payload = local_result["payload"]
        except Exception as exc:  # noqa: BLE001
            fallback_reason = f"local_preprocess_failed: {exc}"
            result["fallback_used"] = True
            failure_entry = build_log_entry(
                stage="local_preprocess",
                provider=local_config.provider,
                model=local_config.model,
                task_id=task_id,
                project_id=project_id,
                selected_route=selected_route,
                loaded_modules=[item["path"] for item in input_payload["evidence"]],
                request_id=None,
                usage={},
                input_metrics=json_size_metrics(input_payload),
                output_metrics={"bytes": 0, "chars": 0},
                latency_ms=0.0,
                status="failed_fallback_to_cloud",
                notes=fallback_reason,
            )
            write_log_entry(log_path, failure_entry)
            result["local_error"] = str(exc)
    else:
        result["fallback_used"] = True
        fallback_reason = "local_preprocess_skipped: no local configuration provided"

    result["cloud"] = run_cloud_stage(
        config=cloud_config,
        task_text=task_text,
        input_payload=input_payload,
        local_payload=local_payload,
        fallback_reason=fallback_reason,
        include_full_evidence=include_full_evidence,
        task_id=task_id,
        project_id=project_id,
        selected_route=selected_route,
        log_path=log_path,
    )
    return result
