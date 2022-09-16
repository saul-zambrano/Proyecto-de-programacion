from pydoc import cli
from django.shortcuts import render, redirect
from productos.models import Cliente, Direccion
# Create your views here.
def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def registrarse(request):
    return render(request, 'registrarse.html')


def registrar_usuario(request):
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    dni = request.POST['dni']
    pais = request.POST['pais']
    ciudad = request.POST['ciudad']
    direccion = request.POST['direccion']
    email = request.POST['email']
    password = request.POST['password']

    cliente = Cliente.objects.create(email=email, password=password, nombres=nombres, apellidos=apellidos, dni=dni)
    # ultimo_id_cliente = Cliente.objects.latest('id')
    # direccion = Direccion.objects.create(pais=pais, ciudad=ciudad, direccion=ultimo_id_cliente)
    
    return redirect('inicio')