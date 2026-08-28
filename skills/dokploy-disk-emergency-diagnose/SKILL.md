---
name: dokploy-disk-emergency-diagnose
description: Diagnostica pressão crítica de disco Dokploy com consultas limitadas e sem apagar dados.
---
# Dokploy disk emergency diagnosis

## Purpose and scope

Classify `DISK_FULL`, `DISK_CRITICAL`, `INODE_PRESSURE`,
`DOCKER_LOG_PRESSURE`, `DOCKER_STORAGE_PRESSURE`, or `UNKNOWN_STORAGE` under
`READ_ONLY`.

## Procedure

Collect `df`/inodes; narrow one filesystem at a time; inspect Docker root
classes and JSON log metadata; compare visible bytes with allocation; check
deleted-open files, journal and cache. Record the largest log and compare two
safe observations when a growth rate is available; check whether rotation is
missing or unverified. Every broad query has scope and timeout.

## Decision, safety, validation

Identify owner, retention, recovery and risk before proposing any action. No
prune, delete, truncate, rotate, restart, or restore. Output a sanitized
diagnosis, urgency and authorization gate; validate later only after an
approved remediation by rechecking capacity and workload health.
