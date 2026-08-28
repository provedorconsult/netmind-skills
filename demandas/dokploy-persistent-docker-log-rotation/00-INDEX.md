# Demand — Dokploy Persistent Docker Log Rotation

## Objective

Establish and validate durable Docker JSON log retention after the emergency
mitigation of `LIVE-001`. Source: PR #43, where disk recovery succeeded but
rotation remains `NOT YET APPLIED`.

## Required sequence

1. Reconcile current Docker version, driver, `daemon.json`, existing/new
   container behavior, capacity and owner requirements.
2. Define justified `max-size`/`max-file` policy and expected allocation.
3. Preserve/parse/merge/validate existing daemon configuration.
4. Determine recreation/restart/downtime needs per existing workload.
5. Apply only under explicit production authorization.
6. Validate new and existing containers, capacity, Docker/Swarm/Dokploy and
   authorized application endpoints; exercise approved rollback.
7. Implement monitoring/alerting and update `LIVE-001` only after validation.

## Safety

Changing `daemon.json` is not sufficient proof of rotation for existing
containers. No daemon restart, recreation, deployment, deletion, prune, or
configuration change is authorized by this specification. Each must be a
separately approved production action with rollback and validation.

## Deliverables

Compatibility evidence, policy rationale, change/rollback plan, existing
container matrix, before/after snapshots, monitoring thresholds, acceptance
matrix, and Skill updates. Keep identifiers and configuration values sanitized.
