#!/bin/bash
# script to start project in development stage

set -e


if [ -f ../.env ]; then
  export $(grep '^ENVIRONMENT=*' ../.env | xargs)
fi

if [ "$ENVIRONMENT" = "dev" ] && [ -n "$VIRTUAL_ENV" ]; then
  echo "-- Development Stage --"

  sudo service mariadb restart
  sudo service apache2 restart

  export PYTHONPATH=./app:
elif [ "$ENVIRONMENT" = "prod" ]; then
  echo "-- Production Stage --"
else
  echo "!! Error: Make sure the ENVIRONMENT variable is set in the .env file and the virtual environment is active."
  exit
fi

python ./app/main.py
