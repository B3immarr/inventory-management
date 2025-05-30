from django.shortcuts import render
from .models import Item, Category, Brand
# Create your views here.


# inventory/views.py
from django.shortcuts import render
from .models import Items

def item_list(request):
    items = Items.objects.all()  # Get all items from the database
    return render(request, 'item_list.html', {'items': items})