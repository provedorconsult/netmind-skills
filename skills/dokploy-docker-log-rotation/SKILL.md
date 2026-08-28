---
name: dokploy-docker-log-rotation
description: Planeja e aplica somente com autorização explícita uma política Docker de retenção de logs, preservando daemon.json, containers existentes e rollback.
---
# Dokploy Docker log rotation

## Purpose and scope

Prevent uncontrolled `json-file` growth. Inputs: confirmed target, explicit
change authorization, approved retention requirements, maintenance impact
owner, and rollback owner.

## Discovery and preconditions

Read Docker default/per-container driver and options, `daemon.json` existence
and JSON validity, log allocation, free disk/inodes, container health, and
existing-container behavior. Preserve sanitized pre-change evidence. A daemon
default may apply only to newly created containers; do not claim existing
containers inherit it without verification.

## Diagnostic versus remediation versus persistent configuration

- **Diagnostic:** read the driver, current policy, `daemon.json`, aggregate
  allocation, and existing-container options. It changes nothing.
- **Emergency remediation:** a separately authorized, target-specific action
  may reduce confirmed log pressure; it does not configure future retention.
- **Persistent configuration:** changing daemon defaults or recreating
  containers is a separate authorized change with compatibility, downtime,
  rollback, and new-versus-existing verification.

## Authorized procedure

1. Read and parse existing `daemon.json`; never overwrite unrelated keys.
2. Derive `max-size`/`max-file` from approved capacity, traffic, retention and
diagnostic requirements; document expected allocation and tradeoff.
3. Back up the current configuration outside the exhausted filesystem when
applicable; merge and validate JSON.
4. Apply only with explicit authorization. Any daemon restart or container
recreation is a separately authorized impact action.
5. Validate driver/options for new and existing containers, log boundedness,
free disk, Docker/Swarm/Dokploy/application health; rollback through the saved
configuration only when authorized.

## Safety and output

No blind `daemon.json` overwrite, prune, log deletion, restart, or recreation.
Output `POLICY_PROPOSED`, `APPLIED_AND_VALIDATED`, or `BLOCKED` with evidence.
Current VPS state must be stated as `NOT YET APPLIED` until behavior is proven.
