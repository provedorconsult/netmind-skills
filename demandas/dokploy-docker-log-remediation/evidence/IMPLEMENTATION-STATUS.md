# Dokploy Docker JSON Log Remediation — Maker status

## Emergency production action and post-change snapshot

**Authorization:** explicit and limited to previously identified Docker JSON
log files. One prevalidated active `json-file` log was reduced using
`truncate -s 0`, preserving its descriptor and without removing containers,
images, volumes, services, or configuration.

| Target | Path | Container / service | Before | After |
|---|---|---|---:|---:|
| #1 | Docker JSON log (sanitized) | active standalone container (sanitized) | 52,015 MiB | 0 MiB |

At 2026-08-28T20:27:02Z, root free space rose from 0 to 48,702 MiB and root
usage fell from 100% to 36%. Aggregate JSON logs fell from 56,883 MiB to
4,869 MiB. Docker (28.5.0), Swarm, and the target container remained active.
No application, Dokploy UI/API, proxy, PostgreSQL, DNS, or TLS endpoint was
functionally tested because no endpoint scope was authorized.

## Pre-change snapshot

2026-08-28: root 79,103 MiB total, 78,353 MiB used, 0 MiB free (100%); inodes
10%. Docker 28.5.0, active Swarm, default `json-file`, 44 running containers,
9 services, 46 tasks. `daemon.json` is absent; all running containers report
`json-file`. JSON logs total 56,883 MiB across 70 files; largest is 52,015 MiB.

## Goal status

| Goal | Status | Result |
|---|---|---|
| G01 | PASS | Current incident and target reconfirmed read-only. |
| G02 | PASS | Before evidence preserved without log content. |
| G03 | PASS | One confirmed active JSON log was truncated under explicit emergency authorization. |
| G04 | PASS | Rotation Skill implemented; apply remains gated. |
| G05 | PASS | Root, target log, Docker, Swarm, and container state were rechecked. |
| G06 | BLOCKED | Requires authorized change and approved endpoint scope. |
| G07 | PASS | Parametric monitoring plan documented below. |
| G08 | PASS | LIVE-001 is MITIGATED; rotation and application validation remain pending. |
| G09 | PASS | Storage and two new Skills retrofitted from confirmed evidence. |

## Monitoring and prevention

Monitor root free space/inodes, aggregate Docker JSON logs, largest log and
growth rate. Define Warning/Critical/Emergency thresholds from approved
capacity, retention and recovery objectives; do not hard-code thresholds before
the owner supplies those inputs. Alert on missing rotation or rapid growth.

## Required authorization for G03

An approved production change plan must select the affected workload(s),
retention policy, evidence-preservation decision, truncation/configuration
mechanism, rollback, maintenance impact, and validation endpoints. No generic
Docker prune is an acceptable substitute.
