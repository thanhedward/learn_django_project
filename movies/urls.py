from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    path('stats/', views.movie_stats, name='movie_stats'),
    path('view_movies/', views.movies_view, name='movies_view'),
    ]