#!/bin/bash

if [ -z "${1}" ]; then
    read -p "Please enter db password: " postgres_password
else
    postgres_password=${1}
fi

export POSTGRES_PASSWORD=${postgres_password}
export MY_EMAIL=""
export CERTBOT_MODE=--force-renewal

docker compose down
docker compose pull
docker compose up -d db backend frontend