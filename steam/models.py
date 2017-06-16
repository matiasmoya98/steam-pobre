from django.db import models
from django.utils import timezone

class Juego(models.Model):
    nombre = models.CharField(max_length=200)  
    genero = models.CharField(max_length=200)  
    fecha_de_lanzamiento = models.DateTimeField(
            default=timezone.now)
    distribuidor = models.CharField(max_length=200) 
    precio = models.CharField(max_length=200) 
    descripcion= models.TextField()

    def __str__(self):
        return self.nombre
