from django.urls import re_path
from shop.views import ShopView
from shop.views import ShopCreateView
from shop.views import ShopScheduleUpdateView

urlpatterns = [
    re_path(r'^$', ShopView.as_view(), name='shop'),
    re_path(r'^create/$', ShopCreateView.as_view(), name='shop-create'),
    re_path(r'^schedule-update/$', ShopScheduleUpdateView.as_view(), name='schedule-update')
]
