---
name: buzz-mobile-pairing-diagnosis
description: Diagnose Buzz Desktop mobile-pairing failures, especially WebSocket 404s, without changing the relay, proxy, database, or deployment.
---

# Buzz Mobile Pairing Diagnosis

## Purpose

Identify the first failed layer in the NIP-AB pairing path and produce sanitized evidence. Begin in `READ` mode; this skill does not authorize a deployment, proxy change, restart, or database action.

## When to use

Use when Buzz Desktop pairing fails during **Settings → Mobile**, the QR closes early, or a client reports WebSocket `404`, `400`, `401`, `403`, TLS failure, refusal, or timeout. It does not prove that a mobile device paired; use `buzz-mobile-pairing-validation` for that outcome.

## Preconditions and inputs

- Authorized `READ` access to the deployment or its documented control plane.
- `<BUZZ_DOMAIN>` and the deployed `<BUZZ_VERSION>` or image reference.
- A safe way to inspect proxy/service status and filtered logs when public probes are insufficient.

Use Source-of-Truth credentials only in memory. Do not print environment blocks, database URLs, tokens, private keys, access keys, or raw production logs. Reporting the public `BUZZ_PAIRING_RELAY_URL` is allowed.

## Read-only procedure

1. Record the desktop error and time window. Do not infer that a QR rendering problem is a relay failure until transport is tested.
2. Fetch NIP-11 from `https://<BUZZ_DOMAIN>` with `Accept: application/nostr+json`. Record only `name`, `software`, `version`, `supported_nips`, and `pairing_relay_url`.
3. Classify discovery:
   - a valid `ws://` or `wss://` `pairing_relay_url` is the pairing endpoint;
   - when it is absent and NIP-43 is advertised, current Buzz desktop clients use `wss://<BUZZ_DOMAIN>/pair`;
   - otherwise confirm the deployed desktop implementation before assuming the main relay is the pairing endpoint.
4. Probe the main relay and the resolved pairing endpoint independently with a standards-valid WebSocket upgrade. Record status, certificate result, and endpoint only.
5. Inspect effective main-relay configuration without dumping its environment. Record `BUZZ_PAIRING_RELAY_URL` as `PRESENT`/ `ABSENT` and its public value if present.
6. Inspect service inventory, image/version, entrypoint, command, listener port, health, network attachment, and filtered pairing/proxy logs. Locate `buzz-pair-relay` or an equivalent version-supported service.
7. Trace client → DNS/TLS → proxy router/rule → proxy service → pairing container → internal port. For a path deployment, verify that `/pair` reaches pairing, not the main relay.
8. Stop at the first unproven layer and classify the likely cause. Keep remediation separate until evidence supports it.

## Diagnostic matrix

| Symptom | Evidence | Likely cause | Next safe check |
| --- | --- | --- | --- |
| WebSocket `404` at `/pair` | Main relay works; pairing path is 404 | absent service or proxy route | service inventory and router target |
| `pairing_relay_url` absent | NIP-11 has no field | no advertised endpoint | effective `BUZZ_PAIRING_RELAY_URL` |
| Container stopped | runtime unavailable | service did not start or exited | image, entrypoint, port, filtered logs |
| `400` on malformed probe | endpoint responds before upgrade | invalid probe or protocol reject | repeat valid handshake |
| `401` or `403` | proxy/service denies connection | policy or access gate | identify enforcing layer |
| TLS/DNS failure | lookup or certificate fails | public publication issue | hostname, DNS, SNI, certificate |
| Refused or timeout | no reachable listener | network, port, service failure | listener and proxy network |
| WSS `101` | valid upgrade succeeds | transport works | E2E validation |

## Expected evidence

```text
version: <BUZZ_VERSION | UNKNOWN>
nip11: PASS | FAIL
pairing_relay_url: PRESENT | ABSENT | INVALID
main_wss: PASS | FAIL
pairing_wss: PASS | FAIL
pairing_service: PRESENT | ABSENT | UNHEALTHY | UNKNOWN
route: CONFIRMED | MISROUTED | UNKNOWN
cause: <classification>
secrets: none-recorded
```

## Escalation and references

When a dedicated service or route is confirmed missing or misconfigured, use `buzz-pairing-relay-deployment` only with explicit `WRITE` authorization. Verify the deployed version against [desktop resolution](https://github.com/block/buzz/blob/eed74bde2f4797714335ac10c56c0b0244c1def4/desktop/src-tauri/src/commands/pairing.rs), [NIP-11](https://github.com/block/buzz/blob/eed74bde2f4797714335ac10c56c0b0244c1def4/crates/buzz-relay/src/nip11.rs), and [relay configuration](https://github.com/block/buzz/blob/eed74bde2f4797714335ac10c56c0b0244c1def4/crates/buzz-relay/src/config.rs).
