# Contextos validados

Este documento registra somente evidância reutilizável de plataforma. IPs, hostnames, usuários, seriais, configurações e topologia do ambiente observado foram deliberadamente excluídos.

## Huawei MA5800-X7

- Data da validação: 12-08-2026.
- Plataforma: MA5800-X7.
- Software: MA5800V100R018C00, patch SPH507.
- Contexto: user view.
- `[CONFIRMADO] display version`: aceito; exigiu `<cr>`, apresentou uma página e retornou ao prompt após avanço manual.
- `[PENDENTE DE VALIDAÇÃO] display current-configuration`: sem argumento, exigiu um filtro entre `interface`, `ont`, `port` e `service-port`; nenhuma configuração foi coletada.
- Resultado de backup: falha controlada; nenhum backup parcial foi promovido a sucesso.

## Cisco ASR1001-X

- Data da validação: 12-08-2026.
- Plataforma: ASR1001-X.
- Software: IOS XE 17.09.03a.
- Contexto: privileged EXEC.
- `[CONFIRMADO] show version`: aceito e concluído.
- `[CONFIRMADO] terminal length ?`: informou faixa `0-512` e `0` para desabilitar pausas.
- `[CONFIRMADO] terminal length 0`: aceito, com efeito somente na sessão.
- `[CONFIRMADO] show running-config`: aceito; saída com cabeçalho, `end`, prompt final e sem marcador de paginação.
- `[INFERIDO] show startup-config`: não executado.
- Resultado de backup: coleta completa antes da sanitização externa ao repositório.

## Limites

- A confirmação vale somente para plataforma, software e contexto registrados.
- Credenciais foram fornecidas por canal local ignorado pelo Git e não fazem parte desta evidância.
- Nenhum comando de configuração, persistência, exportação, reload ou restauração foi executado.
- Não usar esta evidância para inferir que os equipamentos existam em outra rede.
