from django.urls import path
from . import views

urlpatterns = [
    path('basket_product_list/', views.product_list_view, name='basket_product_list'),
    path('create_product/', views.create_product_view, name='create_product'),
    path('update_product/<int:id>/update/', views.update_product_view, name='update_product'),
    path('delete_product/<int:id>/delete/', views.delete_product_view, name='delete_product'),

]