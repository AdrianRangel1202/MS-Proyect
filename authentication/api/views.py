from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from django.http import JsonResponse
import requests

# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    url = "http://127.0.0.1:8000/users/get_user"
    response = requests.get(url)
    
    if response.status_code == 200:
        return Response(response.json())


@api_view(['POST','PUT','DELETE'])
@permission_classes([IsAdminUser])
def post_users(request):

    if request.method == "POST":
        url = "http://127.0.0.1:8000/users/post_user"

        data = {
            "username": request.data["username"],
            "email": request.data["email"],
            "password": request.data["password"],
        }
        response = requests.post(url, json=data)
        return Response(response.json())