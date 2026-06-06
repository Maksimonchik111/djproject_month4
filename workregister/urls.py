from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.auth_login_view, name='login'),
    path('logout/', views.auth_logout_view, name='logout'),
    path('resume_list/', views.resume_list_view, name='resume_list'),

]