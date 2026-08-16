#!/usr/bin/env python3
"""Generate the mandatory concise execution prompt from Checker to Maker."""

import argparse


VERDICTS = {"approve", "request-changes", "blocked"}


def build_prompt(goal, pr, head, verdict, details=""):
    if verdict == "approve":
        action = "No further implementation changes. Hand off the PR to the authorized merge operator; after GitHub confirms the merge, run post-merge validation."
    elif verdict == "request-changes":
        action = "Apply the requested corrections below, re-run validation, push the new HEAD, and request Checker review again."
    else:
        action = "Stop work on the PR and resolve the blocker below before resubmitting it to the Checker."

    lines = [
        "MAKER EXECUTION PROMPT",
        f"Goal: {goal}",
        f"PR: #{pr}",
        f"HEAD: {head}",
        f"Verdict: {verdict}",
        f"Action: {action}",
    ]
    if verdict != "approve":
        if not details.strip():
            raise ValueError(f"--details is required for verdict '{verdict}'")
        lines.append(f"Details: {details.strip()}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate the mandatory concise Checker-to-Maker execution prompt.")
    parser.add_argument("--goal", required=True)
    parser.add_argument("--pr", required=True, type=int)
    parser.add_argument("--head", required=True)
    parser.add_argument("--verdict", required=True, choices=sorted(VERDICTS))
    parser.add_argument("--details", default="")
    args = parser.parse_args()
    print(build_prompt(args.goal, args.pr, args.head, args.verdict, args.details))


if __name__ == "__main__":
    main()
