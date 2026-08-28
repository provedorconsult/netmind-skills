# DOKPLOY-VPS-G08 — Growth timeline

## Goal

Determine current size, historical size, growth rate/source, and whether
growth is steady, sudden, deployment/log/backup/Docker/database related, or
unknown.

## Procedure

Use existing monitoring, filesystem timestamps, safe metadata, and prior
sanitized evidence. Never infer a timeline from one snapshot. If history is
insufficient, return `UNKNOWN — BASELINE ABSENT` and define future baseline
measurements.

## Output

`GROWTH-TIMELINE` with evidence window, confidence, limitations, and next
read-only measurements.
