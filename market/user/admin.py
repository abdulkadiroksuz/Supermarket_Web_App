from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Adress

# Register new user with customer fields  

class CustomerAdressInline(admin.TabularInline):
    model = Adress
    readonly_fields = ()
    extra = 1
    
class CustomerAdmin(admin.ModelAdmin):
    inlines = (CustomerAdressInline, )
    readonly_fields = ("user",)
      
admin.site.register(Customer, CustomerAdmin)

class AdressAdmin(admin.ModelAdmin): 
    list_display = ("customer", "title", "full_adress")

admin.site.register(Adress, AdressAdmin)