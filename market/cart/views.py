from django.shortcuts import render
from market.settings import MEDIA_URL
from item.models import Category
from user.models import Customer

from .models import Cart,CartProduct


# Create your views here.
def cart(request):
    categories = Category.objects.all()
    customer = Customer.objects.get(user=request.user)
    try:
        cart = Cart.objects.get(customer=customer)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(customer=customer)

    cart_products = (
        CartProduct.objects.filter(cart=cart)
        .select_related("product")
        .values(
            "product__id",
            "product__name",
            "product__price",
            "product__description",
            "product__slug",
            "product__image",
            "quantity",
        )
    )

    context = {
        "categories": categories,
        "items": cart_products,
        "total_items": len(cart_products),
    }
    return render(request, "cart.html", context)
