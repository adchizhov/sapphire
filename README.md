## SAPPHIRE
### Description
Programming Assignment Task (this is a secret for which company!)

### How to run
**Simple way** -> You will need `docker` and `docker-compose` to run this app simple way, just type in project root `make image run`  
and visit `0.0.0.0:8000` in browser after it built  

Harder way (_Is not advised_) -> make virtualenv, install postgres with postgis + geos, install requirements.txt, setup database and fill `.env` accordingly,  
run `python manage.py runserver`  

### Project structure
`build` - docker etc. related stuff and scripts (such as wait_for_postgres.py), `run.sh` as entrypoint to run app via docker  
`data` - initial sites.json  
`points` - points app (with Point & PointCategory models), Hazard is a PointCategory, lets not hardcode Point as Hazard  
`sapphire` - project root app with settings  
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