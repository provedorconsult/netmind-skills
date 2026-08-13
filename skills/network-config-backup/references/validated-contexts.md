# Contextos validados

Este documento registra somente evidância reutilizável de plataforma. IPs, hostnames, usuários, seriais, configurações e topologia do ambiente observado foram deliberadamente excluídos.

## Huawei MA5800-X7

- Data da validação: 12-08-2026.

| Classificação/comando | Fabricante e modelo | Contexto | Escopo confirmado | Limitações |
|---|---|---|---|---|
| `[CONFIRMADO] display version` | Huawei MA5800-X7 | MA5800V100R018C00/SPH507, user view | O comando foi aceito, confirmou produto, release e patch e retornou ao prompt | Exigiu `<cr>` e avanço manual de uma página; não generalizar para outra release, modelo ou modo |
| `[PENDENTE DE VALIDAÇÃO] display current-configuration` | Huawei MA5800-X7 | MA5800V100R018C00/SPH507, user view | A tentativa sem argumento observou que a CLI exigiu um filtro | Nenhum filtro foi executado ou confirmado, nenhuma configuração foi coletada e não há critério de completude validado |

- Resultado de backup: falha controlada; nenhum backup parcial foi promovido a sucesso.

## Cisco ASR1001-X

- Data da validação: 12-08-2026.

| Classificação/comando | Fabricante e modelo | Contexto | Escopo confirmado | Limitações |
|---|---|---|---|---|
| `[CONFIRMADO] show version` | Cisco ASR1001-X | IOS XE 17.09.03a, privileged EXEC | O comando foi aceito e a coleta de versão foi concluída | A primeira tentativa paginada foi invalidada; não generalizar para outra release, modelo ou modo |
| `[CONFIRMADO] terminal length ?` | Cisco ASR1001-X | IOS XE 17.09.03a, privileged EXEC | A ajuda informou faixa `0-512` e `0` para desabilitar pausas | Confirma somente a ajuda observada nesse contexto |
| `[CONFIRMADO] terminal length 0` | Cisco ASR1001-X | IOS XE 17.09.03a, privileged EXEC | O comando foi aceito e removeu pausas na coleta subsequente | Efeito limitado à sessão observada; não persiste configuração |
| `[CONFIRMADO] show running-config` | Cisco ASR1001-X | IOS XE 17.09.03a, privileged EXEC, após `terminal length 0` | Saída completa com cabeçalho, linha `end`, prompt final e sem marcador de paginação | A saída exige sanitização antes de versionar; não confirma a configuração persistida |
| `[INFERIDO] show startup-config` | Cisco ASR1001-X | IOS XE 17.09.03a, privileged EXEC | Nenhum; comando não executado | Permanece inferido até evidência real |

- Resultado de backup: coleta completa antes da sanitização externa ao repositório.

## Limites

- A confirmação vale somente para plataforma, software e contexto registrados.
- Credenciais foram fornecidas por canal local ignorado pelo Git e não fazem parte desta evidância.
- Nenhum comando de configuração, persistência, exportação, reload ou restauração foi executado.
- Não usar esta evidância para inferir que os equipamentos existam em outra rede.
