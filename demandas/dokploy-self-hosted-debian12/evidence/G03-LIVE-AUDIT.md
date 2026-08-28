# DOKPLOY-G03 — Sanitized live audit

**Scope:** authorized read-only SSH session with privileged read commands.
**Collection time:** 2026-08-28T16:57:29Z through 2026-08-28T16:57:51Z.

## Facts

| Area | Fact |
|---|---|
| Access | SSH authentication and `sudo` elevation succeeded. |
| Host | Debian 12; kernel `6.1.0-49-amd64`; 48 logical CPUs. |
| Memory | RAM capacity was collected; the exact capacity is omitted from repository evidence because it is host-specific. |
| Root filesystem | Approximately 79 GiB capacity; 100% used with no available MiB reported. Inodes were 10% used. |
| Network | A default route and DNS configuration are present; ten TCP listeners were counted. |
| Firewall | UFW was active. No firewall rules were read or modified. |
| Docker | Installed, server version 28.5.0; Swarm state `active`. |
| Orchestration | 9 services, 45 task records, 15 networks, 42 volumes, and 44 running containers were counted. Names and configuration were deliberately not recorded. |
| Components | Filtered service-name counts indicated Dokploy and PostgreSQL matches. No Traefik match was found by name; this is an observation, not proof that traffic is unmanaged. |
| Dokploy CLI | `dokployctl` was not installed. |

## Observations

- The root filesystem capacity condition is immediately actionable only after
  separate authorization: remediation may delete data or interrupt workloads.
- A bounded follow-up collection on 2026-08-28 did not obtain a Docker-data
  size aggregate within 20 seconds; the journal aggregate was also unreadable
  in that collection. These are collection limitations, not evidence that
  either source caused the capacity condition.
- The audit did not collect raw logs, container environments, service names,
  domains, certificates, or backup configuration. Those are **UNKNOWN** rather
  than healthy/absent.

## Inferences explicitly withheld

- No conclusion is made about application health, TLS validity, Traefik
  topology, PostgreSQL integrity, or backup recoverability.
- A missing `dokployctl` binary does not prove Dokploy is unhealthy.
