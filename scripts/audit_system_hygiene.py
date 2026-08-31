#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ROOTS = ("docs", "blocks", "skills", "agent-library", "projects", "knowledge-library")
GENERATED_PREFIXES = ("indexes/",)
HISTORY_PATH = ROOT / "logs" / "hygiene-history.jsonl"
PERSISTENCE_THRESHOLD = 3


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except Exception:
        return ""


def is_shallow_repository() -> bool:
    return git("rev-parse", "--is-shallow-repository").lower() == "true"


def markdown_files() -> list[Path]:
    rows: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if ".git" in path.parts or "node_modules" in path.parts:
            continue
        if rel.startswith(GENERATED_PREFIXES):
            continue
        rows.append(path)
    return sorted(rows)


def first_status(text: str) -> str | None:
    for pattern in (
        r"^Lifecycle status:\s*(.+)$",
        r"^Lifecycle State:\s*(.+)$",
        r"^Current status:\s*(.+)$",
        r"^Status:\s*(.+)$",
    ):
        match = re.search(pattern, text, re.I | re.M)
        if match:
            return match.group(1).strip().strip("` ")
    section = re.search(
        r"(?ims)^#{2,4}\s+(?:Lifecycle Status|Lifecycle State|Current Status|Status)\s*$\s*\n+\s*`?([^\n`]+)`?",
        text,
    )
    return section.group(1).strip().strip("` ") if section else None


def first_date(text: str) -> datetime | None:
    for pattern in (
        r"^Updated:\s*(\d{4}-\d{2}-\d{2})",
        r"^Captured:\s*(\d{4}-\d{2}-\d{2})",
        r"^Date checked:\s*(\d{4}-\d{2}-\d{2})",
        r"^Date:\s*(\d{4}-\d{2}-\d{2})",
    ):
        match = re.search(pattern, text, re.I | re.M)
        if match:
            try:
                return datetime.strptime(match.group(1), "%Y-%m-%d").replace(tzinfo=timezone.utc)
            except ValueError:
                pass
    return None


def head_date() -> datetime:
    raw = git("show", "-s", "--format=%cI", "HEAD")
    if raw:
        try:
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            pass
    return datetime.now(timezone.utc)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def is_retired_status(status: str | None) -> bool:
    if not status:
        return False
    lowered = status.lower()
    return any(token in lowered for token in ("deprecated", "retired", "replaced", "superseded", "archived"))


def warning_id(kind: str, detail: str = "") -> str:
    suffix = hashlib.sha256(detail.encode("utf-8")).hexdigest()[:10] if detail else "general"
    return f"{kind}:{suffix}"


def load_history() -> list[dict]:
    if not HISTORY_PATH.exists():
        return []
    rows: list[dict] = []
    for line in HISTORY_PATH.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
            if isinstance(row, dict):
                rows.append(row)
        except json.JSONDecodeError:
            continue
    return rows


def consecutive_occurrences(history: list[dict], current_warning_ids: set[str]) -> dict[str, int]:
    counts = {wid: 1 for wid in current_warning_ids}
    for wid in current_warning_ids:
        for row in reversed(history):
            if wid in set(row.get("warning_ids", [])):
                counts[wid] += 1
            else:
                break
    return counts


def block_usage(path: Path, now: datetime) -> dict:
    rel = path.parent.relative_to(ROOT).as_posix() + "/"
    last_raw = git("log", "-1", "--format=%cI", "--", rel)
    last_touched = None
    age_days = None
    if last_raw:
        try:
            dt = datetime.fromisoformat(last_raw.replace("Z", "+00:00"))
            last_touched = dt.date().isoformat()
            age_days = max(0, (now - dt).days)
        except ValueError:
            pass
    count_30 = git("rev-list", "--count", "--since=30.days.ago", "HEAD", "--", rel)
    count_90 = git("rev-list", "--count", "--since=90.days.ago", "HEAD", "--", rel)
    return {
        "block": rel.rstrip("/").split("/")[-1],
        "path": rel,
        "last_touched": last_touched,
        "age_days": age_days,
        "commits_30d": int(count_30) if count_30.isdigit() else 0,
        "commits_90d": int(count_90) if count_90.isdigit() else 0,
    }


def append_history(snapshot: dict) -> None:
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with HISTORY_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(snapshot, ensure_ascii=False, sort_keys=True) + "\n")


