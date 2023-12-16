from django.shortcuts import render
from django.db.models import Sum
from item.models import Category, Product
from order.models import OrderProduct
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    categories = Category.objects.all()
       
    context = {
        'categories':categories,
        'popularProducts': get_popular_products(),
    }
    return render(request, 'core/index.html', context)

def search(request, search_text): 
    # get products whose name contains search_text non case-sensitive 
    products = Product.objects.filter(name__icontains=search_text)
    paginator = Paginator(products,6)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    context = {
        'search_text': search_text,
        'page_obj': page_obj,
    }
    return render(request, 'core/search.html',context)


def get_popular_products():
    """
    gets the 8 most popular products

    RELATED SQL QUERY ->\n
    SELECT *\n 
    FROM item_product\n
    WHERE id IN (\n
        SELECT product_id\n
        FROM order_orderproduct\n
        GROUP BY product_id\n
        ORDER BY SUM(quantity) DESC\n
        LIMIT 8);\n
    """
    subquery = (
        OrderProduct.objects
        .annotate(total=Sum("quantity"))
        .values("product_id")
        .order_by('-total')  # Use '-' to order in descending order (highest total first)
    )
    
    return Product.objects.filter(id__in=subquery)






