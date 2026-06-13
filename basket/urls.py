from django.urls import path
from . import views

urlpatterns = [
    path('basket_product_list/', views.ProductListView.as_view(), name='basket_product_list'),
    path('create_product/', views.CreateProductView.as_view(), name='create_product'),
    path('update_product/<int:id>/update/', views.UpdateProductView.as_view(), name='update_product'),
    path('delete_product/<int:id>/delete/', views.DeleteProductView.as_view(), name='delete_product'),

]