def write_step_summary(snapshot: dict, warning_rows: list[dict], runtime_warnings: list[str], errors: list[str]) -> None:
    target = os.getenv("GITHUB_STEP_SUMMARY")
    if not target:
        return
    blocks = snapshot["block_usage"]
    quiet_blocks = sorted(blocks, key=lambda row: (row["commits_90d"], -(row["age_days"] or 0)))[:8]
    history_state = "SHALLOW — activity metrics may be incomplete" if snapshot["git_history_shallow"] else "full history"
    lines = [
        "## PEOS System Hygiene",
        "",
        f"**Errors:** {len(errors)}  |  **Warnings:** {len(warning_rows)}  |  **Persistent warnings:** {sum(1 for row in warning_rows if row['consecutive'] >= PERSISTENCE_THRESHOLD)}",
        f"**Git history:** {history_state}",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Domain blocks | {snapshot['metrics']['domain_blocks']} |",
        f"| Internal projects | {snapshot['metrics']['internal_projects']} |",
        f"| Candidate artifacts | {snapshot['metrics']['candidates']} |",
        f"| Undated candidates | {snapshot['metrics']['undated_candidates']} |",
        f"| Active top-level standards | {snapshot['metrics']['top_level_standards']} |",
        "",
    ]
    if runtime_warnings:
        lines += ["### Data-quality warnings", ""] + [f"- {item}" for item in runtime_warnings] + [""]
    if warning_rows:
        lines += ["### Warnings", "", "| ID | Consecutive runs | State | Message |", "|---|---:|---|---|"]
        for row in warning_rows:
            state = "ACTION_REQUIRED" if row["consecutive"] >= PERSISTENCE_THRESHOLD else "warning"
            message = row["message"].replace("|", "\\|")
            lines.append(f"| `{row['id']}` | {row['consecutive']} | {state} | {message} |")
        lines.append("")
    if errors:
        lines += ["### Errors", ""] + [f"- {item}" for item in errors] + [""]
    lines += ["### Lowest recent block activity", "", "| Block | Last touched | Commits 30d | Commits 90d |", "|---|---|---:|---:|"]
    for row in quiet_blocks:
        lines.append(f"| `{row['path']}` | {row['last_touched'] or 'unknown'} | {row['commits_30d']} | {row['commits_90d']} |")
    lines += ["", "> Low activity is a review signal only. It does not authorize automatic deletion, deprecation, or promotion.", ""]
    with open(target, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--record-history", action="store_true", help="Append this run to logs/hygiene-history.jsonl")
    args = parser.parse_args()

    errors: list[str] = []
    warning_messages: list[tuple[str, str]] = []
    runtime_warnings: list[str] = []
    info: list[str] = []

    shallow = is_shallow_repository()
    if shallow:
        runtime_warnings.append(
            "Shallow repository detected. Structural checks remain valid, but block last_touched/30d/90d activity signals may be incomplete or misleading. Use a full clone or fetch full history before relying on activity metrics."
        )

    required = [
        "START_HERE.md",
        "docs/ROUTER.md",
        "projects/ROUTER.md",
        "blocks/PROJECT_INDEX.md",
        "skills/PROJECT_INDEX.md",
        "knowledge-library/PROJECT_INDEX.md",
        "agent-library/PROJECT_INDEX.md",
        "docs/KNOWLEDGE_SYSTEM.md",
        "docs/INDEXING_STANDARD.md",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"Required canonical hygiene/navigation artifact is missing: {rel}")

    files = markdown_files()
    texts = {path.relative_to(ROOT).as_posix(): read(path) for path in files}

    block_index = texts.get("blocks/PROJECT_INDEX.md", "")
    router = texts.get("docs/ROUTER.md", "")
    block_entrypoints = sorted(ROOT.glob("blocks/**/BLOCK.md"))
    missing_blocks = []
    for path in block_entrypoints:
        rel_dir = path.parent.relative_to(ROOT).as_posix().rstrip("/") + "/"
        if rel_dir not in block_index and f"{rel_dir}BLOCK.md" not in router:
            missing_blocks.append(rel_dir)
    if missing_blocks:
        errors.append("Domain block entrypoints are not discoverable from blocks/PROJECT_INDEX.md or docs/ROUTER.md: " + ", ".join(missing_blocks))
    info.append(f"Domain block entrypoints checked: {len(block_entrypoints)}")

    project_router = texts.get("projects/ROUTER.md", "")
    project_entrypoints = sorted(ROOT.glob("projects/*/PROJECT.md"))
    missing_projects = []
    for path in project_entrypoints:
        rel = path.relative_to(ROOT / "projects").as_posix()
        if rel not in project_router:
            missing_projects.append(rel)
    if missing_projects:
        errors.append("Internal projects missing from projects/ROUTER.md: " + ", ".join(missing_projects))
    info.append(f"Internal project entrypoints checked: {len(project_entrypoints)}")

    skills_index = texts.get("skills/PROJECT_INDEX.md", "")
    skill_entrypoints = sorted(ROOT.glob("skills/**/SKILL.md"))
    unindexed_skills = []
    for path in skill_entrypoints:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in skills_index and path.parent.relative_to(ROOT).as_posix() + "/" not in skills_index:
            unindexed_skills.append(rel)
    if unindexed_skills:
        detail = ", ".join(unindexed_skills)
        warning_messages.append((warning_id("unindexed-skills", detail), f"Skills not visible in skills/PROJECT_INDEX.md ({len(unindexed_skills)}): {detail}"))

    now = head_date()
    aged_candidates: list[str] = []
    undated_candidates = 0
    candidate_count = 0
    for rel, text in texts.items():
        if not rel.startswith(CANONICAL_ROOTS):
            continue
        status = first_status(text)
        if not status or "candidate" not in status.lower():
            continue
        candidate_count += 1
        dt = first_date(text)
        if dt is None:
            undated_candidates += 1
        elif (now - dt).days > 120:
            aged_candidates.append(rel)
    info.append(f"Candidate artifacts detected: {candidate_count}; undated: {undated_candidates}")
    if aged_candidates:
        detail = ", ".join(aged_candidates)
        warning_messages.append((warning_id("aged-candidates", detail), f"Candidate artifacts older than 120 days need review ({len(aged_candidates)}): {detail}"))

    by_hash: dict[str, list[str]] = defaultdict(list)
    for rel, text in texts.items():
        if rel.startswith(CANONICAL_ROOTS) and not rel.endswith("/README.md") and not rel.endswith("PROJECT_INDEX.md"):
            by_hash[hashlib.sha256(normalize(text).encode("utf-8")).hexdigest()].append(rel)
    duplicates = [rels for rels in by_hash.values() if len(rels) > 1]
    if duplicates:
        detail = "; ".join(" = ".join(group) for group in duplicates)
        warning_messages.append((warning_id("duplicate-markdown", detail), f"Exact/normalized duplicate canonical Markdown groups ({len(duplicates)}): {detail}"))

    orphan_standards = []
    docs_standards = sorted((ROOT / "docs").glob("*_STANDARD.md"))
    for path in docs_standards:
        rel = path.relative_to(ROOT).as_posix()
        status = first_status(texts.get(rel, ""))
        if is_retired_status(status):
            continue
        filename = path.name
        if not any(other_rel != rel and (rel in other_text or filename in other_text) for other_rel, other_text in texts.items()):
            orphan_standards.append(rel)
    if orphan_standards:
        detail = ", ".join(orphan_standards)
        warning_messages.append((warning_id("orphan-standards", detail), f"Possibly orphaned active top-level standards ({len(orphan_standards)}): {detail}"))
    info.append(f"Top-level standards checked for active inbound references: {len(docs_standards)}")

    changelog = texts.get("CHANGELOG.md", "")
    changelog_age = None
    match = re.search(r"^##\s+(\d{4}-\d{2}-\d{2})\s*$", changelog, re.M)
    if match:
        latest = datetime.strptime(match.group(1), "%Y-%m-%d").replace(tzinfo=timezone.utc)
        changelog_age = (now - latest).days
        info.append(f"Latest curated CHANGELOG milestone age: {changelog_age} day(s)")
        if changelog_age > 60:
            warning_messages.append((warning_id("stale-changelog"), f"CHANGELOG.md has no curated milestone for {changelog_age} days; review whether major system changes are missing."))
    else:
        warning_messages.append((warning_id("unparseable-changelog"), "CHANGELOG.md has no parseable YYYY-MM-DD milestone heading."))

    usage = [block_usage(path, now) for path in block_entrypoints]
    history = load_history()
    current_ids = {wid for wid, _ in warning_messages}
    persistence = consecutive_occurrences(history, current_ids)
    warning_rows = [{"id": wid, "message": message, "consecutive": persistence.get(wid, 1)} for wid, message in warning_messages]

    snapshot = {
        "schema_version": 3,
        "recorded_at": now.isoformat(),
        "commit": git("rev-parse", "HEAD") or "unknown",
        "git_history_shallow": shallow,
        "activity_metrics_reliable": not shallow,
        "metrics": {
            "domain_blocks": len(block_entrypoints),
            "internal_projects": len(project_entrypoints),
            "skills": len(skill_entrypoints),
            "candidates": candidate_count,
            "undated_candidates": undated_candidates,
            "top_level_standards": len(docs_standards),
            "changelog_age_days": changelog_age,
            "errors": len(errors),
            "warnings": len(warning_rows),
            "persistent_warnings": sum(1 for row in warning_rows if row["consecutive"] >= PERSISTENCE_THRESHOLD),
        },
        "warning_ids": sorted(current_ids),
        "warnings": warning_rows,
        "runtime_warnings": runtime_warnings,
        "block_usage": usage,
    }

    print("PEOS System Hygiene Audit")
    print("=========================")
    for row in info:
        print(f"INFO: {row}")
    for row in runtime_warnings:
        print(f"WARNING [shallow-history:general]: {row}")
    for row in warning_rows:
        state = "ACTION_REQUIRED" if row["consecutive"] >= PERSISTENCE_THRESHOLD else "WARNING"
        print(f"{state} [{row['id']}] consecutive={row['consecutive']}: {row['message']}")
    for row in errors:
        print(f"ERROR: {row}")
    print("Block usage signals:" + (" [UNRELIABLE: shallow history]" if shallow else ""))
    for row in sorted(usage, key=lambda item: (item["commits_90d"], item["path"])):
        print(f"  {row['path']} last_touched={row['last_touched'] or 'unknown'} commits_30d={row['commits_30d']} commits_90d={row['commits_90d']}")
    print(f"Summary: {len(errors)} error(s), {len(warning_rows)} warning(s), {snapshot['metrics']['persistent_warnings']} action-required signal(s)")

    write_step_summary(snapshot, warning_rows, runtime_warnings, errors)
    if args.record_history:
        append_history(snapshot)
        print(f"History appended: {HISTORY_PATH.relative_to(ROOT).as_posix()}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
