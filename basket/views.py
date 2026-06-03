from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from .forms import BasketForm


def create_product_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/basket_product_list/')
    else:
        form = BasketForm()

    return render(request, 'create_product.html', {'form': form})



def product_list_view(request):
    if request.method == 'GET':
        basket_products = Basket.objects.all().order_by('-id')

        return render(request, 'product_list.html', {'basket_products': basket_products})


def update_product_view(request, id):
    basket_product_id = get_object_or_404(Basket, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket_product_id)
        if form.is_valid():
            form.save()
            return redirect('/basket_product_list/')
    else:
        form = BasketForm(instance=basket_product_id)

    return render(request, 'update_product.html' , {'form': form, 'basket_product_id': basket_product_id})

def delete_product_view(request, id):
    basket_product_id = get_object_or_404(Basket, id=id)
    basket_product_id.delete()
    return redirect('/basket_product_list/')