from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list_view, name='product_list'),
    path('category_list/', views.category_list_view, name='category_list'),
    path('category_products/<int:id>/', views.category_products_view, name='category_products'),
]