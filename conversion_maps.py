from __future__ import annotations

from datetime import datetime
from datetime import timezone


def get_conversion_maps():
    return {
        "fetch_ticker": fetch_ticker_conversion_map(),
        "watch_ticker": watch_ticker_conversion_map(),
        "watch_trades": watch_trades_conversion_map()
    }


def timestamp_to_datetime(value):
    """Converts a Unix timestamp (in milliseconds) to a datetime object."""
    return datetime.fromtimestamp(value / 1000.0, tz=timezone.utc)
    # return dt.strftime("%Y-%m-%d %H:%M:%S")


def iso_to_datetime(value):
    """Converts an ISO 8601 datetime string to a datetime object."""
    return datetime.fromisoformat(value.rstrip('Z')).replace(tzinfo=timezone.utc)
    # return dt.strftime("%Y-%m-%d %H:%M:%S")


def fetch_ticker_conversion_map():
    conversion_map = {
        "symbol": {"str": str},
        "timestamp": {"int": timestamp_to_datetime},
        "datetime": {"str": iso_to_datetime},
        "high": {"str": float},
        "low": {"str": float},
        "bid": {"str": float},
        "bidVolume": {"str": float},
        "ask": {"str": float},
        "askVolume": {"str": float},
        "vwap": {"str": float},
        "open": {"str": float},
        "close": {"str": float},
        "last": {"str": float},
        "previousClose": {"str": float},
        "change": {"str": float},
        "percentage": {"str": float},
        "average": {"str": float},
        "baseVolume": {"str": float},
        "quoteVolume": {"str": float},
        "info": {
            "symbol": {"str": str},
            "priceChange": {"str": float},
            "priceChangePercent": {"str": float},
            "weightedAvgPrice": {"str": float},
            "prevClosePrice": {"str": float},
            "lastPrice": {"str": float},
            "lastQty": {"str": float},
            "bidPrice": {"str": float},
            "bidQty": {"str": float},
            "askPrice": {"str": float},
            "askQty": {"str": float},
            "openPrice": {"str": float},
            "highPrice": {"str": float},
            "lowPrice": {"str": float},
            "volume": {"str": float},
            "quoteVolume": {"str": float},
            "openTime": {"int": timestamp_to_datetime},  # dt
            "closeTime": {"int": timestamp_to_datetime},  # dt
            "firstId": {"str": int},
            "lastId": {"str": int},
            "count": {"str": int},
        }
    }
    return conversion_map


def watch_ticker_conversion_map():
    conversion_map = {
        "symbol": {"str": str},
        "timestamp": {"datetime": timestamp_to_datetime},
        "datetime": {"datetime": iso_to_datetime},
        "high": {"str": float},
        "low": {"str": float},
        "bid": {"str": float},
        "bidVolume": {"str": float},
        "ask": {"str": float},
        "askVolume": {"str": float},
        "vwap": {"str": float},
        "open": {"str": float},
        "close": {"str": float},
        "last": {"str": float},
        "previousClose": {"str": float},
        "change": {"str": float},
        "percentage": {"str": float},
        "average": {"str": float},
        "baseVolume": {"str": float},
        "quoteVolume": {"str": float},
        "info": {
            "e": {"str": str},
            "E": {"int": timestamp_to_datetime},
            "p": {"str": float},
            "P": {"str": float},
            "w": {"str": float},
            "x": {"str": float},
            "c": {"str": float},
            "Q": {"str": float},
            "b": {"str": float},
            "B": {"str": float},
            "a": {"str": float},
            "A": {"str": float},
            "o": {"str": float},
            "h": {"str": float},
            "l": {"str": float},
            "v": {"str": float},
            "q": {"str": float},
            "O": {"int": timestamp_to_datetime},
            "C": {"int": timestamp_to_datetime},
            "F": {"str": int},
            "L": {"str": int},
            "n": {"str": int},
        }
    }
    return conversion_map


def watch_trades_conversion_map():
    conversion_map = {
        "info": {
            "e": {"str": str},
            "E": {"datetime": timestamp_to_datetime},
            "s": {"str": str},
            "t": {"str": int},
            "p": {"str": float},
            "q": {"str": float},
            "b": {"str": int},
            "a": {"str": int},
            "T": {"datetime": timestamp_to_datetime},
            "m": {"str": bool},
            "M": {"str": bool},
        },
        "timestamp": {"datetime": timestamp_to_datetime},
        "datetime": {"datetime": iso_to_datetime},
        "symbol": {"str": str},
        "id": {"str": int},
        "order": {"str": str},
        "type": {"str": str},
        "side": {"str": str},
        "takerOrMaker": {"str": str},
        "price": {"str": float},
        "amount": {"str": float},
        "cost": {"str": float},
        "fee": {"str": float},
        "fees": []
    }
    return conversion_map
