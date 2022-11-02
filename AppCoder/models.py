from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    anio_lanzamiento = models.IntegerField()
    desarrolladora = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    
class Equipo(models.Model):
    nombre  = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    reglas = models.CharField(max_length=255)
    puntos = models.IntegerField()
    
    def __str__(self):
        return self.nombre