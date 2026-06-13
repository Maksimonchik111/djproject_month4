from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Category, Product



class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"


class CategoryListView(ListView):
    model = Category
    template_name = "categories.html"
    context_object_name = "categories"


# 3. Продукты конкретной категории
class CategoryProductsListView(ListView):
    model = Product
    template_name = "category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("id")
        self.category = get_object_or_404(Category, id=category_id)
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context
