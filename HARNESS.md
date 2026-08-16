# NetMind Goal Harness

The Git-native harness coordinates the existing G01–G10 catalog; it does not execute a goal merely because the catalog exists. Its source files are under [`.harness/`](.harness/).

## Lifecycle

`discover → isolate → maker → verify → open PR → checker → maker execution prompt → approval gate → merge → post-merge → next goal`

The Maker works on only the active catalog goal and never merges. The Checker reviews the GitHub pull request, publishes one concise execution prompt for the Maker, and publishes exactly one literal verdict: `approve`, `request-changes`, or `blocked`.

The Checker execution prompt is mandatory for every verdict. It must identify the Goal, PR, reviewed HEAD, verdict, and one direct next action. For `request-changes` or `blocked`, it must include the concrete correction or blocker. The prompt is operational guidance; it is not a merge authorization.

Only a complete, case-sensitive PR comment `approve` by the configured Checker login, with an open PR and green CI, authorizes merging. The merge gate queries GitHub directly; `current.json` cannot authorize a merge by itself. The `approve` comment must remain exactly `approve` so the social gate stays machine-verifiable.

`request-changes` sends the goal back to `MAKER_RUNNING`. `blocked` ends the active lifecycle. After GitHub confirms that the PR is merged into `main`, post-merge reconciliation marks the goal complete and makes only its sequential successor ready.

## Checker → Maker execution prompt

Generate the prompt deterministically with:

```bash
python3 scripts/harness-checker-prompt.py --goal G08 --pr 18 --head <sha> --verdict approve
```

For changes or a blocker, pass concise details:

```bash
python3 scripts/harness-checker-prompt.py --goal G08 --pr 18 --head <sha> --verdict request-changes --details 'Corrigir X; adicionar Y; repetir validação.'
```

The Checker should publish the generated prompt as a separate PR conversation comment, then publish the exact verdict as a second comment. Never append the prompt to `approve`.

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
