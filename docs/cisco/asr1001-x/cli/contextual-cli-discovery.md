---
fabricante: cisco
modelo: [asr1001-x]
categoria: cli
topicos: [discovery, cli, ios-xe, context]
descricao: "Descoberta contextual de sintaxe no Cisco ASR1001-X antes de comandos não confirmados."
versao_firmware_testada: "IOS XE 17.09.03a"
ultima_atualizacao: "2026-08-15"
---

# Descoberta contextual da CLI

Fonte legada: `skills/cisco-asr1001x/02-cli-discovery/SKILL.md`. A CLI real
prevalece; esta evidência não transforma comandos inferidos em sintaxe válida.

## Pré-requisitos

Identificar o ASR1001-X, executar `show version` de forma sanitizada e
confirmar modo, privilégio, escopo, release IOS XE e acesso alternativo antes
de qualquer mudança.

## Consultas candidatas

As linhas abaixo são `[INFERIDO]` na fonte e exigem ajuda contextual no modo
correto antes de uso:

```text
?
show ?
show interfaces ?
show ip ?
show bgp ?
show pppoe ?
show platform ?
configure terminal
interface ?
router ?
```

Executar um token por vez e registrar a saída sanitizada. Uma consulta aceita
é `[DISCOVERY]`; uma rejeição literal é `[ERRO]`; somente ação bem-sucedida
pode ser `[CONFIRMADO]`.

## Limites de segurança

Ajuda contextual em modo de configuração pode revelar opções mutáveis. Não
concluir linha mutável sem autorização e classificar toda mudança como
`[DESTRUTIVO]`. Não usar sintaxe de memória, expor segredos, fazer
reload/clear/reset como primeiro passo ou persistir antes da validação.
