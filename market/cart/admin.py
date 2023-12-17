from django.contrib import admin
from .models import Cart, CartProduct

class CartProductInline(admin.TabularInline):  # or admin.StackedInline
    model = CartProduct
    extra = 1

class CartProductAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ['cart__customer__user__username', 'product__name']

admin.site.register(CartProduct, CartProductAdmin)

class CartAdmin(admin.ModelAdmin):
    inlines = [CartProductInline]
    list_display = ('customer', 'get_total_prodcuts', 'get_total_quantity', 'get_total_amount')
    search_fields = ['customer__user__username']
    readonly_fields = ['customer']

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.cartproduct_set.all())

    def get_total_amount(self, obj):
        return sum(item.quantity * item.product.price for item in obj.cartproduct_set.all())

    def get_total_prodcuts(self, obj):
        return obj.cartproduct_set.count()
    
    get_total_quantity.short_description = 'Total Quantity'
    get_total_amount.short_description = 'Total Amount'
    get_total_prodcuts.short_description = 'Total Products'

admin.site.register(Cart, CartAdmin)

