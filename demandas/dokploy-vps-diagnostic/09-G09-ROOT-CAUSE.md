# DOKPLOY-VPS-G09 — Root-cause classification

## Goal

Consolidate filesystem, Docker, logs, packages, application data, and timeline
evidence without elevating a hypothesis to fact.

## Required matrix

For Docker images/volumes/layers/logs/cache, journald, PostgreSQL, application
data, deleted-open files, package cache, and other allocation record evidence
for, evidence against, owner/recovery requirement, and status:
`CONFIRMED`, `PROBABLE`, `POSSIBLE`, `REJECTED`, or `UNKNOWN`.

## Gate

Only `CONFIRMED` evidence permits `ROOT_CAUSE_CONFIRMED`. Otherwise output the
best-supported classification and the smallest safe next observation.
