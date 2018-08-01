from django.urls import re_path
from django.conf.urls import include
from rest_framework import routers
from api.views import UserViewSet
from api.views import AuthView
from api.views import IsAuthView
from api.views import RegisterView
from api.views import ShopViewSet

# from rest_framework.authtoken import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'shop', ShopViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^api-token-auth/', views.obtain_auth_token),  # url for token authentication
    re_path(r'^', include(router.urls), name='api'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^auth/', AuthView.as_view(), name='api-auth'),
    re_path(r'^is-auth/', IsAuthView.as_view(), name='api-is-auth'),
    re_path(r'^register/', RegisterView.as_view(), name='api-register'),
]
