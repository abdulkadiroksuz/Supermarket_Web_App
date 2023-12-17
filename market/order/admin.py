from django.contrib import admin
from .models import Order, OrderProduct
# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = [field.name for field in OrderProduct._meta.get_fields()]
    can_delete = False
    extra = 0
    
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
    list_display = ('customer', 'total_price' , 'date', 'status')
    search_fields = ['customer']
    readonly_fields = ['customer', 'total_price' , 'date']
    
    
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    readonly_fields = ['order', 'product', 'quantity']
    
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)

