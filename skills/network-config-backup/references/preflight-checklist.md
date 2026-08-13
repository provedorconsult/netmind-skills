# Checklist de readiness

Interromper a coleta se qualquer item obrigatório estiver ausente ou divergente.

- [ ] Equipamento existe no inventário do Source of Truth.
- [ ] Nome canônico confirmado.
- [ ] Fabricante confirmado.
- [ ] Modelo confirmado.
- [ ] Endereço de gerenciamento autorizado.
- [ ] Acesso e janela de leitura autorizados.
- [ ] Alvo da sessão confere com o inventário.
- [ ] Comando candidato identificado para a plataforma.
- [ ] Sintaxe e modo CLI validados no contexto.
- [ ] Classificação do comando registrada.
- [ ] Paginação tratada sem comando mutável não autorizado.
- [ ] Timeout `${READ_TIMEOUT_SECONDS}` definido.
- [ ] Marcador `${EXPECTED_END_MARKER}` definido.
- [ ] Diretório de destino corresponde à categoria e ao nome canônico.
- [ ] Arquivo de destino não existe.
- [ ] Backup anterior identificado ou ausência registrada.
- [ ] Sanitização e revisão manual disponíveis.
- [ ] Mecanismo e destino da evidência definidos.
- [ ] Critérios de completude, falha e abort definidos.
