# VPS diagnostic report — LIVE-001

**Collection:** 2026-08-28, authorized `READ_ONLY` session. No production
mutation occurred.

## G01–G08 evidence

| Goal | Result | Evidence |
|---|---|---|
| G01 Safety baseline | PASS | SSH and `sudo` revalidated; target identity marker matched. |
| G02 Host | PASS | Debian 12, active Swarm, no zombie processes, one failed systemd unit, and no current CPU/memory/I/O PSI pressure observed. |
| G03 Filesystem | PASS | Root: 79,103 MiB total, 78,354 MiB used, 0 MiB available, 100%; inodes 10%. `/var`: 76,360 MiB; `/var/lib`: 75,360 MiB. |
| G04 Docker storage | PASS | Docker root is the standard `/var/lib/docker`; containers 56,886 MiB, overlay 14,665 MiB, volumes 3,281 MiB, images 35 MiB, BuildKit 140 MiB. |
| G05 Logs | PASS | Container JSON logs: 71 files, 56,880 MiB total, largest 52,014 MiB. Persistent journal: 767 MiB. Deleted-open files: zero entries/zero MiB. |
| G06 Package/cache | PASS | APT cache: 200 MiB; APT lists: 140 MiB; temporary/home/opt/srv classes each approximately 1 MiB. |
| G07 Application data | PASS | Docker volume class is 3,281 MiB. Data contents, application identities, and configuration were not inspected. |
| G08 Growth timeline | BLOCKED | No historical size baseline exists. Largest log was modified at collection time, but modification time does not establish growth onset or rate. |

## Safety limitations

`journalctl --disk-usage` returned no usable aggregate although the persistent
journal directory was measured. Application identities, log content, domains,
and resource names were intentionally not collected.
