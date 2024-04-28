from django.shortcuts import render

# Create your views here.
def list_products(request):
    return render(request, 'list_products.html')