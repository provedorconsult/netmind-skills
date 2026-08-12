# Cisco ASR1001-X Rollback

Rollback deve existir antes da mudança, usar sintaxe validada e restaurar o último estado conhecido. `reload` não é método normal.

## Checklist comum

1. Capturar `show version`, uptime, CPU e memória.
2. Capturar configuração sanitizada do objeto e consumidores.
3. Identificar sessões/protocolos/clientes afetados.
4. Definir critério de abort.
5. Descobrir e validar comandos reversos com `?`.
6. Garantir console/out-of-band ou sessão administrativa preservada.
7. Reverter em ordem inversa.
8. Validar decision tree e registrar resultado.
9. Persistir somente após aprovação.

## Interface e VLAN/subinterface

Restaurar shutdown state, description, encapsulation, IP/IPv6, MTU, VRF, ACL, NAT e service-policy. Não remover parent/subinterface antes de migrar dependências.

## Rotas

Restaurar linha anterior, distância, next-hop e tracking. Verificar RIB, CEF e tráfego nos dois sentidos.

## BGP

Restaurar neighbor, AFI/SAFI, prefix-list e route-map com sequência/direção originais. Preferir soft validation quando confirmada; nunca resetar todo o BGP automaticamente.

## Route-map, prefix-list e ACL

Restaurar sequências e bindings exatos. Considerar implicit deny e todos os consumidores antes de remover policy.

## NAT/CGNAT

Restaurar modo, pools, classificação, inside/outside, overload e logging. Não trocar modo com traduções ativas nem limpar translations sem autorização.

## PPPoE e AAA/RADIUS

Preservar sessão administrativa. Restaurar Virtual-Template, grupos, method lists, pools e service-policy. Usar somente assinante de teste; não derrubar sessões em massa.

## QoS

Remover attachment novo antes de substituir policy; restaurar class-map, policy-map, hierarquia e direção anteriores; comparar counters.

## Boot, SSH e gestão

Não recarregar. Restaurar BOOT/config-register, VTY, AAA, ACL, VRF e source-interface mantendo acesso alternativo.

