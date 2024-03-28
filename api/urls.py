from __future__ import annotations

from django.urls import path

from . import views

urlpatterns = [
    path('visuals_api', views.visuals_api, name="api_visuals"),
    path('reports_api', views.reports_api, name="api_reports"),
]
