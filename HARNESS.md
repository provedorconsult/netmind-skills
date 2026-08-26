# NetMind Goal Harness

The Git-native harness coordinates the existing G01–G10 catalog; it does not execute a goal merely because the catalog exists. Its source files are under [`.harness/`](.harness/).

## Lifecycle

`discover → isolate → maker → verify → open PR → checker → approval gate → maker merge → post-merge → next goal`

The Maker works on only the active catalog goal, opens or updates its pull request, obtains CI, and hands the PR to the automated Checker. The Checker reviews the real GitHub pull request and publishes exactly one verdict: `approve`, `request-changes`, or `blocked`.

Only a complete, case-sensitive PR comment `approve` by the configured Checker login, with an open PR and green CI, authorizes merging. The merge gate queries GitHub directly; `current.json` cannot authorize a merge by itself.

`approve` changes the lifecycle to `MERGE_AUTHORIZED`; it does not perform the merge. The **Maker is the merge executor** and may merge only after the merge gate confirms `MERGE_AUTHORIZED`. The Checker never merges.

Immediately before merging, the Maker must re-check the real GitHub PR state: the PR must remain open and mergeable, CI must still be green, and the reviewed HEAD must not have changed. A new commit after review invalidates the previous merge authorization and requires a new Checker review. The Maker must not self-approve, bypass CI, ignore `request-changes` or `blocked`, or preserve stale approval through force-push.

`request-changes` sends the goal back to `MAKER_RUNNING`. `blocked` ends the active lifecycle. After the Maker merges and GitHub confirms that the PR is merged into `main`, post-merge reconciliation marks the goal complete and makes only its sequential successor ready.

## Operation

Validate the repository definition:

```bash
bash scripts/harness-validate.sh
```

Evaluate a real pull request using the login of the automated Checker:

```bash
python3 scripts/harness-merge-gate.py --repo provedorconsult/netmind-skills --pr 123 --checker-login '<checker-login>'
```

The command denies authorization if GitHub cannot supply the PR evidence. When it returns `MERGE AUTHORIZED`, the Maker may execute the merge for that reviewed PR state. The test fixtures are in `tests/harness/`; CI runs them with `bash scripts/test-harness-gates.sh`.

Each execution records the fields in [the evidence template](.harness/templates/evidence-template.md) and appends structured events to `.harness/state/iteration-log.jsonl`.
