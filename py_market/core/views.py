from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm

# Create your views here.


def index(request):
    items = Item.objects.all()[0:6]
    cates = Category.objects.all()[0:3]

    return render(
        request, "core/index.html", {"items": list(items), "categories": cates}
    )


def contact(request):
    return render(request, "core/contact.html", {})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/login")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})
