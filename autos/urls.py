from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página de inicio
    path('detalle/<int:auto_id>/', views.detalle, name='detalle'),  # Ruta para detalle de auto
    # Añade aquí más paths según tus necesidades
]


