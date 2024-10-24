from django.urls import path
from . import views

urlpatterns = [
    path('coaching/', views.display_clients, name = 'display_clients' ),
]