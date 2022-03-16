from django.shortcuts import render

def electronics(request):
    product_dict={
        'product1':'Mac',
        'product2':'IPhone',
        'product3':'Dell'
    }
    return render(request, 'productsapp/products.html', product_dict)

def toys(request):
    product_dict={
        'product1':'Teddy Bear',
        'product2':'Doll',
        'product3':'World of Warcraft'
    }
    return render(request, 'productsapp/products.html', product_dict)

def shoes(request):
    product_dict={
        'product1':'Adidas',
        'product2':'Nike',
        'product3':'Tisza'
    }
    return render(request, 'productsapp/products.html', product_dict)

def index(request):
    return render(request, 'productsapp/index.html')