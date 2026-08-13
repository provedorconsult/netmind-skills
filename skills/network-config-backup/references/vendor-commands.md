# Comandos candidatos por plataforma

Aplicar a [classificação formal](command-classification.md). Estes comandos são candidatos, não scripts. Confirmar fabricante, modelo, versão, modo CLI e sintaxe com a skill específica e a ajuda contextual antes do uso.

## Huawei MA5800

Contexto validado: MA5800-X7, MA5800V100R018C00, patch SPH507, user view. Ver [evidência sanitizada](validated-contexts.md).

1. Contexto e versão: `[CONFIRMADO] display version`; a CLI exige confirmação `<cr>`.
2. Paginação da versão: `[CONFIRMADO]` avanço manual com espaço no prompt `---- More`.
3. Marcador final da versão: `[CONFIRMADO]` retorno ao prompt de user view.
4. Configuração corrente global: `[PENDENTE DE VALIDAÇÃO] display current-configuration`; nessa visão, a CLI exigiu `interface`, `ont`, `port` ou `service-port` e não retornou configuração.
5. Sequência completa de backup: `[PENDENTE DE VALIDAÇÃO]`; não declarar sucesso com coleta parcial por filtros.

### Discovery seguro para futura sessão autorizada

1. Confirmar fabricante, modelo, release, patch, user view e autorização somente para discovery; parar se o contexto divergir.
2. Executar `[PENDENTE DE VALIDAÇÃO] display current-configuration ?` literalmente, sem completar uma opção nem pressionar Enter após remover `?`.
3. Registrar a saída sanitizada da ajuda, inclusive `<cr>`, opções, filtros, mensagens de erro e prompt final. Uma opção apenas exibida permanece `[DISCOVERY]`; não vira `[CONFIRMADO]`.
4. Observar se a própria ajuda pagina. Se houver paginação, usar somente avanço manual já validado no contexto e interromper se qualquer entrada puder ser interpretada como comando.
5. Não executar os filtros exibidos nesta etapa. Propor uma coleta posterior somente se a ajuda permitir construir uma cobertura verificavelmente exaustiva, sem sintaxe presumida.

Critério de completude para uma futura coleta: todos os domínios de configuração enumerados pela própria CLI devem estar cobertos uma única vez; cada saída deve começar no contexto esperado, terminar no prompt esperado e não conter paginação residual, erro, timeout, desconexão ou truncamento. Se a CLI não fornecer uma enumeração exaustiva ou se qualquer domínio não puder ser coletado, o resultado permanece `[PENDENTE DE VALIDAÇÃO]` e nenhum conjunto parcial deve ser publicado como backup.

Tratar `save`, escrita, cópia, exportação, transferência para servidor, reload, reboot e restauração como `[PROIBIDO]` no fluxo automático.

## Cisco ASR1001-X / IOS XE

Contexto validado: ASR1001-X, IOS XE 17.09.03a, privileged EXEC. Ver [evidência sanitizada](validated-contexts.md).

1. Contexto e versão: `[CONFIRMADO] show version`.
2. Descoberta de paginação: `[CONFIRMADO] terminal length ?`; a CLI informou a faixa `0-512` e `0` como sem pausas.
3. Controle de paginação da sessão: `[CONFIRMADO] terminal length 0`; efeito limitado à sessão observada.
4. Configuração corrente: `[CONFIRMADO] show running-config`; cabeçalho, linha `end` e retorno ao prompt observados sem paginação ou truncamento.
5. Configuração persistida: `[INFERIDO] show startup-config`; não executado na validação.
6. Marcador final: `[CONFIRMADO]` retorno ao prompt privileged EXEC depois da linha `end`.

Classificar `copy running-config startup-config`, `write memory`, exportação, transferência para servidor, reload e restauração como `[PROIBIDO]` no fluxo automático. Eles persistem ou alteram estado e nunca fazem parte implícita de uma coleta somente de leitura.

## Plataformas sem procedimento

Não inventar sintaxe. Consultar ajuda contextual somente quando comprovadamente segura, registrar a lacuna como `[PENDENTE DE VALIDAÇÃO]` e propor extensão parametrizada. Não coletar até existir critério verificável de completude.
