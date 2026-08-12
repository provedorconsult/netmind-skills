# Codex Skills — Huawei MA5800-X7

Pacote reutilizável de Skills operacionais para o Codex trabalhar com Huawei MA5800-X7 sem inventar sintaxe. A evidência primária é uma sessão real na **MA5800V100R018, patch SPH507**. Nenhuma criação deste repositório acessou ou alterou a OLT.

## Autoridade e classificação

A CLI do equipamento-alvo é a autoridade de sintaxe. Validar versão e usar `?` antes de todo comando que não esteja `[CONFIRMADO]`.

- `[CONFIRMADO]`: executado com sucesso na OLT observada.
- `[DISCOVERY]`: consulta literal com `?` executada.
- `[INFERIDO]`: proveniente de documentação, ainda não confirmado.
- `[DESTRUTIVO]`: cria, altera ou remove configuração; exige confirmação explícita.
- `[ERRO]`: comando rejeitado ou mensagem literal observada.
- `[VERSÃO DIFERENTE]`: documentação/sintaxe que não foi validada em R018.

Um comando mutável pode receber simultaneamente `[CONFIRMADO][DESTRUTIVO]`.

## Equipamento e baseline

| Item | Valor observado |
|---|---|
| Plataforma | MA5800-X7 |
| Versão | MA5800V100R018 |
| Patch | SPH507 |
| 0/1 | H907CGHF |
| 0/8 | H901MPLA Active_normal |
| 0/9 | H901MPLA Standby_normal |
| 0/10 e 0/11 | H901PILA |
| PON/ONT | 0/1/0, ONT-ID 0 |
| ONT | EG8145X6-10, SN 4857544354ABCFB2 |
| Uplink | 0/8/0 |
| Gestão | VLAN 10, Vlanif10 10.101.0.2/30, gateway 10.101.0.1 |
| Clientes | VLAN 100 |
| Service-port | 1000, GEM 1, VLAN 100, up |

Baseline relevante:

```text
vlan 10 smart
vlan 100 smart
vlan desc 10 description "gerencia"
port vlan 10 0/8 0
port vlan 100 0/8 0
interface Vlanif10
 description "MGMT"
 ip address 10.101.0.2 255.255.255.252
ip route-static 0.0.0.0 0.0.0.0 10.101.0.1
```

Não executar este bloco como script. Ele é um registro do estado observado.

## Estado de bancada e arquitetura-alvo

A ONT autorizada é uma unidade de bancada. O estado atualmente informado pelo operador é **bridge**; esse é o baseline de rollback, não o objetivo final.

```text
EG8145X6-10 (route mode, PPPoE client, NAT/DHCP/Wi-Fi)
  → GPON 0/1/0
  → T-CONT 0 / DBA 201
  → GEM 1
  → Service-Port 1000
  → VLAN 100
  → Uplink 0/8/0
  → ASR1001-X (BNG/PPPoE)
  → AAA/RADIUS
```

A MA5800 presta acesso GPON/L2 e pode atuar como plano de provisionamento OMCI da WAN da ONT. A sessão PPPoE termina na EG8145X6-10; o ASR1001-X continua sendo o servidor/BNG e o AAA/RADIUS autentica. A credencial pode precisar ser entregue operacionalmente à ONT pela OLT/NMS, mas nunca deve ser armazenada nestas Skills, no Git, em exemplos, PRs ou logs.

A sintaxe para profile de WAN roteada/PPPoE ainda não foi confirmada na R018. Ela deve ser descoberta na CLI e validada contra o firmware exato da ONT de bancada antes de qualquer alteração.

## Objetos observados

- DBA 200: DBA-VLAN100-2G-OMCI, Type 5, Fix/Assure/Max 2048/2048/2048000 kbps, best-effort.
- DBA 201: DBA-OMCI-GPON-1G, Type 5, 2048/2048/1024000 kbps, best-effort, bind-times 1.
- Line profile 100: LINE-OMCI-VLAN-100; PQ; mapping VLAN; T-CONT 0 → DBA 201; GEM 1 ETH.
- Default line profile 0: line-profile_default_0; T-CONT 0 → DBA 2; T-CONT 1 → DBA 0.
- Service profile 100: SRV-OMCI-VLAN-100; ETH 1–4 em VLAN 100.
- Service-port 1000: ONT 0/GEM 1 → VLAN 100, translate, up.
- Modo atual da ONT de bancada: bridge, conforme informação do operador.
- Objetivo: profile de roteamento com WAN PPPoE na ONT; sintaxe ainda não confirmada.

## Fluxo seguro

