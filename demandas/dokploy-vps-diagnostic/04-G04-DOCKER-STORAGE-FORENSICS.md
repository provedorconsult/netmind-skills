# DOKPLOY-VPS-G04 — Docker storage forensics

## Goal

Investigate Docker root storage, overlay layers, containers, images, volumes,
build cache, snapshots, and log allocation without listing configuration or
running a cleanup.

## Bounded strategy

`TOP_LEVEL → SUBDIRECTORY → TARGETED QUERY → TIMEOUT → ALTERNATIVE QUERY`.
Every query records command class, scope, timeout, result, and limitation.
Do not repeat a timed-out broad aggregate indefinitely.

## Evidence and decision

Report class-level bytes, persistence/owner class, and orphaned-object
*evidence* only; do not label an object safe to remove without retention and
recovery proof. Output `DOCKER-STORAGE-MAP` or `PARTIAL` with limitation.
