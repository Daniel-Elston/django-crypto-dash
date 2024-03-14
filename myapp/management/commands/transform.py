from __future__ import annotations

import asyncio

import pyarrow as pa
import pyarrow.parquet as pq
from django.core.management.base import BaseCommand

from conversion_maps import get_conversion_maps
from utils.file_handler import load_json

conversion_map = get_conversion_maps()['fetch_ticker']


def convert_value(value, conversions):
    """Converts a value to a specific type using conversion functions."""
    for _, func in conversions.items():
        try:
            return func(value)
        except (ValueError, TypeError):
            continue
    return value


def recursive_convert(data, conversion_map):
    """Walks through the data converting values based on the conversion_map."""
    if isinstance(data, dict):
        return {k: recursive_convert(v, conversion_map.get(k, {})) for k, v in data.items()}
    elif isinstance(data, list):
        return [recursive_convert(i, conversion_map) for i in data]
    else:
        return convert_value(data, conversion_map)


class TransformCommand(BaseCommand):
    help = 'Transforms raw data into a format suitable for storage in the database.'

    async def async_transform(self):
        extracted_data = await load_json('data/temp/fetch_ticker_1.json')
        transformed_data = recursive_convert(extracted_data, conversion_map)
        table = pa.Table.from_pylist(transformed_data)
        pq.write_table(table, 'data/temp/prepared_fetch_ticker.parq')

        self.stdout.write(self.style.SUCCESS(
            'Successfully ran Transform pipeline'))

    def handle(self, *args, **kwargs):
        asyncio.run(self.async_transform())


Command = TransformCommand
