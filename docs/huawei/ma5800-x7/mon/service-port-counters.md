---
fabricante: huawei
modelo: [ma5800-x7]
categoria: mon
topicos: [service-port, counters, vlan, monitoring]
descricao: "Leitura de estado e contadores de service-port para observabilidade."
versao_firmware_testada: "MA5800V100R018 / SPH507"
ultima_atualizacao: "2026-08-15"
---

# Monitoramento de service-port

Fonte legada: `COMMAND-MATRIX.md` e `MA5800-CLI-COMMANDS.md`. Os comandos são
consultas `[CONFIRMADO]` de baixo risco na MA5800V100R018/SPH507.

## Consultas

```text
display service-port 1000
display statistics service-port 1000
display port vlan 0/1/0
display port vlan 0/8/0
```

`display service-port 1000` consulta o estado do fluxo; a evidência original
registra admin enable/state up. `display statistics service-port 1000` consulta
os contadores do fluxo. As consultas de porta conferem a VLAN na PON e no
uplink.

## Interpretação segura

Correlacionar contadores com a tentativa de serviço e com o estado do
service-port. Contadores em zero não provam isoladamente a causa da falha:
preservar a evidência e seguir o diagnóstico de GEM mapping antes de alterar
camadas posteriores.

## Limites

O ID `1000` é evidência do baseline legado, não um valor a assumir para outro
alvo. Não alterar service-port, VLAN ou uplink neste procedimento de
monitoramento.
