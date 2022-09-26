from django.shortcuts import render

# from ionix_sa.productos.models import Carrito
from carrito.Carrito import Carrito
from productos.models import Producto
from django.shortcuts import redirect
# Create your views here.
def carrito(request):
    return render(request, 'carrito.html')


def agregar_producto(request, id_producto):
    shop = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    shop.agregar(producto)
    return redirect("carrito")


def eliminar_producto(request, id_producto):
    shop = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    shop.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, id_producto):
    shop = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    shop.restar(producto)
    return redirect("carrito")


def limpiar_carrito(request):
    shop = Carrito(request)
    shop.limpiar()
    return redirect("carrito")