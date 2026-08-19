#!/usr/bin/env python3
"""Derive and verify Harness projections from catalog merge facts."""
import argparse
import json
from pathlib import Path
def canonical(goal): return {key: value for key, value in goal.items() if key != "file"}
def derive(catalog):
    completed = [canonical(goal) for goal in catalog.get("completedGoals", [])]
    active = catalog.get("activeGoal")
    return {"goal": active, "status": "COMPLETE" if active is None else "READY", "completedGoal": completed[-1]["id"] if completed else None, "nextGoal": None, "completedGoals": completed}
def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--catalog", default=".harness/sprints/current.json"); parser.add_argument("--current", default=".harness/state/current.json"); parser.add_argument("--check", action="store_true"); parser.add_argument("--write", action="store_true")
    args = parser.parse_args(); expected = derive(json.loads(Path(args.catalog).read_text(encoding="utf-8")))
    current_path = Path(args.current)
    if args.write:
        current = json.loads(current_path.read_text(encoding="utf-8")); current.update(expected)
        current_path.write_text(json.dumps(current, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("HARNESS PROJECTION UPDATED"); return 0
    if not args.check: print(json.dumps(expected, indent=2, ensure_ascii=False)); return 0
    current = json.loads(current_path.read_text(encoding="utf-8")); mismatch = [key for key, value in expected.items() if current.get(key) != value]
    if mismatch: print("HARNESS DRIFT: " + ", ".join(mismatch)); return 1
    print("HARNESS STATE PASS"); return 0
if __name__ == "__main__": raise SystemExit(main())
