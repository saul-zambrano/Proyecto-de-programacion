from django.shortcuts import render

# Create your views here.
def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')