#! /usr/bin/bash

docker login --username ${GITHUB_USERNAME} --password ${GITHUB_TOKEN} ghcr.io

# docker pull ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-api:${CIRCLE_SHA1:0:7}
# docker pull ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-menu:${CIRCLE_SHA1:0:7}

# docker stop cocktail-api
# docker stop cocktail-menu

docker compose down

docker compose -f $1 up -d

# docker run -p 8000:8000 --name cocktail-api --rm -d ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-api:${CIRCLE_SHA1:0:7} || exit 1
# docker run -p 8080:8080 --name cocktail-menu --rm -d ghcr.io/${GITHUB_USERNAME}/${CIRCLE_PROJECT_REPONAME}/cocktail-menu:${CIRCLE_SHA1:0:7} || exit 1

ufw allow 8080