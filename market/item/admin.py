from django.contrib import admin
from .models import Category, Product, ProductCategory
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'product')
admin.site.register(ProductCategory, ProductCategoryAdmin)
