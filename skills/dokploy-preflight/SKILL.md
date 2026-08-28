---
name: dokploy-preflight
description: Avalia um host candidato a Dokploy em Debian 12 com checks somente leitura e retorna READY ou BLOCKED sem alterar o host.
---
# Dokploy preflight

## Purpose

Decide whether a confirmed, controlled host can proceed to an authorized
Dokploy installation. This Skill never repairs a failed preflight.

## Scope and inputs

Inputs are a confirmed target, authorized `READ` scope, intended hostname and
domain, and the installation resource baseline. Do not infer them from DNS or
scan a network.

## Preconditions

Validate the SSH host key and identity. Stop on unexpected identity,
authentication failure, or missing authorization.

## Procedure — read-only checks

1. Collect OS release, kernel, CPU, RAM, root filesystem capacity/free space,
   inode use, default route, resolver presence, and hostname.
2. Check listeners for the required public ports without changing firewall.
3. Check Docker installation/version, Swarm state, existing services,
   networks, volumes, and non-Dokploy workloads.
4. Classify each condition as `PASS`, `WARN`, `BLOCKED`, or `UNKNOWN`.

## Decision tree

```text
Unsupported OS / insufficient resource / occupied required port / existing Swarm
  → BLOCKED: preserve evidence and require an approved strategy
All required checks pass
  → READY: authorize the separate installation Skill if desired
Unknown critical input
  → BLOCKED: do not continue silently
```

## Evidence and validation

Record timestamp, target identity sanitized, command class, result, and reason.
The output is exactly `READY` or `BLOCKED` with the failing checks.

## Safety boundaries

No package install, Swarm initialization, firewall/DNS change, service stop,
prune, or cleanup is permitted.
