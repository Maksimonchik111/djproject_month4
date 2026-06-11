from django.urls import path
from . import views

urlpatterns = [
    path('tour_list/', views.tour_list_view, name='tour_list'),
    path('tour_list/<int:id>/', views.tour_detail_view, name='tour_detail'),
    path('tour_seacrh/', views.search_view, name='tour_search'),
]