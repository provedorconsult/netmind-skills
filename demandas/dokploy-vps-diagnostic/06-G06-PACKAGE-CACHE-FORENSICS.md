# DOKPLOY-VPS-G06 — Package and cache forensics

## Goal

Measure APT/package cache, temporary files, old kernel artifacts, Snap/Flatpak
when present, and other host cache classes.

## Procedure and output

Use only read-only package/cache metadata and bounded size aggregation. Record
installed versus cache allocation as distinct facts. No `apt clean`,
`autoremove`, deletion, or kernel removal. Output `PACKAGE-CACHE-MAP` with
candidate retention owner and `UNKNOWN` where policy is absent.
