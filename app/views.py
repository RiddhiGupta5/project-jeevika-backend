from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (UserLoginSerializer, UserSignupSerializer,)


# Ping Server
class PingView(APIView):
    permission_class = (AllowAny,)

    def get(self, request):
        return Response({"message":"OK"}, status=status.HTTP_200_OK)

# Sign up a new user View
class UserSignupView(APIView):
    permission_classes = (AllowAny,)

    # Sigup user (create new object)
    def post(self, request):
        
        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            user_data = serializer.data
            User.objects.create_user(
                email=user_data['email'], 
                password=user_data['password'], 
                username=user_data['username'], 
                phone_no=user_data['phone_no'],
                address=user_data['address'])

            user = authenticate(email=user_data['email'], password=user_data['password'])
            token, _ = Token.objects.get_or_create(user=user)
            user_data['id'] = user.id
            user_data['token'] = token.key
            
            return Response({"message":"User Signed up successfully", "User":user_data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View for user login
class UserLoginView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        req_data = request.data
        user = authenticate(email=req_data['email'], password=req_data['password'])
        if not user:
            return Response({"message":"Invalid Details"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message":"User Logged In", 
                "User":{
                    "id":user.id,
                    "email":user.email,
                    "username":user.username,
                    "phone_no":user.phone_no,
                    "address":user.address,
                    "token":token.key
            }})

# Signout new user
class UserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        response = {
            "message":"User logged out", 
            "Details":{
                "id": user.id,
                "email":user.email,
                "username":user.username,
                "phone_no":user.phone_no,
                "address":user.address
            }}
        request.user.auth_token.delete()
        return Response(response, status=status.HTTP_200_OK)