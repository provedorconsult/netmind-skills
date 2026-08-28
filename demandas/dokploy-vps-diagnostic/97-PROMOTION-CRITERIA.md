# Promotion criteria — Dokploy VPS Forensic Diagnostic

## Required before promotion

- Root cause is sufficiently classified with evidence, or the remaining
  uncertainty and next observation are explicit.
- LIVE-001 is updated from forensic evidence.
- Remediation and post-remediation validation plans exist.
- Test matrix and acceptance contract are evaluated with evidence.
- Skill gaps and retrofit proposal are traceable to confirmed findings.
- `git diff --check` and applicable CI pass.
- No destructive action is presented as performed or implied by diagnosis.

## States

`NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `READY_FOR_REVIEW`, `APPROVED`, and
`DONE`. Only the Checker can authorize integration under the existing Harness;
CI does not authorize merge.

## Relationship to source demand

```text
Dokploy VPS Forensic Diagnostic ── evidence feedback ──> Dokploy Skills
```

This demand does not replace or duplicate the source demand's homologation.
