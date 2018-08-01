from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer  # write nested model serializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from shop.models import Schedule
from shop.models import DayOfWeek
from shop.models import ScheduleRecord
from shop.models import Break
from shop.models import Shop


class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class DayOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfWeek
        fields = ('id', 'name')


class BreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Break
        fields = ('name', 'schedule_record_id', 'time_start', 'time_end')


class ScheduleRecordSerializer(WritableNestedModelSerializer):
    breaks = BreakSerializer(many=True)

    class Meta:
        model = ScheduleRecord
        fields = ('id', 'day_of_week_id', 'time_open', 'time_close', 'is_holiday', 'breaks')


class ScheduleSerializer(WritableNestedModelSerializer):
    schedule_records = ScheduleRecordSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ('name', 'schedule_records')


class ShopSerializer(WritableNestedModelSerializer):
    schedule = ScheduleSerializer()

    class Meta:
        model = Shop
        fields = ('id', 'name', 'shop_owner_id', 'schedule', 'is_open')
