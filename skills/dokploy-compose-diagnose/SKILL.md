---
name: dokploy-compose-diagnose
description: Diagnostica contratos Compose usados por Dokploy sem expor ambientes, segredos ou alterar workloads.
---
# Dokploy Compose diagnosis

## Purpose, scope, and inputs

Locate L5 compose-contract faults from an approved project reference, symptom,
and `READ` authorization.

## Procedure and read-only checks

Compare sanitized declared service, network, volume, port, healthcheck, image,
and dependency contracts against filtered runtime evidence. Never print `.env`,
secrets, raw compose contents, or container environments.

## Decision tree

Invalid/missing contract evidence → compose layer. Healthy contract but failed
runtime → deployment diagnosis. Routing symptom → Traefik diagnosis. Otherwise
mark `UNKNOWN`.

## Evidence, safety, validation, output

Record contract mismatch category, not secret values. No compose edit, deploy,
redeploy, or variable change. Validate an authorized correction by checking
parsed contract and workload health. Output `CONTRACT_MISMATCH`, `RUNTIME`,
`UNKNOWN`, or `BLOCKED`.
