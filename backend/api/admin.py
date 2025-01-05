from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'updated_at']
