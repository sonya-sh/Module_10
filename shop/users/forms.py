from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class RegistrForm(forms.Form):
    username = forms.CharField(max_length=20, label='Логин')
    name = forms.CharField(max_length=20, label='Имя')
    surname = forms.CharField(max_length=20, label='Фамилия')
    phone_number = forms.CharField(max_length=20, label='Номер телефона')
    birth_date = forms.DateField(label="Дата рождения")
    email = forms.EmailField(max_length=254, help_text='This field is required')
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password_1 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'name', 'surname', 'email', 'phone_number', 'birth_date')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'name', 'surname', 'email', 'phone_number', 'username', 'birth_date')


class ChangeProfile(forms.Form):
    name = forms.CharField(label='Имя', required=False)
    surname = forms.CharField(label='Фамилия', required=False)
    phone_number = forms.DecimalField(label="Телефон", max_digits=11, decimal_places=0, required=False)
    email = forms.EmailField(label="Электронная почта", required=False)


class ChangeData1(forms.Form):
    username = forms.CharField(label='Логин', required=False)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=False)
    password_1 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput, required=False)


