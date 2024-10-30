#! /usr/bin/bash

docker login --username ${GITHUB_USERNAME} --password ${GITHUB_TOKEN} ghcr.io

docker compose down

docker compose -f $1 up -d

ufw allow 8080