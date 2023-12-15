from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from item.models import Category, Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    categories = Category.objects.all()
    
     #  SQL QUERY ->
#       SELECT p.*
#       FROM item_product p
#       JOIN (
#           SELECT product_id, SUM(quantity) AS total
#           FROM order_orderproduct
#           GROUP BY product_id
#       ) op ON p.id = op.product_id
#       ORDER BY op.total DESC;
    
    context = {
        'categories':categories,
        # 'popular_products': popular_products[:12],
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





