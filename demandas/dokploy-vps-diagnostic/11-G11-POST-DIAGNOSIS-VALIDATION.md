# DOKPLOY-VPS-G11 — Post-diagnosis validation

## Goal

Define objective validation for a separately authorized remediation.

## Checks

Recheck filesystem free space/inodes, Docker/Swarm/Dokploy component health,
PostgreSQL readiness, approved application health endpoints, log pressure, and
deployment state. Compare against the G01 baseline and root-cause prediction.

## Result

Each check is `PASS`, `FAIL`, or `BLOCKED`. A capacity increase alone does not
pass if persistence, application health, or recovery guarantees regress.
