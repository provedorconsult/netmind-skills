# Acceptance contract — Dokploy VPS Forensic Diagnostic

- **AC01 Access:** authorized VPS access method succeeds and target identity is
  confirmed without storing credentials.
- **AC02 Baseline:** `DIAGNOSTIC-BASELINE` preserves initial state.
- **AC03 Filesystem:** allocated filesystem use is measured hierarchically.
- **AC04 Docker:** Docker root/storage is investigated with bounded queries.
- **AC05 Logs:** journal and log allocation are investigated safely.
- **AC06 Deleted-open:** deleted-but-open-file state is classified.
- **AC07 Inodes:** inode condition is recorded.
- **AC08 Application data:** persistent application data is classified without
  content disclosure.
- **AC09 Timeouts:** each bounded-query limitation is recorded.
- **AC10 Cause:** LIVE-001 has a supported root-cause classification.
- **AC11 Plan:** remediation options have risk, rollback, validation, and
  authorization gates.
- **AC12 Safety:** no cleanup, delete, prune, restart, deployment, or other
  production mutation occurred during diagnosis.
- **AC13 Retrofit:** Skill gaps are evidence-linked.
- **AC14 Improvements:** each proposed Skill change has validation criteria.

All criteria must be `PASS`, `FAIL`, or `BLOCKED`; no `PASS` is inferred from
an existing document or from a single `df` result.
