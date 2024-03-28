from __future__ import annotations

from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')


def datatables(request):
    return render(request, 'dashboard/datatables.html')


def reports(request):
    return render(request, 'dashboard/reports.html')


def visuals(request):
    return render(request, 'dashboard/visuals.html')


def test(request):
    return render(request, 'dashboard/test.html')
