from django.urls import path
from .views import cart, update_product, delete_product

app_name = 'cart'

urlpatterns = [
    path("", cart, name="cart"),
    path("update_cart_item", update_product, name="update_product"),
    path("delete_cart_item", delete_product, name="update_product"),
]