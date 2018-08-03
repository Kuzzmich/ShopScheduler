from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from drf_writable_nested import WritableNestedModelSerializer  # write nested model serializer
from api.models import Schedule
from api.models import ScheduleRecord
from api.models import Break
from api.models import Shop


class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class BreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Break
        fields = ('name', 'schedule_record_id', 'time_start', 'time_end')


class ScheduleRecordSerializer(WritableNestedModelSerializer):
    breaks = BreakSerializer(many=True)

    class Meta:
        model = ScheduleRecord
        fields = ('id', 'day_of_week', 'time_open', 'time_close', 'is_holiday', 'breaks')


class ScheduleSerializer(WritableNestedModelSerializer):
    schedule_records = ScheduleRecordSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ('name', 'schedule_records')


class ShopSerializer(WritableNestedModelSerializer):
    schedule = ScheduleSerializer(required=False)   # how right is this?

    class Meta:
        model = Shop
        fields = ('id', 'name', 'shop_owner_id', 'is_open', 'schedule')

    def create(self, validated_data):
        shop = Shop.objects.create(**validated_data)
        schedule = Schedule.objects.create(shop_id=shop, name=shop.name + ' schedule')
        for i in range(7):
            ScheduleRecord.objects.create(schedule_id=schedule, day_of_week=i, is_holiday=True)
        return shop
