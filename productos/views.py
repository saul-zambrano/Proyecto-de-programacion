from django.shortcuts import render
from productos.models import Producto
# Create your views here.
def cuadernos(request):
    productos_registrados = Producto.objects.filter(cat_prod_id=3)
    return render(request, 'cuadernos.html', {'productos_registrados':productos_registrados})

def lapices_colores(request):
    productos_registrados = Producto.objects.filter(cat_prod_id=2)
    return render(request, 'lapices_colores.html', {'productos_registrados':productos_registrados})
    
    
def marcadores(request):
    productos_registrados = Producto.objects.filter(cat_prod_id=1)

    return render(request, 'marcadores.html', {'productos_registrados':productos_registrados})