from django.urls import re_path
from user.views import RegisterView

urlpatterns = [
    re_path(r'^register/', RegisterView.as_view(), name='register'),
]
