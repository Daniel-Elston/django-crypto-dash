from __future__ import annotations

import asyncio

import ccxt.pro as ccxtpro
from django.core.management.base import BaseCommand

from utils.file_handler import save_json
from utils.file_handler import temp_file_reset


class ExtractCommand(BaseCommand):
    help = 'Transforms raw data into a format suitable for storage in the database.'

    async def ticker(self, symbol='BTC/USDT', exchange_name='binance', batch_size=60, max_items=60*5):
        """Watch the ticker for a specific symbol."""
        exchange = getattr(ccxtpro, exchange_name)()
        filepath = 'data/temp/fetch_ticker.json'

        await temp_file_reset(filepath)
        batch = []

        try:
            while len(batch) < max_items:
                ticker = await exchange.fetch_ticker(symbol)
                # pprint.pprint(ticker)
                print('Saving batch')
                # print('=' * 80)
                batch.append(ticker)

                if len(batch) % batch_size == 0:
                    print('Saving batch')
                    await save_json(batch, filepath)

                await asyncio.sleep(1)

                if len(batch) >= max_items:
                    print('Maximum items reached, final save...')
                    await save_json(batch, filepath)
                    break

        except Exception as e:
            print(f"Error:{e}")

        finally:
            await exchange.close()

    async def async_extract(self):
        await self.ticker()

        self.stdout.write(self.style.SUCCESS(
            'Successfully ran Extract pipeline'))

    def handle(self, *args, **kwargs):
        asyncio.run(self.async_extract())


Command = ExtractCommand
