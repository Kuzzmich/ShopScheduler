from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from shop.forms import ShopForm


class ShopView(TemplateView):
    template_name = 'shop_detail.html'


class ShopCreateView(TemplateView, FormMixin):
    template_name = 'shop_create.html'
    form_class = ShopForm


class ShopScheduleUpdateView(TemplateView):
    template_name = 'shop_schedule_update.html'
