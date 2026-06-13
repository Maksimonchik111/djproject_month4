from django.urls import path
from . import views

urlpatterns = [
    path('tour_list/', views.TourListView.as_view(), name='tour_list'),
    path('tour_list/<int:id>/', views.TourDetailView.as_view(), name='tour_detail'),
    path('tour_seacrh/', views.SearchView.as_view(), name='tour_search'),
]