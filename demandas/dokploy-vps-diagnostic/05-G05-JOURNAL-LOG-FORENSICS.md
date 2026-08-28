# DOKPLOY-VPS-G05 — Journal and log forensics

## Goal

Investigate journald, system/Docker/application log allocation, rotation and
retention metadata, large log classes, and deleted-but-open files.

## Procedure

Use size/metadata-only, bounded read checks. Compare `df` and `du` evidence;
inspect open deleted file *metadata* without log contents. Record whether log
retention is known, unknown, or contradicted by observed allocation.

## Safety and output

No vacuum, truncation, rotation, restart, or deletion. Output `LOG-MAP` and a
deleted-open-files verdict: `OBSERVED`, `NOT_OBSERVED`, or `UNKNOWN`.
