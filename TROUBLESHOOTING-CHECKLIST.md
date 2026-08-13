# Checklist de troubleshooting

- [ ] Registrar horário, release, patch, escopo e sintoma.
- [ ] Preservar comando e erro literalmente.
- [ ] Aplicar os 20 nós da decision tree e parar na primeira falha.
- [ ] OLT acessível; boards e PON normais.
- [ ] Autofind/ONT adicionada/ONT online.
- [ ] DBA/profile/bind-times compatíveis.
- [ ] T-CONT e GEM presentes.
- [ ] Em `mapping-mode VLAN`, GEM mapping explícito liga a VLAN/flow de serviço ao GEM usado pelo service-port.
- [ ] Service-port existe, está up e possui contadores coerentes com a tentativa de serviço.
- [ ] VLAN na PON e uplink.
- [ ] Uplink físico/placa normal.
- [ ] WAN route/profile está aplicada à ONT de bancada.
- [ ] VLAN chega ao BNG.
- [ ] PADI/PADO/PADR/PADS e LCP chegam ao estado esperado.
- [ ] AAA/RADIUS responde.
- [ ] ONT recebe IP por IPCP e possui rota/DNS.
- [ ] NAT, DHCP e bindings LAN/Wi-Fi funcionam.
- [ ] Usar `?` para sintaxe desconhecida.
- [ ] Não mudar camada posterior nem fazer múltiplas mudanças.

## Assinatura de falha: GEM mapping ausente

Se a ONT está online, o service-port está `up`, a VLAN existe na PON/uplink, mas o service-port permanece em zero bytes/pacotes, a WAN PPPoE está `Disconnected` e o BNG não registra PADI/PADR, verificar primeiro se o line profile contém um mapping explícito da VLAN/flow para o GEM referenciado pelo service-port. Não atribuir automaticamente a falha a AAA, NAT, RADIUS ou `Match state: mismatch`.
