from __future__ import annotations

import asyncio
import pprint

import ccxt.pro as ccxtpro
from django.core.management.base import BaseCommand

from utils.file_handler import save_json


async def ticker(symbol='BTC/USDT', exchange_name='binance', batch_size=2):
    """Watch the ticker for a specific symbol."""
    exchange = getattr(ccxtpro, exchange_name)()
    counter = 0
    batch = []

    try:
        while True:
            ticker = await exchange.fetch_ticker(symbol)
            # ticker = await get_fetch_ticker()
            pprint.pprint(ticker)
            print('=' * 80)
            batch.append(ticker)
            counter += 1

            if counter % batch_size == 0:
                batch_n = counter // batch_size
                print(f'Saving batch: {batch_n}')
                await save_json(batch, f'data/temp/fetch_ticker_{batch_n}.json')
                batch = []

            await asyncio.sleep(1)

            if counter >= 4:
                break

    except Exception as e:
        print(f"Error saving data:{e}")

    finally:
        await exchange.close()


class ExtractCommand(BaseCommand):
    help = 'Transforms raw data into a format suitable for storage in the database.'

    async def async_extract(self):
        await ticker()

        self.stdout.write(self.style.SUCCESS(
            'Successfully ran Extract pipeline'))

    def handle(self, *args, **kwargs):
        asyncio.run(self.async_extract())


Command = ExtractCommand
