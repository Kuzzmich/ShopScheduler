from django import forms


class FormRegister(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'username',
                                                                             'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'ng-model': 'password',
                                                                 'class': 'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'first_name',
                                                                               'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'last_name',
                                                                              'class': 'form-control'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'ng-model': 'email',
                                                                            'class': 'form-control'}))
