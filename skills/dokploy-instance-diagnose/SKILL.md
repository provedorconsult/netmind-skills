---
name: dokploy-instance-diagnose
description: Diagnostica indisponibilidade da instância Dokploy por camadas antes de qualquer correção autorizada.
---
# Dokploy instance diagnosis

## Purpose and scope

Locate failure at L0 host, L1 Docker, L2 Swarm, or L3 Dokploy. Inputs are a
symptom, sanitized target, and `READ` authorization.

## Procedure and read-only checks

Confirm host capacity/listeners, Docker daemon health, Swarm service/task
health, then the Dokploy component's filtered status. Stop at the first layer
that proves the fault; otherwise mark the cause `UNKNOWN`.

## Decision tree, evidence, and validation

`host → docker → swarm → dokploy`; record observed status, failed layer,
hypothesis versus confirmed cause, and next Skill. Validate by repeating the
same read check after any separately authorized action.

## Safety boundaries and output

Do not restart services. Output `LAYER_IDENTIFIED`, `NO_FAULT_OBSERVED`, or
`BLOCKED` with evidence and authorized-action requirements.
