from __future__ import annotations

from django.urls import path

from . import views

urlpatterns = [
    path("reports", views.reports, name='reports'),
    path("index_dash", views.index_dash, name='dash-index'),
    path("datatables", views.datatables, name='dash-datatables'),
    path('', views.index, name='dahs-index'),
    path('visuals', views.visuals, name="visuals")
]
