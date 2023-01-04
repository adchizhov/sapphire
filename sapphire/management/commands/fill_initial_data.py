import json
import logging
import os.path
import sys

import requests
from django.conf import settings
from django.contrib.gis.geos import Polygon
from django.core.management.base import BaseCommand

from sites.models import Site

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Load sites from source'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clean',
            action='store_true',
            help='Drop all sites which are exists before create',
        )
        parser.add_argument(
            '--from-gist',
            action='store_true',
            help='Get latest sites.json from gist',
        )

    def handle(self, *args, **options):
        if options['clean']:
            logger.info("`clean` parameter passed -> drop existed sites from database")
            Site.objects.filter().delete()
        if Site.objects.count():
            logger.info(f'Table {Site._meta.db_table} already contains data, import aborted')
            sys.exit(0)
        if options['from_gist']:
            source_url = 'https://gist.githubusercontent.com/ekeydar/60fb52013bee62f0ed66b4bdfbd1bfa0/raw/a7ae162fbfb0202cb3040e977aab62f15df44ac1/sites.json'
            logger.info(f'Get latest sites.json from {source_url}')
            try:
                response = requests.get(source_url, timeout=5)
            except requests.Timeout as e:
                logger.error('Timeout error occurs while fetching data from source')
                sys.exit(1)
            data = response.json()
        else:
            source_path = os.path.join(settings.BASE_DIR, 'data', 'sites.json')
            logger.info(f'Parsing sites.json from {source_path}')
            with open(source_path, 'r') as source_file:
                data = json.loads(source_file.read())
        list_of_sites_to_create = []
        for element in data:
            list_of_sites_to_create.append(Site(title=element['title'], polygon=Polygon(element['points'])))
        # you do not need transaction.atomic here, it is already uses atomic transactions
        Site.objects.bulk_create(list_of_sites_to_create)
        logger.info(f'Process finished, created {len(list_of_sites_to_create)} sites in total.')
