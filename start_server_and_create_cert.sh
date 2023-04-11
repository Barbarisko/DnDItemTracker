#!/bin/bash

if [ -z "${1}" ]; then
    read -p "Please enter db password: " postgres_password
else
    postgres_password=${1}
fi

if [ -z "${2}" ]; then
    read -p "Please enter your email address: " email
else
    email=${2}
fi

export POSTGRES_PASSWORD=${postgres_password}
export MY_EMAIL=${email}
export CERTBOT_MODE=--staging

docker compose up -d

mkdir dhparam
openssl dhparam -out dhparam/dhparam-2048.pem 2048

