---
fabricante: huawei
modelo: [ma5800-x7]
categoria: diag
topicos: [gem, mapping, service-port, pppoe]
descricao: "Diagnóstico de falha de serviço causada por GEM mapping ausente."
versao_firmware_testada: "MA5800V100R018 / SPH507"
ultima_atualizacao: "2026-08-15"
---

# Falha de serviço por GEM mapping ausente

Fonte legada: `TROUBLESHOOTING-CHECKLIST.md`. Aplicar a árvore de decisão
vigente e parar na primeira falha; este diagnóstico não autoriza mudança.

## Assinatura observada

- ONT online.
- Service-port `up`.
- VLAN presente na PON e no uplink.
- Service-port permanece com zero bytes/pacotes.
- WAN PPPoE está `Disconnected`.
- BNG não registra PADI/PADR.

## Verificação prioritária

Verificar se o line profile possui um mapping explícito da VLAN/flow para o GEM
referenciado pelo service-port. Em `mapping-mode VLAN`, essa ligação deve usar
o GEM efetivamente usado pelo service-port.

## Limites da conclusão

Não atribuir automaticamente a causa a AAA, NAT, RADIUS ou
`Match state: mismatch`. Também não criar, remover ou alterar mapping durante
o diagnóstico sem autorização `WRITE`, sintaxe confirmada, precheck, impacto,
rollback e pós-validação.
