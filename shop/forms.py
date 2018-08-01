from django import forms


class ShopForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'ng-model': 'name',
                                                                         'class': 'form-control'}))