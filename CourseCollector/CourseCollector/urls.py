from django.contrib import admin
from django.urls import path
from courseApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CourseList),
    path('addCourse/',views.AddCourse),
    path('updateCourse/<int:id>',views.UpdateCourse),
    path('deleteCourse/<int:id>',views.DeleteCourse),
]
