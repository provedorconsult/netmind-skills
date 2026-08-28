---
name: dokploy-install-debian12
description: Orienta uma instalação Dokploy reproduzível em host Debian 12 controlado, com gates e validação sem sobrescrever instalações existentes.
---
# Dokploy installation on Debian 12

## Purpose and scope

Install only on a host that `dokploy-preflight` returned `READY`. It is for a
new controlled host, never for resetting or replacing an existing installation.

## Inputs and preconditions

Require explicit `WRITE` authorization, approved maintenance window, confirmed
host/domain, rollback/abort owner, and backup destination. Confirm Docker,
Swarm, required ports, and network state immediately before acting.

## Procedure

1. `PRECHECK`: preserve read-only baseline evidence and abort criteria.
2. `HOST`: prepare only the approved host prerequisites.
3. `DOCKER → SWARM → DOKPLOY`: execute the vendor-supported procedure pinned
   to an approved version; stop at the first error.
4. `HEALTH → DOMAIN/TLS → TEST DEPLOY → BACKUP`: validate each layer before
   advancing.
5. `FINAL VALIDATION`: record service health, persistent data locations, DNS/
   TLS checks, and a test deployment result.

## Decision tree

- Existing Docker, Swarm, installation, occupied port, conflicting network, or
  partial installation: `BLOCKED`; do not remove/recreate anything.
- Resource shortfall: `BLOCKED`.
- Failed installation: collect evidence, preserve state, use only an approved
  recovery procedure.

## Evidence, validation, and output

Output `INSTALLED_AND_VALIDATED`, `BLOCKED`, or `FAILED_WITH_EVIDENCE`.
Evidence includes version, timestamps, approved actions, health checks, and
rollback point, never secrets.

## Safety boundaries

No unapproved upgrade, rollback, DNS/firewall change, prune, volume removal,
or Swarm recreation.
