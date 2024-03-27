
from .views import get_users
from django.urls import path



urlpatterns = [
    path('user/', get_users),
]

