---
name: dokploy-audit-readonly
description: Coleta um snapshot sanitizado e somente leitura de host, Docker, Swarm e componentes Dokploy sem expor segredos ou configurações brutas.
---
# Dokploy read-only audit

## Purpose, scope, and inputs

Collect facts from a confirmed authorized host under `READ`. Inputs are the
target identity, time window, and permitted evidence destination.

## Procedure

Collect host OS/kernel/resources/filesystems; route/resolver/listener and
firewall status; Docker version/health; Swarm state and aggregate
service/task/network/volume counts; and filtered component presence. Do not
dump compose files, container environment, credentials, domains, raw logs, or
application names.

## Decision tree

```text
Authentication/identity failure → stop and return sanitized evidence
Read-only fact explains incident → hand off to matching diagnostic Skill
Critical fact without confirmed cause → record issue; require authorization
```

## Evidence, failure conditions, validation, output

Separate `FACT`, `OBSERVATION`, `INFERENCE`, and `UNKNOWN`; include timestamps
and command class. Validate that no secret or customer-specific identifier was
persisted. Output `COMPLETE`, `PARTIAL`, or `BLOCKED`.

## Safety boundaries

No restart, deploy, prune, remove, upgrade, rollback, DNS/firewall mutation,
or raw sensitive output.
