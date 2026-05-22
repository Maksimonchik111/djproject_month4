from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_view, name="Books"),
]