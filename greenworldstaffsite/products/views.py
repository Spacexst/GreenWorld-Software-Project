from django.shortcuts import render
from .models import Product, Staff

from django.views.generic import ListView
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'product_list'

class StaffListView(ListView):
    model = Staff
    template_name = "staff_list/staff_list.html"
    context_object_name = "staff_list"
