from django.shortcuts import render
from .models import Shop,Item,Order

def index_view(request):
    shop = Shop.objects.all()
    return render(request,'shop/index.html',{
        'shops':shop
    })
# Create your views here.
