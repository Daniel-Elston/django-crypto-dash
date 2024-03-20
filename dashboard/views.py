from __future__ import annotations

from django.shortcuts import render
# from django.views.generic import DetailView
# from django.views.generic import ListView

# from data_management.models import CryptoFetchTicker

# class CryptoPriceListView(ListView):
#     model = CryptoPrice
#     template_name = 'index.html'


def index(request):
    return render(request, 'index.html')


def datatables(request):
    return render(request, 'datatables.html')


def index_dash(request):
    return render(request, 'index_dash.html')


def reports(request):
    return render(request, 'reports.html')


def visuals(request):
    return render(request, 'visuals.html')
