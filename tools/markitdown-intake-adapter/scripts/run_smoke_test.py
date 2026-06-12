from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from generate_smoke_samples import generate_samples


EXPECTED_STATUSES = {
    "pdf_text": "PASS",
    "pdf_scan": "NEEDS_OCR",
    "docx": "PASS",
    "pptx": "PASS",
    "xlsx": "PASS",
    "html": "PASS",
    "csv": "PASS",
    "zip": "PASS",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the MarkItDown intake adapter smoke suite.")
    parser.add_argument("--project-root", required=True, help="Root path of the adapter project.")
    return parser


def convert_one(project_root: Path, sample_name: str, input_path: Path, output_dir: Path) -> dict[str, str]:
    script_path = project_root / "scripts" / "convert_local.py"
    output_path = output_dir / f"{sample_name}.md"
    completed = subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--input",
            str(input_path),
            "--output",
            str(output_path),
        ],
        check=False,
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()
    payload = json.loads(stdout) if stdout else {}
    payload.update(
        {
            "sample": sample_name,
            "returncode": str(completed.returncode),
            "stderr": stderr,
            "markdown_exists": str(output_path.exists()),
            "output_path": str(output_path),
        }
    )
    return payload


def write_report(report_path: Path, results: list[dict[str, str]], overall_status: str) -> None:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        "# MarkItDown Intake Adapter Smoke Test",
        "",
        f"Timestamp: {timestamp}",
        f"Overall-Status: {overall_status}",
        "",
        "| Sample | Expected | Actual | Return Code | Output |",
        "| --- | --- | --- | --- | --- |",
    ]

    for result in results:
        sample = result["sample"]
        expected = EXPECTED_STATUSES[sample]
        actual = result.get("status", "ERROR")
        returncode = result.get("returncode", "1")
        output_name = Path(result.get("output_path", "")).name
        lines.append(f"| {sample} | {expected} | {actual} | {returncode} | {output_name} |")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = build_parser().parse_args()
    project_root = Path(args.project_root).resolve()
    temp_root = project_root / ".tmp-smoke"
    samples_dir = temp_root / "samples"
    outputs_dir = temp_root / "outputs"
    report_path = project_root / "logs" / "latest.md"

    if temp_root.exists():
        shutil.rmtree(temp_root)

    samples = generate_samples(samples_dir)
    outputs_dir.mkdir(parents=True, exist_ok=True)

    failures: list[str] = []
    results: list[dict[str, str]] = []

    try:
        for sample_name, input_path in samples.items():
            result = convert_one(project_root, sample_name, input_path, outputs_dir)
            results.append(result)

            expected = EXPECTED_STATUSES[sample_name]
            actual = result.get("status", "ERROR")
            markdown_exists = result.get("markdown_exists") == "True"

            if result.get("returncode") != "0":
                failures.append(f"{sample_name}: converter exit code was {result.get('returncode')}")
            elif actual != expected:
                failures.append(f"{sample_name}: expected {expected}, got {actual}")
            elif expected == "PASS" and not markdown_exists:
                failures.append(f"{sample_name}: PASS result did not create Markdown output")
        overall_status = "PASS" if not failures else "FAIL"
        write_report(report_path, results, overall_status)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
