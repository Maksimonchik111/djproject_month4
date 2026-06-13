from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('resume_list/', views.ResumeListView.as_view(), name='resume_list'),
    path('resume_list/<int:id>/', views.ResumeDetailView.as_view(), name='resume_detail'),
    path('resume_seacrh/', views.SearchView.as_view(), name='resume_search'),
]