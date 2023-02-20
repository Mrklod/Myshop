from django.shortcuts import render

def index(request):
    context = {'title':'test Title','username':'Sasha'}
    return render(request,'products/index.html',context=context)


def products(request):
    context = {'title':'Каталог'}
    return render(request,'products/products.html')