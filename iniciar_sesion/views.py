from django.shortcuts import render, redirect

# Create your views here.
def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def registrarse(request):
    return render(request, 'registrarse.html')


def registrar_usuario(request):
    return redirect('/')