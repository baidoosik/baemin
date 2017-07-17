from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from shop.models import Shop,Item,Order
from shop.forms import OrderModelForm
# Create your views here.

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()

    return render(request,'accounts/signup_form.html',
                  {'form':form
            })

@login_required
def profile(request):
    user= request.user
    my_order = Order.objects.filter(user=user).all()

    return render(request,'accounts/profile.html',{
        'user':user,
        'order_list':my_order,
    })