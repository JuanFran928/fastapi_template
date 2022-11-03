#! /usr/bin/env bash
set -e

if [ -f ../.env ]; then
  export $(grep '^ENVIRONMENT=*' ../.env | xargs)
fi


if [ "$ENVIRONMENT" = "dev" ] && [ -n "$VIRTUAL_ENV" ]; then
  echo "-- Development Stage --"

  sudo service redis-server restart
  export PYTHONPATH=./app:

  python app/tests_pre_start.py
  bash ./scripts/test.sh "$@"
elif [ "$ENVIRONMENT" = "test" ]; then
  echo "-- Testing Stage --"
  python app/tests_pre_start.py
  bash ./scripts/test.sh "$@"
else
  echo "!! Error: Make sure the ENVIRONMENT variable is set in the .env file and the virtual environment is active."
  exit
fi
