from django.shortcuts import render, redirect
from django.db.models import Q
from item.models import Category,Product
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    
    context = {
        'categories':categories,
    }
    return render(request, 'core/index.html', context)



def search(request):
    search_text = request.GET.get('search_text')
    
    if search_text is None:
        search_text = ''
        
    categories = Category.objects.all()
    filtered_products = Product.objects.filter(
        Q(name__icontains=search_text) | Q(description__icontains=search_text)
    )
    
    context = {
        'categories':categories,
        'products':filtered_products
    }
    
    return render(request, 'core/search.html', context)

