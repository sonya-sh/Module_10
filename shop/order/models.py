from django.db import models
from users.models import CustomUser
from catalog.models import Product


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, to_field='id')
    phone = models.TextField(help_text='телефон заказчика', null=True)
    email = models.EmailField(help_text='Email', null=True)
    structure = models.TextField(default='Пусто', help_text='Состав заказа')
    cost = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, help_text='Стоимость заказа')
    address = models.CharField(max_length=300, null=True, help_text='Адрес доставки')
    created_on = models.DateTimeField(auto_now_add=True, help_text='Время создания записи')

    class Meta:
        ordering = ('-created_on',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
