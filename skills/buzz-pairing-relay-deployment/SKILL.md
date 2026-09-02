---
name: buzz-pairing-relay-deployment
description: Remediate a confirmed Buzz NIP-AB pairing-relay publication or advertisement failure with explicit deployment authorization.
---

# Buzz Pairing Relay Deployment

## Purpose

Deploy or repair a dedicated NIP-AB pairing relay only after a read-only diagnosis confirms a missing, stopped, misrouted, or unadvertised endpoint. This skill changes infrastructure and requires explicit `WRITE` authorization for the named deployment.

## When to use

Use after `buzz-mobile-pairing-diagnosis` finds the pairing relay absent, unreachable, routed incorrectly, or not announced through NIP-11. Do not use to mask a 404 with a synthetic response or change unrelated PostgreSQL, Redis, object storage, identities, credentials, or main-relay routes.

## Preconditions

- Confirmed `<BUZZ_VERSION>` and an image with a supported pairing-relay binary.
- Explicit authorization to alter `<DOKPLOY_PROJECT>` or equivalent deployment and perform a controlled redeploy.
- Current service, network, proxy, and rollback state recorded without secrets.
- Endpoint design selected: dedicated `<PAIRING_DOMAIN>` is preferred; `wss://<BUZZ_DOMAIN>/pair` is valid only when the proxy can isolate that path.

## Remediation procedure

1. Verify the version-supported executable and bind setting. In currently supported Buzz images this is `/usr/local/bin/buzz-pair-relay`, normally bound with `BUZZ_PAIR_RELAY_BIND_ADDR=0.0.0.0:5000`. Treat other versions as version-specific until source or documentation confirms equivalence.
2. Add a stateless pairing service using the same compatible image as the main relay. Override the image **entrypoint** with the pairing executable when the image defaults to `buzz-relay`; a Compose `command` may append arguments and run the wrong binary.
3. Attach only required application and proxy networks. Expose the pairing port internally; do not publish databases, Redis, or object storage.
4. Configure proxy WebSocket upgrades, TLS, and one intended target:
   - dedicated hostname: `<PAIRING_DOMAIN>` → pairing service on its internal port;
   - path route: `Host(<BUZZ_DOMAIN>) && PathPrefix(/pair)` → pairing service.
   Ensure the path rule wins over a main-relay catch-all without changing existing hostname behavior.
5. Set `BUZZ_PAIRING_RELAY_URL=wss://<PAIRING_DOMAIN>` or `wss://<BUZZ_DOMAIN>/pair`, exactly matching the published route. Do not substitute `http://` or `https://` where the deployed version requires `ws://` or `wss://`.
6. Review minimal diff, record abort conditions, and deploy only the authorized service set. Do not recreate volumes or modify unrelated configuration.
7. If health fails or the main relay regresses, stop and apply rollback; do not change routes speculatively.

## Validation and rollback

After deployment, repeat NIP-11 and independent main/pairing WebSocket probes.

- NIP-11 must advertise the configured `pairing_relay_url`.
- Pairing must complete its expected upgrade, normally HTTP `101`, not `404`.
- Main relay WebSocket must still work.
- A running container or HTTP `200` is insufficient; continue with `buzz-mobile-pairing-validation`.

Rollback is the smallest reversal of the pairing service, proxy route, and `BUZZ_PAIRING_RELAY_URL` change. It must not delete volumes, communities, credentials, databases, or the main relay. Use the platform's documented rollback method and revalidate the pre-change main relay.

## Failure modes

| Failure | Evidence | Next action |
| --- | --- | --- |
| Wrong binary | main relay runs or process exits | inspect image entrypoint and use confirmed executable |
| Wrong port/network | proxy timeout/refusal | compare listener, service target, proxy network |
| Traefik misrouting | `/pair` reaches main relay | make path rule explicit and verify target |
| Incorrect URL | NIP-11 points to unreachable endpoint | correct URL and route together |
| TLS/DNS failure | handshake cannot reach proxy | repair public publication |
| Version incompatibility | binary/config differs | stop and verify exact release source |

## References

- [Pairing relay source](https://github.com/block/buzz/tree/eed74bde2f4797714335ac10c56c0b0244c1def4/crates/buzz-pair-relay)
- [Official Helm deployment](https://github.com/block/buzz/blob/eed74bde2f4797714335ac10c56c0b0244c1def4/deploy/charts/buzz/templates/pairing-relay.yaml)
- [Relay environment validation](https://github.com/block/buzz/blob/eed74bde2f4797714335ac10c56c0b0244c1def4/crates/buzz-relay/src/config.rs)
