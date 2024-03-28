from __future__ import annotations

from django.db import models
from django_pandas.managers import DataFrameManager


class CryptoFetchTicker(models.Model):
    symbol = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    datetime = models.DateTimeField()
    high = models.FloatField()
    low = models.FloatField()
    bid = models.FloatField()
    bidVolume = models.FloatField()
    ask = models.FloatField()
    askVolume = models.FloatField()
    vwap = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    last = models.FloatField()
    previousClose = models.FloatField()
    change = models.FloatField()
    percentage = models.FloatField()
    average = models.FloatField()
    baseVolume = models.FloatField()
    quoteVolume = models.FloatField()
    info = models.JSONField()
    # symbol = models.CharField(max_length=100)
    # priceChange = models.FloatField()
    # priceChangePercent = models.FloatField()
    # weightedAvgPrice = models.FloatField()
    # prevClosePrice = models.FloatField()
    # lastPrice = models.FloatField()
    # lastQty = models.FloatField()
    # bidPrice = models.FloatField()
    # bidQty = models.FloatField()
    # askPrice = models.FloatField()
    # askQty = models.FloatField()
    # openPrice = models.FloatField()
    # highPrice = models.FloatField()
    # lowPrice = models.FloatField()
    # volume = models.FloatField()
    # quoteVolume = models.FloatField()
    # openTime = models.DateTimeField()
    # closeTime = models.DateTimeField()
    # firstId = models.IntegerField()
    # lastId = models.IntegerField()
    # count = models.IntegerField()

    objects = models.Manager()  # Django Manager
    pdobjects = DataFrameManager()  # Pandas Manager

    def __str__(self):
        return self.symbol


class CryptoOrder(models.Model):
    pass


class CryptoTrades(models.Model):
    pass
