from __future__ import annotations

import json
import os

from django.http import JsonResponse

from data_management.models import CryptoFetchTicker
# from django.shortcuts import render


def load_json(filepath):
    """Load data from a json file."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
            return json.loads(content)
    return []


data = load_json('data/temp/fetch_ticker.json')


def total_views(request):
    queryset = CryptoFetchTicker.objects.all()
    dct = {
        "labels": [],
        "data": [],
    }
    for item in queryset:
        dct['labels'].append(item.timestamp)
        dct['data'].append(item.close)

    return JsonResponse(dct)


def visuals(request):
    queryset = CryptoFetchTicker.objects.all()
    dct = {
        "labels": [],
        "data": [],
    }
    for item in queryset:
        dct['labels'].append(item.timestamp)
        dct['data'].append(item.close)

    return JsonResponse(dct)
