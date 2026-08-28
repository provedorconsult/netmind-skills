---
name: dokploy-postgres-diagnose
description: Diagnostica PostgreSQL em Dokploy preservando confidencialidade, volumes e integridade de dados.
---
# Dokploy PostgreSQL diagnosis

## Purpose, scope, inputs

Investigate L6 database symptoms under `READ`. Require the owning application,
approved connection method, and sanitized error evidence.

## Procedure and read-only checks

Check host capacity, workload status, volume attachment/capacity, listener,
and a least-privilege database readiness query when credentials and policy
authorize it. Do not dump databases or list application environment values.

## Decision tree and evidence

Storage/host fault → return to L0/L7. Workload fault → deployment diagnosis.
Connection/auth/application fault → preserve sanitized evidence. Distinguish
readiness, authentication, schema, corruption, and capacity hypotheses.

## Safety boundaries, validation, output

No restart, migration, SQL write, restore, volume change, or credential reset.
Validate an authorized remedy with readiness plus application health. Output
`DATABASE_LAYER_IDENTIFIED`, `UNKNOWN`, or `BLOCKED`.
