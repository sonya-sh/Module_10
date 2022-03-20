from django import forms


class AddOrder(forms.Form):
    phone = forms.CharField(min_length=1, max_length=15, label='Номер телефона')
    address = forms.CharField(min_length=1, max_length=250, label='Адрес доставки')
    email = forms.EmailField(min_length=1, max_length=100, label='Email')

