from django.shortcuts import render
from sessionApp.forms import ItemForm
from django.http import HttpResponse

def pageCount(request):
    count=request.session.get('count',0)
    count=count+1
    request.session['count']=count
    return render(request, 'sessionApp/count.html',{'count':count})

def index(request):
    return render(request, 'sessionApp/inde.html')

def addItem(request):
    form=ItemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render(request,'sessionApp/addItem.html',{'form':fom})

def displayCart(request):
    return render(request, 'sessionApp/displayItems.html')