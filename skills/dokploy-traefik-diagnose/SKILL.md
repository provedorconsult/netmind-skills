---
name: dokploy-traefik-diagnose
description: Diferencia falhas Traefik 404 e 502 com diagnóstico somente leitura, DNS e TLS sanitizados.
---
# Dokploy Traefik diagnosis

## Purpose and scope

Diagnose L4 traffic routing only after L0–L3 are healthy enough. Inputs:
authorized endpoint reference, expected response class, and `READ` scope.

## Procedure

Check listener reachability, filtered proxy workload state, router/service
attachment evidence, backend health, and public DNS/TLS from the approved
perspective. A 404 suggests routing/match evaluation; a 502 suggests an
unhealthy or unreachable backend, neither proves it alone.

## Evidence and decision tree

Capture response class, timestamp, layer, and sanitized status. Stop on the
first demonstrated layer. `DNS/TLS` fault routes to domain diagnosis; backend
fault routes to deployment/compose diagnosis.

## Safety, validation, output

No router, certificate, DNS, or proxy restart/change. Repeat the same request
after authorized repair. Output `ROUTING`, `BACKEND`, `DNS_TLS`, `UNKNOWN`, or
`BLOCKED`.
