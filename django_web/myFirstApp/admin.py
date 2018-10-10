from django.contrib import admin

# Register your models here.
from .models import Product,Category

class ProductAdmin(admin.ModelAdmin):
    fields = ['product_name','product_cost']
    list_display = ('product_name','product_cost')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
