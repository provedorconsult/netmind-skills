# DOKPLOY-G13 — Controlled-environment homologation

## Preconditions

Dedicated Debian 12 host, approved DNS/test domain, non-production credentials,
disposable application data, rollback owner, and separate backup destination.

## Test register

| ID | Precondition | Action | Expected | Actual / evidence | Result |
|---|---|---|---|---|---|
| H01 | clean host | preflight | READY | pending controlled host | BLOCKED |
| H02 | H01 | install | healthy Dokploy | pending | BLOCKED |
| H03 | H02 | test deploy | health endpoint passes | pending | BLOCKED |
| H04 | H03 | domain/TLS check | valid routing/certificate | pending | BLOCKED |
| H05 | H03 | database/volume backup then isolated restore | data validation passes | pending | BLOCKED |
| H06 | H03 | controlled failure injection and diagnosis | layer and recovery proven | pending | BLOCKED |

No production host will be used to satisfy these tests. `BLOCKED` is evidence
of missing controlled-environment authority, not a passing result.
