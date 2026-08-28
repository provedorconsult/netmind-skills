# Persistent Docker Log Rotation — implementation plan

## G01–G02: reconciliation and current state

Trace PR #41 → confirmed JSON-log cause → PR #43 emergency mitigation →
`LIVE-001 = MITIGATED`. Read Docker version/root/storage/log drivers,
per-container options, `daemon.json` existence and JSON validity, aggregate and
largest logs, and Swarm/Dokploy lifecycle. Sanitize identities.

## G03–G04: policy and daemon configuration

Parameterize `max-size` and `max-file` from approved capacity, traffic/growth,
retention and diagnostic needs; expected allocation is eligible containers ×
max-size × max-file. Procedure: `READ → BACKUP → PARSE → VALIDATE → MERGE →
REVIEW → APPLY → VALIDATE`. Preserve unrelated JSON. **PRODUCTION
AUTHORIZATION REQUIRED** for daemon change or restart.

## G05–G06: existing, new, Swarm and Dokploy

Daemon defaults do not prove changes for existing containers/tasks. Per
workload: discover driver/options, image, volumes, ports, networks, health,
dependencies, owner, rolling-update/recreation need, downtime, rollback and
validation. Flow: `DISCOVER → CLASSIFY → SELECT → AUTHORIZE → RECREATE/UPDATE
→ VALIDATE`. New-container rotation requires a controlled non-production test.
Discover Dokploy behavior read-only; do not assume it preserves daemon policy.

## G07–G09: validation, monitoring and rollback

Compare before/after disk/inodes, daemon, drivers/options, Docker/Swarm,
Dokploy, proxy, database and authorized endpoints. Monitor root/inodes,
aggregate/largest JSON logs, growth and missing rotation using parameterized
Warning/Critical/Emergency thresholds. Rollback: `BACKUP → CHANGE → VALIDATE →
FAILURE → RESTORE → VALIDATE`; daemon rollback does not restore existing tasks.

## G10: Skills and standard runbook

Use the chain `dokploy-storage-diagnose` → `dokploy-disk-emergency-diagnose` →
`dokploy-docker-log-rotation` → monitoring → validation. See `RUNBOOK.md`.

## Tests and acceptance

Version/root/driver/daemon absent-or-existing/JSON/merge/policy/Skill/Harness/
CI are static/read-only. New-container rotation, existing behavior, Swarm,
Dokploy, controlled rotation, disk, thresholds and rollback are `BLOCKED`
until controlled environment or explicit production authorization.
