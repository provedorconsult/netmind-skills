# DOKPLOY-VPS-G02 — Host forensics

## Goal and scope

Measure OS/kernel/uptime, CPU/RAM/load, filesystem/inodes/mounts/partitions,
LVM/swap, network, processes and systemd health to distinguish storage,
memory, CPU, and I/O pressure.

## Procedure

Use bounded `READ_ONLY` summaries; record values and state classes, not command
output that identifies customers or workloads. Explicitly mark unsupported
subsystems `NOT_APPLICABLE` and unavailable facts `UNKNOWN`.

## Decision and output

Classify each pressure dimension as `OBSERVED`, `NOT_OBSERVED`, or `UNKNOWN`.
Do not infer storage cause from root fullness alone. Output `HOST-FORENSICS`
and pass only with timestamped, sanitized evidence.
