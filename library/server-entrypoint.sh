#!/bin/sh

until cd /test/library
do
    echo "Waiting for server volume..."
done

python manage.py makemigrations
until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2 
done

python manage.py collectstatic --noinput

pytest

gunicorn library.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4 --reload
