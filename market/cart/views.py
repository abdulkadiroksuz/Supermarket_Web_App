from django.db import connection
from django.db.models.fields.files import ImageFieldFile
from market.settings import MEDIA_URL
from django.shortcuts import render
from item.models import Category
from user.models import Customer

from .models import Cart


# Create your views here.
def cart(request):
    categories = Category.objects.all()
    customer = Customer.objects.get(user=request.user)
    try:
        cart = Cart.objects.get(customer=customer)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(customer=customer)
    cart = cart.id

    raw_sql_query = (
        "SELECT p.*, c.quantity "
        + "FROM cart_cartproduct as c "
        + "INNER JOIN item_product as p "
        + " ON c.product_id = p.id "
        + "WHERE c.cart_id = "
        + str(
            cart,
        )
        + ";"
    )

    with connection.cursor() as cursor:
        cursor.execute(raw_sql_query)
        results = cursor.fetchall()

    # Convert results to dictionary by dict comprehension
    results_dict = [
        {
            "product": {
                "id": x[0],
                "name": x[1],
                "price": x[2],
                "description": x[3],
                "slug": x[5],
                "image": "/media/"+x[6],
            },
            "quantity": x[7],
        }
        for x in results
    ]
    context = {
        "categories": categories,
        "items": results_dict,
        "total_items": len(results),
    }
    return render(request, "cart.html", context)
