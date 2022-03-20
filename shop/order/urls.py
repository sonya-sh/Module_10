from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('registration_order/', views.order_create, name='order'),
]
