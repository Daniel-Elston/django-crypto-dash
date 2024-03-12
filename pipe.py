import asyncio
import aiohttp
import time
import datetime
import aiofiles
import ccxt.pro as ccxtpro
import ccxt
import pandas as pd
import numpy as np
import os
import json

from utils.setup_env import setup_project_env
project_dir, config, setup_logs = setup_project_env()


async def save_to_json(data, filename):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(json.dumps(data))

async def load_from_json(filename):
    async with aiofiles.open(filename, 'r') as file:
        return json.loads(await file.read())


async def ticker(symbol, exchange_name='binance', batch_size=30):
    exchange = getattr(ccxtpro, exchange_name)()
    counter = 0
    batch = []
    
    try:
        while True:
            ticker = await exchange.fetch_ticker(symbol) # todo: decompose!
            print(ticker)
    #         batch.append(ticker)
    #         counter += 1
            
    #         if counter % batch_size == 0:
    #             batch_n = counter // batch_size
    #             print(f'Saving batch: {batch_n}')
    #             await save_to_json(batch, f'data/tests/watch_trades{batch_n}.json')
    #             batch = []
            
    #         await asyncio.sleep(1)
    
    # except Exception as e:
    #     print(f"Error saving data:{e}")
            
    finally:
        await exchange.close()

symbol = 'BTC/USDT'  # Example symbol
asyncio.run(ticker(symbol))

# ToDo:
# watch_ticker, watch_order_book, watch_trades


# from utils.get_dtypes import get_ticker_types

# def main():
#     file_path = 'data/tests/fetch_ticker_1.json'
#     get_ticker_types(file_path)
            
# if __name__ == '__main__':
#     main()