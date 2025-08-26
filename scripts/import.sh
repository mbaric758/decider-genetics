#!/bin/bash -c
sleep 2
ls /data/jobim/neo4j-admin-import-call.sh
if [ -f /data/jobim/neo4j-admin-import-call.sh ]; then
  chmod +x /data/jobim/neo4j-admin-import-call.sh
  /data/jobim/neo4j-admin-import-call.sh
fi
neo4j start
sleep 10
neo4j stop
