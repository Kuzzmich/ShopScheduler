from django.urls import re_path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken import views
from api.views import UserViewSet
from api.views import RegisterView
from api.views import ShopViewSet
from api.views import CheckOpenView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    re_path(r'^', include(router.urls), name='api'),
    re_path(r'^register/', RegisterView.as_view(), name='api-register'),
    re_path(r'^check-open/', CheckOpenView.as_view(), name='api-check-open'),
]
