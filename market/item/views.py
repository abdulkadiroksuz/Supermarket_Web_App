from django.shortcuts import get_object_or_404, render

from .models import Product, Category
from storage.models import StorageProduct
from django.db.models import Sum
from django.core.paginator import Paginator
# Category and realted products
def category(request, category_slug):
    # Retrieve the category object based on the provided slug
    category_object = get_object_or_404(Category, slug=category_slug)

    categories = Category.objects.all()
    # Retrieve all products associated with the category
    associated_products = Product.objects.filter(productcategory__category=category_object)

    paginator = Paginator(associated_products,2)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    context = {
        'categories': categories,
        'category': category_object,
        'page_obj' : page_obj,
    }
    
    return render(request, 'item/category.html', context)


def product(request, product_slug):
    product_object = get_object_or_404(Product, slug=product_slug)
    stock = StorageProduct.objects.filter(product = product_object).aggregate(Sum("quantity"))["quantity__sum"]
    
    categories = Category.objects.all()
    
    stock_status = "In Stock"
    if (stock is None) or stock==0:
        stock_status = "Out of Stock"

    isRunningOut = False
    if (stock <= 5 and stock > 0):
        isRunningOut = True
     
    context = {
        'categories': categories,
        'product': product_object,
        'stock_status': stock_status,
        'isRunningOut': isRunningOut,
        'stock' : stock
    }
    
    return render(request, 'item/product.html', context)
