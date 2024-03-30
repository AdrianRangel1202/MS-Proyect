from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import  status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse



@api_view(["GET"])
def UsersViews(request):
    users = User.objects.all()
    srlz = UserSerializer(users, many=True)
    return Response(srlz.data)
    
@api_view(["POST"])
def Insert_Users(request):
    if request.method == "POST":
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            return Response({"Mensaje":"User Create successfully"}, status=status.HTTP_201_CREATED)
        else:
             return Response({"Mensaje":"Error Create User"}, status=status.HTTP_401_UNAUTHORIZED)
        
    
   

@api_view(["PUT"])
def put_user(request):

    if request.method == "PUT": 
        user_serializer = UserSerializer(data = request.data)

        if user_serializer.is_valid():
            user = User.objects.get(username = request.data["username"])
            if user:
                user_serializer.save()
                return Response({"Mensaje": "User Update successfully"}, status=status.HTTP_200_OK) 
            else:
                return ({"Error":"User Not Exist"}, status.HTTP_404_NOT_FOUND)
        
        elif not user_serializer.is_valid():  
            return ({"Error":"User Not Exist"}, status.HTTP_404_NOT_FOUND)


        """return Response({"Error":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_serializer = UserSerializer(data = data)
        user_serializer.save()

        return Response({"Mensaje": "User Update successfully"}, status=status.HTTP_200_OK)"""
    
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





"""up_user.username = data["username"]
    up_user.email = data["email"]
    up_user.password = make_password(data["password"])"""