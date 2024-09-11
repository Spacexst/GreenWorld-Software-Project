from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm


# Class-based view for listing products
@login_required
def productList(request):
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
# View to create a new article.
class ProductCreate(CreateView):
    template_name = 'products/product_create.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

# View to update an article.
class ProductUpdate(UpdateView, LoginRequiredMixin):
    template_name = "products/product_update.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object
        return context
    
            

# View for article deletion confirmation.
class ProductDelete(DeleteView, LoginRequiredMixin):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy("product_list")



# Class-based view for listing staff

