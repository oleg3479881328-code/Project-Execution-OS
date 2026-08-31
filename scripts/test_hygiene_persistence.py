#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDITOR = ROOT / "scripts" / "audit_system_hygiene.py"

spec = importlib.util.spec_from_file_location("audit_system_hygiene", AUDITOR)
if spec is None or spec.loader is None:
    raise RuntimeError("Unable to load audit_system_hygiene.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

warning = "test-warning:fixed"

history_two = [
    {"warning_ids": [warning]},
    {"warning_ids": [warning]},
]
counts = module.consecutive_occurrences(history_two, {warning})
assert counts[warning] == 3, counts
assert counts[warning] >= module.PERSISTENCE_THRESHOLD

history_broken = [
    {"warning_ids": [warning]},
    {"warning_ids": []},
    {"warning_ids": [warning]},
]
counts = module.consecutive_occurrences(history_broken, {warning})
assert counts[warning] == 2, counts
assert counts[warning] < module.PERSISTENCE_THRESHOLD

history_four = [
    {"warning_ids": [warning]},
    {"warning_ids": [warning]},
    {"warning_ids": [warning]},
]
counts = module.consecutive_occurrences(history_four, {warning})
assert counts[warning] == 4, counts
assert counts[warning] >= module.PERSISTENCE_THRESHOLD

print("Hygiene persistence escalation test passed.")
print("Verified: two prior consecutive occurrences + current occurrence = ACTION_REQUIRED threshold (3).")
print("Verified: a gap resets the consecutive sequence.")
