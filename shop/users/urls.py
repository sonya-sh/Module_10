from django.urls import path, include
from .views import SignUpView
from . import views

urlpatterns = [
    path('', views.sign_in, name='users'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.sign_up, name='sign_up'),
]
