from django.http import JsonResponse
from django.shortcuts import render
from item.models import Category, Product
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


def update_product(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        cart_item = CartProduct.objects.get(product=product_id, cart=cart)
        new_quantity = request.POST.get("new_quantity")
        cart_item.quantity = new_quantity
        cart_item.save()
    
def delete_product(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        cart_item = CartProduct.objects.get(product=product_id, cart=cart)
        cart_item.delete()
        
def get_navbar_cart(request):
    if request.method == "GET":
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        total_products = CartProduct.objects.filter(cart=cart).count()
        
        data = {
            "total_cart_products": total_products
            }
    return JsonResponse(data)

def add_to_cart(request):
    if request.method == "POST":
        try:
            quantity = request.POST.get("quantity")
            product_slug = request.POST.get("product_slug")
            product = Product.objects.get(slug=product_slug)
            customer = Customer.objects.get(user=request.user)
            cart = Cart.objects.get(customer=customer)
            new_value = CartProduct(cart=cart, product=product, quantity=quantity)
            new_value.save()
            return JsonResponse({"success": True})
        except:
            return JsonResponse({"error": True})
    return JsonResponse({"error": True})