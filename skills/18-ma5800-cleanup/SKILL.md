---
name: 18-ma5800-cleanup
description: Auditar e remover somente objetos órfãos da MA5800-X7 com confirmação explícita, referências, bind-times, impacto e rollback.
---

# Cleanup MA5800

## Objetivo

Evitar acúmulo sem remover objetos ativos ou default.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Janela, autorização de exclusão, inventário completo e backup textual.

## Comandos confirmados

- [CONFIRMADO] `display dba-profile all`
- [CONFIRMADO][DESTRUTIVO] `dba-profile delete profile-id 100`
- [CONFIRMADO][DESTRUTIVO] `dba-profile delete profile-id 101`

## Comandos de descoberta

- [DISCOVERY] Descobrir sintaxe de remoção para outros tipos; não extrapolar `dba-profile delete`.

## Sintaxe

Após as duas exclusões confirmadas, IDs 100 e 101 deixaram de aparecer.

## Exemplos

Antes de excluir DBA: consultar profile, bind-times, line profiles/T-CONT e `display dba-profile all`.

## Resultado esperado

Somente objeto explicitamente aprovado deixa de aparecer; dependentes permanecem íntegros.

## Erros conhecidos

`does not exist` exige confirmar ID/contexto; `already existed` não prova consultabilidade.

## Diagnóstico

Localizar referências em ambas as direções e confirmar zero uso.

## Dependências

Line profiles, T-CONTs, ONTs e service-ports.

## Riscos

Exclusão é destrutiva e pode interromper várias ONTs.

## Rollback

Recriar requer parâmetros exatos e ID disponível; registrar tudo antes.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não apagar automaticamente; não excluir default; não confiar só em nome/ID.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

