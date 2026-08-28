# G05 Existing containers

Daemon defaults do not prove existing tasks changed. Per sanitized workload
record image, volumes, networks, ports, environment reference, healthcheck,
dependencies, restart policy, owner, recreation/rolling-update need, downtime,
rollback and validation. `DISCOVER → CLASSIFY → SELECT → AUTHORIZE →
RECREATE/UPDATE → VALIDATE`; never automate recreation.
