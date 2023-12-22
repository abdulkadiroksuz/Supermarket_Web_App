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
    Gets the 8 most popular products.

    RELATED SQL QUERY ->\n
    SELECT p.*\n
    FROM item_product p\n
    INNER JOIN order_orderproduct o\n
    ON p.id = o.product_id\n
    GROUP BY o.product_id\n
    ORDER BY SUM(o.quantity) DESC;
    """
    subquery = (
        OrderProduct.objects
        .values('product_id')
        .annotate(total=Sum('quantity'))
        .order_by('-total')  # Use '-' to order in descending order (highest total first)
        .values_list('product_id', flat=True)
    )[:8]

    return Product.objects.filter(id__in=subquery)






