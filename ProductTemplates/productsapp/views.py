from django.shortcuts import render

def electronics(request):
    product_dict={
        'heading':'ELECTRONICS',
        'image1':'image/Mac.jpg',
        'product1':'Mac',
        'image2':'image/Android.jpg',
        'product2':'Android',
        'image3':'image/Dell.jpg',
        'product3':'Dell'
    }
    return render(request, 'productsapp/products.html', product_dict)

def toys(request):
    product_dict={
        'heading':'TOYS',
        'image1':'image/TeddyBear.jpg',
        'product1':'Teddy Bear',
        'image2':'image/Doll.jpg',
        'product2':'Doll',
        'image3':'image/Wow.jpg',
        'product3':'World of Warcraft'
    }
    return render(request, 'productsapp/products.html', product_dict)

def shoes(request):
    product_dict={
        'heading':'SHOES',
        'image1':'image/Adidas.jpg',
        'product1':'Adidas',
        'image2':'image/Nike.jpg',
        'product2':'Nike',
        'image3':'image/Tisza.jpg',
        'product3':'Tisza'
    }
    return render(request, 'productsapp/products.html', product_dict)

def index(request):
    return render(request, 'productsapp/index.html')