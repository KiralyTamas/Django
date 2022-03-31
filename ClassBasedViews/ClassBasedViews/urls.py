from django.contrib import admin
from django.urls import path
from cbvApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GreetingView.as_view())
]
