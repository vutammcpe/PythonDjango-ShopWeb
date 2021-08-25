from django.shortcuts import render
from.models import Item
from django.views.generic import ListView, DetailView

# Create your views here.




class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home-page.html"


class CheckoutView(ListView):
    model = Item
    paginate_by = 10
    template_name = "checkout-page.html"

class ItemDetailView(DetailView):
    model = Item
    paginate_by = 10
    template_name = "product-page.html"



