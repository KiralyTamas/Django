from django.shortcuts import render

def electronics(request):
    product_dict={
        'heading':'ELECTRONICS',
        'image1':'images/Mac.jpg',
        'product1':'Mac',
        'image2':'images/Android.jpg',
        'product2':'Android',
        'image3':'images/Dell.jpg',
        'product3':'Dell'
    }
    return render(request, 'productsapp/products.html', product_dict)

def toys(request):
    product_dict={
        'heading':'TOYS',
        'image1':'images/TeddyBear.jpg',
        'product1':'Teddy Bear',
        'image2':'images/Doll.jpg',
        'product2':'Doll',
        'image3':'images/Wow.jpg',
        'product3':'World of Warcraft'
    }
    return render(request, 'productsapp/products.html', product_dict)

def shoes(request):
    product_dict={
        'heading':'SHOES',
        'image1':'images/Adidas.jpg',
        'product1':'Adidas',
        'image2':'images/Nike.jpg',
        'product2':'Nike',
        'image3':'images/Tisza.jpg',
        'product3':'Tisza'
    }
    return render(request, 'productsapp/products.html', product_dict)

def index(request):
    return render(request, 'productsapp/index.html')