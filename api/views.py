from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
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
from api.serializers import ScheduleSerializer
from api.serializers import DayOfWeekSerializer
from api.serializers import ScheduleRecordSerializer
from api.serializers import BreakSerializer
from api.authentication import QuietBasicAuthentication
from shop.models import Schedule
from shop.models import DayOfWeek
from shop.models import ScheduleRecord
from shop.models import Break


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class ScheduleViewSet(viewsets.ModelViewSet):
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer
#
#
# class DayOfWeekViewSet(viewsets.ModelViewSet):
#     queryset = DayOfWeek.objects.all()
#     serializer_class = DayOfWeekSerializer
#
#
# class ScheduleRecordViewSet(viewsets.ModelViewSet):
#     queryset = ScheduleRecord.objects.all()
#     serializer_class = ScheduleRecordSerializer
#
#
# class BreakViewSet(viewsets.ModelViewSet):
#     queryset = Break.objects.all()
#     serializer_class = BreakSerializer


class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class IsAuthView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        content = {
            'user': request.user.username,
            'auth': request.auth
        }
        return Response(content)


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


class ScheduleView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        schedule = Schedule.objects.get(pk=1)
        # days_of_week = DayOfWeek.objects.all()
        schedule_serializer = ScheduleSerializer(schedule)
        # days_serializer = DayOfWeekSerializer(days_of_week, many=True)

        return Response({
            'schedule': schedule_serializer.data,
            # 'days_of_week': days_serializer.data
        })
