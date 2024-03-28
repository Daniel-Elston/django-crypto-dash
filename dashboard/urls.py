from __future__ import annotations

from django.urls import path

from . import views

urlpatterns = [
    path("datatables", views.datatables, name='datatables'),
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('visuals', views.visuals, name="visuals"),
    path("reports", views.reports, name='reports'),
    path("test", views.test, name="test"),
]
