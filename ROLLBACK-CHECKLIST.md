# Checklist de rollback

- [ ] Definir critério de abort antes da mudança.
- [ ] Capturar displays e parâmetros completos do estado anterior.
- [ ] Mapear referências e Binding times.
- [ ] Confirmar que nenhum objeto é default/compartilhado.
- [ ] Validar sintaxe reversa com `?` antes da janela.
- [ ] Obter autorização explícita para comandos destrutivos.
- [ ] Garantir acesso de gestão/out-of-band.
- [ ] Reverter na ordem inversa da criação.
- [ ] Remover WAN route/PPPoE com sintaxe validada e restaurar o baseline bridge da ONT de bancada.
- [ ] Parar ao primeiro erro de rollback e reconsultar estado.
- [ ] Validar ONT, service-port, VLAN, uplink, PPPoE e gestão.
- [ ] Registrar resultado e objetos residuais.
- [ ] Nunca improvisar delete/undo.
