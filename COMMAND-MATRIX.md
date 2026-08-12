# Command Matrix

Matriz compacta; detalhes e saídas estão em [MA5800-CLI-COMMANDS.md](MA5800-CLI-COMMANDS.md).

| Comando | Modo | Função | Status | Risco |
|---|---|---|---|---|
| `display dba-profile all [detail]` | User/System view | Inventário DBA | [CONFIRMADO] | Baixo |
| `display ont-lineprofile gpon all [detail]` | User/System view | Inventário line profiles | [CONFIRMADO] | Baixo |
| `display ont-srvprofile gpon all` | User/System view | Inventário service profiles | [CONFIRMADO] | Baixo |
| `display ont autofind all` | User/System view | ONTs descobertas | [CONFIRMADO] | Baixo |
| `display ont info summary 0/1/0` | User/System view | Estado ONT | [CONFIRMADO] | Baixo |
| `display service-port 1000` | User/System view | Estado de fluxo | [CONFIRMADO] | Baixo |
| `display port vlan 0/1/0` | User/System view | VLAN na PON | [CONFIRMADO] | Baixo |
| `display port vlan 0/8/0` | User/System view | VLAN no uplink | [CONFIRMADO] | Baixo |
| `dba-profile add ... type5 ...` | Config | Criar DBA | [CONFIRMADO][DESTRUTIVO] | Alto |
| `dba-profile delete profile-id 100/101` | Config | Excluir DBA | [CONFIRMADO][DESTRUTIVO] | Crítico |
| `ont-lineprofile gpon profile-id 100 ...` | Config | Criar line profile | [CONFIRMADO][DESTRUTIVO] | Alto |
| `tcont 0 dba-profile-id 201` | Line profile | Associar DBA | [CONFIRMADO][DESTRUTIVO] | Alto |
| `ont-srvprofile gpon profile-id 100 ...` | Config | Criar service profile | [CONFIRMADO][DESTRUTIVO] | Alto |
| `port vlan eth 1..4 translation 100 user-vlan 100` | Service profile | Mapear portas | [CONFIRMADO][DESTRUTIVO] | Alto |
| `port 0 ont-auto-find enable` | GPON interface | Habilitar descoberta | [CONFIRMADO][DESTRUTIVO] | Médio |
| `ont add 0 0 sn-auth ... omci ...` | GPON interface | Adicionar ONT | [CONFIRMADO][DESTRUTIVO] | Alto |
| `service-port 1000 vlan 100 ...` | Config | Criar fluxo | [CONFIRMADO][DESTRUTIVO] | Alto |
| `port vlan 100 0/8 0` | Config | VLAN no uplink | [CONFIRMADO][DESTRUTIVO] | Alto |
| `port vlan 10 0/8 0` | Config | Gestão no uplink | [CONFIRMADO][DESTRUTIVO] | Crítico |
| Todos os comandos terminados em `?` no catálogo | Contextual | Descobrir sintaxe | [DISCOVERY] | Baixo |

