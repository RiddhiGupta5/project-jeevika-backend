import hashlib
from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organization, CustomToken
from .serializers import (Organization)
from .helper_functions import get_object, get_token


# TODO: 1. Change this to org



# Ping Server
class PingView(APIView):

    def get(self, request):
        return Response({"message":"OK"}, status=status.HTTP_200_OK)

# Sign up a new user View
class UserSignupView(APIView):

    # Sigup user (create new object)
    def post(self, request):

        user_data = {}
        user_data['email'] = request.data.get("email", None)
        user_data['username'] = request.data.get("username", None)
        user_data['phone_no'] = request.data.get("phone_no", None)
        user_data['address'] = request.data.get("address", None)
        user_data['password'] = request.data.get("password", None)
        if len(user_data['password'])<6:
            return Response({"Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSignupSerializer(data=user_data)       

        if serializer.is_valid():
            serializer.save()

            user = CustomUser.objects.get(email=user_data['email'])
            token = get_token(user.id, 0)
            user_data['token'] = token
            del user_data['password']
            try:
                usertoken = CustomToken.objects.get(object_id=user.id, user_type=0)
                return Response({"message":"User Already Logged in", "User":user_data}, status=status.HTTP_400_BAD_REQUEST)
            except CustomToken.DoesNotExist:
                CustomToken.objects.create(
                    user_type=0,
                    object_id=user.id,
                    token=token
                )
                return Response({"message":"User Signed up successfully", "User":user_data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# View for user login
class UserLoginView(APIView):
    
    def post(self, request):
        req_data = request.data
        try:
            user = CustomUser.objects.get(email=req_data['email'])
        except CustomUser.DoesNotExist:
            return Response({"message":"Invalid Email"}, status=status.HTTP_400_BAD_REQUEST)
        
        m = hashlib.md5()     
        m.update(req_data['password'].encode("utf-8"))
        if user.password == str(m.digest()):
            token = get_token(user.id, 0)
            try:
                usertoken = CustomToken.objects.get(object_id=user.id, user_type=0)
                token = usertoken.token
            except CustomToken.DoesNotExist:
                CustomToken.objects.create(
                    user_type=0,
                    object_id=user.id,
                    token=token
                )
            return Response({"message":"User Logged in", 
                "User":{
                    "id":user.id,
                    "email":user.email,
                    "username":user.username,
                    "phone_no":user.phone_no,
                    "address":user.address,
                    "token":token
                }
            })
        else:
            return Response({"message":"Invalid Password"}, status=status.HTTP_403_FORBIDDEN)
        

# Signout new user
class UserLogoutView(APIView):

    def get(self, request, format=None):

        # Get User and delete the token
        token = request.headers.get('Authorization', None)
        if token is None or token=="":
            return Response({"message":"Authorization credentials missing"}, status=status.HTTP_403_FORBIDDEN)
        
        user = get_object(token)
        if user is None:
            return Response({"message":"User Already Logged Out"}, status=status.HTTP_403_FORBIDDEN)

        response = {
            "message":"User logged out", 
            "Details":{
                "id": user.id,
                "email":user.email,
                "username":user.username,
                "phone_no":user.phone_no,
                "address":user.address
            }}
        
        usertoken = CustomToken.objects.get(object_id=user.id, user_type=0)
        usertoken.delete()
        return Response(response, status=status.HTTP_200_OK)


