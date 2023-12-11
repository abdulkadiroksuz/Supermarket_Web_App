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

# used to update the quantity of the product in the cart
def update_product(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        cart_item = CartProduct.objects.get(product=product_id, cart=cart)
        new_quantity = request.POST.get("new_quantity")
        cart_item.quantity = new_quantity
        cart_item.save()

# used to delete the product from the cart
# when the use clicks on the delete button
# or make the quantity of the product to 0    
def delete_product(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        cart_item = CartProduct.objects.get(product=product_id, cart=cart)
        cart_item.delete()

# returns the count of the products in the cart        
def get_navbar_cart(request):
    if request.method == "GET":
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        total_products = CartProduct.objects.filter(cart=cart).count()
        
        data = {
            "total_cart_products": total_products
            }
    return JsonResponse(data)

# used to add the product to the cart
def add_to_cart(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"})

    try:
        product_slug = request.POST.get("product_slug")
        product = Product.objects.get(slug=product_slug)

        customer = Customer.objects.get(user=request.user)
        cart, created = Cart.objects.get_or_create(customer=customer)

        add_quantity = int(request.POST.get("quantity", 1))

        isExists = CartProduct.objects.filter(product=product, cart=cart).exists()
        if isExists:
            existing = CartProduct.objects.get(product=product, cart=cart)
            existing.quantity = existing.quantity + add_quantity
            existing.save()
            return JsonResponse({"success": True})
        else:
            new_value = CartProduct(cart=cart, product=product, quantity=add_quantity)
            new_value.save()
            return JsonResponse({"success": True})
        
    except Exception as e:
        return JsonResponse({"error": str(e)})