from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_list/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie_search/', views.SearchView.as_view(), name='movie_search'),
    path('user_register/', views.RegisterView.as_view(), name='user_register'),
    path('user_login/', views.AuthLoginView.as_view(), name='user_login'),
    path('user_logout/', views.AuthLogoutView.as_view(), name='user_logout'),
    path('movie_list/<int:id>/add_comment/', views.CommentCreateView.as_view(), name='add_comment'),
    path('movie_list/<int:id>/book_vip/', views.VipBookingCreateView.as_view(), name='book_vip'),
    path('movie_add/', views.MovieCreateView.as_view(), name='movie_add'),
    path('movie_edit/<int:id>/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('movie_delete/<int:id>/', views.MovieDeleteView.as_view(), name='movie_delete'),
]