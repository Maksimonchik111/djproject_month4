from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from .forms import BasketForm
from django.views import generic

class CreateProductView(generic.CreateView):
    template_name = 'create_product.html'
    form_class = BasketForm
    model = Basket
    success_url = '/basket_product_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateProductView, self).form_valid(form=form)



class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    model = Basket
    context_object_name = 'basket_products'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class UpdateProductView(generic.UpdateView):
    template_name = 'update_product.html'
    form_class = BasketForm
    success_url = '/basket_product_list/'
    model = Basket
    context_object_name = "basket_product_id"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=product_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateProductView, self).form_valid(form=form)


class DeleteProductView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'product_id'
    success_url = '/basket_product_list/'
    model = Basket

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=product_id)
