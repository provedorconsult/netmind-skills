# DOKPLOY acceptance and test-matrix status

| Contract | Status | Evidence |
|---|---|---|
| AC01 Discovery | PASS | `G01-GITHUB-DISCOVERY.md` documents scoped searches, classifications, sources, and gaps. |
| AC02 Forensics | PASS | `G02-FORENSICS.md` separates confirmed facts, references, legacy material, and unknowns. |
| AC03 Live Audit | PASS | `G03-LIVE-AUDIT.md` is sanitized, timestamped, and read-only. |
| AC04 Canonical Baseline | PASS | `CANONICAL-ARCHITECTURE.md` separates current, legacy/reference, and canonical contract. |
| AC05 Skills | PASS | Eleven Skills define purpose, scope, inputs/preconditions, procedure, decisions, evidence, failure/safety, validation, and output. |
| AC06 Installation | PASS | `dokploy-install-debian12` has reproducible gates; controlled install execution remains H02 BLOCKED. |
| AC07 Diagnosis | PASS | Layered diagnostic Skills are implemented without implicit change. |
| AC08 Recovery | BLOCKED | Procedure exists, but live backup inventory and controlled restore evidence are unavailable. |
| AC09 Golden Host | PASS | `GOLDEN-HOST-CHECKLIST.md` distinguishes tiers and readiness. |
| AC10 Runbook | PASS | `INCIDENT-RUNBOOK.md` covers INC-001 through INC-016. |
| AC11 Harness | PASS | `HARNESS-INTEGRATION.md` preserves existing Harness authority and goal-ID mapping. |
| AC12 Security | PASS | No secrets or raw operational identifiers were committed; destructive actions are gated. |
| AC13 Homologation | BLOCKED | Controlled host and approval have not been provided; test register records all results as BLOCKED. |

## Test Matrix result

Discovery, forensics, audit, static Skill structure, decision contracts, and
incident coverage are evidenced above. Install, deploy, DNS/TLS, backup,
restore, upgrade/rollback, and failure-injection execution remain `BLOCKED`;
they must not be marked PASS without a controlled host and evidence.

## Repository validation evidence

PR #39 CI passed both `Validate docs, indexes and links` and `Validate all
Skills` at the implementation HEAD on 2026-08-28. This supplies the complete
repository validator with its CI-pinned PyYAML dependency; local structural
checks and Harness validation also passed.

## Promotion result

**BLOCKED.** The documented capability is reviewable, but AC08 and AC13 lack
the mandatory controlled-environment recovery proof. `LIVE-001` also requires
explicit production-impact authorization before remediation.
