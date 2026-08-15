---
fabricante: cisco
modelo: [asr1001-x]
categoria: config
topicos: [vlan, subinterface, dot1q, prechecks]
descricao: "Prechecks para configuração de subinterfaces 802.1Q no Cisco ASR1001-X."
versao_firmware_testada: "N/A"
ultima_atualizacao: "2026-08-15"
---

# Prechecks para VLAN e subinterface

Fonte legada: `skills/cisco-asr1001x/10-vlan-subinterfaces/SKILL.md`. A fonte
não fornece versão real; não assumir IOS ou IOS XE além do que for confirmado
no alvo.

## Descoberta antes da mudança

Os comandos abaixo são `[INFERIDO]` e devem ser validados com `?`:

```text
interface TenGigabitEthernet<PATH>
interface TenGigabitEthernet<PATH>.<SUBINTERFACE>
encapsulation dot1Q <VLAN_ID>
ip address <IP> <MASK>
show running-config interface <INTERFACE>
```

## Verificações obrigatórias

Confirmar o nome real com `interface ?`; distinguir L2, L3, subinterface,
bridge-domain e BDI; validar tag, interface pai, MTU, IP e sobreposição.
Capturar a interface completa antes de alterar.

## Risco e rollback

Encapsulation ou IP incorretos podem derrubar gestão, PPPoE ou upstream. Toda
escrita é `[DESTRUTIVO]` e exige autorização explícita. O rollback restaura
encapsulation, endereço, description e estado administrativo previamente
capturados.
