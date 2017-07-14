from django.db import models
from django.utils import timezone

class Genero(models.Model):
    nombre = models.CharField(max_length=200)    
    imagen = models.ImageField(upload_to='static/images/genero',
                               blank=True,
                               null=True)
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=200)  
    genero = models.ForeignKey('Genero')  
    fecha_de_lanzamiento = models.DateTimeField(
            default=timezone.now)
    distribuidor = models.CharField(max_length=200) 
    precio = models.CharField(max_length=200) 
    descripcion= models.TextField()
    imagen = models.ImageField(upload_to='static/images/juego',
                               blank=True,
                               null=True)   
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    descripcion_user = models.TextField()
    nacionalidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre



