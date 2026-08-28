---
name: dokploy-swarm-diagnose
description: Diagnostica o estado Docker Swarm do Dokploy com evidência somente leitura e sem recriar o cluster.
---
# Dokploy Swarm diagnosis

## Purpose, scope, inputs, and preconditions

Investigate L2 Swarm after host and Docker checks. Require confirmed target,
symptom, and `READ` authorization.

## Procedure and read-only checks

Inspect local Swarm state, aggregate node/service/task health, task error
class, resource pressure, networks, and required persistent-volume attachment.
Sanitize names, addresses, and configuration values.

## Decision tree

Host/Docker fault → return to lower layer. Quorum, scheduling, network, task,
or volume evidence → classify a Swarm cause. No proof → `UNKNOWN`.

## Evidence, failure, safety, validation, output

Record layer, timestamps, aggregate state, and evidence. Never run `swarm
init`, `swarm leave`, force removal, or service scale/redeploy. After an
authorized repair, repeat the exact failed check. Output `CAUSE_IDENTIFIED`,
`ESCALATE`, or `BLOCKED`.
