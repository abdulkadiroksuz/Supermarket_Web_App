from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path("", views.cart, name="cart"),
    path("update_cart_item", views.update_product, name="update_product"),
    path("delete_cart_item", views.delete_product, name="delete_product"),
    path("update_navbar_cart", views.get_navbar_cart, name="update_navbar_cart"),
    path("add_item_to_cart", views.add_to_cart, name="add_item_to_cart"),
    path("checkout", views.checkout, name="checkout"),
]