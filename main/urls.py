from django.urls import re_path
from main.views import MainView

urlpatterns = [
    re_path(r'^$', MainView.as_view(), name='index')
]
