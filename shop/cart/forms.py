from django import forms
from phonenumber_field.modelfields import PhoneNumberField

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class AddOrder(forms.Form):
    name = forms.CharField(max_length=120, label='Ваше имя')
    phone = forms.CharField(min_length=5, max_length=15, label='Ваш телефон')
    address = forms.CharField(max_length=300, label='Адрес доставки')