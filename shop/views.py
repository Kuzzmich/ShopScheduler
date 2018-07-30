from django.shortcuts import render
from django.views.generic.base import TemplateView


class ShopView(TemplateView):
    template_name = 'shop.html'
