#!/usr/bin/env python3
"""Authorize a NetMind merge only from GitHub PR evidence."""

import argparse
import json
import subprocess
import sys
from datetime import datetime
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
    command = [
        "gh", "pr", "view", str(pr), "--repo", repo, "--json",
        "state,isDraft,headRefOid,mergeStateStatus,statusCheckRollup,comments,commits",
    ]
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


def parse_timestamp(value):
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def head_commit(evidence):
    head = evidence.get("headRefOid")
    if not isinstance(head, str) or not head:
        return None
    return next((commit for commit in evidence.get("commits", []) if commit.get("oid") == head), None)


def latest_checker_verdict(comments, checker_login):
    verdicts = [
        comment for comment in comments
        if is_checker_comment(comment, checker_login)
        and comment.get("body") in {"approve", "request-changes", "blocked"}
    ]
    if not verdicts:
        return None
    if any(parse_timestamp(comment.get("createdAt")) is None for comment in verdicts):
        return None
    return max(verdicts, key=lambda comment: parse_timestamp(comment["createdAt"]))


def evaluate(evidence, checker_login):
    if evidence.get("state") != "OPEN":
        return deny("PR is not open")
    if evidence.get("isDraft") is not False:
        return deny("PR is draft or draft status is unknown")
    if evidence.get("mergeStateStatus") != "CLEAN":
        return deny("PR is not mergeable without conflicts")
    current_head = head_commit(evidence)
    if current_head is None:
        return deny("current PR HEAD is unknown")
    head_timestamp = parse_timestamp(current_head.get("committedDate"))
    if head_timestamp is None:
        return deny("current PR HEAD timestamp is unknown")
    if not ci_green(evidence.get("statusCheckRollup", [])):
        return deny("CI is not green")
    comments = evidence.get("comments", [])
    if not any(is_checker_comment(comment, checker_login) for comment in comments):
        return deny("Checker has not executed")
    verdict = latest_checker_verdict(comments, checker_login)
    if verdict is None:
        return deny("Checker has no timestamped exact verdict")
    if verdict.get("body") != "approve":
        return deny(f"latest Checker verdict is {verdict.get('body')!r}")
    if parse_timestamp(verdict.get("createdAt")) <= head_timestamp:
        return deny("Checker approval predates current PR HEAD")
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
