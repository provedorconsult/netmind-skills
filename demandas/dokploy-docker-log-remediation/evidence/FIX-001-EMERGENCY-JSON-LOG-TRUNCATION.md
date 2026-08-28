# FIX-001 — Emergency Docker JSON log truncation

## Problem and evidence

`LIVE-001`: root was full because an active Docker JSON log occupied 52,015
MiB. PR #41 confirmed JSON logs as the primary cause; G01/G02 reconfirmed
100% root use, `json-file` for all running containers, and no daemon policy.

## Correction

Under explicit limited emergency authorization, `truncate -s 0` was applied to
one prevalidated active JSON log descriptor. No file, container, image, volume,
service, or configuration was removed or changed.

## Risk, rollback, validation, prevention

Historic content of the target log cannot be restored; metadata evidence was
preserved. Root free space rose to 48,702 MiB, the target container stayed
running, and Docker/Swarm remained active. A separately authorized rotation
policy is required for prevention; see `dokploy-docker-log-rotation`.
