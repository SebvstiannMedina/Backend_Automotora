from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegistroView


app_name = 'autos'

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.AcercaView.as_view(), name='acerca'),
    path('cuenta/', views.CuentaView.as_view(), name='cuenta'),
    path('mantencion/', views.MantencionView.as_view(), name='mantencion'),
    path('productos/', views.ProductosView.as_view(), name='productos'),
    path('inventario/', views.InventarioView.as_view(), name='inventario'),
    path('sedan/', views.sedan, name='sedan'),
    path('motos/', views.motos, name='motos'),
    path('hatchback/', views.hatchback, name='hatchback'),
    path('suv/', views.suv, name='suv'),
    path('noticias/', views.noticias, name='noticias'),
    path('registro/', RegistroView.as_view(), name='registro'),  # Cambiado a RegistroView
    path('apivalores/', views.apivalores, name='apivalores'),
    path('productos/', views.ProductoListView.as_view(), name='productos_list'),  # Cambiado a productos_list
    path('agrega/', views.agrega, name='agrega'),
    path('manage_product/', views.ManageProductView.as_view(), name='manage_product'),
    path('bmwx5/', views.bmwx5, name='bmwx5'),
    path('hyundaisantafe/', views.hyundaisantafe, name='hyundaisantafe'),
    path('kiasportage/', views.kiasportage, name='kiasportage'),
    path('toyotarav4/', views.toyotarav4, name='toyotarav4'),
    path('hyundaisantafe/', views.hyundaisantafe, name='hyundaisantafe'),
    path('hondacivic/', views.hondacivic, name='hondacivic'),
    path('sedan/', views.sedan, name='sedan'),  # Duplicado, deberías mantener uno
    path('hyundaielantra/', views.hyundaielantra, name='hyundaielantra'),
    path('kiacerato/', views.kiacerato, name='kiacerato'),
    path('toyotacorolla/', views.toyotacorolla, name='toyotacorolla'),
    path('kawasaki/', views.kawasaki, name='kawasaki'),
    path('yamaha/', views.yamaha, name='yamaha'),
    path('suzuki/', views.suzuki, name='suzuki'),
    path('honda/', views.honda, name='honda'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]
