# Arquitetura canônica do NetMind Skills

## Decisão

O NetMind Skills é um **Network Equipment Skill Registry AI-Native**.
A arquitetura canônica é um contrato lógico para identificar equipamento,
compatibilidade, capacidades, Skills e evidências. A árvore atual de `docs/`
é a projeção operacional de navegação; não é substituída neste Goal.

```text
Device Fingerprint
  → Equipment Registry → Compatibility Registry → Capability Registry
  → Skill Router → Skill / Command / Procedure / Error / Evidence
```

## Estrutura física atual

| Área | Estado atual | Papel canônico |
|---|---|---|
| `docs/<fabricante>/<modelo>/<categoria>/` | Dois fabricantes, dois modelos, cinco categorias. | Projeção navegável de módulos ativos. |
| `INDEX.md`, `docs/*/INDEX.md`, `llms.txt` | Gerados pelo builder. | Pontos de entrada e navegação. |
| `skills/` | Skills legadas parametrizadas e catálogos. | Fonte histórica para registro/migração incremental. |
| Catálogos legados | Comandos, erros, procedimentos e evidências. | Fontes de registries futuros. |
| `.harness/` | Goals, PR, CI e Checker. | Processo de mudança, não registry. |

As categorias são `cli`, `config`, `diag`, `mon` e `update`.
`categoria: index` é metadado exclusivo de navegação. Versão, firmware e
patch aparecem apenas quando a fonte existente os comprova; não há registry
central versionado.

## Identidade e roteamento

Um Device Fingerprint é descoberta sanitizada, nunca credencial ou dado de
cliente:

```text
manufacturer → family → model → software/CLI → version → firmware/patch
→ observed capabilities → evidence reference
```

O Skill Router usa campos comprovados para consultar Equipment, Compatibility
e Capability registries. Ele seleciona Skills, procedimentos, comandos,
diagnósticos e rollback, preservando `[CONFIRMADO]`, `[DISCOVERY]`,
`[INFERIDO]`, `[ERRO]` e classes de risco existentes. Ausência de contexto
exige discovery seguro ou bloqueio, nunca inferência.

## Componentes canônicos

| Componente | Responsabilidade | Estado atual |
|---|---|---|
| Device Fingerprint | Contexto observado e evidência sanitizada. | Contrato; coleta futura. |
| Equipment Registry | Fabricante, família, modelo e software. | Dados distribuídos; registry futuro. |
| Compatibility Registry | Compatibilidade explícita. | Futuro; não inferir por caminho. |
| Capability Registry | Capability, pré-condições e evidência. | Futuro; evidência distribuída. |
| Command Registry | Comando, contexto, risco, versão e evidência. | Catálogos legados; normalização futura. |
| Error Registry | Retorno literal, diagnóstico e ação segura. | Bancos legados; normalização futura. |
| Procedure Registry | Procedimento, validação, abort e rollback. | Skills/módulos; normalização futura. |
| Evidence Registry | Prova sanitizada, contexto e classificação. | Distribuída; registry futuro. |
| Skill Router | Seleção por fingerprint e registries. | Contrato; implementação futura. |

## Índices e compatibilidade

`llms.txt` é o ponto de entrada AI-Native. `INDEX.md` e índices de modelo
fornecem fabricante → modelo → categoria → módulo. O builder é determinístico.
Índices listam módulos ativos, mas não provam compatibilidade; o agente valida
fingerprint e evidência antes de executar. Futura `docs/_deprecated/` fica
fora dos índices operacionais conforme [a política](deprecation-policy.md).

## Decisões e consequências

| Decisão | Motivo | Consequência | Migração futura |
|---|---|---|---|
| Manter `docs/<fabricante>/<modelo>/<categoria>/`. | Navegação validada. | Índices e módulos atuais compatíveis. | Referências de registry sem mover massa. |
| Não usar diretórios para versão, firmware ou capability. | Caminho não prova compatibilidade. | Evita fatos inventados. | Registries explícitos com evidência. |
| Manter Skills/catálogos como fontes. | Preserva histórico técnico. | Nenhum conteúdo removido. | Migração por Goals dedicados. |
| Separar evidência de aplicabilidade. | Observação não se generaliza. | Router exige contexto comprovado. | Evidence/Compatibility registries. |
| Manter `.harness/` fora da taxonomia. | Governa mudança, não dispositivo. | Harness inalterado. | Endurecimento em Goal próprio. |

## Migrações futuras identificadas

1. Criar formatos versionados de Equipment, Compatibility e Capability
   registries com evidência obrigatória.
2. Normalizar comandos, erros e procedimentos sem apagar fontes legadas.
3. Implementar Skill Router conservador por fingerprint e compatibilidade.
4. Migrar Huawei e Cisco somente em Goals próprios com auditoria.
5. Criar registry MikroTik somente com fonte técnica primária.

## Limitações

Este Goal não cria registries completos, não altera Skills, não coleta
fingerprints reais e não declara versões, capacidades ou compatibilidades.
Não reproduz dados de clientes, credenciais ou evidência sensível.
