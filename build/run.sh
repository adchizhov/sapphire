#!/bin/sh

python -m build.wait_for_postgres &&  # wait until postgres (with postgis is up)
python manage.py migrate &&  # run migrate
python manage.py collectstatic --no-input --clear &&  # collect static -> it is served via whitenoise
python manage.py fill_initial_data --from-gist &&  # fill database with sites
python manage.py loaddata fixtures/points.json --app points.point &&  # fill database 2 Hazard and 2 Shelter points
gunicorn sapphire.wsgi:application --workers=1 --bind 0.0.0.0:8000;  # fire up the service
