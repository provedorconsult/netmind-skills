# Cisco ASR1001-X Decision Tree

Responder **SIM**, **NÃO** ou **DESCONHECIDO**. Parar em **NÃO/DESCONHECIDO**; não alterar camada posterior.

1. Equipamento responde?
2. SSH funciona?
3. CPU normal?
4. Memória normal?
5. Interface está UP/UP?
6. IP está configurado corretamente?
7. Rota existe e resolve no CEF?
8. BGP necessário está Established?
9. PPPoE/IPoE necessário está ativo?
10. AAA/RADIUS autentica?
11. Cliente recebe IPv4/IPv6?
12. QoS/service-policy está correto?
13. NAT/CGNAT necessário existe?
14. Tráfego sai pela interface/upstream correto?
15. Tráfego de retorno chega?
16. BGP anuncia o prefixo esperado?
17. Internet funciona?

## Evidência por nó

| Nó | Evidência candidata |
|---|---|
| 1–2 | reachability autorizada, `show users`, `show ip ssh` |
| 3 | `show processes cpu`, `show platform resources` |
| 4 | `show processes memory`, `show memory statistics` |
| 5–6 | `show interfaces <INTERFACE>`, briefs IPv4/IPv6 |
| 7 | RIB e CEF do prefixo |
| 8,16 | summary, neighbor, advertised/received e policy |
| 9–11 | PPPoE fases, Virtual-Access, AAA, pool/IP |
| 12 | `show policy-map interface` |
| 13 | translations, statistics, pool e ACL |
| 14–15 | rota/CEF/ARP/ND e evidência nos dois sentidos |
| 17 | teste autorizado ponta a ponta |

Todos os comandos da tabela são `[INFERIDO]` até validação na CLI.

