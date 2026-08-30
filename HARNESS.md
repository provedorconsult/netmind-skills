# NetMind Goal Harness

The Git-native harness coordinates the existing G01–G10 catalog; it does not execute a goal merely because the catalog exists. Its source files are under [`.harness/`](.harness/).

## Lifecycle

`discover → isolate → maker → verify → open PR → checker → approval gate → maker merge → post-merge → next goal`

The Maker works on only the active catalog goal, opens or updates its pull request, obtains CI, and hands the PR to the automated Checker. The Checker reviews the GitHub pull request and publishes exactly one verdict: `approve`, `request-changes`, or `blocked`.

Only a complete, case-sensitive PR comment `approve` by the configured Checker login authorizes merging. The gate accepts it only when the PR is open, non-Draft and cleanly mergeable; its HEAD SHA is known; CI is green for the queried PR HEAD; the latest Checker verdict is `approve`; and the same Checker has a native GitHub `APPROVED` review whose commit OID equals the current HEAD. The literal comment must not predate that native review. A new commit therefore invalidates a prior approval and requires re-review. The merge gate queries GitHub directly; `current.json` cannot authorize a merge by itself.

`approve` changes the lifecycle to `MERGE_AUTHORIZED`; it does not perform the merge. The Maker is the merge executor and may merge only after the merge gate confirms `MERGE_AUTHORIZED`. The Checker never merges. Immediately before merging, the Maker must re-check the real PR state; the PR must remain open and mergeable, CI must still be green, and the reviewed HEAD must not have changed.

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

## Estado sequencial e reconciliações retrospectivas

`completedGoal` e `completedGoals` em `.harness/state/current.json` representam
somente a sequência que pode promover o próximo Goal. Uma reconciliação já
integrada, mas que não avança essa sequência, deve ter `sequenceRole` igual a
`RETROSPECTIVE` no catálogo e espelhar sua evidência de merge em
`retrospectiveCompletedGoals` no estado corrente. Ela não pode alterar
`completedGoal`, `activeGoal` ou `nextGoal`.

G18 é o último Goal sequencial concluído (`SEQUENTIAL`). G19 é uma
reconciliação retrospectiva de predecessor G17 e, embora concluída, não
promove sucessor. `bash scripts/harness-validate.sh` e
`python3 scripts/harness-state-fixtures.py` verificam essa regra.
