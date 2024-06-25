from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Auto

class RegistroMantenimientoView(View):
    def get(self, request):
        # Aquí puedes agregar la lógica necesaria para obtener los registros de mantenimiento
        registros = [
            {'nombre': 'Juan Pérez', 'fecha': '2024-06-25', 'modelo': 'Nissan', 'tipo': 'Sedan'},
            {'nombre': 'María García', 'fecha': '2024-06-24', 'modelo': 'Kia', 'tipo': 'Hatchback'},
            # Agrega más registros según sea necesario
        ]
        return render(request, 'registro_mantenimiento.html', {'registros': registros})
    
class AcercaView(View):
    def get(self, request):
        return render(request, 'acerca.html')

class InventarioView(View):
    def get(self, request):
        return render(request, 'inventario.html')

class CuentaView(View):
    def get(self, request):
        return render(request, 'cuenta.html')

class MantencionView(View):
    def get(self, request):
        return render(request, 'mantencion.html')

class ProductosView(View):
    def get(self, request):
        return render(request, 'productos.html')

def index(request):
    autos = Auto.objects.all()
    return render(request, 'autos/index.html', {'autos': autos})

def detalle(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'autos/detalle.html', {'auto': auto})

def sedan(request):
    return render(request, 'sedan.html')

def motos(request):
    return render(request, 'motos.html')

def hatchback(request):
    return render(request, 'hatchback.html')

def suv(request):
    return render(request, 'suv.html')

def noticias(request):
    return render(request, 'noticias.html')

def acerca(request):
    return render(request, 'acerca.html')

def cuenta(request):
    return render(request, 'cuenta.html')

def registro_mantenimiento(request):
    if request.method == 'POST':
        # Aquí irá la lógica para procesar el formulario de registro de mantenimiento
        # Por ahora, simplemente redireccionaremos a la página de inicio
        return redirect('autos:index')
    else:
        return render(request, 'mantencion.html')

def apivalores(request):
    return render(request, 'apivalores.html')