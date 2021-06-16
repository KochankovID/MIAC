#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

bash ./wait-for-it.sh "$db_host:$db_port"

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Start server
echo "Starting server"
gunicorn --log-level DEBUG --bind 0.0.0.0:8000 miac.wsgi:application
