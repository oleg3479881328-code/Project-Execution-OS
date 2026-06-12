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

EXPECTED_REJECTIONS = {
    "reject_url_python": {
        "input": "https://example.com/test.pdf",
        "expected_status": "ERROR",
        "message_fragment": "URL-like inputs are not allowed",
    },
    "reject_unc_python": {
        "input": r"\\server\share\test.pdf",
        "expected_status": "ERROR",
        "message_fragment": "Windows network-share and device-namespace paths are not allowed",
    },
    "reject_device_python": {
        "input": r"\\?\C:\temp\test.pdf",
        "expected_status": "ERROR",
        "message_fragment": "Windows network-share and device-namespace paths are not allowed",
    },
    "reject_url_powershell": {
        "input": "https://example.com/test.pdf",
        "message_fragment": "URL-like inputs are not allowed",
    },
    "reject_unc_powershell": {
        "input": r"\\server\share\test.pdf",
        "message_fragment": "Windows network-share and device-namespace paths are not allowed",
    },
    "reject_device_powershell": {
        "input": r"\\?\C:\temp\test.pdf",
        "message_fragment": "Windows network-share and device-namespace paths are not allowed",
    },
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


def run_python_rejection_check(project_root: Path, check_name: str, output_dir: Path) -> dict[str, str]:
    script_path = project_root / "scripts" / "convert_local.py"
    output_path = output_dir / f"{check_name}.md"
    check = EXPECTED_REJECTIONS[check_name]
    completed = subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--input",
            check["input"],
            "--output",
            str(output_path),
        ],
        check=False,
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    stdout = completed.stdout.strip()
    payload = json.loads(stdout) if stdout else {}
    payload.update(
        {
            "sample": check_name,
            "returncode": str(completed.returncode),
            "stderr": completed.stderr.strip(),
            "message_fragment": check["message_fragment"],
            "markdown_exists": str(output_path.exists()),
            "output_path": str(output_path),
            "kind": "python-rejection",
        }
    )
    return payload


def run_powershell_rejection_check(project_root: Path, check_name: str, output_dir: Path) -> dict[str, str]:
    script_path = project_root / "convert-file.ps1"
    output_path = output_dir / f"{check_name}.md"
    check = EXPECTED_REJECTIONS[check_name]
    completed = subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script_path),
            "-InputFile",
            check["input"],
            "-OutputFile",
            str(output_path),
        ],
        check=False,
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    combined_output = "\n".join(part for part in [completed.stdout.strip(), completed.stderr.strip()] if part).strip()
    return {
        "sample": check_name,
        "status": "ERROR" if completed.returncode != 0 else "PASS",
        "returncode": str(completed.returncode),
        "stderr": combined_output,
        "message_fragment": check["message_fragment"],
        "markdown_exists": str(output_path.exists()),
        "output_path": str(output_path),
        "kind": "powershell-rejection",
    }


def write_report(
    report_path: Path,
    results: list[dict[str, str]],
    rejection_results: list[dict[str, str]],
    overall_status: str,
) -> None:
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

    lines.extend(
        [
            "",
            "## Rejection Checks",
            "",
            "| Check | Layer | Expected | Actual | Return Code | Result |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    for result in rejection_results:
        check_name = result["sample"]
        actual = result.get("status", "ERROR")
        returncode = result.get("returncode", "1")
        kind = result.get("kind", "rejection")
        fragment = result.get("message_fragment", "")
        output_text = result.get("stderr", "") or result.get("message", "")
        outcome = "PASS" if fragment in output_text else "FAIL"
        lines.append(f"| {check_name} | {kind} | ERROR | {actual} | {returncode} | {outcome} |")

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
    rejection_results: list[dict[str, str]] = []

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

        for check_name in ["reject_url_python", "reject_unc_python", "reject_device_python"]:
            result = run_python_rejection_check(project_root, check_name, outputs_dir)
            rejection_results.append(result)
            if result.get("returncode") == "0":
                failures.append(f"{check_name}: expected non-zero exit code for Python rejection check")
            if result.get("status") != EXPECTED_REJECTIONS[check_name]["expected_status"]:
                failures.append(f"{check_name}: expected ERROR status")
            combined_output = (result.get("stderr", "") + "\n" + result.get("message", "")).strip()
            if EXPECTED_REJECTIONS[check_name]["message_fragment"] not in combined_output:
                failures.append(f"{check_name}: expected rejection message fragment was missing")

        for check_name in ["reject_url_powershell", "reject_unc_powershell", "reject_device_powershell"]:
            result = run_powershell_rejection_check(project_root, check_name, outputs_dir)
            rejection_results.append(result)
            if result.get("returncode") == "0":
                failures.append(f"{check_name}: expected non-zero exit code for PowerShell rejection check")
            if EXPECTED_REJECTIONS[check_name]["message_fragment"] not in result.get("stderr", ""):
                failures.append(f"{check_name}: expected rejection message fragment was missing")

        overall_status = "PASS" if not failures else "FAIL"
        write_report(report_path, results, rejection_results, overall_status)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
