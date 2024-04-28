from django.http import HttpResponse
from .models import Product
from django.shortcuts import render

def check_product(request):
    product = request.GET.get('product')
    products = Product.objects.filter(name=product)

    return render(request, 'partials/htmx_components/check_product.html', {'products': products})

def save_product(request):
    name = request.POST.get('product')
    price = request.POST.get('price')

    product = Product(
        name = name,
        price = price
    )

    product.save()

    return HttpResponse('Saved successfully')