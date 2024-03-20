from __future__ import annotations

from django.urls import path

from . import views

urlpatterns = [
    path('total_views', views.total_views, name="api_total_views"),
]
