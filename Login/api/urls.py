from django.urls import path
from .views import UsersViews, Insert_Users, put_user, Del_user
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'Users', UsersViews, basename="Create_users")

urlpatterns = [
    path('get_user', UsersViews, name = "Vista_de_usuarios"),
    path('post_user', Insert_Users, name = "Insertar_usuarios"),
    path('put_user', put_user, name = "Actualizar_user"),
    path('del_user', Del_user, name = "Eliminar Usuarios")
]
