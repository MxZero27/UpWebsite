from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Products, Images

# Create your views here.
def index(request):
    products = Products.objects.all()
    #Hot Sellers
   # Hot = Products.objects.all.order_by('SoldCount')
    return render(request, 'Home/home.html', {'products': products})

def detail_view(request,):
    products = get_object_or_404(Products,)
    photos = Images.objects.filter(products=products)
    return render(request, 'detail.html', {
        'products':products,
        'photos':photos
    })

def home(request):
    Hot = Products.objects.order_by('SoldCount')
    products = Products.objects.all()
    return render(request, 'Home/home.html', {'products': products, 'Hot':Hot})