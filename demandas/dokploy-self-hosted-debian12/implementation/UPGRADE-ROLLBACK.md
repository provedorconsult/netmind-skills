# DOKPLOY-G09 — Upgrade and rollback contract

## Upgrade gate

`AUDIT → backup validation → version/compatibility review → authorized change
→ health check → application validation`.

Record the known-good version, immutable artifacts, compatibility evidence,
abort criteria, owner, and time window before change. If any is absent, stop.

## Rollback gate

`Identify known-good → preserve evidence → authorized rollback → validate`.

Rollback must be version and data compatible; it is not synonymous with
redeploying an arbitrary prior image. Restoration of persistent data follows
the backup/restore contract.

## Boundary

The audited host received no upgrade or rollback. Homologation is required to
promote this procedure beyond documented readiness.
