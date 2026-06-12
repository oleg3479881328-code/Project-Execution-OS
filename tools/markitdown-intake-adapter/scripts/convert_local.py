from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

os.environ["PYTHON_DOTENV_DISABLED"] = "1"

from markitdown import MarkItDown

DEFAULT_MAX_BYTES = 50 * 1024 * 1024
MEANINGFUL_TEXT_MIN_CHARS = 20
URL_LIKE_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
WINDOWS_DRIVE_PATTERN = re.compile(r"^[a-zA-Z]:[\\/]")


def is_windows_non_local_path(path_text: str) -> bool:
    return path_text.startswith("\\\\") or path_text.startswith("//")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert one approved local document to Markdown using MarkItDown convert_local()."
    )
    parser.add_argument("--input", required=True, help="Path to an existing local file.")
    parser.add_argument("--output", required=True, help="Path to the Markdown output file.")
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_BYTES,
        help=f"Maximum allowed input size in bytes. Default: {DEFAULT_MAX_BYTES}.",
    )
    return parser


def error_result(message: str, input_path: Path, output_path: Path, exit_code: int = 1) -> int:
    payload = {
        "status": "ERROR",
        "message": message,
        "input_path": str(input_path),
        "output_path": str(output_path),
    }
    print(json.dumps(payload, ensure_ascii=True))
    return exit_code


def normalize_text(markdown: str) -> str:
    return re.sub(r"\s+", " ", markdown).strip()


def has_meaningful_text(markdown: str) -> bool:
    normalized = normalize_text(markdown)
    if len(normalized) < MEANINGFUL_TEXT_MIN_CHARS:
        return False

    alnum_count = sum(char.isalnum() for char in normalized)
    return alnum_count >= MEANINGFUL_TEXT_MIN_CHARS


def main() -> int:
    args = build_parser().parse_args()
    input_path = Path(args.input).expanduser()
    output_path = Path(args.output).expanduser()

    input_text = str(input_path)
    if URL_LIKE_PATTERN.match(input_text) and not WINDOWS_DRIVE_PATTERN.match(input_text):
        return error_result("URL-like inputs are not allowed. Local files only.", input_path, output_path)
    if is_windows_non_local_path(input_text):
        return error_result(
            "Windows network-share and device-namespace paths are not allowed. Local files only.",
            input_path,
            output_path,
        )

    try:
        resolved_input = input_path.resolve(strict=True)
    except FileNotFoundError:
        return error_result("Input file was not found.", input_path, output_path)

    if not resolved_input.is_file():
        return error_result("Input path must point to a file.", resolved_input, output_path)

    file_size = resolved_input.stat().st_size
    if file_size > args.max_bytes:
        return error_result(
            f"Input file exceeds the configured size limit ({file_size} > {args.max_bytes} bytes).",
            resolved_input,
            output_path,
        )

    resolved_output = output_path.resolve(strict=False)
    resolved_output.parent.mkdir(parents=True, exist_ok=True)

    converter = MarkItDown(enable_plugins=False)

    try:
        result = converter.convert_local(str(resolved_input))
        markdown = result.text_content or ""
    except Exception as exc:  # pragma: no cover - validation goes through runtime behavior
        return error_result(f"Conversion failed: {exc}", resolved_input, resolved_output)

    normalized = normalize_text(markdown)
    status = "PASS"
    message = "Conversion succeeded."
    if resolved_input.suffix.lower() == ".pdf" and not has_meaningful_text(markdown):
        status = "NEEDS_OCR"
        message = "PDF conversion produced no meaningful text and likely needs OCR."

    if status == "PASS" and not normalized:
        return error_result("Conversion produced empty Markdown.", resolved_input, resolved_output)

    resolved_output.write_text(markdown, encoding="utf-8")
    payload = {
        "status": status,
        "message": message,
        "input_path": str(resolved_input),
        "output_path": str(resolved_output),
        "bytes": file_size,
        "characters": len(normalized),
    }
    print(json.dumps(payload, ensure_ascii=True))
    return 0 if status in {"PASS", "NEEDS_OCR"} else 1


if __name__ == "__main__":
    sys.exit(main())
