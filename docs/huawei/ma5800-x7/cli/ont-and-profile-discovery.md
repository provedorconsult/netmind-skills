---
fabricante: huawei
modelo: [ma5800-x7]
categoria: cli
topicos: [discovery, ont, profiles, dba]
descricao: "Consultas seguras para inventariar ONTs, perfis e DBA na MA5800-X7."
versao_firmware_testada: "MA5800V100R018 / SPH507"
ultima_atualizacao: "2026-08-15"
---

# Descoberta de ONT, perfis e DBA

Fonte legada: `MA5800-CLI-COMMANDS.md` e `COMMAND-MATRIX.md`. Esta é
evidência de leitura; não é um script de operação.

## Pré-condições

- Confirmar equipamento autorizado, release e contexto da CLI.
- Usar somente escopo `READ` ou `DISCOVERY`.
- Preservar o retorno literal e parar diante de identidade divergente.

## Consultas confirmadas

Os comandos abaixo estão `[CONFIRMADO]` na base MA5800V100R018/SPH507 e têm
risco baixo.

```text
display dba-profile all
display dba-profile all detail
display ont-lineprofile gpon all
display ont-lineprofile gpon all detail
display ont-srvprofile gpon all
display ont autofind all
display ont info summary 0/1/0
```

Use `display dba-profile all` antes de reutilizar um ID. Para investigar o
caminho de argumento sem alterar estado, a evidência legada registra
`display ont info summary ?` como `[DISCOVERY]`.

## Forma rejeitada preservada

```text
display ont info 0/1
```

Esta forma foi `[ERRO]` na CLI observada. Não inferir argumentos a partir dela;
redescobrir a sintaxe com `?` no contexto real.

## Limites

Os resultados não autorizam configuração. Qualquer comando desconhecido deve
ser descoberto com `?`; confirmar versão, alvo e contexto antes de reutilizar
esta evidência.
