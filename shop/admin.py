from django.contrib import admin
from shop.models import Shop
from shop.models import Schedule
from shop.models import DayOfWeek
from shop.models import ScheduleRecord
from shop.models import Break


admin.site.register(Shop)
admin.site.register(Schedule)
admin.site.register(DayOfWeek)
admin.site.register(ScheduleRecord)
admin.site.register(Break)
