from django.contrib import admin
from .models import Area, Storage, StorageProduct

# Register your models here.
admin.site.register(Area)
admin.site.register(Storage)


class StorageProductAdmin(admin.ModelAdmin):
    list_display = ("product", "storage", "quantity")

admin.site.register(StorageProduct, StorageProductAdmin)
