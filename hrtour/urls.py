from django.urls import path
from . import views

urlpatterns = [
    path('tour_list/', views.tour_list_view, name='tour_list')
]