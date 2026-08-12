# Checklist de provisionamento de ONT

- [ ] Confirmar MA5800V100R018/SPH507 ou marcar divergência.
- [ ] Confirmar board/PON normal e F/S/P.
- [ ] Consultar autofind e validar SN, VendorID, EquipmentID e local físico.
- [ ] Consultar `display dba-profile all`, ID, valores e Binding times.
- [ ] Validar capacidade/ont-type contra DBA Max.
- [ ] Consultar line profile, T-CONT e GEM.
- [ ] Consultar service profile e ETH/VLAN.
- [ ] Confirmar ONT-ID e service-port ID livres.
- [ ] Registrar baseline e rollback; obter autorização.
- [ ] Executar somente comando confirmado ou redescoberto com `?`.
- [ ] Confirmar sucesso do `ont add`.
- [ ] Confirmar ONT online, SN/modelo e óptica.
- [ ] Criar/validar service-port somente após GEM/ONT.
- [ ] Confirmar service-port up.
- [ ] Confirmar VLAN 100 na PON e uplink.
- [ ] Confirmar chegada ao BNG, PPPoE, AAA e IP.
- [ ] Não registrar credenciais.

