# Comandos candidatos por plataforma

Aplicar a [classificação formal](command-classification.md). Estes comandos são candidatos, não scripts. Confirmar fabricante, modelo, versão, modo CLI e sintaxe com a skill específica e a ajuda contextual antes do uso.

## Huawei MA5800

Sequência de leitura ainda não validada em equipamento real para esta skill:

1. Contexto e versão: `[INFERIDO] display version`.
2. Descoberta da configuração: `[INFERIDO] display current-configuration ?`.
3. Configuração corrente: `[INFERIDO] display current-configuration`.
4. Desabilitação de paginação: `[PENDENTE DE VALIDAÇÃO]`.
5. Marcador inequívoco de fim da configuração: `[PENDENTE DE VALIDAÇÃO]`.

Sem sintaxe validada de paginação ou marcador final, não declarar a coleta completa. Tratar `save`, exportação, transferência para servidor, reboot e restauração como `[PROIBIDO]` no fluxo automático.

## Cisco ASR1001-X / IOS XE

Sequência de leitura ainda não validada no equipamento-alvo:

1. Contexto e versão: `[INFERIDO] show version`.
2. Controle de paginação da sessão: `[INFERIDO] terminal length 0`; validar efeito e sintaxe no alvo antes de usar.
3. Configuração corrente: `[INFERIDO] show running-config`.
4. Configuração persistida: `[INFERIDO] show startup-config`.
5. Marcador final: `[INFERIDO]` retorno ao prompt EXEC esperado, sem `--More--`, timeout, desconexão ou erro.

Classificar `copy running-config startup-config`, `write memory`, exportação, transferência para servidor, reload e restauração como `[PROIBIDO]` no fluxo automático. Eles persistem ou alteram estado e nunca fazem parte implícita de uma coleta somente de leitura.

## Plataformas sem procedimento

Não inventar sintaxe. Consultar ajuda contextual somente quando comprovadamente segura, registrar a lacuna como `[PENDENTE DE VALIDAÇÃO]` e propor extensão parametrizada. Não coletar até existir critério verificável de completude.
