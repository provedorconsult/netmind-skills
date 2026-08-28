---
name: dokploy-deployment-diagnose
description: Diagnostica build e deployment Dokploy por evidência sem redeploy ou alteração implícita.
---
# Dokploy deployment diagnosis

## Purpose and scope

Investigate L5 application deployment or build failure after lower layers are
checked. Inputs are the approved deployment reference, expected version, and
sanitized failure evidence.

## Procedure

Inspect immutable deployment metadata, filtered task state, healthcheck result,
image availability, dependency readiness, and sanitized error class. Separate
build, pull, configuration, migration, healthcheck, and runtime failures.

## Decision tree and evidence

First failed stage identifies the next owner/Skill. No causal evidence remains
`UNKNOWN`. Record version reference, timestamps, failure stage, and evidence
without log dumps or environment variables.

## Safety boundaries, validation, output

No deploy/redeploy, rollback, image deletion, migration, or restart. Validate
an authorized remedy using the original healthcheck and expected version.
Output `BUILD`, `DEPLOY`, `DEPENDENCY`, `RUNTIME`, `UNKNOWN`, or `BLOCKED`.
