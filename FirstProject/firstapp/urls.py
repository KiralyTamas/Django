from django.urls import path
from firstapp.views import index, display,displayDateTime

urlpatterns=[
    path('', index),
    path('display/', display),
    path('date/', displayDateTime)
]