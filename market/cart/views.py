from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Case, When, IntegerField, Subquery, OuterRef
from django.db import transaction
from .models import Cart,CartProduct
from storage.models import StorageProduct
from user.models import Customer, Adress
from item.models import Product
from order.models import Order, OrderProduct


def cart(request):
    # Get the customer associated with the current user
    customerObj = Customer.objects.get(user=request.user)

    # Try to get an existing cart for the customer, or create a new one if it doesn't exist
    cartObj, created = Cart.objects.get_or_create(customer=customerObj)

    cart_products = get_adjusted_cart_products(cartObj)
    
    address_list = Adress.objects.filter(customer=customerObj)

    context = {
        "items": cart_products,
        "total_items": len(cart_products),
        "address_list": address_list,
    }

    return render(request, "cart.html", context)

def get_adjusted_cart_products(cartObj: Cart):
    """
    Get cart products with adjusted quantities.\n

    Adjusted quantity is the quantity of the product in the cart.\n
    If it is less than or equal to the quantity of the product in the storage,\n
    else it is the quantity of the product in the storage.\n    
    
    SQL Query ->\n
    SELECT\n
        p.id AS product_id,\n
        p.name AS product_name,\n
        p.price AS product_price,\n
        p.description AS product_description,\n
        p.slug AS product_slug,\n
        p.image AS product_image,\n
    CASE\n
        WHEN cp.quantity > sp.quantity THEN sp.quantity\n
        ELSE cp.quantity\n
    END AS adjusted_quantity\n
    FROM\n
        cart_cartproduct cp\n
    INNER JOIN\n
        item_product p ON cp.product_id = p.id\n
    LEFT JOIN\n
    	(SELECT product_id, sum(quantity) as quantity FROM storage_storageproduct sp GROUP BY product_id) sp\n 
    ON p.id = sp.product_id\n
    WHERE\n
        cp.cart_id = <cart_id>;\n

    """
    storage_subquery = (
        StorageProduct.objects.filter(product=OuterRef('product_id'))
        .values('product')
        .annotate(sum_quantity=Sum('quantity'))
        .values('sum_quantity')
    )

    cart_products = (
        CartProduct.objects.filter(cart=cartObj)
        .select_related("product")
        .annotate(
            adjusted_quantity=Case(
                When(quantity__gt=Subquery(storage_subquery), then=Subquery(storage_subquery)),
                default=F("quantity"),
                output_field=IntegerField(),
            )
        )
        .values(
            "product__id",
            "product__name",
            "product__price",
            "product__description",
            "product__slug",
            "product__image",
            "adjusted_quantity",
        )
    )

    return cart_products



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
            cart_item.quantity = stock
            cart_item.save()
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
            if new_quantity > 10:
                err_msg = f"You can't add more.\nYou already have {existing.quantity} in your cart."
                return JsonResponse({"success": False, "error": err_msg})
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
    
    
def checkout(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method"})
    try:
        customerObj = get_object_or_404(Customer, user=request.user)
        cartObj = get_object_or_404(Cart, customer=customerObj)
        
        totalPrice = float(request.POST.get("total_price"))
        addressId = int(request.POST.get("adress_id"))
        addressObj = get_object_or_404(Adress, id=addressId)
        # Create order
        orderObj = Order(customer=customerObj, total_price=totalPrice, address=addressObj)
        orderObj.save()        

        cartProducts = CartProduct.objects.filter(cart=cartObj)
        orderProducts = []
        with transaction.atomic():
            for cartProduct in cartProducts:
                stock = StorageProduct.objects.filter(product=cartProduct.product).aggregate(Sum('quantity'))['quantity__sum']
                if cartProduct.quantity > stock:
                    orderObj.delete()
                    return JsonResponse({"success": False, "error": "Not enough stock for some products, Please refresh the page."})
                else:
                    orderProductObj = OrderProduct(order=orderObj, product=cartProduct.product, quantity=cartProduct.quantity)
                    orderProducts.append(orderProductObj)
            
            for orderProduct in orderProducts:
                orderProduct.save()
            cartObj.delete()
        return JsonResponse({"success": True})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "error": "Server error"})