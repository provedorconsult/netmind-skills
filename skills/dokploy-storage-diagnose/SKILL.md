---
name: dokploy-storage-diagnose
description: Diagnostica capacidade, volumes e backup Dokploy com agregados seguros e sem limpeza automática.
---
# Dokploy storage diagnosis

## Purpose and scope

Investigate L7 storage, disk-full, volume, and backup symptoms with `READ`.

## Procedure

Collect filesystem and inode capacity, bounded aggregate consumption, Docker
volume count/attachment state, and backup evidence metadata. Classify backup
as `UNKNOWN` until existence, integrity, restore, and data validation are each
proven.

### Disk-emergency read-only path

When filesystem pressure is observed, use a bounded hierarchy: filesystem root
→ `/var` → `/var/lib` → Docker root → `containers`, `overlay2`, `volumes`,
`image`, and `buildkit`. Each query must stay on one filesystem, have a timeout,
and record scope, result, and limitation. Do not repeat a timed-out broad query
indefinitely.

For a disproportionately large container directory, aggregate JSON log file
metadata only: count, total size, largest size, modification-time bucket, and
owner class. Do not read log content or persist resource names. Compare `df`
against `du`; if visible sizes do not explain allocated blocks, run a bounded
deleted-but-open-file metadata check when the host supports it. Check journald
and package-cache allocation as separate hypotheses.

## Decision tree

Disk full → classify `DOCKER_LOG_PRESSURE`, `DOCKER_STORAGE_PRESSURE`,
`LOG_PRESSURE`, `DELETED_OPEN_FILES`, or `UNKNOWN_STORAGE` from evidence;
every outcome is a HIGH-risk authorization gate. Inode full follows a separate
path. Volume attachment/capacity fault → identify owner and recovery plan.
Missing backup evidence → `NOT_VALIDATED`, never healthy.

## Evidence, safety, validation, output

Do not prune, delete, truncate, rotate, remove volume, or restore. Before an
authorized option is proposed, establish what is stored, why, owner, retention,
recovery requirement, risk, rollback, and validation. Record capacity facts and
collection limitations. Validate an approved remedy by rechecking capacity and
workload health. Output `CAPACITY`, `VOLUME`, `BACKUP_GAP`,
`DOCKER_LOG_PRESSURE`, `DELETED_OPEN_FILES`, `UNKNOWN_STORAGE`, or `BLOCKED`.
