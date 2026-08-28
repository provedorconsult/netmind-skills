# DOKPLOY-VPS-G10 — Remediation plan

## Goal

Produce, but do not execute, evidence-based immediate, short-term, long-term,
and prevention options after G09.

## Required record per option

`Action`, `risk class`, expected impact, precondition, backup requirement,
rollback, validation, owner, and explicit authorization requirement.

## Safety gate

No generic “run Docker prune” recommendation. First establish what is stored,
why, owner, retention, recovery, and risk. Any delete/prune/truncate/restart
is `HIGH_RISK` or `DESTRUCTIVE` until proven otherwise.
