from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list_view(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})


def category_list_view(request):
    categories = Category.objects.all()

    return render(request, 'categories.html', {'categories': categories})


def category_products_view(request, id):
    category =  get_object_or_404(Category, id=id)

    products = Product.objects.filter(category=category)

    return render(request, 'category_products.html', {'category': category,'products': products})