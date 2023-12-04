from django.shortcuts import get_object_or_404, render

from .models import Product, Category

# Category and realted products
def category(request, category_slug):
    # Retrieve the category object based on the provided slug
    category_object = get_object_or_404(Category, slug=category_slug)

    categories = Category.objects.all()
    # Retrieve all products associated with the category
    products_in_category = Product.objects.filter(category=category_object)

    context = {
        'categories': categories,
        'category': category_object,
        'products': products_in_category,
    }
    
    return render(request, 'item/category.html', context)


def product(request, product_slug):
    product_object = get_object_or_404(Product, slug=product_slug)

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'product': product_object,
    }
    
    return render(request, 'item/product.html', context)
