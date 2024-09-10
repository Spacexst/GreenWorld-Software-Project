from django.urls import path
from .views import productList, ProductUpdate
from .import views
#app_name = 'products'

urlpatterns = [
path("products/", productList, name="product_list"),
path('product/<int:pk>/update/',
        ProductUpdate.as_view(), name='product_update'),
    
    #path('product/create', views.ProductCreate.as_view(), name='product_create'),
    #path('product/update/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    #path('product/delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    ]
