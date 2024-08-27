from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, User

# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'product_list'

