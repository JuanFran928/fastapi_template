#script to remove and create database in development stage

#!!!!DO NOT USE THIS SCRIPT IN PRODUCTION!!!!

#!/bin/bash
set -e

sudo service mariadb restart

DB_NAME=${1:-test_database}

sudo mysql -u root -e "drop database $DB_NAME;"
echo "Database '$DB_NAME' dropped."
sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"
echo "Database '$DB_NAME' created."



#!!!!DO NOT USE THIS SCRIPT IN PRODUCTION!!!!
