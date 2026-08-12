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
12. Service-Port existe?
13. Service-Port está UP?
14. VLAN está na PON?
15. VLAN está no uplink?
16. Uplink está UP?
17. VLAN chega ao BNG?
18. PPPoE chega ao BNG?
19. AAA/RADIUS autentica?
20. Cliente recebe IP?

## Evidência confirmada disponível

- Nó 4: `display ont autofind all`.
- Nó 6: `display ont info summary 0/1/0`.
- Nós 7/10/11: `display ont-lineprofile gpon all detail`.
- Nó 8: `display ont-srvprofile gpon all`.
- Nó 9: `display dba-profile all detail`.
- Nós 12/13: `display service-port 1000`.
- Nó 14: `display port vlan 0/1/0`.
- Nó 15: `display port vlan 0/8/0`.

Para os demais nós, descobrir a sintaxe no equipamento responsável ou usar sua ferramenta autorizada. A árvore diagnostica; ela não autoriza mudança.

