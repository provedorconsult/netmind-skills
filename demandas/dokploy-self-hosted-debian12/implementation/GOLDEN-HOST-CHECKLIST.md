# DOKPLOY-G10 — Golden Host checklist

## Sizing tiers

| Tier | Use | Requirement |
|---|---|---|
| Minimum | controlled proof-of-concept | Debian 12, capacity for OS/runtime/data, public routing plan, and no pre-existing conflicting Swarm |
| Recommended | sustained non-critical workload | dedicated SSD/NVMe capacity, monitored free space, external backup target, validated restore, least-privilege access |
| Production | critical workload | redundancy strategy, tested recovery objective, monitored host/application health, approved change control and explicit ownership |

## Ready checklist

- [ ] `dokploy-preflight` is `READY` with dated evidence.
- [ ] Host identity, hostname, DNS and public port ownership are approved.
- [ ] Disk capacity and inode monitoring are configured; no capacity alert is open.
- [ ] Docker/Swarm conflict strategy is approved; no existing cluster is overwritten.
- [ ] Dokploy version and vendor installation source are approved.
- [ ] TLS/DNS validation and project isolation requirements are defined.
- [ ] Persistent stores have owner, retention, backup, and restore validation.
- [ ] Monitoring, logs, access control, incident ownership, and rollback gates are documented.
- [ ] Test deployment passes health checks without exposing secrets.
