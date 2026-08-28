# Dokploy Self-Hosted — Debian 12 Standard Log Rotation Runbook

## Purpose and scope

Configure durable Docker log retention without unsafe cleanup.

## Prerequisites and discovery

Confirm target, policy inputs, owner, rollback and endpoint plan. Read current
Docker/daemon/container/Swarm/Dokploy state before proposing change.

## Policy and daemon.json

Derive parameters from capacity and retention. Backup, parse, merge and
validate JSON; preserve unrelated keys.

## Existing/new containers, Swarm and Dokploy

Assess existing recreation/rolling-update requirements separately from new
container inheritance. Discover Dokploy behavior; do not assume preservation.

## Validation, monitoring and rollback

Prove actual rotation with a controlled workload, then validate health and
capacity. Monitor disk/inodes/log growth/rotation absence. Roll back config and
workloads only under approved procedure.

## Emergency recovery and troubleshooting

Use disk-emergency diagnosis; preserve evidence and identify owner/retention
before any targeted remediation. Never use generic prune.

## Production authorization gate

**PRODUCTION AUTHORIZATION REQUIRED** for daemon change, Docker restart,
recreation, service update or redeploy.
