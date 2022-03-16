from django.contrib import admin
from django.urls import path
from templatesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firsttemplate/', views.renderTemplate),
    path('empinfo/', views.renderEmployee)
]