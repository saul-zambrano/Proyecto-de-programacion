"""ionix_sa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path
from carrito.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from productos.views import marcadores, cuadernos, lapices_colores
from sobre_nosotros.views import inicio
from carrito.views import carrito
from cliente.views import cliente
from cliente.views import metodo_pago


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('marcadores', marcadores, name='marcadores'),
    path('cuadernos', cuadernos, name='cuadernos'),
    path('lapices_colores', lapices_colores, name='lapices_colores'),
    path('carrito', carrito, name='carrito'),
    path('cliente', cliente, name='cliente'),
    path('metodo_pago', metodo_pago, name="metodo_pago"),
    path('agregar/<int:id_producto>', agregar_producto, name="Add"),
    path('restar/<int:id_producto>', restar_producto, name="Sub"),
    path('eliminar/<int:id_producto>', eliminar_producto, name="Del"),
    path('limpiar/', limpiar_carrito, name="CLS")
]
