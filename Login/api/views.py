from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import  status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password


@api_view(["GET"])
def UsersViews(request):

    users = User.objects.all()
    srlz = UserSerializer(users, many=True)
    return Response(srlz.data)
    
@api_view(["POST"])
def Insert_Users(request):

    data = request.data
    User.objects.create(username = data["username"],
                            email = data["email"],
                            password = make_password(data["password"]))
    
    return Response({"Mensaje":"User Create successfully"}, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def put_user(request):

    try:
        data = request.data
        up_user = User.objects.get(id = data["username"])
    except User.DoesNotExist:
        return ({"Error":"User Not Exist"}, status.HTTP_404_NOT_FOUND)

    if request.username != up_user.username:
        return Response({"Error":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    
    up_user.username = data["username"]
    up_user.email = data["email"]
    up_user.password = make_password(data["password"])
    up_user.save()

    new_user = User.objects.get(username = data["username"])
    srlz = UserSerializer(new_user)
    return Response({"Mensaje": "User Update successfully"}, status=status.HTTP_200_OK)
  
@api_view(["DELETE"])
def Del_user(request):
    try:
        data = request.data
        user = User.objects.get(username = data["username"])
    except User.DoesNotExist:
        return Response({"Error": "User Not Exist"}, status=status.HTTP_404_NOT_FOUND)

    if data["username"] != user.username:
        return Response({"error":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    
    user.delete()
    return Response({"mensaje":"User deleted successfully"}, status=status.HTTP_200_OK)

