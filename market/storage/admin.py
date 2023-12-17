from django.contrib import admin
from .models import Area, Storage, StorageProduct

# Register your models here.

admin.site.register(Area)
admin.site.register(Storage)

class StorageProductInline(admin.TabularInline):
    model = StorageProduct
    readonly_fields = ("product", "storage")
    extra = 1

class StorageProductAdmin(admin.ModelAdmin):
    list_display = ("product", "storage", "quantity")
    readonly_fields = ("product", "storage")


admin.site.register(StorageProduct, StorageProductAdmin)
