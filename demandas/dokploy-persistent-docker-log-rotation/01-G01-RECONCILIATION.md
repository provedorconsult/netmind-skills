# G01 Reconciliation

PR #41 confirmed Docker JSON logs as root cause. PR #43 truncated one authorized
active log, recovered ~48.7 GiB, and left `LIVE-001` **MITIGATED**. Persistent
rotation remains not applied; this demand exists to prepare it without mutation.
