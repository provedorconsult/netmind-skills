# DOKPLOY-VPS-G12 — Skill retrofit

## Goal

Compare confirmed forensic evidence with the Dokploy Skills from PR #39:
audit, instance, storage, Swarm, PostgreSQL, Traefik, deployment, Compose, and
domain diagnosis.

## Required mapping

For every confirmed gap record `EVIDENCE → PROBLEM → SKILL GAP → PROPOSED
CHANGE → VALIDATION`. Assess bounded hierarchy scans, Docker root inspection,
container-log metadata, deleted-open detection, journald storage, inode/mount
discrepancy, growth baselines, and timeout handling only when evidence supports
them.

## Potential new Skill

Consider `dokploy-disk-emergency-diagnose` only if LIVE-001 is recurrent or
current Skills demonstrably lack the needed safe path. It must output
`SAFE_DIAGNOSIS`, never automatic cleanup.
