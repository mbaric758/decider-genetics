#!/bin/bash -c
sleep 2
ls /data/b/neo4j-admin-import-call.sh
if [ -f /data/b/neo4j-admin-import-call.sh ]; then
  chmod +x /data/b/neo4j-admin-import-call.sh
  /data/b/neo4j-admin-import-call.sh
fi
neo4j start
sleep 10
neo4j stop
