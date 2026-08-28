---
name: dokploy-domain-diagnose
description: Diagnostica DNS e TLS de domínios Dokploy com consultas externas somente leitura.
---
# Dokploy domain diagnosis

## Purpose, scope, inputs

Diagnose L8 DNS/TLS for a domain explicitly supplied by the authorized Source
of Truth. Do not discover domains by scanning services.

## Procedure and read-only checks

Check authoritative resolution from approved resolvers, reachability on the
expected public ports, HTTP response class, certificate validity/hostname
match, and proxy/backend handoff. Sanitize domain and address evidence in the
repository.

## Decision tree

Resolution mismatch → DNS; certificate mismatch/expiry → TLS; valid edge but
404/502 → Traefik; no confirmed fault → `UNKNOWN`.

## Evidence, safety, validation, output

Record resolver/result class/time, not addresses or certificate bodies. No DNS,
certificate, proxy, or firewall modification. Recheck from the same resolver
after authorized change. Output `DNS`, `TLS`, `PROXY`, `UNKNOWN`, or `BLOCKED`.
