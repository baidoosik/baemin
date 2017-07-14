from django.shortcuts import render


def index_view(request):
    return render(request,'shop/index.html')
# Create your views here.
