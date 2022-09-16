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
from productos.views import marcadores, cuadernos, lapices_colores
from sobre_nosotros.views import inicio
from iniciar_sesion.views import iniciar_sesion, registrarse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('marcadores', marcadores, name='marcadores'),
    path('cuadernos', cuadernos, name='cuadernos'),
    path('lapices_colores', lapices_colores, name='lapices_colores'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('iniciar_sesion/registrarse', registrarse, name='registrarse')
    path('registrar_usuario', registrarse, name='registrar_usuario')
]
