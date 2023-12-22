#!/bin/bash

if [ -z "${1}" ]; then
    read -p "Please enter db password: " postgres_password
else
    postgres_password=${1}
fi

if [ -z "${2}" ]; then
    port=8085
else
    email=${2}
fi

export POSTGRES_PASSWORD=${postgres_password}
export WEB_APP_PORT=${port}

docker compose down
docker compose pull
docker compose up -d