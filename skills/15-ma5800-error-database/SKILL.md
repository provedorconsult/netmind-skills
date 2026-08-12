---
name: 15-ma5800-error-database
description: Interpretar erros literais observados na MA5800-X7 R018 e escolher verificações seguras sem assumir estado de objetos.
---

# Banco de Erros MA5800

## Objetivo

Mapear mensagem → diagnóstico → ação de leitura.

## Quando usar

Usar quando a tarefa corresponder à descrição desta Skill. Validar primeiro release, patch, modo CLI e escopo.

## Pré-requisitos

Copiar erro literalmente, modo e comando.

## Comandos confirmados

- [CONFIRMADO] Usar os displays apontados em `MA5800-ERROR-DATABASE.md`.

## Comandos de descoberta

- [DISCOVERY] Descobrir somente sintaxe ausente com `?`.

## Sintaxe

Não normalizar nem traduzir o texto do erro no registro.

## Exemplos

`already existed` não prova que `display ... profile-id` terá sucesso.

## Resultado esperado

Erro classificado, hipótese limitada e verificação não destrutiva.

## Erros conhecidos

Oito mensagens canônicas estão no documento global.

## Diagnóstico

Correlacionar contexto, ID, references/bind-times e primeira camada falha.

## Dependências

CLI commands e decision tree.

## Riscos

Ação baseada apenas na mensagem pode apagar objeto errado.

## Rollback

Nenhuma ação automática; cada correção deve ter rollback.

## Regras de segurança

Preferir `display`; classificar cada comando; consultar referências e Binding times; exigir confirmação explícita para `[DESTRUTIVO]`; não registrar credenciais; tratar a CLI desta OLT como autoridade.

## O que NÃO fazer

Não converter erro em autorização para criar, reduzir ou excluir.

## Fonte

- Evidência primária: sessão CLI fornecida pelo operador, MA5800V100R018, patch SPH507.
- Referência oficial Huawei: portal de suporte MA5800 e guias oficiais listados no README.
- A CLI do equipamento prevalece sobre documentação. Marcar material de outra release como `[VERSÃO DIFERENTE]`.

