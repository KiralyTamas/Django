from django.contrib import admin
from django.urls import path
from regapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registerForm),
]
