from django.contrib import admin
from .models import Product

# Register your models here.
<<<<<<< HEAD
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Staff)
=======
admin.site.register(Product)
>>>>>>> a3b17b56d99f8bf8ceeb9d15814e3a3740c9159e

