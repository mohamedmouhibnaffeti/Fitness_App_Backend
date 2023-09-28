from django.shortcuts import render
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import AllowAny
from .models import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.backends import ModelBackend
from .authentication import EmailAuthBackend
from .tokens import create_jwt_for_user
# Create your views here.


class Signup(generics.GenericAPIView):
    permission_classes=[]
    serializer = SignUpSerializer
    def post(self, request:Request):
        data = request.data
        serializer_class = self.serializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            response = {
                "message" : "user created successfully",
                "data" : serializer_class.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes=[AllowAny]
    def post(self, request:Request):
        email = request.data.get("email")
        #username = User.objects.get(email=email).username
        password = request.data.get("password")
        user = EmailAuthBackend.authenticate(self,request, username=email,password=password)
        if user is not None:
            try : 
                tokens = create_jwt_for_user(user)
                response = {"message" : "Login Successful",
                        "Tokens" : tokens
                        }
                return Response(data=response, status=status.HTTP_200_OK)
            except:
                return Response(data={'message' : 'User has no auth token'}, status=status.HTTP_200_OK)
        else :
            return Response(data={"message" : "Login Failed"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    def get(self, request):
        content = {
            "user": str(request.user), "Token": str(request.auth)
        } 
        return Response(data=content, status=status.HTTP_200_OK)
    

class get_users(APIView):
    permission_classes=[AllowAny]
    def get(self,response):
        users = User.objects.all()
        users_serializer = SignUpSerializer(instance=users, many=True)
        response = {
            "message" : "Users",
            "data" : users_serializer.data
        }
        return Response(data=response)





"""
authentication_classes([AllowAny])
@api_view(['POST'])
def sign_up(request:Request):
    permission_classes=[]
    data = request.data
    serializer_class = SignUpSerializer(data=data)
    if serializer_class.is_valid():
        serializer_class.save()
        response = {
            "message" : "user created successfully",
            "data" : serializer_class.data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
"""

