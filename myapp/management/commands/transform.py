    
from django.core.management.base import BaseCommand
from asyncio import run
from myapp.management.commands.load import load_from_json
import logging
from pprint import pprint

from utils.setup_env import setup_project_env
from conversion_maps import get_conversion_maps

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
        return [recursive_convert(item, conversion_map) for item in data]
    else:
        return convert_value(data, conversion_map)


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        
    help = 'Transforms raw data into a format suitable for storage in the database.'
    
    def handle(self, *args, **kwargs):
        run(self.async_handle())

    async def async_handle(self):
        data = await load_from_json('data/tests/fetch_ticker_1.json')
        self.logger.debug(pprint(data[0]))
        
        converted_data = recursive_convert(data, conversion_map)
        self.logger.debug(pprint(converted_data[0]))

        self.stdout.write(self.style.SUCCESS('Successfully ran data processing pipeline'))
