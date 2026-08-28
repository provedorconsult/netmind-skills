# G02 Current state

Read-only discovery: Docker version/root/storage/log driver, `docker info`,
daemon JSON existence/validity, sanitized container/service/task aggregates,
log paths/sizes/aggregate/largest, filesystem and inodes. Handle daemon JSON
absent and present; never assume driver, Swarm, Compose or Dokploy behavior.
