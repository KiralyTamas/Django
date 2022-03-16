from django.urls import path
from quoteapp.views import displayQuote

urlpatterns = [
    path('quote/', displayQuote)
]