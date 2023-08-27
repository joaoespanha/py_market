from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
from django.db.models import Q


# Create your views here.


# VINHO RESERVADO CHARDONNAY COM A BOBINHA
def items(request):
    query = request.GET.get("query", "")
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get("category", 0)
    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(
        request,
        "item/items.html",
        context={
            "items": items,
            "query": query,
            "categories": categories,
            "category_id": int(category_id),
        },
    )


def details(request, id):
    item = get_object_or_404(Item, pk=id)
    rel_items = Item.objects.filter(category=item.category).exclude(pk=id)[0:3]

    return render(
        request,
        "item/item_details.html",
        context={"item": item, "related_items": rel_items},
    )


@login_required
def new(request):
    form = NewItemForm(request.POST, request.FILES)
    if form.is_valid():
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()

        return redirect("item:details", id=item.id)
    else:
        form = NewItemForm()
        return render(request, "item/form.html", {"form": form, "title": "Add Item"})


@login_required
def edit(request, id):
    item = get_object_or_404(Item, pk=id, created_by=request.user)
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()

        return redirect("item:details", id=item.id)
    else:
        form = NewItemForm(instance=item)
        return render(request, "item/form.html", {"form": form, "title": "Edit Item"})


@login_required
def delete(request, id):
    item = get_object_or_404(Item, pk=id, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")
