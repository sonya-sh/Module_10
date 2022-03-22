from .models import CustomUser
from .forms import RegistrForm, ChangeProfile, ChangeData1
from catalog.models import Product
from order.models import Order
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import json


def start(response):
    return render(response, "users/start.html")


def sign_up(request):
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            data_user = form.cleaned_data
            data = {'form': form}
            if CustomUser.objects.filter(username=data_user['username']).exists():
                return render(request, 'users/form_registration_alert.html', data)
            if data_user['password_1'] == data_user['password']:
                del data_user['password_1']
                user = CustomUser.objects.create_user(**data_user)
                user.save()
                return render(request, 'users/form_complete.html')
            else:
                return render(request, 'users/form_registration_alert_password.html', data)
        else:
            data = {'form': form}
            return render(request, 'users/form_registration_alert.html', data)
    form = RegistrForm()
    data = {'form': form}
    return render(request, 'users/form_registration.html', data)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'users/login_success.html')
    else:
        return render(request, 'users/login.html')


def sign_in(request):
    return render(request, 'base2.html')


def logout_user(request):
    logout(request)
    return render(request, 'users/login.html')


def history(request):
    sell_base = Order.objects.filter(id_user=request.user.id)
    if sell_base:
        sell = Order.objects.filter(id_user=request.user.id)
    else:
        sell = None
    return render(request, 'users/history.html', context={'sell': sell})


def detail_order(request, order_id):
    order = Order.objects.get(id=order_id)
    cart = json.loads(order.structure)
    products = Product.objects.filter(id__in=cart.keys())
    for product in products:
        product.value = cart[str(product.id)]['quantity']
    cart['cost'] = order.cost
    return render(request, 'users/detail_order.html', context={'order': order, 'products': products, 'cart': cart})


def change_data1(request):
    user = CustomUser.objects.get(id=request.user.id)
    form = ChangeData1()
    if request.method == "POST":
        form = ChangeData1(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            if data_form['username']:
                user.username = data_form['username']
            if data_form['password_1'] == data_form['password']:
                if data_form['password']:
                    user.set_password(data_form['password'])
            else:
                context = {'form': form}
                return render(request, 'users/change_data1_alert.html', context=context)
            user.save()
            return render(request, 'users/change_profile_complete.html')
    context = {'form': form}
    return render(request, 'users/change_data1.html', context=context)


def change_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    form = ChangeProfile()
    if request.method == "POST":
        form = ChangeProfile(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            if data_form['name']:
                user.name = data_form['name']
            if data_form['surname']:
                user.surname = data_form['surname']
            if data_form['phone_number']:
                user.phone_number = data_form['phone_number']
            if data_form['email']:
                user.email = data_form['email']

            user.save()
            return render(request, 'users/change_profile_complete.html')
    context = {'form': form}
    return render(request, 'users/change_profile.html', context=context)