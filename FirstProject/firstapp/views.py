from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse('<h1>This is the Opening Page</h1>')

def display(request):
    return HttpResponse("<h1>My first Django App!!</h1>")

def displayDateTime(request):
    dt=datetime.now()
    s="<b>Current Date and Time: </b>"+str(dt)
    return HttpResponse(s)