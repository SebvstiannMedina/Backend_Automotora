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
    path('registro/', views.registro, name='registro'),  # Aquí está la corrección
    path('apivalores/', views.apivalores, name='apivalores'),
    path('productos/', views.ProductoListView.as_view(), name='productos'),
    path('agrega/', views.ProductoListView.as_view(), name='agrega'),
    path('manage_product/', views.ManageProductView.as_view(), name='manage_product'),
    path('bmwx5/', views.bmwx5, name='bmwx5'),
    path('hyundaisantafe/', views.hyundaisantafe, name='hyundaisantafe'),
    path('kiasportage/', views.kiasportage, name='kiasportage'),
    path('toyotarav4/', views.toyotarav4, name='toyotarav4'),
    path('hyundaisantafe/', views.hyundaisantafe, name='hyundaisantafe')
]