from django.urls import re_path
from shop.views import ShopView

urlpatterns = [
    re_path(r'^', ShopView.as_view(), name='shop')
]
