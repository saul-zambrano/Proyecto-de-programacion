from django.contrib import admin
from productos.models import CategoriaProducto, Cliente, MetodoPago, Direccion, Producto, Orden, OrdenDetalle, Carrito
# Register your models here.
admin.site.register(CategoriaProducto)
admin.site.register(Cliente)
admin.site.register(MetodoPago)
admin.site.register(Direccion)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(OrdenDetalle)
admin.site.register(Carrito)