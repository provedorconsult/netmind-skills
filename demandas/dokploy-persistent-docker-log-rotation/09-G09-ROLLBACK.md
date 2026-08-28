# G09 Rollback

`BACKUP → CHANGE → VALIDATE → FAILURE → RESTORE → VALIDATE`. Restoring daemon
JSON does not restore existing container/task logging; recreation/service
rollback is separately authorized.
