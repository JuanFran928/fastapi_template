#!/bin/bash
# script to create database, user and password in development stage
set -e

sudo service mariadb restart

DB_USER=${1:-test_user}

DB_NAME=${2:-test_database}

DB_PASS=${3:-password}

# Create Users
sudo mysql -u root -e "CREATE USER IF NOT EXISTS '$DB_USER'@'%' IDENTIFIED BY '$DB_PASS';"
echo "User '$DB_USER' created"

# Create Databases
sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"
echo "Database '$DB_NAME' created."


# Grant All Privileges
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'%' IDENTIFIED BY '$DB_PASS';"

echo "Mariadb Users '$DB_USER', and databases '$DB_NAME' created."
