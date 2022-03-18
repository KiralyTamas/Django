from django.contrib import admin
from django.urls import path
from productsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('electronics/',views.electronics),
    path('toys/',views.toys),
    path('shoes/',views.shoes),
]
