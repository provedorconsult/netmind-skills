#!/usr/bin/env python3
"""Authorize a NetMind merge only from current, complete GitHub PR evidence."""

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

VERDICTS = {"approve", "request-changes", "blocked"}

def deny(reason):
    print(f"MERGE DENIED: {reason}")
    return 1

def load_evidence(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read GitHub evidence: {exc}") from exc

def github_evidence(repo, pr):
    command = ["gh", "pr", "view", str(pr), "--repo", repo, "--json", "state,isDraft,mergeStateStatus,headRefOid,commits,statusCheckRollup,comments"]
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return json.loads(result.stdout)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        raise ValueError("unable to query complete GitHub PR evidence with gh") from exc

def parse_time(value):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc) if value else None
    except ValueError:
        return None

def head_commit_time(evidence):
    for commit in evidence.get("commits", []):
        if commit.get("oid") == evidence.get("headRefOid"):
            return parse_time(commit.get("committedDate"))
    return None

def ci_green(checks):
    return bool(checks) and all(check.get("status") == "COMPLETED" and check.get("conclusion") == "SUCCESS" for check in checks)

def evaluate(evidence, checker_login):
    if evidence.get("state") != "OPEN": return deny("PR is not open")
    if evidence.get("isDraft") is not False: return deny("PR is draft or draft state is unknown")
    if evidence.get("mergeStateStatus") != "CLEAN": return deny("PR merge state is not CLEAN")
    if not evidence.get("headRefOid"): return deny("PR HEAD is unknown")
    head_time = head_commit_time(evidence)
    if head_time is None: return deny("HEAD commit or its timestamp is unknown")
    if not ci_green(evidence.get("statusCheckRollup", [])): return deny("CI is not green for the queried HEAD")
    verdicts = [comment for comment in evidence.get("comments", []) if comment.get("author", {}).get("login") == checker_login and comment.get("body") in VERDICTS]
    if not verdicts: return deny("Checker has not published a literal verdict")
    earliest = datetime.min.replace(tzinfo=timezone.utc)
    latest = max(verdicts, key=lambda item: parse_time(item.get("createdAt")) or earliest)
    if latest.get("body") != "approve": return deny("latest Checker verdict is invalidating")
    if (parse_time(latest.get("createdAt")) or earliest) <= head_time: return deny("approve is not newer than the current HEAD")
    print("MERGE AUTHORIZED")
    return 0

def main():
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--evidence")
    source.add_argument("--repo")
    parser.add_argument("--pr", type=int)
    parser.add_argument("--checker-login", required=True)
    args = parser.parse_args()
    if args.repo and not args.pr: parser.error("--repo requires --pr")
    try:
        evidence = load_evidence(args.evidence) if args.evidence else github_evidence(args.repo, args.pr)
    except ValueError as exc:
        return deny(str(exc))
    return evaluate(evidence, args.checker_login)

if __name__ == "__main__": raise SystemExit(main())
