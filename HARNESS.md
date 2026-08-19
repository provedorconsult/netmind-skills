# NetMind Goal Harness

The Git-native harness coordinates the existing G01–G10 catalog; it does not execute a goal merely because the catalog exists. Its source files are under [`.harness/`](.harness/).

## Lifecycle

`goal ready → acceptance contract → test matrix → maker → preflight → CI → checker → approval gate → merge → auto reconcile → done`

The Maker works on only the active catalog goal and never merges. The automated Checker reviews the GitHub pull request and publishes exactly one verdict: `approve`, `request-changes`, or `blocked`.

Only a complete, case-sensitive PR comment `approve` by the configured Checker login authorizes merging when it is newer than the current PR HEAD. The PR must be open, non-Draft, `CLEAN`, have a known HEAD commit and green CI for that query. A later `request-changes` or `blocked` invalidates the approval. The merge gate queries GitHub directly; `current.json` cannot authorize a merge by itself.

Every new Goal starts with the Acceptance Contract in `.harness/templates/goal-template.json`: scope, exclusions, required evidence, acceptance criteria, negative cases, regressions, security constraints and artifacts. Every criterion maps to a test; otherwise it is `UNTESTED` and the Goal cannot proceed. Evidence is explicitly classified as `OBSERVED`, `CONFIRMED`, `DERIVED` or `UNKNOWN`.

`request-changes` sends the goal back to `MAKER_RUNNING`. `blocked` ends the active lifecycle. After GitHub confirms that the PR is merged into `main`, post-merge reconciliation updates only the verified projection; it never creates or promotes a Goal.

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

Run preflight before requesting Checker:

```bash
python3 scripts/harness-pr-preflight.py --goal <contract.json> --evidence <pr-evidence.json> --main-sha <main-sha> --branch <branch>
```

`current.json`, sprint and iteration information are projections. `python3 scripts/harness-project-state.py --check` reports `HARNESS DRIFT` when a projection diverges from the catalog merge facts.

Each execution records the fields in [the evidence template](.harness/templates/evidence-template.md) and appends structured events to `.harness/state/iteration-log.jsonl`.
