from django.contrib import admin
from django.urls import path
from moviesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('moviesList/', views.moviesList),
    path('addMovies/', views.addMovies),
]
