from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('category_products/<int:id>/', views.CategoryProductsListView.as_view(), name='category_products'),
]