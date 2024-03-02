from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import  status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password


@api_view(["GET"])
def UsersViews(request):
    if request.method == "GET":
        users = User.objects.all()
        srlz = UserSerializer(users, many=True)
        return Response(srlz.data)
    
@api_view(["POST"])
def Insert_Users(request):
    if request.method == "POST":
        data_user = request.data
        password = make_password(data_user["password"])
        User.objects.create(username = data_user["username"],
                            email = data_user["email"],
                            password = password)
    user = User.objects.filter(username = data_user["username"])
    srlz = UserSerializer(user, many = True)
    return Response(srlz.data)

@api_view(["PUT"])
def put_user(request):
    if request.method == "PUT":
        data_user = request.data
        up_user = User.objects.get(id = data_user["id"])

        if up_user:
           up_user.username = data_user["username"]
           up_user.email = data_user["email"]
           up_user.password = make_password(data_user["password"])
           up_user.save()

        new_user = User.objects.get(username = data_user["username"])
        srlz = UserSerializer(new_user)
        return Response(srlz.data)
    
@api_view(["DELETE"])
def Del_user(request):
    if request.method == "DELETE":
        data_user = request.data
        user = User.objects.get(id = data_user["id"])
        user.delete()
        return Response({"mensaje": "Usuario eliminado"})



# {"username":"adrian", "email": "Hola@gmail.com", "password": "hola"}