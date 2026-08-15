---
fabricante: cisco
modelo: [asr1001-x]
categoria: diag
topicos: [pppoe, bng, nat, troubleshooting]
descricao: "Diagnóstico de PPPoE ativo sem assumir navegação funcional no ASR1001-X."
versao_firmware_testada: "IOS XE 17.09.03a"
ultima_atualizacao: "2026-08-15"
---

# PPPoE ativo sem navegação

Fonte legada: `skills/cisco-asr1001x/24-pppoe-troubleshooting/SKILL.md`.
Iniciar em `READ-ONLY` e parar na primeira falha objetiva.

## Evidência confirmada

Em IOS XE 17.09.03a, a fonte registra como `[CONFIRMADO]`:

```text
show pppoe session all
show ip route <SUBSCRIBER_IP>
show ip nat statistics
show ip nat translations
```

## Sequência de diagnóstico

Seguir ONT, VLAN/uplink, PADI/PADO/PADR/PADS, LCP, autenticação,
AAA/RADIUS, IPCP/IP, Virtual-Access, rota/FIB, policy/ACL, NAT/CGNAT,
upstream, retorno e DNS/HTTP/HTTPS. Capturar counters antes e depois de uma
janela curta; configuração estática não prova encaminhamento.

## Sessão UP com IP

Confirmar rota do assinante, RX/TX do Virtual-Access durante tráfego real e,
para RFC6598/RFC1918, tradução NAT/CGNAT dinâmica. RX crescendo sem tradução
dinâmica indica investigar classificação, binding ou pool NAT; não é motivo
para alterar PPPoE.

## Limites

`clear pppoe`, reset de sessão e mudanças de Virtual-Template são
`[DESTRUTIVO]`, afetam clientes e não fazem parte do diagnóstico padrão.
