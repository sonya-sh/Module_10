from django.db import models
from users.models import CustomUser


class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, to_field='id')
    products = models.TextField(default='Пусто')

