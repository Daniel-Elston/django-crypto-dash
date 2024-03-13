from __future__ import annotations

import logging
from asyncio import run

from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand

from conversion_maps import get_conversion_maps
from myapp.models import CryptoFetchTicker
from utils.setup_env import setup_project_env

project_dir, config, setup_logs = setup_project_env()
mapping_store = get_conversion_maps()
conversion_map = mapping_store['fetch_ticker']


class LoadCommand(BaseCommand):
    help = 'Load raw data into database.'

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def handle(self, prepared_data):
        run(self.async_load(prepared_data))

    async def async_load(self, prepared_data):
        instances = [CryptoFetchTicker(**data) for data in prepared_data]
        await sync_to_async(CryptoFetchTicker.objects.bulk_create)(instances)

        self.stdout.write(self.style.SUCCESS(
            'Successfully ran Load pipeline'))


Command = LoadCommand
