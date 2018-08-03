from django.contrib import admin
from api.models import Shop
from api.models import Schedule
from api.models import ScheduleRecord
from api.models import Break


admin.site.register(Shop)
admin.site.register(Schedule)
admin.site.register(ScheduleRecord)
admin.site.register(Break)

