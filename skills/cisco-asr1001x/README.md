# Skills Cisco ASR1001-X para ISP

Pacote profissional para Codex operar de forma conservadora em Cisco ASR1001-X como edge router/BNG de ISP. Nenhum acesso ou alteração foi realizado no equipamento durante a criação.

## Estado de evidência

A versão real do IOS XE ainda não foi fornecida. A primeira coleta obrigatória é `show version`, com saída sanitizada. Até uma linha ser aceita na CLI real:

- `[CONFIRMADO]`: executada com sucesso no ASR de referência.
- `[DISCOVERY]`: consulta de ajuda `?` executada e registrada.
- `[INFERIDO]`: candidato baseado no prompt ou documentação Cisco.
- `[DESTRUTIVO]`: cria, altera, remove, limpa, reinicia ou persiste estado.
- `[ERRO]`: comando rejeitado e retorno literal preservado.
- `[VERSÃO DIFERENTE]`: exemplo de outra release/plataforma.

IOS clássico, IOS XE e IOS XR não são intercambiáveis. A CLI real é a autoridade.

## Fluxo obrigatório

```text
SHOW
  ↓
ANALISAR
  ↓
VALIDAR
  ↓
PROPOR
  ↓
CONFIRMAR
  ↓
ALTERAR
  ↓
VALIDAR
  ↓
DOCUMENTAR
```

Antes de mudança: comando, objetivo, impacto, dependências, resultado esperado, validação e rollback. Não usar `reload`, `clear` ou reset de protocolo como primeira ação.

## Arquitetura de referência

```text
Cliente
  → ONT EG8145X6-10
  → Huawei MA5800-X7 (GPON/GEM/Service-Port/VLAN)
  → Cisco ASR1001-X (BNG/PPPoE/AAA/NAT/CGNAT/BGP)
  → Upstream
  → Internet
```

A OLT de destino deve ser alcançada somente pelo caminho autorizado, usando valores do inventário: `ssh -l ${DOWNSTREAM_USERNAME} ${DOWNSTREAM_HOST}`. Nunca tentar acesso direto pela Internet.

## Segurança e sanitização

Nunca armazenar senha, secret, key, token, RADIUS shared-secret, SNMP community, BGP password, credencial PPPoE ou chave SSH. Usar `<USERNAME>`, `<PASSWORD>`, `<SECRET>`, `<RADIUS_SECRET>`, `<BGP_PASSWORD>`, `<IP>` e `<ASN>`.

Ao coletar running/startup config, sanitizar também valores cifrados ou hash. Não enviar configuração bruta ao Git.

## Documentos

- [Matriz de comandos](CISCO-ASR1001X-COMMANDS.md)
- [Banco de erros](CISCO-ASR1001X-ERROR-DATABASE.md)
- [Decision tree](CISCO-ASR1001X-DECISION-TREE.md)
- [Rollback](CISCO-ASR1001X-ROLLBACK.md)

## Índice das Skills

