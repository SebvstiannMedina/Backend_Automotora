from django.db import models
import uuid
# Create your models here.
from django.db import models


class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self) -> str:
        return self.nombre

class Comuna(models.Model):
    idCom = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False,blank=False)
    region = models.ForeignKey(Region,on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.nombre

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name='Id del rol')
    nombre = models.CharField(max_length=50, null=False,blank=False)
    def __str__(self) -> str:
        return self.nombre

class Usuario(models.Model):
    idUsuario =models.AutoField(primary_key=True,verbose_name='Id del usuario')
    rut = models.CharField(max_length=13,null=False, blank=False)
    nombre = models.CharField(max_length=15,null=False, blank=False)
    apellido = models.CharField(max_length=20, null=False, blank=False)
    telefono = models.CharField(max_length=15,null=False, blank=False)
    fNacimiento = models.DateField(null=False, blank=False)
    correo = models.EmailField(max_length=254,null=False, blank=False)
    clave = models.CharField(max_length=12,null=False,blank=False)
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.rut

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True,verbose_name='Id de la direccion')
    calle = models.CharField(max_length=50,null=False,blank=False)
    numero = models.CharField(max_length=6,null=False,blank=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

class Venta(models.Model):
    idVenta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)



class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    existencia = models.PositiveIntegerField()
    url_imagen = models.URLField()

    def __str__(self):
        return self.nombre
    
