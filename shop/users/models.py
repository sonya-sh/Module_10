from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField('Имя', max_length=255, default='')
    surname = models.CharField('Фамилия', max_length=255, default='')
    phone_number = models.CharField('Номер телефона', max_length=255, default='')
    email = models.EmailField('Электронная почта', max_length=255, default='')


