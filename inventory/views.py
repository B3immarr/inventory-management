from django.shortcuts import render
from .models import Item, Category, Brand
# Create your views here.


# inventory/views.py

def item_list(request):
    category = request.GET.get('category')
    brand = request.GET.get('brand')

    items = Item.objects.all()
    if category:
        items = items.filter(category=category)
    if brand:
        items = items.filter(brand=brand)

    categories = Item.objects.values_list('category', flat=True).distinct()
    brands = Item.objects.values_list('brand', flat=True).distinct()

    return render(request, 'item_list.html', {
        'items': items,
        'categories': categories,
        'brands': brands,
    })
