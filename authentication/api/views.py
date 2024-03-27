from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
import requests

# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    url = "http://127.0.0.1:8000/users/get_user"
    response = requests.get(url)
    if response.status_code == 200:
        return Response(response.content)


@api_view(['POST','PUT','DELETE'])
@permission_classes([IsAdminUser])
def get_users(request):

    if request.method == "POST":
        url = "http://127.0.0.1:8000/users/post_user"
        data_user = {
            "username": request.username,
            "email": request.email,
            "password": request.password,
        }
        response = requests.post(url, data=data_user)
        return Response(response.content)