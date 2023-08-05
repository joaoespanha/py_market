from django.shortcuts import render, get_object_or_404
from .models import Item
# Create your views here.
def details(request, item_id):
    item =  get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category).exclude(pk=item_id)[0:3]

    return render(request, 'item/item_details.html', context={'item':item, 'related_items':related_items} )