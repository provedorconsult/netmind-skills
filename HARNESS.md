# NetMind Goal Harness

The Git-native harness coordinates the existing G01–G10 catalog; it does not execute a goal merely because the catalog exists. Its source files are under [`.harness/`](.harness/).

## Lifecycle

`discover → isolate → maker → verify → open PR → checker → approval gate → merge → post-merge → next goal`

The Maker works on only the active catalog goal and never merges. The automated Checker reviews the GitHub pull request and publishes exactly one verdict: `approve`, `request-changes`, or `blocked`.

Only a complete, case-sensitive PR comment `approve` by the configured Checker login, with an open PR and green CI, authorizes merging. The merge gate queries GitHub directly; `current.json` cannot authorize a merge by itself.

`request-changes` sends the goal back to `MAKER_RUNNING`. `blocked` ends the active lifecycle. After GitHub confirms that the PR is merged into `main`, post-merge reconciliation marks the goal complete and makes only its sequential successor ready.

## Operation

Validate the repository definition:

```bash
bash scripts/harness-validate.sh
```

Evaluate a real pull request using the login of the automated Checker:

```bash
python3 scripts/harness-merge-gate.py --repo provedorconsult/netmind-skills --pr 123 --checker-login '<checker-login>'
```

The command denies authorization if GitHub cannot supply the PR evidence. The test fixtures are in `tests/harness/`; CI runs them with `bash scripts/test-harness-gates.sh`.

Each execution records the fields in [the evidence template](.harness/templates/evidence-template.md) and appends structured events to `.harness/state/iteration-log.jsonl`.
