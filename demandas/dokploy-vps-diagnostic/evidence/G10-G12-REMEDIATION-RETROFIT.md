# DOKPLOY-VPS-G10–G12 — Remediation, validation, and Skill retrofit

## G10 — plan only; not executed

| Horizon | Action | Class | Preconditions / rollback / validation |
|---|---|---|---|
| Immediate | Identify the owning workload from approved operator context; preserve relevant log evidence before any size reduction. | HIGH_RISK | Explicit approval, retention owner, recovery/evidence decision; validate free space and workload health. |
| Short term | Apply an approved log-retention/rotation policy to the confirmed workload(s). | HIGH_RISK | Pre-change snapshot and rollback procedure; validate log continuity, disk capacity, Docker/Swarm/application health. |
| Long term | Establish capacity alerts and retained size baselines for JSON logs, volumes, and root filesystem. | LOW_RISK to MEDIUM_RISK | Monitoring owner and thresholds; validate alert delivery without generating excess logs. |
| Prevention | Configure platform-supported logging limits at deployment/runtime design time. | MEDIUM_RISK | Compatibility review; rollback to prior configuration; validate deployment and retention behavior. |

No `prune`, deletion, truncation, restart, or logging change was run.

## G11 — post-remediation validation contract

PASS requires: root free space above an approved threshold; inode use normal;
Docker and Swarm healthy; Dokploy/PostgreSQL/application health checks healthy;
log growth bounded; and no persistence/recovery regression. Otherwise FAIL or
BLOCKED.

## G12 — confirmed Skill gap and retrofit

**Evidence → gap:** LIVE-001 was caused by JSON log allocation, while the
existing storage Skill named bounded aggregates but lacked an explicit
hierarchical Docker-log path and deleted-open-file decision.

**Change:** `dokploy-storage-diagnose` now requires filesystem narrowing,
container-log metadata aggregation, `df`/`du` discrepancy handling,
deleted-open-file check, timeout recording, and owner/retention/recovery gates
before any remediation option.

**Validation:** rerun this read-only path on an authorized target and confirm
that it classifies `DISK_FULL`, `INODE_FULL`, `DOCKER_LOG_PRESSURE`,
`DELETED_OPEN_FILES`, or `UNKNOWN_STORAGE` without performing cleanup.
