from django.urls import path
from .views import cart, update_product, delete_product, get_navbar_cart, add_to_cart

app_name = 'cart'

urlpatterns = [
    path("", cart, name="cart"),
    path("update_cart_item", update_product, name="update_product"),
    path("delete_cart_item", delete_product, name="delete_product"),
    path("update_navbar_cart", get_navbar_cart, name="update_navbar_cart"),
    path("add_item_to_cart", add_to_cart, name="add_item_to_cart"),
]