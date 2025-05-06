"""
defines url mapping for dashboard API
"""

from django.urls import path
from dashboard.views.DashboardView import DashBoardView
from dashboard.views.ChatView import ChatView


urlpatterns = [
    path('', DashBoardView.as_view()),
     path('/ask', ChatView.as_view())
]