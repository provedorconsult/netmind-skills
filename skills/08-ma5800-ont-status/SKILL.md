---
name: 08-ma5800-ont-status
description: Verificar estado, identidade, distância e potência óptica de ONT GPON na MA5800-X7 R018 sem alterar configuração.
---

# Status Operacional da ONT

## Objetivo

Confirmar se a ONT existe e está online no F/S/P correto.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Conhecer F/S/P; acesso de leitura.

## Comandos confirmados

- [CONFIRMADO] `display ont info summary 0/1/0`

## Comandos de descoberta

- [DISCOVERY] `display ont info summary ?`.

## Sintaxe

Usar F/S/P completo. `display ont info 0/1` não é válido neste contexto.

## Exemplos

Exemplo parametrizado: ONT `${ONT_ID}` online, SN `${ONT_SERIAL}`, modelo `${ONT_MODEL}`, distância `${ONT_DISTANCE}`, Rx/Tx `${ONT_RX_DBM}`/`${ONT_TX_DBM}`.

## Resultado esperado

total 1, online 1 e identidade correspondente.

## Erros conhecidos

[ERRO] `display ont info 0/1` foi rejeitado; [ERRO] `Failure: The ONT does not exist`.

## Diagnóstico

Confirmar F/S/P e ONT-ID, autofind, provisionamento, alimentação e óptica.

## Dependências

ONT adicionada na PON 0/1/0.

## Riscos

Interpretar potência sem limites documentados da óptica pode gerar diagnóstico errado.

## Rollback

Não aplicável.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não declarar a ONT saudável apenas por estar online; correlacionar serviço e óptica.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.
