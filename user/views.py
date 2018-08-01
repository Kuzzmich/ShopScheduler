from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from user.forms import FormRegister


class RegisterView(TemplateView, FormMixin):
    template_name = 'register.html'
    form_class = FormRegister
