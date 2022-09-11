from django.shortcuts import render
from productos.models import Producto
# Create your views here.
def productos(request):
    productos_registrados = Producto.objects.all()

    return render(request, 'productos.html', {'productos_registrados':productos_registrados})