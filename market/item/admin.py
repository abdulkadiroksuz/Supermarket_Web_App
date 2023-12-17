from django.contrib import admin
from .models import Category, Product, ProductCategory

# Inline Editing for ProductCategory
class ProductCategoryInline(admin.TabularInline):
    model = ProductCategory
    extra = 1
class CategoryProductInline(admin.TabularInline):
    model = ProductCategory
    extra = 1

# Customizing ProductAdmin List View
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductCategoryInline]
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name', 'description']


# Prepopulating Slug Fields
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryProductInline]
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'product')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
