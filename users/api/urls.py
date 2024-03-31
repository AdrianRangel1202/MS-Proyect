from django.urls import path
from .views import UsersViews, filter_user


urlpatterns = [
    path('', UsersViews, name = "Vistas de usuarios"),
    path('id=<int:pk>', filter_user, name = "Filtrar Usuarios")
]
