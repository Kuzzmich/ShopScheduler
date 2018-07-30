from django.urls import re_path
from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet
# from api.views import ScheduleViewSet
# from api.views import DayOfWeekViewSet
# from api.views import ScheduleRecordViewSet
# from api.views import BreakViewSet
from api.views import AuthView
from api.views import IsAuthView
from api.views import RegisterView
from api.views import ScheduleView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
# router.register(r'schedule-detail', ScheduleViewSet)
# router.register(r'day-of-week', DayOfWeekViewSet)
# router.register(r'schedule-record', ScheduleRecordViewSet)
# router.register(r'break', BreakViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls), name='api'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^auth/', AuthView.as_view(), name='api-auth'),
    re_path(r'^is-auth/', IsAuthView.as_view(), name='api-is_auth'),
    re_path(r'^register/', RegisterView.as_view(), name='api-register'),
    re_path(r'^schedule/', ScheduleView.as_view(), name='api-schedule'),
]
