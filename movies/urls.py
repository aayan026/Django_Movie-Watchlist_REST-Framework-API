from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('edit/<int:movie_id>/', views.movie_edit, name='movie_edit'),
    path('delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),
]
