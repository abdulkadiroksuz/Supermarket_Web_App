from django.contrib import admin
from .models import Category, Product, ProductCategory
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Category,CategoryAdmin)

admin.site.register(Product)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'product')
admin.site.register(ProductCategory, ProductCategoryAdmin)
