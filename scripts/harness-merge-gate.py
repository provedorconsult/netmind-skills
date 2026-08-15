#!/usr/bin/env python3
"""Authorize a NetMind merge only from GitHub PR evidence."""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def deny(reason):
    print(f"MERGE DENIED: {reason}")
    return 1


def load_evidence(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read GitHub evidence: {exc}") from exc


def github_evidence(repo, pr):
    command = ["gh", "pr", "view", str(pr), "--repo", repo, "--json", "state,mergeStateStatus,statusCheckRollup,comments"]
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("unable to query GitHub PR evidence with gh") from exc
    return json.loads(result.stdout)


def ci_green(checks):
    return bool(checks) and all(
        check.get("status") == "COMPLETED" and check.get("conclusion") == "SUCCESS"
        for check in checks
    )


def is_checker_comment(comment, checker_login):
    author = comment.get("author", {})
    return author.get("login") == checker_login


def evaluate(evidence, checker_login):
    if evidence.get("state") != "OPEN":
        return deny("PR is not open")
    if not ci_green(evidence.get("statusCheckRollup", [])):
        return deny("CI is not green")
    comments = evidence.get("comments", [])
    if not any(is_checker_comment(comment, checker_login) for comment in comments):
        return deny("Checker has not executed")
    if not any(is_checker_comment(comment, checker_login) and comment.get("body") == "approve" for comment in comments):
        return deny("no exact Checker comment 'approve'")
    print("MERGE AUTHORIZED")
    return 0


def main():
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--evidence", help="saved JSON from GitHub PR API")
    source.add_argument("--repo", help="GitHub owner/repository; requires --pr")
    parser.add_argument("--pr", type=int, help="GitHub pull request number")
    parser.add_argument("--checker-login", required=True, help="automated Checker's exact GitHub login")
    args = parser.parse_args()
    if args.repo and not args.pr:
        parser.error("--repo requires --pr")
    try:
        evidence = load_evidence(args.evidence) if args.evidence else github_evidence(args.repo, args.pr)
    except ValueError as exc:
        return deny(str(exc))
    return evaluate(evidence, args.checker_login)


if __name__ == "__main__":
    raise SystemExit(main())
