from django.contrib import admin
from .models import Category, Brand, Item
# Register your models here.


# inventory/admin.py
from django.contrib import admin
from django import forms
from .models import Item, Category, Brand

class ItemFormAdmin(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'quantity': forms.NumberInput(attrs={'type': 'number', 'min': '0'}),
        }

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemFormAdmin
    list_display = ['id', 'name', 'brand', 'quantity', 'category', 'created_at', 'image']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'brand', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']