from django.contrib import admin
from .models import User, Product, Staff

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Staff)

