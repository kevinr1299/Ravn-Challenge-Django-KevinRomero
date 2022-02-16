#!/bin/bash
python manage.py migrate;
python manage.py collectstatic --noinput;
python manage.py seedpeople 20;
gunicorn --worker-tmp-dir=/dev/shm --workers=4 --timeout 50 --bind=0.0.0.0:8000 starwars.wsgi;