1. Ler baseline e confirmar R018/SPH507.
2. Aplicar [árvore de decisão](MA5800-DECISION-TREE.md) e parar na primeira falha.
3. Consultar o [banco de erros](MA5800-ERROR-DATABASE.md).
4. Conferir o [catálogo CLI](MA5800-CLI-COMMANDS.md) e a [matriz](COMMAND-MATRIX.md).
5. Para sintaxe não confirmada, usar `?` no modo correto.
6. Antes de mudar: dependências, Binding times, impacto, autorização e rollback.
7. Validar primeiro em ONT de teste e registrar o retorno literal.

## Regras de segurança

Nunca inventar sintaxe, alterar gestão/rota sem autorização, excluir defaults, modificar ONT online sem necessidade, misturar OLT e BNG, registrar credenciais ou executar destrutivo sem confirmação. `already existed` não prova que um objeto esteja consultável. Preferir sempre `display`.

## Índice das Skills

1. [Baseline](skills/01-ma5800-baseline/SKILL.md)
2. [CLI discovery](skills/02-ma5800-cli-discovery/SKILL.md)
3. [DBA](skills/03-ma5800-dba/SKILL.md)
4. [Line profile](skills/04-ma5800-line-profile/SKILL.md)
5. [Service profile](skills/05-ma5800-service-profile/SKILL.md)
6. [ONT autofind](skills/06-ma5800-ont-autofind/SKILL.md)
7. [ONT provisioning](skills/07-ma5800-ont-provisioning/SKILL.md)
8. [ONT status](skills/08-ma5800-ont-status/SKILL.md)
9. [GEM/T-CONT](skills/09-ma5800-gem-tcont/SKILL.md)
10. [Service-port](skills/10-ma5800-service-port/SKILL.md)
11. [VLAN](skills/11-ma5800-vlan/SKILL.md)
12. [Uplink](skills/12-ma5800-uplink/SKILL.md)
13. [PPPoE access](skills/13-ma5800-pppoe-access/SKILL.md)
14. [Troubleshooting](skills/14-ma5800-troubleshooting/SKILL.md)
15. [Error database](skills/15-ma5800-error-database/SKILL.md)
16. [Safe change](skills/16-ma5800-safe-change/SKILL.md)
17. [Rollback](skills/17-ma5800-rollback/SKILL.md)
18. [Cleanup](skills/18-ma5800-cleanup/SKILL.md)
19. [Production checklist](skills/19-ma5800-production-checklist/SKILL.md)
20. [ONT WAN PPPoE](skills/20-ma5800-ont-wan-pppoe/SKILL.md)
21. [Decision tree](skills/ma5800-decision-tree/SKILL.md)

## Entregáveis auxiliares

- [Exemplos de uso](EXAMPLES.md)
- [Matriz de comandos](COMMAND-MATRIX.md)
- [Checklist de provisionamento](ONT-PROVISIONING-CHECKLIST.md)
- [Checklist de troubleshooting](TROUBLESHOOTING-CHECKLIST.md)
- [Checklist de rollback](ROLLBACK-CHECKLIST.md)

## Documentação oficial Huawei

As fontes abaixo apoiam conceitos e procedimentos, mas não promovem sintaxe a `[CONFIRMADO]` na R018:

- [Portal oficial SmartAX MA5800](https://support.huawei.com/enterprise/en/access-network/smartax-ma5800-pid-21484577)
- [Huawei: GPON ONU fails to auto discover](https://info.support.huawei.com/network/ptmngsys/Web/tsrev_access/en/content/access/19_gpononu_failure_to_auto_discover/trouble_510602.html)
- [Huawei: GPON ONU profile mismatch](https://info.support.huawei.com/network/ptmngsys/Web/tsrev_access/en/content/access/18_gpononu_profile_match_state_is_mismatch/trouble_515303.html)
- [Huawei: rogue ONT alarm](https://info.support.huawei.com/hedex/api/pages/EDOC1100413634/FEN1022J/03/resources/en-us_alarmref_0000001193617423.html)
- [Huawei: replacing an ONU and service impact](https://info.support.huawei.com/hedex/api/pages/EDOC1100331202/FEM1012J/06/resources/en-us_topic_0317327751.html)
- [Huawei Home Network/ONT documentation portal](https://support.huawei.com/enterprise/en/optical-business/home-network-pid-23708797)
- [Huawei: Understanding PPPoE](https://info.support.huawei.com/hedex/api/pages/EDOC1100149308/AEJ0713J/18/resources/admin/sec_admin_network_pppoe_0003.html)

A pesquisa pública não revelou um command reference R018 completo e acessível para todos os comandos. Por isso, nenhum comando novo foi inferido dessas páginas; exemplos de outras releases devem ser marcados `[VERSÃO DIFERENTE]` e redescobertos com `?`.
