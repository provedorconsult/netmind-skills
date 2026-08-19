#!/usr/bin/env python3
"""Validate the anti-inference evidence contract used by Harness artifacts."""
import argparse
import json
from pathlib import Path

STATUSES = {"OBSERVED", "CONFIRMED", "DERIVED", "UNKNOWN"}
def main():
    parser = argparse.ArgumentParser(); parser.add_argument("evidence")
    args = parser.parse_args()
    try: records = json.loads(Path(args.evidence).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc: print(f"EVIDENCE BLOCKED: cannot read evidence: {exc}"); return 1
    if not isinstance(records, list): records = [records]
    errors = []
    for index, record in enumerate(records):
        status = record.get("status")
        if status not in STATUSES: errors.append(f"record {index}: invalid status")
        if status == "UNKNOWN" and record.get("value") is not None: errors.append(f"record {index}: UNKNOWN must use null value")
        if status == "DERIVED" and record.get("technicalIdentity") is True: errors.append(f"record {index}: technical identity cannot be DERIVED")
        if status in {"OBSERVED", "CONFIRMED"} and not record.get("source"): errors.append(f"record {index}: source is required")
    if errors: print("\n".join("EVIDENCE BLOCKED: " + error for error in errors)); return 1
    print("EVIDENCE PASS"); return 0
if __name__ == "__main__": raise SystemExit(main())
