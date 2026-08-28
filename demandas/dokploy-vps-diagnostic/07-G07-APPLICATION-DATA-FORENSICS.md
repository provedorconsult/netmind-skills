# DOKPLOY-VPS-G07 — Application-data forensics

## Goal

Classify allocation attributable to PostgreSQL, Dokploy metadata, Docker
volumes, application uploads, backups, artifacts, repositories, and temporary
deployment data.

## Safety

Never copy `.env`, database rows, private keys, passwords, tokens, raw logs,
or customer identifiers. Record only path class, owner class, size,
persistence, retention, and evidence quality.

## Decision and output

Distinguish persistent data from rebuildable cache and unknown data. No volume
inspection that reveals contents and no data mutation. Output
`APPLICATION-DATA-MAP` with recovery prerequisites for every candidate action.
