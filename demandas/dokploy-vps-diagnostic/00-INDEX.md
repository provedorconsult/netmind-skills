# Demanda — Dokploy VPS Forensic Diagnostic

## Objective

Determine, through bounded and sanitized read-only evidence, the cause of
`LIVE-001` — root filesystem exhaustion on the authorized Dokploy VPS — and
feed proven gaps back into the Dokploy operational Skills.

## Source and boundary

Source: Dokploy Self-Hosted / Debian 12, implementation PR #39, observed head
`926002e`. Reuse its live audit, issue register, acceptance status, and
diagnostic Skills. This is independent from Dokploy homologation and does not
execute cleanup, remediation, restart, deployment, upgrade, or rollback.

## Lifecycle

`DOKPLOY-VPS-G01 → G02 → G03 → G04 → G05 → G06 → G07 → G08 → G09 → G10 → G11 → G12`

The labels are namespaced to avoid collision with the existing Harness G IDs.
Each future Goal requires its own Maker execution, evidence, CI, and Checker
review; this demand itself is planning only.

## Safety rule

`READ_ONLY → evidence → diagnosis → risk classification → explicit
authorization → action → validation`. A timeout is evidence of a collection
limit, never proof of a storage cause. `DIAGNOSIS ≠ REMEDIATION`.

## Initial known evidence

- Root filesystem was approximately 79 GiB and at 100% usage with no free MiB.
- Inodes were approximately 10% used.
- Bounded Docker aggregate and journal aggregate were inconclusive.
- No cleanup was performed; root cause is `UNKNOWN`.

See the source demand's `evidence/G03-LIVE-AUDIT.md` and
`evidence/LIVE-ISSUES.md` for the sanitized basis.
