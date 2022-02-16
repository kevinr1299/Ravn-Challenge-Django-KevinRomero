#!/bin/bash
until python manage.py migrate 2>/dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "success"

python manage.py collectstatic --noinput
python manage.py seedpeople 20
gunicorn --workers=4 --timeout 50 --bind=0.0.0.0:8000 starwars.wsgi