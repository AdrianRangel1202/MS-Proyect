
from .views import get_users, post_users
from django.urls import path



urlpatterns = [
    path('get_user/', get_users),
    path('post_user/', post_users)
]

