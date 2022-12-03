from django.urls import path
from .views import TeamsView, TeamsIdView


urlpatterns = [
    path('teams/', TeamsView.as_view()),
    path('teams/<int:team_id>/', TeamsIdView.as_view()),
]