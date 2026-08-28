# DOKPLOY-G12 — Harness integration

The existing Harness remains authoritative. This demand adds no alternate
approval, merge, or state mechanism.

```text
Checker → audit → diagnosis → risk classification → Maker action
        → validation → Checker
```

| Class | Handling |
|---|---|
| READ_ONLY | permitted only against confirmed target; preserve sanitized evidence |
| LOW_RISK | explicit task authorization plus validation |
| MEDIUM_RISK | pre-change evidence, owner, rollback, and explicit authorization |
| HIGH_RISK | documented impact, maintenance decision, rollback/abort, and explicit authorization |
| DESTRUCTIVE | never automatic; separate explicit authorization and recovery proof |

The demand's `DOKPLOY-Gxx` labels avoid collision with the Harness catalog's
historic G IDs. Checker must map any future promotion to the real Harness goal
before merging.
