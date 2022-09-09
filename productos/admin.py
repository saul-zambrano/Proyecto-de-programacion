from django.contrib import admin
from productos import CategoriaProducto, Usuario, MetodoPago, Domicilio, Producto, Orden, OrdenDetalle, Carrito
# Register your models here.
admin.site.register(CategoriaProducto)
admin.site.register(Usuario)
admin.site.register(MetodoPago)
admin.site.register(Domicilio)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(OrdenDetalle)
admin.site.register(Carrito)