from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sign_in, name='users'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.sign_up, name='sign_up'),
    path('history/', views.history, name='history'),
    path('history/order_<int:order_id>', views.detail_order, name='detail_order'),
]
