# MA5800 Decision Tree

Responder **SIM**, **NÃO** ou **DESCONHECIDO** a cada nó. Em **NÃO** ou **DESCONHECIDO**, parar. Não alterar camadas posteriores.

1. OLT está acessível?
2. Board está normal?
3. PON está operacional?
4. ONT foi encontrada?
5. ONT foi adicionada?
6. ONT está online?
7. Line Profile existe?
8. Service Profile existe?
9. DBA existe?
10. T-CONT está associado?
11. GEM existe?
12. Com `mapping-mode VLAN`, o GEM possui mapping explícito para a VLAN/flow de serviço?
13. Service-Port existe e usa o mesmo GEM?
14. Service-Port está UP e contabiliza tráfego?
15. VLAN está na PON?
16. VLAN está no uplink?
17. Uplink está UP?
18. VLAN chega ao BNG?
19. PPPoE chega ao BNG?
20. AAA/RADIUS autentica?
21. Cliente recebe IP?

No cenário route, o nó 19 exige antes confirmar que a WAN PPPoE foi aplicada à ONT de bancada. Separar suas fases: PADI, PADO, PADR/PADS, LCP, autenticação PAP/CHAP e IPCP. O nó 21 inclui validar IP/rota/DNS na ONT e, depois, NAT, DHCP e clientes LAN/Wi-Fi.

## Evidência confirmada disponível

- Nó 4: `display ont autofind all`.
- Nó 6: `display ont info summary 0/1/0`.
- Nós 7/10/11/12: consultar o line profile completo; em `mapping-mode VLAN`, registrar o mapping GEM/VLAN e comparar VLAN, GEM e service-port.
- Nó 8: `display ont-srvprofile gpon all`.
- Nó 9: `display dba-profile all detail`.
- Nós 13/14: `display service-port 1000` e, quando disponível, seus contadores.
- Nó 15: `display port vlan 0/1/0`.
- Nó 16: `display port vlan 0/8/0`.

Assinatura crítica: ONT online e service-port UP, mas contadores do service-port em zero, WAN PPPoE `Disconnected` e BNG sem PADI/PADR exigem verificar o GEM mapping antes de alterar WAN, AAA, NAT ou VLAN.

Para os demais nós, descobrir a sintaxe no equipamento responsável ou usar sua ferramenta autorizada. A árvore diagnostica; ela não autoriza mudança.
