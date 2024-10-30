#! /usr/bin/bash

docker login --username ${GITHUB_USERNAME} --password ${GITHUB_TOKEN} ghcr.io

docker pull ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-api:${CIRCLE_SHA1:0:7}
docker pull ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-menu:${CIRCLE_SHA1:0:7}

docker run -p 8000:8000 -d ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-api:${CIRCLE_SHA1:0:7} || exit 1
docker run -p 8080:8080 -d ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-menu:${CIRCLE_SHA1:0:7} || exit 1

ufw allow 8080