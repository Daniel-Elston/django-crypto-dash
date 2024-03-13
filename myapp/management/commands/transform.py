from __future__ import annotations

import logging
from asyncio import run
from pprint import pprint

from django.core.management.base import BaseCommand

from conversion_maps import get_conversion_maps
from utils.file_handler import load_json
from utils.setup_env import setup_project_env

project_dir, config, setup_logs = setup_project_env()
mapping_store = get_conversion_maps()
conversion_map = mapping_store['fetch_ticker']


def convert_value(value, conversions):
    """Converts a value to a specific type using conversion functions."""
    for target_type, func in conversions.items():
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

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    async def async_transform(self):
        data = await load_json('data/tests/fetch_ticker_1.json')

        converted_data = recursive_convert(data, conversion_map)
        return converted_data

    def handle(self):
        prepared_data = run(self.async_transform())
        self.logger.debug(pprint(prepared_data))

        self.stdout.write(self.style.SUCCESS(
            'Successfully ran Transform pipeline'))
        return prepared_data


Command = TransformCommand
