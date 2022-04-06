from django.shortcuts import render
from django.http import HttpResponse
from cookiesApp.forms import ItemForm

def home(request):
    request.session.set_test_cookie()
    return HttpResponse('<b>Home Page</b>')

def page(request):
    if request.session.test_cookie_worked():
        print('Cookie is enabled')
        request.session.delete_test_cookie()
    return HttpResponse('<b>Success</b>')

def countView(request):
    if 'count' in request.COOKIES:
        count=int(request.COOKIES['count'])+1
    else:
        count=1
    count_dict={'count':count}
    response=render(request, 'cookiesApp/count.html',count_dict)
    response.set_cookie('count',count)
    return response

def index(request):
    return render(request, 'cookiesApp/index.html')

def addItem(request):
    form=ItemForm()
    response=render(request,'cookiesApp/addItems.html',{'form':form})
    if request.method=='POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            quantity=form.cleaned_data['quantity']
            response.set_cookie(name,quantity)
    return response

def displayCart(request):
    return render(request, 'cookiesApp/displayItems.html')