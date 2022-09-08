from unicodedata import name
from django.shortcuts import render

# Create your views here.
def productos(request):
    return render(request, 'productos.html')