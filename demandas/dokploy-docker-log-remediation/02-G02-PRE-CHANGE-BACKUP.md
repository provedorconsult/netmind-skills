# DOKPLOY-LOG-G02 — Pre-change evidence

Preservar evidência `BEFORE`: uso/free space/inodes, total/contagem/maior log,
mtime, driver/política, saúde Docker/Swarm/Dokploy/aplicação. Se
`/etc/docker/daemon.json` existir e for alvo de mudança, preservar cópia fora
do filesystem cheio ou registrar método aprovado; nunca criar backup grande de
`/var/lib/docker` no mesmo volume.
