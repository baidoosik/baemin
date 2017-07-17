from django.shortcuts import render,get_object_or_404,redirect
from .models import Shop,Item,Order
from .forms import OrderModelForm
from django.contrib.auth.decorators import login_required

def index_view(request):
    shop = Shop.objects.all()
    return render(request,'shop/index.html',{
        'shops':shop
    })

@login_required
def order_view(request,pk):
    shop = get_object_or_404(Shop, id=pk)
    item_price = Item.objects.filter(shop=shop).all()
    if request.method =='POST':
        form = OrderModelForm(shop,request.POST)
        if form.is_valid:
            order = form.save(commit=False)
            order.user = request.user
            order.shop = shop
            order.save()
            form.save_m2m()
            return redirect('accounts:profile')
    else:
        form= OrderModelForm(shop)

    return render(request,'shop/order.html',{
        'order_form':form,
        'shop':shop,
        'item_price':item_price,
    })
# Create your views here.
