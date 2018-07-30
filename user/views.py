from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from user.form import FormLogin
from user.form import FormRegister


class LoginView(TemplateView, FormMixin):
    template_name = 'login_form.html'
    form_class = FormLogin


class RegisterView(TemplateView, FormMixin):
    template_name = 'register.html'
    form_class = FormRegister
