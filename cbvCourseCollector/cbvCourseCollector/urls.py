from django.contrib import admin
from django.urls import path
from cbvCCApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CourseList.as_view(),name='index'),
    path('<int:pk>/',views.CourseDetail.as_view(), name='detail'),
    path('update/<int:pk>/',views.CourseUpdate.as_view()),
    path('delete/<int:pk>/', views.CourseDelete.as_view()),
    path('create/',views.CourseCreate.as_view())
]