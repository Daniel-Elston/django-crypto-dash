from __future__ import annotations

import logging
from pprint import pprint

from django.core.management.base import BaseCommand

from conversion_maps import get_conversion_maps
from myapp.management.commands.extract import ExtractCommand
from myapp.management.commands.load import LoadCommand
from myapp.management.commands.transform import TransformCommand
from utils.setup_env import setup_project_env


project_dir, config, setup_logs = setup_project_env()
mapping_store = get_conversion_maps()
conversion_map = mapping_store['fetch_ticker']


class ETLCommand(BaseCommand):
    help = 'Run ETL pipeline.'

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def handle(self, *args, **kwargs):
        extract = ExtractCommand()
        extract.handle()

        transform = TransformCommand()
        transform_data = transform.handle()
        pprint(transform_data)

        load = LoadCommand()
        load.handle(transform_data)

        self.stdout.write(self.style.SUCCESS(
            'ETL pipeline executed successfully.'))


Command = ETLCommand
