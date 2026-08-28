# DOKPLOY-VPS-G03 — Filesystem forensics

## Priority goal

Determine where allocated blocks reside without walking indefinitely or reading
application content.

## Procedure

Start filesystem-scoped and depth-limited: root mount, then `/var`, `/var/lib`,
`/var/log`, `/var/cache`, `/tmp`, `/home`, `/opt`, `/srv`, and distinct mounts.
For each path record sanitized path class, size, owner class, file type, age
bucket, and collection timeout. Use `timeout`, one-filesystem boundaries, and
top-level/subdirectory narrowing.

## Decision

Compare `df` blocks with visible-file aggregates. A material discrepancy
requires G05 deleted-open-file checks. Never use `rm`, `truncate`, or delete
options. Output `FILESYSTEM-MAP` plus gaps and candidate owners.
