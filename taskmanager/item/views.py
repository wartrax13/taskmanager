from django.http import HttpResponse
from django.shortcuts import render, redirect

from taskmanager.item.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text')
        Item.objects.create(title=new_item_text)
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
