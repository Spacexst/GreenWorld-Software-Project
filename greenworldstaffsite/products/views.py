from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product
from django.contrib.auth.decorators import login_required


# Class-based view for listing products
@login_required
def ProductList(request):
    model = Product.objects.all()
    template_name = "products/product_list.html"
    return render(request, template_name, {'products': model})

# Function-based view for managing a specific product


def product_management(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # Handle form submission for updating the product
        pass
    return render(request, 'products/product_management.html', {'product': product})



# Class-based view for listing staff

