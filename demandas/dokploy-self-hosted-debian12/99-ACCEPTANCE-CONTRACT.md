# Acceptance Contract — Dokploy Self-Hosted / Debian 12

## AC01 — Discovery
Todos os repositórios/evidências relevantes foram identificados ou classificados com justificativa.

## AC02 — Forensics
Procedimentos e incidentes possuem origem rastreável e fatos separados de hipóteses.

## AC03 — Live Audit
O Dokploy atual possui snapshot read-only sanitizado.

## AC04 — Canonical Baseline
`CURRENT`, `LEGACY` e `CANONICAL` estão separados.

## AC05 — Skills
Cada Skill candidata possui escopo, limites, evidências, testes e critérios de promoção.

## AC06 — Installation
Existe procedimento determinístico para Debian 12 com preflight e pós-validação.

## AC07 — Diagnosis
Existe diagnóstico em camadas sem alteração implícita.

## AC08 — Recovery
Backup, restore, upgrade e rollback possuem critérios verificáveis.

## AC09 — Golden Host
Existe baseline reproduzível para provisionamento rápido.

## AC10 — Runbook
Incidentes comuns possuem diagnóstico inicial determinístico.

## AC11 — Harness
Execução respeita `Goal → Maker/Codex → PR → CI → Checker → approve → merge`.

## AC12 — Security
Segredos não são armazenados; ações destrutivas possuem gate e autorização.

## AC13 — Homologation
O fluxo completo é validado em ambiente controlado antes de promoção.

## Condição de conclusão
Todos os AC aplicáveis possuem evidência `PASS`, ou `N/A` formalmente justificado pelo Checker.
