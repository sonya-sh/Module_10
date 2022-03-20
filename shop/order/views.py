from django.shortcuts import render
from cart.models import CustomUser
from cart.cart import Cart
from order.models import Order
from cart.models import CartItem
from .forms import AddOrder
import json


def order_create(request):
    if request.method == 'POST':
        cart = Cart(request)
        form = AddOrder(request.POST)
        if form.is_valid():
            order_data = form.cleaned_data
            phone = order_data['phone']
            address = order_data['address']
            email = order_data['email']
            cart_base = CartItem.objects.get(id_user=request.user.id)
            order = Order(id_user=CustomUser.objects.get(id=request.user.id),
                          phone=phone,
                          structure=json.dumps(cart.cart),
                          cost=cart.get_total_price(),
                          address=address,
                          email=email
                          )
        order.save()
        cart.cart = {}
        cart_base.products = json.dumps(cart.cart)
        cart_base.save()
        return render(request, 'order_complete.html', context={'order': order})
    form = AddOrder()
    cart = Cart(request)
    cart_base = CartItem.objects.get(id_user=request.user.id)
    cart.cart = json.loads(cart_base.products)
    return render(request, 'order.html', context={'form': form, 'cart': cart})
