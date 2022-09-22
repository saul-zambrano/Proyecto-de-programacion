from django.shortcuts import render

# Create your views here.
def cliente(request):
    if request.method == "POST":
        pass
    return render(request, 'cliente.html')


def metodo_pago(request):
    return render(request, 'metodo_pago.html')