# DOKPLOY-G08 — Backup and restore contract

## Scope

Identify application databases, named volumes, bind mounts, Dokploy metadata,
and external S3/MinIO destinations per application owner. Never infer that all
Docker volumes are disposable.

## Procedure

1. **Inventory (READ):** map owner, data class, persistence location,
   retention, encryption, and restore owner.
2. **Backup (authorized action):** create database/configuration/volume backup
   without exposing secrets.
3. **Existence and integrity:** verify artifact metadata and integrity check.
4. **Restore (controlled environment only):** restore to isolated target; do
   not overwrite the audited host.
5. **Data validation:** validate database/application invariants and record
   result.

## Decision and evidence

`VALIDATED` requires `BACKUP → EXISTENCE → INTEGRITY → RESTORE → DATA
VALIDATION`. A completed job or present object alone is `NOT_VALIDATED`.

## Current status

The live audit did not inspect backup configuration or execute a restore;
therefore recovery validation is **BLOCKED pending an approved controlled
environment and application-specific data owner**.
