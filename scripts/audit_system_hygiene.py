#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ROOTS = ("docs", "blocks", "skills", "agent-library", "projects", "knowledge-library")
GENERATED_PREFIXES = ("indexes/",)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except Exception:
        return ""


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
    patterns = [
        r"^Lifecycle status:\s*(.+)$",
        r"^Current status:\s*(.+)$",
        r"^Status:\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.I | re.M)
        if match:
            return match.group(1).strip().strip("` ")
    return None


def first_date(text: str) -> datetime | None:
    patterns = [
        r"^Updated:\s*(\d{4}-\d{2}-\d{2})",
        r"^Captured:\s*(\d{4}-\d{2}-\d{2})",
        r"^Date checked:\s*(\d{4}-\d{2}-\d{2})",
        r"^Date:\s*(\d{4}-\d{2}-\d{2})",
    ]
    for pattern in patterns:
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


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    info: list[str] = []

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

    # Hard structural rule: every domain BLOCK entrypoint must be discoverable
    # from the curated block index or the live router. We do not auto-delete or
    # auto-promote blocks based on usage.
    block_index = texts.get("blocks/PROJECT_INDEX.md", "")
    router = texts.get("docs/ROUTER.md", "")
    block_entrypoints = sorted(ROOT.glob("blocks/**/BLOCK.md"))
    missing_blocks: list[str] = []
    for path in block_entrypoints:
        rel_dir = path.parent.relative_to(ROOT).as_posix().rstrip("/") + "/"
        if rel_dir not in block_index and f"{rel_dir}BLOCK.md" not in router:
            missing_blocks.append(rel_dir)
    if missing_blocks:
        errors.append(
            "Domain block entrypoints are not discoverable from blocks/PROJECT_INDEX.md or docs/ROUTER.md: "
            + ", ".join(missing_blocks)
        )
    info.append(f"Domain block entrypoints checked: {len(block_entrypoints)}")

    # Hard structural rule: internal project entrypoints must be registered.
    project_router = texts.get("projects/ROUTER.md", "")
    project_entrypoints = sorted(ROOT.glob("projects/*/PROJECT.md"))
    missing_projects: list[str] = []
    for path in project_entrypoints:
        rel = path.relative_to(ROOT / "projects").as_posix()
        if rel not in project_router:
            missing_projects.append(rel)
    if missing_projects:
        errors.append("Internal projects missing from projects/ROUTER.md: " + ", ".join(missing_projects))
    info.append(f"Internal project entrypoints checked: {len(project_entrypoints)}")

    # Skills can be intentionally nested or experimental, so missing curated
    # registration is a review signal rather than an automatic failure.
    skills_index = texts.get("skills/PROJECT_INDEX.md", "")
    skill_entrypoints = sorted(ROOT.glob("skills/**/SKILL.md"))
    unindexed_skills: list[str] = []
    for path in skill_entrypoints:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in skills_index and path.parent.relative_to(ROOT).as_posix() + "/" not in skills_index:
            unindexed_skills.append(rel)
    if unindexed_skills:
        warnings.append(f"Skills not visible in skills/PROJECT_INDEX.md ({len(unindexed_skills)}): " + ", ".join(unindexed_skills[:12]) + (" ..." if len(unindexed_skills) > 12 else ""))

    # Candidate aging is a signal, not a deletion/promotion rule.
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
            continue
        if (now - dt).days > 120:
            aged_candidates.append(rel)
    info.append(f"Candidate artifacts detected: {candidate_count}; undated: {undated_candidates}")
    if aged_candidates:
        warnings.append(f"Candidate artifacts older than 120 days need review ({len(aged_candidates)}): " + ", ".join(aged_candidates[:12]) + (" ..." if len(aged_candidates) > 12 else ""))

    # Exact duplicate canonical Markdown is suspicious, but templates and copied
    # examples can be legitimate, so report rather than delete/fail.
    by_hash: dict[str, list[str]] = defaultdict(list)
    for rel, text in texts.items():
        if not rel.startswith(CANONICAL_ROOTS):
            continue
        if rel.endswith("/README.md") or rel.endswith("PROJECT_INDEX.md"):
            continue
        digest = hashlib.sha256(normalize(text).encode("utf-8")).hexdigest()
        by_hash[digest].append(rel)
    duplicates = [rels for rels in by_hash.values() if len(rels) > 1]
    if duplicates:
        sample = [" = ".join(group) for group in duplicates[:8]]
        warnings.append(f"Exact/normalized duplicate canonical Markdown groups ({len(duplicates)}): " + "; ".join(sample))

    # Standards that nobody else names are possible orphans. This is intentionally
    # soft because some standards are reached through directory-local entrypoints.
    orphan_standards: list[str] = []
    docs_standards = sorted((ROOT / "docs").glob("*_STANDARD.md"))
    combined_by_rel = texts
    for path in docs_standards:
        rel = path.relative_to(ROOT).as_posix()
        filename = path.name
        referenced = False
        for other_rel, text in combined_by_rel.items():
            if other_rel == rel:
                continue
            if rel in text or filename in text:
                referenced = True
                break
        if not referenced:
            orphan_standards.append(rel)
    if orphan_standards:
        warnings.append(f"Possibly orphaned top-level standards ({len(orphan_standards)}): " + ", ".join(orphan_standards[:15]) + (" ..." if len(orphan_standards) > 15 else ""))
    info.append(f"Top-level standards checked for references: {len(docs_standards)}")

    # CHANGELOG is a curated milestone log, not a per-commit ledger. Long silence
    # is a review signal only; Git history and logs/latest.md remain operational evidence.
    changelog = texts.get("CHANGELOG.md", "")
    match = re.search(r"^##\s+(\d{4}-\d{2}-\d{2})\s*$", changelog, re.M)
    if match:
        latest = datetime.strptime(match.group(1), "%Y-%m-%d").replace(tzinfo=timezone.utc)
        age = (now - latest).days
        info.append(f"Latest curated CHANGELOG milestone age: {age} day(s)")
        if age > 60:
            warnings.append(f"CHANGELOG.md has no curated milestone for {age} days; review whether major system changes are missing.")
    else:
        warnings.append("CHANGELOG.md has no parseable YYYY-MM-DD milestone heading.")

    print("PEOS System Hygiene Audit")
    print("=========================")
    for row in info:
        print(f"INFO: {row}")
    for row in warnings:
        print(f"WARNING: {row}")
    for row in errors:
        print(f"ERROR: {row}")
    print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s)")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
