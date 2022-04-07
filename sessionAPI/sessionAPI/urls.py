from django.contrib import admin
from django.urls import path
from sessionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('count/',views.pageCount),
    path('addItem/',views.addItem),
    path('',views.index),
    path('displayItems/',views.displayCart),
]
