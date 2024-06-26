from django.db import models

# Create your models here.
from django.db import models

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