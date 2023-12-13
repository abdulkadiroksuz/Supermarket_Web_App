from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from item.models import Category
from .models import Company

# Create your views here.
def index(request):
    categories = Category.objects.all()
    
    context = {
        'categories':categories,
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

