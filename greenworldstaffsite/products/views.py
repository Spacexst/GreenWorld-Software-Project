from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Staff

# Class-based view for listing products


class ProductList(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'product_list'

# Function-based view for managing a specific product


def product_management(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # Handle form submission for updating the product
        pass
    return render(request, 'products/product_management.html', {'product': product})

# Class-based view for listing staff


class StaffList(ListView):
    model = Staff
    template_name = "staff_list/staff_list.html"
    context_object_name = "staff_list"
