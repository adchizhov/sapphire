## SAPPHIRE
### Description
Programming Assignment Task (this is a secret for which company!)

### How to run
**Simple way** -> You will need `docker` and `docker-compose`, to run this app simple way just type in project root `make image run` 
and visit `0.0.0.0:8000` in browser after it built  

Harder way (_it is not advised_) -> make virtualenv, install postgres with postgis + geos, install requirements.txt, setup database and fill `.env` accordingly, run `python manage.py runserver`  

### Project structure
`build` - docker etc. related stuff and scripts (such as wait_for_postgres.py), `run.sh` as entrypoint to run app via docker
```shell
#!/bin/sh
python -m build.wait_for_postgres &&  # wait until postgres (with postgis is up)
python manage.py migrate &&  # run migrate
python manage.py collectstatic --no-input --clear &&  # collect static -> it is served via whitenoise
python manage.py fill_initial_data --from-gist &&  # fill database with sites
python manage.py loaddata fixtures/points.json --app points.point &&  # fill database with 2 Hazard and 2 Shelter points
gunicorn sapphire.wsgi:application --workers=1 --bind 0.0.0.0:8000;  # fire up the service
```
`fixtures` - initial sites.json from home assignment file and points.json as fixtures  
`points` - points app (with Point & PointCategory models), Hazard is a PointCategory, why limit yourself to one point type, it could be not only `Hazard`, but also a `Shelter` or any other!  
`sapphire` - project root app with settings  
`screenshots` - assets for README.md 
`sites` - sites app  
`static` - css, js, assets...  
`templates` - common templates, contains 404.html, 500.html and base.html template  

### Worth to mention
`python manage.py fill_initial_data` is a custom management command used to get data from sites.json and save to database, 
there are several non-required args:  
1) `--clean` will truncate records in table `sites_site`  
2) `--from-gist` will download `sites.json` from source_url (not from filesystem, but over internet)  

`make clean` -> will delete image and volumes  
`make image` -> will build image  
`make run` -> will run app via docker-compose  
`make image run` -> will build image and run app  

`.env` file is used to store settings for app and postgis, this is pretty straightforward:
```
IMAGE_NAME=sapphire
DEBUG=1
POSTGRES_USER=sapphire_user
POSTGRES_PASSWORD=sapphire_password
POSTGRES_DB=sapphire_db
POSTGRES_PORT=5432
POSTGRES_HOST=postgis
``` 

### Used packages
`django` - framework with gis support  
`environs` - parse `.env` file (look at settings.py)  
`psycopg2-binary` - driver for postgres (postgis)  
`django-extensions` - helpers and utilities for django  
`django-geojson` - set of tools to manipulate GeoJSON with Django  
`requests` - used in `fill_initial_data` management command to request `sites.json`  
`whitenoise` - simplified static file serving
`gunicorn` - wsgi app server to run application

### ETC
I decided to add different types of points, there are not only Hazard points, but Shelter points also
![Hazards and shelters](screenshots/hazards_and_shelters.png?raw=true "Hazards and shelters")