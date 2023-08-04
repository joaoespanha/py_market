from django.shortcuts import render
from item.models import Category, Item
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    items = Item.objects.all()[0:6]
    categories = Category.objects.all()[0:3]

    return render(request, "core/index.html", {"items": list(items), "categories":categories})


def contact(request):
    
    return render(request, "core/contact.html", {})
