from django.shortcuts import render
from .models import *
# Create your views here.


def products(request):
    ctx = {'items': Item.objects.all()}

    return render(request, "products.html", ctx)


def checkout(request):
    return render(request, "checkout.html")


def home(request):
    ctx = {'items': Item.objects.all()}
    return render(request, 'home.html', ctx)
