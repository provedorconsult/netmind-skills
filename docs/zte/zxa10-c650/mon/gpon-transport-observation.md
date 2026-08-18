---
fabricante: zte
modelo: [zxa10-c650]
categoria: mon
topicos: [gpon, onu, tcont, gemport, vlan, service-port, uplink]
descricao: "Consultas somente leitura comprovadas para observar GPON, transporte e service-port na ZXA10 C650 V1.1.2."
versao_firmware_testada: "ZTE ZXA10 Software V1.1.2"
ultima_atualizacao: "2026-08-18"
---

# ZTE ZXA10 C650 — observação GPON e transporte

## Escopo e sanitização

Estas são consultas `READ` observadas em uma C650 V1.1.2. Saídas de ONUs podem
conter serial, estado por assinante e descrição de circuito: preserve a coleta
bruta fora do Git e publique apenas agregados e exemplos anonimizados.

## Consultas confirmadas

```cli
show gpon slot config <slot-confirmado>
show gpon olt config <gpon_olt-confirmada>
show gpon onu state
show gpon onu baseinfo <gpon_olt-confirmada>
show gpon onu tcont <gpon_olt-confirmada>
show gpon onu gemport <gpon_olt-confirmada>
show gpon onu vport <gpon_olt-confirmada>
show service-port interface <gpon_onu-confirmada>
show vlan port <xgei-confirmada>
```

No contexto observado, as placas GPON usavam autenticação `hybrid`; T-CONT,
perfil de VLAN, GEM port, vport e service-port aparecem como objetos distintos.
O `show gpon onu state` exibiu estados `working`, `OffLine`, `LOS` e
`DyingGasp`, portanto estado administrativo não deve ser confundido com saúde
operacional.

## Padrões observados

- Os perfis T-CONT listam tipo e limites FBW, ABW e MBW em kbps.
- Perfis ONU de VLAN expõem nome, modo de tag, CVLAN e prioridade.
- Uma interface XGE observada usava modo trunk e TPID `0x8100`; a lista de VLANs
  e as descrições do uplink são específicas do alvo e não são reproduzidas aqui.
- O service-port observado associa vport e VLAN e informa status e habilitação.

## Validação e troubleshooting

1. Use `show gpon onu state` para separar `working`, `OffLine`, `LOS` e
   `DyingGasp` sem registrar identificadores de assinante.
2. Para uma ONU já autorizada e confirmada no Source of Truth, compare T-CONT,
   GEM port, vport e service-port da mesma referência de interface.
3. Confira o transporte na interface XGE confirmada com `show vlan port`.
4. Se a ajuda contextual não aceitar a referência, pare e registre o retorno
   como `ERRO`; não entre em modo de configuração para tentar corrigir.

Nenhum destes comandos autoriza criação de ONU, perfil, VLAN, GEM, T-CONT ou
service-port, nem `save`, `write`, `commit`, reload ou reset.
