import datetime
import string
import random
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from api.serializers import UserSerializer
from api.serializers import UserRegisterSerializer
from api.serializers import ShopSerializer
from api.models import Shop


# User-api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        salt = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
        request.data['password'] = make_password(request.data['password'], salt=salt, hasher='pbkdf2_sha256')
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# Shop-api
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = ShopSerializer(data={'name': request.data['name'],
                                          'shop_owner_id': request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.shop_owner_id == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response({'You do not have permission to perform this action.'})


# Registration View - I created this one for user registration, but I used UserViewSet for this later.
class RegisterView(APIView):
    def post(self, request, format=None):
        salt = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
        request.data['password'] = make_password(request.data['password'], salt=salt, hasher='pbkdf2_sha256')
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Check shop is open
class CheckOpenView(APIView):
    def post(self, request):
        now = datetime.datetime.now().time()
        today = datetime.datetime.today().weekday()
        shop = Shop.objects.get(pk=int(request.data['shop_id']))
        schedule_record = shop.schedule.schedule_records.get(day_of_week=today)
        is_open = False
        if shop.is_open:
            if not schedule_record.is_holiday:
                if schedule_record.time_open < now < schedule_record.time_close:
                    is_open = True
                    if schedule_record.breaks.all():
                        for pause in schedule_record.breaks.all():
                            if pause.time_start < now < pause.time_end:
                                is_open = False
                                break
        return Response({'shop': shop.name, 'is_open': is_open})
