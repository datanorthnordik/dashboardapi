"""
defines url mapping for dashboard API
"""

from django.urls import path
from dashboard.views.DashboardView import DashBoardView


urlpatterns = [
    path('', DashBoardView.as_view()),
]