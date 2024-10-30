#! /usr/bin/bash

docker login --username ${CIRCLE_PROJECT_USERNAME} --password ${GITHUB_TOKEN} ghcr.io
docker pull ghcr.com/${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-api:${CIRCLE_SHA1:0:7}
docker pull ghcr.com/${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-menu:${CIRCLE_SHA1:0:7}
docker run cocktail-api:${CIRCLE_SHA1:0:7} -p 8000:8000 -d
docker run cocktail-menu:${CIRCLE_SHA1:0:7} -p 8080:8080 -d
ufw allow 8080