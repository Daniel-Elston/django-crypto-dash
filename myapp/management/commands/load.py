from __future__ import annotations

import asyncio

import pyarrow.parquet as pq
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand

from myapp.models import CryptoFetchTicker


class LoadCommand(BaseCommand):
    help = 'Load raw data into database.'

    async def async_load(self):
        filepath = 'data/temp/prepared_fetch_ticker.parq'
        transformed_data = pq.read_table(
            filepath).to_pandas().to_dict('records')

        instances = [CryptoFetchTicker(**data) for data in transformed_data]
        await sync_to_async(CryptoFetchTicker.objects.bulk_create)(instances)

        self.stdout.write(self.style.SUCCESS(
            'Successfully ran Load pipeline'))

    def handle(self, *args, **kwargs):
        asyncio.run(self.async_load())


Command = LoadCommand
