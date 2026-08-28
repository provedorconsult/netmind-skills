# Dokploy Docker JSON Log Remediation — Maker status

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
| G03 | BLOCKED | Truncation/rotation/configuration is a production mutation not authorized. |
| G04 | PASS | Rotation Skill implemented; apply remains gated. |
| G05 | BLOCKED | Requires post-change state. |
| G06 | BLOCKED | Requires authorized change and approved endpoint scope. |
| G07 | PASS | Parametric monitoring plan documented below. |
| G08 | BLOCKED | LIVE-001 cannot close before post-change validation. |
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
