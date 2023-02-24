from django.shortcuts import render
from .models import *

def index(request):
    context = {'title':'test Title','username':'Sasha'}
    return render(request,'products/index.html',context=context)


def products(request):
    context = {'title':'Каталог',
               'products':Products.objects.all(),
               'category':Category.objects.all()}
    return render(request,'products/products.html',context=context)