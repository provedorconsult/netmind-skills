# G18 — PPPoE credential operational knowledge

## Predecessor

`G17`

## Recorded delivery

PR #35 contains the operational PPPoE credential knowledge change. This goal
record exists to make the already-open delivery traceable in the Harness; it
does not modify that PR's technical scope or content.

## Acceptance Contract

### Scope

The delivery is limited to these five files in PR #35:

- `ACCESS-GUARDRAILS.md`;
- `scripts/validate_operational_safety.py`;
- `skills/13-ma5800-pppoe-access/SKILL.md`;
- `skills/cisco-asr1001x/24-pppoe-troubleshooting/SKILL.md`;
- `tests/test_pppoe_credential_operational_knowledge.py`.

It documents safe diagnostic handling of a PPPoE credential. It does not
authorize device changes, credential retrieval, credential generation or the
storage of a real secret.

### Acceptance criteria

1. The access guardrails define the PPPoE password as an operational
   credential supplied only by the authorized Source of Truth, and offer only
   a sanitized availability marker as evidence.
2. The MA5800 and ASR1001-X procedures record a missing credential as
   `UNKNOWN`; when an authorized source makes it available, they record only
   its availability as `CONFIRMADO` and never the value.
3. The documentation states that possession of the credential does not grant
   `WRITE`, `PERSIST` or `HIGH-IMPACT` authority.
4. The operational-safety validator and the dedicated contract test map to
   the guardrail and procedure wording, so removal of a required safety rule
   fails the corresponding automated check.
5. No real credential, customer data, endpoint, topology or device-specific
   secret is introduced by the five-file diff.

### Evidence and test map

- Criteria 1 and 3 map to
  `scripts/validate_operational_safety.py::validate_pppoe_credential_guardrails`
  and the guardrail section in `ACCESS-GUARDRAILS.md`.
- Criteria 2 and 4 map to
  `tests/test_pppoe_credential_operational_knowledge.py` and the two named
  PPPoE procedure sections.
- Criterion 5 maps to the PR #35 five-file scope check and Checker review of
  the diff.
- The dynamic checks are to run in GitHub CI or the authorized VPS. They are
  not executed locally under `AGENTS.md`.

### Negative cases

- No supplied password: record the diagnostic limitation as `UNKNOWN`; do not
  infer, search for or generate a password.
- Supplied password: use it only in the authorized task context and emit only
  the sanitized availability marker.
- Any request to change OLT, AAA, BNG or BRAS: remain blocked without the
  separately authorized operational class and its guardrails.

### Required merge evidence

The Checker must confirm a current open PR, exact reviewed HEAD, green CI for
that HEAD, the full acceptance contract above, and a literal verdict permitted
by `checker.json`. The Maker must not merge without `MERGE_AUTHORIZED`.

## Current state

`BLOCKED` — PR #35 is open, but the independent Checker published `blocked`.
The formal catalog and Acceptance Contract are being supplied by PR #37; until
that PR is merged with authorization, G18 is not a current goal in `main` and
cannot receive `MERGE_AUTHORIZED`.
