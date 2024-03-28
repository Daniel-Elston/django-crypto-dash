from __future__ import annotations

import json
import os

from django.http import JsonResponse
from django.shortcuts import render
from django_pandas.io import read_frame

from data_management.models import CryptoFetchTicker


def load_json(filepath):
    """Load data from a json file."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
            return json.loads(content)
    return []


data = load_json('data/temp/fetch_ticker.json')


def visuals_api(request):
    queryset = CryptoFetchTicker.objects.all()
    dct = {
        "labels": [],
        "data": [],
    }
    for item in queryset:
        dct['labels'].append(item.timestamp)
        dct['data'].append(item.close)
    return JsonResponse(dct)


def reports_api(request):
    queryset = CryptoFetchTicker.objects.all()
    dct = {
        "labels": ['timestamp', 'close'],
        "data": [],
    }
    for item in queryset:
        dct['data'].append([item.timestamp, item.close])
    return JsonResponse(dct)


def CryptoReportView(request):
    qs = CryptoFetchTicker.objects.all()
    df = read_frame(qs)

    columns = [{'field': f.name, 'title': f.verbose_name.title()}
               for f in CryptoFetchTicker._meta.fields]
    json_data = df.to_json(orient='records')

    context = {
        'data': json_data,
        'columns': columns
    }
    return render(request, 'reports.html', context)
