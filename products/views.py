from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product 
from django.utils import timezone

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html',{'product': product})

def product_recent(request):
    #in timedelta place days/hours ago for recent products create time 
    time_day_ago = timezone.now() - timezone.timedelta(days=1)
    recent_products = Product.objects.filter(created_at__gte=time_day_ago)
    return render(request, 'products/most_recent.html', {'recent_products' : recent_products})