from django.urls import path
from .views import ProductList, product_management
from .import views
#app_name = 'products'

urlpatterns = [
path("products/", ProductList, name="product_list"),
path('product/<int:product_id>/edit/',
         product_management, name='product_management'),
    
    #path('product/create', views.ProductCreate.as_view(), name='product_create'),
    #path('product/update/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    #path('product/delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    ]
