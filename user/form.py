from django import forms


class FormLogin(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'ng-model': 'password'}))


class FormRegister(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'ng-model': 'password'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'first_name'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'last_name'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'ng-model': 'email'}))
