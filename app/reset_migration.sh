#Choose a migration to format

#example usage: "sh rm_migrations.sh clients"

sudo service mariadb restart

rm -rf ./alembic/versions/*
sh rm_database.sh
sh database.sh
sh migrations.sh
sh prestart.sh