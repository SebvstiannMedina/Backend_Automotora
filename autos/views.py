from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'autos/index.html', context)

def agrega(request):
    context={}
    return render(request, 'autos/agrega.html', context)

