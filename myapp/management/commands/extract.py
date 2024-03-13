from __future__ import annotations

import asyncio
import logging

import ccxt.pro as ccxtpro
from django.core.management.base import BaseCommand

from utils.file_handler import load_json
from utils.file_handler import save_json
from utils.setup_env import setup_project_env
project_dir, config, setup_logs = setup_project_env()


async def ticker(symbol='BTC/USDT', exchange_name='binance', batch_size=5):
    """Watch the ticker for a specific symbol."""
    exchange = getattr(ccxtpro, exchange_name)()
    counter = 0
    batch = []

    try:
        while True:
            ticker = await exchange.fetch_ticker(symbol)
            # ticker = await get_fetch_ticker()
            print(ticker)
            batch.append(ticker)
            counter += 1

            if counter % batch_size == 0:
                batch_n = counter // batch_size
                print(f'Saving batch: {batch_n}')
                await save_json(batch, f'data/tests/fetch_ticker_{batch_n}.json')
                batch = []

            await asyncio.sleep(1)

            if counter >= 5:
                break

    except Exception as e:
        print(f"Error saving data:{e}")

    finally:
        await exchange.close()


class ExtractCommand(BaseCommand):
    help = 'Transforms raw data into a format suitable for storage in the database.'

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    async def async_extract(self):
        await ticker()
        data = await load_json('data/tests/fetch_ticker_1.json')
        self.logger.debug(data[0])

    def handle(self):
        asyncio.run(self.async_extract())

        self.stdout.write(self.style.SUCCESS(
            'Successfully ran Transform pipeline'))


Command = ExtractCommand
