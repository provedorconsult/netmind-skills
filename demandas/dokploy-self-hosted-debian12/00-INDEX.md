# DEMANDA — Dokploy Self-Hosted / Debian 12

## Objetivo
Transformar evidências reais dos repositórios `provedorconsult` e do Dokploy atual em conhecimento operacional, Skills NetMind, diagnóstico rápido e procedimento reproduzível para provisionar um host Debian 12 com Dokploy.

## Escopo
Discovery GitHub, forensics histórico, auditoria read-only do ambiente atual, arquitetura canônica, preflight, instalação, diagnóstico, storage/backup/restore, upgrade/rollback, Golden Host, incident runbook, integração Harness e homologação.

## Fora de escopo
Implementação imediata das Skills, alterações no Dokploy atual, mudanças destrutivas, merge automático ou promoção de evidência histórica a padrão sem validação.

## Ordem dos Goals

| Goal | Arquivo | Dependência | Resultado |
|---|---|---|---|
| G01 | 01-G01-DISCOVERY-GITHUB.md | — | Inventário |
| G02 | 02-G02-FORENSICS-HISTORICO.md | G01 | Base histórica |
| G03 | 03-G03-AUDITORIA-DOKPLOY-ATUAL.md | G01/G02 | Snapshot |
| G04 | 04-G04-ARQUITETURA-CANONICA.md | G02/G03 | Baseline |
| G05 | 05-G05-SKILL-PREFLIGHT.md | G04 | Preflight |
| G06 | 06-G06-SKILL-INSTALL-DEBIAN12.md | G05 | Instalação |
| G07 | 07-G07-SKILLS-DIAGNOSTICO.md | G04 | Diagnóstico |
| G08 | 08-G08-BACKUP-RESTORE-STORAGE.md | G04/G07 | DR |
| G09 | 09-G09-UPGRADE-ROLLBACK.md | G04/G08 | Ciclo de vida |
| G10 | 10-G10-GOLDEN-HOST.md | G06/G08/G09 | Host padrão |
| G11 | 11-G11-INCIDENT-RUNBOOK.md | G07/G08/G09 | Runbook |
| G12 | 12-G12-HARNESS-CHECKER-MAKER.md | G05–G11 | Governança |
| G13 | 13-G13-HOMOLOGACAO-FINAL.md | G10–G12 | Validação final |

## Estado
`PLANNED` — demanda criada para execução posterior por Goals isolados.

## Regra de execução
`Goal → Maker/Codex → PR → CI → Checker → approve → merge`.
CI verde não autoriza merge. Cada Goal deve possuir evidência verificável e não pode alterar escopo de Goals posteriores.

## Regras de segurança
`READ BEFORE WRITE`; `EVIDENCE BEFORE DIAGNOSIS`; `DIAGNOSIS BEFORE ACTION`; `AUTHORIZATION BEFORE DESTRUCTIVE ACTION`; `VALIDATION AFTER ACTION`.

## Estado histórico versus canônico
Toda descoberta deve ser classificada como `CURRENT`, `LEGACY`, `CANONICAL`, `CONFIRMADO`, `DISCOVERY`, `INFERIDO`, `ERRO` ou `VERSÃO DIFERENTE`, conforme aplicável. Evidência de outro release não deve ser promovida automaticamente.
