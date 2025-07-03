from django.shortcuts import render

from menu.models import Item


# Create your views here.
def home_view(request):
    return render(request, 'main.html')


def items_view(request, category):
    items = Item.objects.filter(category=Item.CategoryChoice[category])
    context = {
        'items':items
    }
    return render(request, f'{category}.html',context)
