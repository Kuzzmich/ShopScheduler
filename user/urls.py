from django.urls import re_path
# from user.views import LoginView
from user.views import RegisterView

urlpatterns = [
    # re_path(r'^login/', LoginView.as_view(), name='login'),
    # re_path(r'^logout/', LogoutView.as_view(), name='logout'),
    re_path(r'^register/', RegisterView.as_view(), name='register'),
]
