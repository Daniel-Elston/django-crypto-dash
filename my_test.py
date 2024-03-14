from __future__ import annotations

import pandas as pd
import pyarrow.parquet as pq

from utils.setup_env import setup_project_env
project_dir, config, setup_logs = setup_project_env()


def inspect_file():
    filepath = 'data/temp/prepared_fetch_ticker.parq'
    transformed_data = pq.read_table(
        filepath).to_pandas().to_dict('records')
    df = pd.json_normalize(transformed_data)
    print(df.head())


def main():
    inspect_file()


if __name__ == '__main__':
    main()
