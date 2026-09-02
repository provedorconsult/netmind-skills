---
name: buzz-mobile-pairing-validation
description: Validate Buzz NIP-AB mobile pairing from NIP-11 and WebSocket transport through a real Desktop-to-Mobile paired result.
---

# Buzz Mobile Pairing Validation

## Purpose

Provide layered acceptance for a repaired or newly deployed Buzz mobile-pairing path. Transport establishes readiness; only a completed Desktop-to-Mobile pairing establishes functional success.

## When to use

Use after a pairing deployment or whenever a change could affect NIP-11, WebSocket routing, TLS, or mobile pairing. Do not declare `PASS` from HTTP `200`, a healthy container, or a QR image alone.

## Preconditions

- `<BUZZ_DOMAIN>` and expected public pairing endpoint.
- A Buzz Desktop session, compatible authorized mobile client, and permission to complete pairing.
- Authorized `READ`/ `TEST` access for sanitized relay and proxy evidence.

Never record QR payloads with sensitive material, private identities, tokens, or raw mobile logs.

## Procedure

1. Fetch NIP-11 and record post-change `supported_nips` and `pairing_relay_url`. Confirm the URL matches the intended public endpoint.
2. Test WebSocket upgrades separately for `wss://<BUZZ_DOMAIN>` and the advertised pairing endpoint. A valid pairing probe normally receives HTTP `101`; treat `404`, TLS failure, refusal, or timeout as fail.
3. In Buzz Desktop, open **Settings → Mobile** and generate a QR. Confirm it remains active and no pairing WebSocket error appears.
4. Scan from mobile, confirm both sides reach verification, compare and approve the six-digit code through the intended user flow, then authorize pairing.
5. Confirm the mobile client remains paired. If policy permits, perform the least-invasive product check establishing that the pair is usable.
6. Capture sanitized timestamps, endpoint status, client versions, result, and non-sensitive literal errors. Correlate logs only on failure.

## Results

```text
nip11: PASS | FAIL
pairing_relay_url: PASS | FAIL
main_wss: PASS | FAIL
pairing_wss: PASS | FAIL
qr_persistent: PASS | FAIL
mobile_scan: PASS | FAIL
six_digit_verification: PASS | FAIL
paired: PASS | FAIL
final: PASS | FAIL | BLOCKED
```

`final: PASS` requires all transport checks and `paired: PASS`. Use `BLOCKED` when the interactive Desktop/mobile acceptance cannot run; do not label it a deployment failure without evidence.

## Failure handling

| Failure | Evidence | Next action |
| --- | --- | --- |
| QR closes with WebSocket `404` | desktop error and pairing 404 | return to `buzz-mobile-pairing-diagnosis` |
| QR remains but phone cannot scan | no mobile connection attempt | validate client compatibility and QR handling |
| Code mismatch or verification fails | both clients reach SAS stage | stop; collect sanitized version/protocol evidence |
| TLS/DNS failure | public probe fails before upgrade | diagnose publication and routing |
| Transport passes but pairing fails | `101` plus functional failure | inspect compatibility and pairing logs without changing infrastructure |

## References

- [Desktop pairing implementation](https://github.com/block/buzz/blob/eed74bde2f4797714335ac10c56c0b0244c1def4/desktop/src-tauri/src/commands/pairing.rs)
- [Pairing relay implementation](https://github.com/block/buzz/tree/eed74bde2f4797714335ac10c56c0b0244c1def4/crates/buzz-pair-relay)
