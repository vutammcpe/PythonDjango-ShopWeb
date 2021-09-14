from django.conf.urls import include
from django.urls import path
from django.views.generic.base import View
from.views import  CheckoutView, HomeView, ItemDetailView



app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
]

    