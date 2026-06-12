# MarkItDown Intake Adapter Smoke Test

Timestamp: 2026-06-12T12:38:27+00:00
Overall-Status: PASS

| Sample | Expected | Actual | Return Code | Output |
| --- | --- | --- | --- | --- |
| pdf_text | PASS | PASS | 0 | pdf_text.md |
| pdf_scan | NEEDS_OCR | NEEDS_OCR | 0 | pdf_scan.md |
| docx | PASS | PASS | 0 | docx.md |
| pptx | PASS | PASS | 0 | pptx.md |
| xlsx | PASS | PASS | 0 | xlsx.md |
| html | PASS | PASS | 0 | html.md |
| csv | PASS | PASS | 0 | csv.md |
| zip | PASS | PASS | 0 | zip.md |

## Rejection Checks

| Check | Layer | Expected | Actual | Return Code | Result |
| --- | --- | --- | --- | --- | --- |
| reject_url_python | python-rejection | ERROR | ERROR | 1 | PASS |
| reject_unc_python | python-rejection | ERROR | ERROR | 1 | PASS |
| reject_device_python | python-rejection | ERROR | ERROR | 1 | PASS |
| reject_url_powershell | powershell-rejection | ERROR | ERROR | 1 | PASS |
| reject_unc_powershell | powershell-rejection | ERROR | ERROR | 1 | PASS |
| reject_device_powershell | powershell-rejection | ERROR | ERROR | 1 | PASS |
