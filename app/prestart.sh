#! /usr/bin/env bash
set -e

if [ -f ../.env ]; then
  export $(grep '^ENVIRONMENT=*' ../.env | xargs)
fi

if [ "$ENVIRONMENT" = "dev" ] && [ -n "$VIRTUAL_ENV" ]; then
  echo "-- Development Stage --"

  sudo service mariadb restart

  export PYTHONPATH=./app:
elif [ "$ENVIRONMENT" = "prod" ]; then
  echo "-- Production Stage --"
else
  echo "$ENVIRONMENT"
  echo "!! Error: Make sure the ENVIRONMENT variable is set in the .env file and the virtual environment is active."
  exit
fi

# Let the DB start
python ./app/pre_start.py

# Run users migrations
alembic upgrade head

# # Run clients migrations
# alembic --name clients upgrade head

# # Run content migrations
# alembic --name content upgrade head

# Create initial data in DB
python ./app/initial_data.py
