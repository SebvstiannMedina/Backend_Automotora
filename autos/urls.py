from django.urls import path
from . import views

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
    path('registro_mante/', views.registro_mantenimiento, name='registro_mante'),
]