| # | Skill | Escopo |
|---|---|---|
| 01 | [Baseline](01-baseline/SKILL.md) | IOS XE, config, hardware e estado |
| 02 | [CLI discovery](02-cli-discovery/SKILL.md) | Ajuda contextual e modos |
| 03 | [Interfaces](03-interface-diagnostics/SKILL.md) | Estado, erros, MTU e flaps |
| 04 | [Óptica](04-optical-diagnostics/SKILL.md) | DOM e thresholds |
| 05 | [IP routing](05-ip-routing/SKILL.md) | RIB/FIB/CEF |
| 06 | [Static routing](06-static-routing/SKILL.md) | Rotas IPv4/IPv6 |
| 07 | [BGP](07-bgp/SKILL.md) | Peers, AFs e policies |
| 08 | [OSPF](08-ospf/SKILL.md) | OSPFv2/OSPFv3 |
| 09 | [IPv6](09-ipv6/SKILL.md) | ND, RA, CEF e BGP |
| 10 | [VLAN/subinterfaces](10-vlan-subinterfaces/SKILL.md) | 802.1Q, BDI e L3 |
| 11 | [PPPoE/BNG](11-pppoe-bng/SKILL.md) | Subscriber termination |
| 12 | [AAA local](12-aaa-local/SKILL.md) | Fallback e method lists |
| 13 | [AAA RADIUS](13-aaa-radius/SKILL.md) | Grupos, autenticação e accounting |
| 14 | [NAT/CGNAT](14-nat-cgnat/SKILL.md) | NAT, PAT e CGN |
| 15 | [ACL](15-acl/SKILL.md) | IPv4, IPv6 e CoPP |
| 16 | [QoS](16-qos/SKILL.md) | MQC |
| 17 | [Policy-map](17-policy-map/SKILL.md) | Policies e attachments |
| 18 | [Route-map/prefix-list](18-route-map-prefix-list/SKILL.md) | Policies de roteamento |
| 19 | [Loopback](19-loopback/SKILL.md) | Router-id e sources |
| 20 | [Management](20-management/SKILL.md) | NTP, logs, SNMP e VRF |
| 21 | [SSH](21-ssh/SKILL.md) | VTY, AAA e acesso |
| 22 | [Boot/config-register](22-boot-config-register/SKILL.md) | BOOT, ROMMON e register |
| 23 | [CPU/memória](23-cpu-memory/SKILL.md) | Recursos e processos |
| 24 | [PPPoE troubleshooting](24-pppoe-troubleshooting/SKILL.md) | Fases da sessão |
| 25 | [BGP troubleshooting](25-bgp-troubleshooting/SKILL.md) | Transporte até FIB |
| 26 | [NAT troubleshooting](26-nat-troubleshooting/SKILL.md) | Classificação e retorno |
| 27 | [Service-policy troubleshooting](27-service-policy-troubleshooting/SKILL.md) | Matches, rate e drops |
| 28 | [Acesso MA5800](28-ma5800-access/SKILL.md) | SSH downstream |
| 29 | [ISP troubleshooting](29-isp-troubleshooting/SKILL.md) | Ponta a ponta |
| 30 | [Safe change](30-safe-change/SKILL.md) | Mudança conservadora |
| 31 | [Production checklist](31-production-checklist/SKILL.md) | Aceite pós-mudança |

## Checklist de produção

- [ ] IOS XE identificado.
- [ ] Configuração anterior registrada e sanitizada.
- [ ] Interfaces e uplinks verificados.
- [ ] IPv4/IPv6 e rotas verificados.
- [ ] BGP verificado.
- [ ] PPPoE/IPoE verificado quando aplicável.
- [ ] AAA/RADIUS verificado.
- [ ] NAT/CGNAT verificado.
- [ ] QoS/service-policy verificado.
- [ ] CPU e memória normais.
- [ ] SSH e gestão preservados.
- [ ] Rollback disponível.
- [ ] Configuração persistida somente após validação e autorização.

## Fontes oficiais Cisco

Estas fontes apoiam candidatos `[INFERIDO]`; não confirmam a sintaxe do equipamento até `show version` e discovery:

- [ASR1001-X Hardware Installation Guide](https://www.cisco.com/c/en/us/td/docs/routers/asr1000/install/guide/1001-x/asr1hig-book/router_overview.html)
- [ASR1001-X power-up and initial configuration](https://www.cisco.com/c/en/us/td/docs/routers/asr1000/install/guide/1001-x/asr1hig-book/pwr_up_init_configuartion.html)
- [ASR1000 Operations and Maintenance](https://www.cisco.com/c/en/us/td/docs/routers/asr1000/operations/guide/asr1000ops/verifying_hardware_installation.html)
- [IOS XE 17.x IP Routing/BGP](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_irg-basic-net-0.html)
- [IOS XE 16.7 PPPoE on Ethernet](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bbdsl/configuration/xe-16-7/bba-xe-16-7-book/bba-pppoe-enet-xe.html)
- [ASR1000 Carrier Grade NAT](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_nat/configuration/xe-16/nat-xe-16-book/iadnat-cgn.html)
- [ASR1000 QoS using MQC](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/quality-of-service/quality-of-service/m_qos-mqc-0.html)
- [IOS XE 16.12 ASR1000 Software Configuration Guide](https://www.cisco.com/c/en/us/td/docs/routers/asr1000/configuration/guide/chassis/xe-16-12/asr1000-software-config-guide-16-12.pdf)
- [IOS XE 17.x OSPF](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iro-cfg-0.html)
- [IOS XE 17.x IPv6 basic connectivity](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_ip6-add-basic-conn-xe.html)
- [IOS XE 17.x RADIUS](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-cfg-radius.html)
- [IOS XE 17.x ISG IPv6/IP subscriber sessions](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/application-services/b-application-services/m_isg-ipv6.html)
