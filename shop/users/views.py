from django.shortcuts import render
from .models import CustomUser
from .forms import RegistrForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm


def start(response):
    return render(response, "users/start.html")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Main')
    template_name = 'users/registr.html'


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
