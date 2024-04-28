from django.shortcuts import render
from .models import Product

# Create your views here.
def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})