#!/bin/sh

# wait for DB to start
sleep 10

# Perform database migrations
echo "Performing database migrations..."
python manage.py migrate --settings=core.settings.warehouse_app

# Create superuser
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell --settings=core.settings.warehouse_app

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8001 --settings=core.settings.warehouse_app
