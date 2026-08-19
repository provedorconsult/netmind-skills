#!/usr/bin/env python3
"""Block a PR before Checker review when its Goal contract is incomplete or stale."""
import argparse
import json
from pathlib import Path

REQUIRED = ("scope", "outOfScope", "evidenceRequired", "acceptanceCriteria", "negativeCases", "regressionTests", "securityConstraints", "expectedArtifacts")
def read(path): return json.loads(Path(path).read_text(encoding="utf-8"))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--goal", required=True); parser.add_argument("--evidence", required=True)
    parser.add_argument("--main-sha", required=True); parser.add_argument("--branch", required=True); parser.add_argument("--changed-file", action="append", default=[])
    args = parser.parse_args()
    try: goal, pr = read(args.goal), read(args.evidence)
    except (OSError, json.JSONDecodeError) as exc: print(f"PREFLIGHT BLOCKED: cannot read input: {exc}"); return 1
    errors = [f"Goal contract missing {field}" for field in REQUIRED if not goal.get(field)]
    if goal.get("status") != "READY": errors.append("Goal is not READY")
    if goal.get("predecessor") and not goal.get("predecessorMerged"): errors.append("predecessor is not confirmed merged")
    if pr.get("state") != "OPEN" or pr.get("isDraft") is not False: errors.append("PR must be open and non-draft")
    if pr.get("headRefName") != args.branch: errors.append("PR branch does not match declared branch")
    if not pr.get("headRefOid"): errors.append("PR HEAD is missing")
    if pr.get("baseRefOid") != args.main_sha: errors.append("PR base is STALE")
    checks = pr.get("statusCheckRollup", [])
    if not checks: errors.append("CI evidence is absent")
    elif any(check.get("status") != "COMPLETED" or check.get("conclusion") != "SUCCESS" for check in checks): errors.append("CI is not green")
    allowed = set(goal.get("scope", [])) | set(goal.get("expectedArtifacts", []))
    outside = [name for name in args.changed_file if allowed and name not in allowed]
    if outside: errors.append("changed files outside contract scope: " + ", ".join(outside))
    test_map = goal.get("acceptanceTestMap", {})
    if set(goal.get("acceptanceCriteria", [])) - set(test_map): errors.append("acceptance criteria are UNTESTED")
    for path in test_map.values():
        if not Path(path).is_file(): errors.append(f"mapped test is missing: {path}")
    for path in goal.get("evidenceRequired", []):
        if "/" in path and not Path(path).exists(): errors.append(f"required evidence is missing: {path}")
    if errors:
        print("\n".join(f"PREFLIGHT BLOCKED: {error}" for error in errors)); return 1
    print("PREFLIGHT PASS"); return 0
if __name__ == "__main__": raise SystemExit(main())
