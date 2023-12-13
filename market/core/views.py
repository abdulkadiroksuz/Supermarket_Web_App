from django.http import JsonResponse
from django.shortcuts import render
from .models import Company
from item.models import Category

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

def load_footer(request):
    if request.method == "GET":
        company = Company.objects.get(id=1)
        
        data = {
            "company_name": company.name,
            "company_phone": company.phone,
            "company_address": company.address,
            "company_email": company.email,
            }
    return JsonResponse(data)

