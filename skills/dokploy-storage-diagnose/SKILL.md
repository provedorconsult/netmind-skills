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

## Decision tree

Disk full/inode full → HIGH risk issue and authorization gate. Volume
attachment/capacity fault → identify owner and recovery plan. Missing backup
evidence → `NOT_VALIDATED`, never healthy.

## Evidence, safety, validation, output

Do not prune, delete, truncate, rotate, remove volume, or restore. Record
capacity facts and collection limitations. Validate an approved remedy by
rechecking capacity and workload health. Output `CAPACITY`, `VOLUME`,
`BACKUP_GAP`, `UNKNOWN`, or `BLOCKED`.
