#!/bin/bash

cd src

echo "Running Migrations"

python manage.py db upgrade

echo "Seeding DB"
python manage.py seed_db

echo "Starting App"

flask run --host='0.0.0.0'