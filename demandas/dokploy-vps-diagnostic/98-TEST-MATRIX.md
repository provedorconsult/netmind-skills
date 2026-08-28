# Test matrix — Dokploy VPS Forensic Diagnostic

Every future execution records `ID`, precondition, read-only action, expected,
actual, evidence, and `PASS`/`FAIL`/`BLOCKED`. `PASS` requires evidence.

| ID | Area | Expected evidence |
|---|---|---|
| T01 | filesystem usage | root allocation and free-block baseline |
| T02 | inode usage | inode pressure classification |
| T03 | `/var` | bounded top-level size map |
| T04 | `/var/lib` | bounded allocation map |
| T05 | Docker root | root-dir class and size/limitation |
| T06 | Docker volumes | aggregate persistence and owner classes |
| T07 | Docker images | aggregate image allocation |
| T08 | Docker layers | overlay/writable-layer allocation or limitation |
| T09 | Docker logs | metadata-only log allocation |
| T10 | build cache | cache class allocation and retention owner |
| T11 | journald | journal allocation/retention metadata |
| T12 | deleted-open files | observed/not-observed/unknown verdict |
| T13 | package cache | cache and obsolete-artifact allocation |
| T14 | PostgreSQL | persistent storage allocation class |
| T15 | application volumes | owner, persistence, retention class |
| T16 | backup artifacts | existence and allocation class, never data content |
| T17 | timeout handling | bounded query limitation recorded without looping |
| T18 | root cause | evidence matrix with confidence classification |
| T19 | remediation safety | authorization, backup, rollback, validation per option |
| T20 | Skill retrofit | evidence-to-gap-to-change mapping |
