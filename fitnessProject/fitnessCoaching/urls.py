from django.urls import path
from . import views


urlpatterns = [
    path("coaching/<int:id>/",views.coach_details, name = 'coach_details'),
    path("coaching/", views.display_coaches, name = 'display_coaches'),
]