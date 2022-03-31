from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class GreetingView(View):
    def get(self,request):
        return HttpResponse("<h1>First CBV says hello!!</h1>")