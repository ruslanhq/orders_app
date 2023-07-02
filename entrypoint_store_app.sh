#!/bin/sh

# wait for DB to start
sleep 10

# Perform database migrations
echo "Performing database migrations..."
python manage.py migrate --settings=core.settings.store_app

# Create superuser
echo "Creating superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell --settings=core.settings.store_app

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000 --settings=core.settings.store_app
