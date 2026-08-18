---
fabricante: zte
modelo: [zxa10-c650]
categoria: cli
topicos: [fingerprint, hardware, discovery, gpon]
descricao: "Fingerprint e consultas READ/DISCOVERY confirmadas em uma ZTE ZXA10 C650 com software V1.1.2."
versao_firmware_testada: "ZTE ZXA10 Software V1.1.2"
ultima_atualizacao: "2026-08-18"
---

# ZTE ZXA10 C650 — fingerprint e discovery de CLI

## Fingerprint observado

Evidência sanitizada de uma sessão autorizada registrou banner `TITAN`, prompt
`ZTE650` e `show software` retornando `ZXA10 C650` com `ZTE ZXA10 Software`
na versão `V1.1.2`. A equivalência operacional C610/ZTE650 foi autorizada para
essa coleta, mas a identidade literal acima é a única confirmada por CLI.

O inventário confirmou duas placas GPON GFGH de 16 portas e controladoras SFUH
em estados ativo e standby. Seriais, caminho da imagem e demais identificadores
de equipamento permanecem fora do repositório.

## Consultas confirmadas

Todos os comandos abaixo foram aceitos como `READ` no contexto observado:

```cli
show software
show hostname
show card
show equipment
show interface brief
show vlan summary
show gpon profile tcont
show gpon onu profile vlan
```

`show ?` e ajuda contextual como `show gpon onu ?` são `DISCOVERY`. O comando
`show version` foi rejeitado nesta CLI; não o trate como alternativa para
`show software`.

## Regras de uso

- Confirme o fingerprint antes de reutilizar a sintaxe em outra OLT ou release.
- Use `?` para descobrir a forma completa de `gpon_olt-`, `gpon_onu-`, `vport-`
  e `xgei-`; não deduza a numeração de slots ou portas.
- Não registre IPs, serial de ONU, LOID, senhas, comunidades SNMP, descrições
  de clientes ou a configuração bruta.
- Esta evidência não confirma compatibilidade para outra C610/C650 ou versão.

## Resultado esperado

As consultas retornam a identidade da plataforma, o inventário sanitizável e
a gramática de consulta para GPON. Divergência de modelo, software, prompt ou
host key requer interromper a automação e nova validação.
