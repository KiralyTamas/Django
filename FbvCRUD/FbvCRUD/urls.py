from django.contrib import admin
from django.urls import path
from fbvApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getStudent),
    path('create/',views.createStudent),
    path('delete/<int:id>',views.deleteStudent),
    path('update/<int:id>',views.updateStudent)
]
