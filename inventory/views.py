# inventory/views.py
from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()  # Get all items from the database
    return render(request, 'item_list.html', {'items': items})