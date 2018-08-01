from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
import string
import random
from api.serializers import UserSerializer
from api.serializers import UserRegisterSerializer
from api.serializers import ShopSerializer
from api.authentication import QuietBasicAuthentication
from shop.models import Shop


# User-api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Shop-api
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


# Authentication View
class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


# Check is user authenticated
class IsAuthView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        content = {
            'id': request.user.id,
            'user': request.user.username,
            'auth': request.auth
        }
        return Response(content)


# Registration View
class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        salt = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
        request.data['password'] = make_password(request.data['password'], salt=salt, hasher='pbkdf2_sha256')
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
