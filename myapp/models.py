from django.db import models

class CryptoTicker(models.Model):
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

    def __str__(self):
        return self.symbol


class CryptoOrder(models.Model):
    pass


class CryptoTrades(models.Model):
    pass


