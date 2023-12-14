from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from item.models import Category, Product
from user.models import Customer

from .models import Cart,CartProduct
from storage.models import StorageProduct


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
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method","stock":-1})
    try:
        product_id = request.POST.get("product_id")
        product_obj = get_object_or_404(Product, id=product_id)
        customer_obj = Customer.objects.get(user=request.user)
        cart_obj = Cart.objects.get(customer=customer_obj)
        cart_item = CartProduct.objects.get(product=product_id, cart=cart_obj)
        new_quantity = int(request.POST.get("new_quantity"))
        
        stock = StorageProduct.objects.filter(product=product_obj).aggregate(Sum('quantity'))['quantity__sum']
        if new_quantity > stock:
            err_msg = f"Not enough stock, {stock} left."
            return JsonResponse({"success": False, "error": err_msg, "stock":stock})
        else:
            cart_item.quantity = new_quantity
        cart_item.save()
        return JsonResponse({"success": True})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "error": "Server error", "stock":-1})

# used to delete the product from the cart
# when the use clicks on the delete button
# or make the quantity of the product to 0    
def delete_product(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method"})
    try:
        product_id = request.POST.get("product_id")
        customer_obj = get_object_or_404(Customer, user=request.user)
        cart_obj = get_object_or_404(Cart, customer=customer_obj)
        cart_item = CartProduct.objects.get(product=product_id, cart=cart_obj)
        cart_item.delete()
        return JsonResponse({"success": True})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "error": "Server error"})

# returns the count of the products in the cart        
def get_navbar_cart(request):
    if request.method == "GET":
        customer = Customer.objects.get(user=request.user)
        cart, isCreated = Cart.objects.get_or_create(customer=customer)
        if isCreated:
            total_products = 0
        else:
            total_products = CartProduct.objects.filter(cart=cart).count()
        
        data = {
            "total_cart_products": total_products
            }
    return JsonResponse(data)

# used to add the product to the cart
def add_to_cart(request):
    if request.method != 'POST':
        return JsonResponse({"success": False, "error": "Invalid request method"})

    try:
        product_slug = request.POST.get("product_slug")
        product_obj = get_object_or_404(Product, slug=product_slug)

        customer_obj = get_object_or_404(Customer, user=request.user)
        cart_obj, created = Cart.objects.get_or_create(customer=customer_obj)

        add_quantity = int(request.POST.get("quantity", 1))
        
        stock = StorageProduct.objects.filter(product=product_obj).aggregate(Sum('quantity'))['quantity__sum']
        
        is_exists = CartProduct.objects.filter(product=product_obj, cart=cart_obj).exists()
        if is_exists:
            existing = CartProduct.objects.get(product=product_obj, cart=cart_obj)
            new_quantity = existing.quantity + add_quantity
            if new_quantity > stock:
                err_msg = f"Not enough stock, {stock} left.\nYou already have {existing.quantity} in your cart."
                return JsonResponse({"success": False, "error": err_msg})
            existing.quantity = new_quantity
            existing.save()
            return JsonResponse({"success": True})
        else:
            if add_quantity > stock:
                err_msg = f"Not enough stock, {stock} left."
                return JsonResponse({"success": False, "error": err_msg})
            new_value = CartProduct(cart=cart_obj, product=product_obj, quantity=add_quantity)
            new_value.save()
            return JsonResponse({"success": True})
        
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "error": "Server error"})