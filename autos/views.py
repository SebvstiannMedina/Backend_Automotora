from django.shortcuts import render, get_object_or_404
from .models import Auto

def index(request):
    autos = Auto.objects.all()
    return render(request, 'autos/index.html', {'autos': autos})

def detalle(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'autos/detalle.html', {'auto': auto})
