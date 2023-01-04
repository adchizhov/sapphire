#!/bin/sh

python -m build.wait_for_postgres &&
python manage.py migrate &&
python manage.py collectstatic --no-input --clear &&
python manage.py fill_initial_data --from-gist &&
gunicorn sapphire.wsgi:application --workers=1 --bind 0.0.0.0:8000;
