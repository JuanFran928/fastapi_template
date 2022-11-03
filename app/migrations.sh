#Generate migrations when models are updated

#example usage: "sh migrations.sh clients"

if [ -f ../.env ]; then
  export $(grep '^ENVIRONMENT=*' ../.env | xargs)
fi


if [ "$ENVIRONMENT" = "dev" ] && [ -n "$VIRTUAL_ENV" ]; then
  echo "-- Development Stage --"
  sudo service mariadb restart
  export PYTHONPATH=./app:
  
  echo " Insert migration name for database $1:"
  read migration_text
  
  alembic revision --autogenerate -m "$migration_text"
  
else
  echo "!! Error: Make sure the ENVIRONMENT variable is set in the .env file and the virtual environment is active."
  exit
fi
