from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Customer, Adress

# Register new user with customer fields
admin.site.unregister(User)
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Customer'

class CustomUserAdmin(UserAdmin):
    inlines = (CustomerInline, )
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Adress)