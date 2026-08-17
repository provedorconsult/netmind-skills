# Guia das Demandas — NetMind Skills

Este arquivo é o índice operacional das demandas analisadas pelo Checker.

A pasta `demandas/` contém o material de entrada para planejamento e execução dos próximos Goals. Este guia registra o entendimento atual do Checker, a ordem técnica recomendada e o estado de liberação de cada demanda.

## Regra operacional

- O arquivo da demanda é a fonte do escopo específico.
- Este guia define a ordem e o estado de liberação.
- O Maker executa somente o Goal explicitamente autorizado pelo Checker.
- Uma demanda `DEFER`, `REWORK` ou `BLOCKED` não deve ser executada por iniciativa do Maker.
- O Checker deve revisar a PR no HEAD efetivamente submetido e emitir o veredito conforme o Harness.
- CI verde não substitui revisão do Checker nem autoriza merge por si só.

## Fluxo

```text
Demanda
  → análise do Checker
  → Goal autorizado
  → prompt conciso para o Maker
  → Maker
  → PR
  → CI
  → Checker
  → approve / request-changes / blocked
  → merge gate
  → pós-merge
  → próximo Goal
```

## Classificações do Checker

| Estado | Significado |
|---|---|
| `READY` | Demanda suficientemente definida e liberada para virar execução. |
| `ACCEPT` | Demanda aceita como Goal, aguardando autorização operacional. |
| `REWORK` | Escopo precisa ser ajustado antes da execução. |
| `DEFER` | Demanda válida, mas dependências ou prioridade recomendam adiamento. |
| `BLOCKED` | Pré-condição necessária não está disponível. |
| `REJECT` | Demanda não deve ser executada. |

## Ordem técnica recomendada

### Fase A — Governança e integridade

| Ordem | Demanda | Estado atual | Decisão |
|---:|---|---|---|
| 1 | [01 — Harden Harness Merge Gate](01-HARDEN-HARNESS-MERGE-GATE.md) | `READY` | Primeiro Goal autorizado |
| 2 | [02 — Equipment Registry Evidence Integrity](02-EQUIPMENT-REGISTRY-EVIDENCE-INTEGRITY.md) | `ACCEPT` | Focar integridade real de âncoras |
| 3 | [15 — Metadata GitHub e Issues](15-METADATA-GITHUB-E-ISSUES.md) | `ACCEPT` | Pode ser executada sem bloquear o núcleo |
| 4 | [16 — Reduzir ruído do Secret Scan](16-REDUZIR-RUIDO-SECRET-SCAN.md) | `ACCEPT` | Correção contextual, sem allowlist ampla |

### Fase B — Identidade

| Ordem | Demanda | Estado atual | Decisão |
|---:|---|---|---|
| 5 | [05 — Device Fingerprint v1](05-DEVICE-FINGERPRINT-V1.md) | `ACCEPT` | Contrato/schema antes da coleta real |

### Fase C — Aplicabilidade

| Ordem | Demanda | Estado atual | Decisão |
|---:|---|---|---|
| 6 | [03 — Compatibility Registry v1](03-COMPATIBILITY-REGISTRY-V1.md) | `ACCEPT` | Sem inferência de compatibilidade |
| 7 | [04 — Capability Registry v1](04-CAPABILITY-REGISTRY-V1.md) | `ACCEPT` | Capability não concede autorização operacional |
| 8 | [06 — Skill Router v1](06-SKILL-ROUTER-V1.md) | `ACCEPT` | Depende de Fingerprint + Compatibility + Capability |

### Fase D — Conhecimento operacional

| Ordem | Demanda | Estado atual | Decisão |
|---:|---|---|---|
| 9 | [07 — Command Registry](07-COMMAND-REGISTRY.md) | `ACCEPT` | Contrato primeiro; migração incremental |
| 10 | [08 — Error Registry](08-ERROR-REGISTRY.md) | `ACCEPT` | Preservar versão e contexto |
| 11 | [09 — Procedure/Evidence Registries](09-PROCEDURE-EVIDENCE-REGISTRIES.md) | `REWORK` | Separar conceitualmente Procedure de Evidence |

### Fase E — Migração

| Ordem | Demanda | Estado atual | Decisão |
|---:|---|---|---|
| 12 | [10 — Huawei Full Migration](10-HUAWEI-FULL-MIGRATION.md) | `ACCEPT` | Migração incremental e auditável |
| 13 | [11 — Cisco Full Migration](11-CISCO-FULL-MIGRATION.md) | `ACCEPT` | Não generalizar versão/CLI sem evidência |

### Fase F — Expansão

| Ordem | Demanda | Estado atual | Decisão |
|---:|---|---|---|
| 14 | [12 — Multi-vendor Expansion](12-MULTI-VENDOR-EXPANSION.md) | `DEFER` | Após estabilização dos registries base |

### Fase G — Validação final

| Ordem | Demanda | Estado atual | Decisão |
|---:|---|---|---|
| 15 | [13 — E2E AI-Native Validation](13-E2E-AI-NATIVE-VALIDATION.md) | `DEFER` | Somente após implementação funcional do núcleo |
| 16 | [14 — Final Release Gate](14-FINAL-RELEASE-GATE.md) | `DEFER` | Último gate do ciclo |

## Documentos auxiliares

- [Instruções do Checker](00-INSTRUCOES-CHECKER.md)
- [Matriz das demandas](98-MATRIZ-DEMANDAS.md)
- [Ordem original/recomendada](99-ORDEM-RECOMENDADA.md)

## Núcleo arquitetural

A sequência que deve ser preservada é:

```text
Device Fingerprint
    ↓
Equipment Registry
    ↓
Compatibility Registry
    ↓
Capability Registry
    ↓
Skill Router
    ↓
Command / Procedure / Error / Evidence
```

O Equipment Registry representa identidade técnica e evidência. Não deve ser usado para inferir capability, compatibility ou autorização operacional.

## Estado atual do Checker

**Pacote:** `chore/add-checker-demands`

**Commit de origem:** `44d0a11 chore: add checker demand package`

**Próximo Goal:** `01 — Harden Harness Merge Gate`

**Status:** `READY FOR MAKER`

Este guia não autoriza merge. A autorização de merge continua sujeita ao Harness, CI e veredito do Checker no HEAD efetivamente revisado.
