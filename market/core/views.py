from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from item.models import Category, Product


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

    categories = Category.objects.all()
    
    # get products whose name or description contains search_text non case-sensitive 
    search_filter = Q(name__icontains=search_text) | Q(description__icontains=search_text)
    products = Product.objects.filter(search_filter)
    
    context = {
        'search_text': search_text,
        'products': products,
        'categories': categories,
    }
    return render(request, 'core/search.html',context)





