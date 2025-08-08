#!/bin/bash -c
cd /usr/app/
cp -r /src/* .
cp JOBIM_example/biocypher_config.yaml config/biocypher_config.yaml
poetry install
poetry run python3 create_knowledge_graph.py
chmod -R 777 biocypher-log