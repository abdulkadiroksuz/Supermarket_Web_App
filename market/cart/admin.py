from django.contrib import admin
from .models import Cart, CartProduct
# Register your models here.
admin.site.register(Cart)

#admin panel view
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
admin.site.register(CartProduct,CartProductAdmin)
