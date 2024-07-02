from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import RegistroForm
from django.views import View
from .models import Auto, Producto, Usuario
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Producto
#este import se usa para los modelos de autorizacion de django 
from django.contrib.auth.models import User


class RegistroMantenimientoView(View):
    def get(self, request):
        registros = [
            {'nombre': 'Juan Pérez', 'fecha': '2024-06-25', 'modelo': 'Nissan', 'tipo': 'Sedan'},
            {'nombre': 'María García', 'fecha': '2024-06-24', 'modelo': 'Kia', 'tipo': 'Hatchback'},
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
        return render(request, 'usuario/productos.html')
    
class agregaView(View):
    def get(self, request):
        return render(request, 'autos/agrega.html')
    
def agrega(request):
    return render(request, 'autos/agrega.html')

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
        return redirect('autos:index')
    else:
        return render(request, 'mantencion.html')

def apivalores(request):
    return render(request, 'apivalores.html')

def productos(request):
    return render(request, 'usuario/productos.html')

def agrega(request):
    return render(request, 'admin/agrega.html')

class ProductoListView(View):
    def get(self, request):
        productos = Producto.objects.all()
        return render(request, 'agregar_editar_eliminar.html', {'productos': productos})

class ManageProductView(View):
    def post(self, request):
        action = request.POST.get('action')
        
        if action == 'add':
            nombre = request.POST.get('nombre_del_producto')
            valor = request.POST.get('valor_del_producto')
            existencia = request.POST.get('existencia_del_producto')
            url_imagen = request.POST.get('url_imagen')
            Producto.objects.create(nombre=nombre, valor=valor, existencia=existencia, url_imagen=url_imagen)
        
        elif action == 'edit':
            producto_id = request.POST.get('producto_a_editar')
            atributo = request.POST.get('atributo_a_editar')
            nuevo_valor = request.POST.get('nuevo_valor')
            producto = Producto.objects.get(id=producto_id)
            setattr(producto, atributo, nuevo_valor)
            producto.save()
        
        elif action == 'delete':
            producto_id = request.POST.get('producto_a_eliminar')
            Producto.objects.get(id=producto_id).delete()

        return redirect('autos:producto_list')
    
def registro(request):
    return render(request, 'registro.html')

def bmwx5(request):
    return render(request, 'bmwx5.html')

def hyundaisantafe(request):
    return render(request, 'hyundaisantafe.html')

def kiasportage(request):
    return render(request, 'kiasportage.html')

def toyotarav4(request):
    return render(request, 'toyotarav4.html')

def hyundaisantafe(request):
    return render(request, 'hyundaisantafe.html')

def sedan(request):
    return render(request, 'sedan.html')

def hondacivic(request):
    return render(request, 'hondacivic.html')

def hyundaielantra(request):
    return render(request, 'hyundaielantra.html')

def kiacerato(request):
    return render(request, 'kiacerato.html')

def toyotacorolla(request):
    return render(request, 'toyotacorolla.html')

def kawasaki(request):
    return render(request, 'kawasaki.html')

def yamaha(request):
    return render(request, 'yamaha.html')

def suzuki(request):
    return render(request, 'suzuki.html')

def honda(request):
    return render(request, 'Honda.html')

class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'registro.html', {'form': form})
    # yo aca en lo personal no uso esto por lo mismo ya que es un poco enredado a mi hasta hoy me cuesta prueba ahora 

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('autos:index')
        return render(request, 'registro.html', {'form': form})

class CuentaView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'cuenta.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            #funcion es para uso de login de la tabla de admin de django 
            login(request, user)
            return redirect('autos:index')
        return render(request, 'cuenta.html', {'form': form})
    
def loginForm(request):
    if request.method == "POST":
        #campo del formulario
        correoForm = request.POST.get('txtUser')
        clave = request.POST.get('txtPass')
        #Funcion se valida en la tabla users de django no en la bse de datos 
        u_auth = authenticate(request, username=correoForm, password=clave)
        #aca deberia ir el objects create de tu DB es decir como le llames a tu tabla en la db 
        usuario = Usuario.objects.get(correo=correoForm)
        #esto es oopcional es para dejar si el usuario esta vigente o no es decir si no ha sido borrado de la db ya que es un borrado logico
        is_vig = usuario.vigencia
        if u_auth is not None and is_vig:
            #y aca se usa el login que te mencione
            login(request, u_auth)
            #declaraciones de variables para el uso de permisos en html para manejo de plantillas
            request.session['id_perfil'] = usuario.perfil_id
            request.session['id_usuario'] = usuario.id
            return redirect('index')
        else:
            #esto es en caso de que uses sweet alert un componente de javascript que arroja alertas bonitas
            return HttpResponse("Tu cuenta no está vigente. Contacta al administrador.")
    else:
        return render(request, "login.html")
def viewReg(request):

    return render(request, 'registro.html')
def crear_usuario(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        fNacimiento = request.POST.get('fNacimiento')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        #aca debes registrar el usuario en la tabla user de django 
        # Crear usuario
        User.objects.create_user(correo, '', password)
        Usuario.objects.create(username=correo, rut=rut, nombre=nombre, apellido=apellido, telefono=telefono, fNacimiento=fNacimiento, correo=correo, password=password)
        return HttpResponse('Usuario creado correctamente')
#ahora revisa la db para ver si es que llego algo
def editar_perfil(request):
    return render(request, 'editar_perfil.html')

def registro_mante(request):
    return render(request, 'registro_mante.html')
