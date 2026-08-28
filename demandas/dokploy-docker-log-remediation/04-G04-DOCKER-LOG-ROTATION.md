# DOKPLOY-LOG-G04 — Docker log rotation

Criar a Skill `dokploy-docker-log-rotation`. Fluxo: descobrir driver/política,
identificar logs sem gestão, calcular retenção/capacidade, ler e fazer merge
de `daemon.json`, validar JSON, aplicar somente mudança autorizada e verificar
novos versus containers existentes. Nunca sobrescrever `daemon.json`; mudança
de daemon pode exigir restart e containers existentes podem exigir recriação —
ambas requerem autorização própria.
