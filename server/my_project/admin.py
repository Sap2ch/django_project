from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price', 'currency', 'photo')
    

admin.site.register(Product, ProductAdmin)
