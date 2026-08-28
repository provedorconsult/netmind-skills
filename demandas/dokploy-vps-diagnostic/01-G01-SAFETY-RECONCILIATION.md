# DOKPLOY-VPS-G01 — Safety reconciliation

## Goal

Produce `DIAGNOSTIC-BASELINE` before any VPS forensic query.

## Required evidence

Confirm target identity, SSH method, read-only authorization, branch/PR state,
initial `df`/inode facts, and source artifacts from PR #39. Separate the live
production VPS from any future homologation host.

## Procedure and safety

Use only a marker handshake and bounded read commands. Sanitize host, IP,
domain, services, volumes, and credentials. Stop on host-key or identity
divergence. Do not modify the VPS.

## Output and promotion

`DIAGNOSTIC-BASELINE` with timestamp, evidence references, unknowns, and
`READ_ONLY` classification. Promotion requires a preserved baseline and no
production mutation.
