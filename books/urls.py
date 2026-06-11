from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list_view, name="book_list"),
    path('book_list/<int:id>/', views.book_detail_view, name='book_detail'),
    path('seacrh/', views.search_view, name='search'),
]