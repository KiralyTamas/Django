from django.contrib import admin
from django.urls import path
from modelforms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listProjects/', views.listProjects),
    path('addProjects/', views.addProject),
    path('', views.index),
]