# DOKPLOY-VPS-G09 — Root cause

## Classification matrix

| Hypothesis | Evidence for | Evidence against | Status |
|---|---|---|---|
| Container JSON logs | 56,880 MiB; largest one 52,014 MiB; container directory 56,886 MiB | None material | **CONFIRMED** |
| Docker writable layers | Docker logical report shows about 180 MiB container writable use | 56,886 MiB directory allocation is explained by JSON logs | REJECTED as primary cause |
| Docker images | 35 MiB directory class; 14.11 GB logical images | Insufficient to explain root allocation; logical figure includes shared layers | REJECTED as primary cause |
| Docker volumes / application data | 3,281 MiB | Insufficient to explain root allocation | REJECTED as primary cause |
| Journald | 767 MiB | Insufficient to explain root allocation | REJECTED as primary cause |
| Deleted-open files | None detected | None | REJECTED |
| Package cache | 340 MiB combined | Insufficient to explain root allocation | REJECTED |

## Root-cause verdict

`ROOT_CAUSE_CONFIRMED`: unbounded Docker JSON container-log allocation is the
primary cause of `LIVE-001`. The largest log remained active at collection
time. Owner application/service is intentionally `UNKNOWN` because resource
identities and log contents were outside the safe evidence scope.

## Risk

The root filesystem has no reported free MiB. Further logging, Docker writes,
deployments, or database/application writes can fail. Remediation requires
explicit authorization because it can discard evidence or affect workloads.
